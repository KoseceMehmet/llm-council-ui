import streamlit as st
import asyncio
from ui.styles import apply_dorkforge_theme
from ui.components import render_sidebar
from core.council import execute_council_session, execute_chairman_synthesis

st.set_page_config(
    page_title="LLM Council NOC Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_dorkforge_theme()

if "council_members" not in st.session_state:
    st.session_state.council_members = [
        {"id": 1, "name": "AGENT_RECON", "provider": "OpenRouter", "model": "google/gemini-2.0-flash-001", "role": "Analyze input data from a reconnaissance and surface attack perspective."},
        {"id": 2, "name": "AGENT_CRITIC", "provider": "Groq", "model": "llama-3.3-70b-versatile", "role": "Evaluate findings for logical fallacies, edge-cases, and false positives."},
        {"id": 3, "name": "AGENT_EXPLOIT", "provider": "Ollama (Local)", "model": "qwen2.5-coder:latest", "role": "Provide proof-of-concept automation code and verification scripts."}
    ]

if "debate_results" not in st.session_state:
    st.session_state.debate_results = None

api_keys, chairman_provider, chairman_model = render_sidebar()

st.markdown("<h1>LLM COUNCIL // OPERATIONS DASHBOARD</h1>", unsafe_allow_html=True)
st.caption("Multi-Agent Parallel Reasoning and Synthesis Architecture")

col_prompt, col_file = st.columns([3, 1])

with col_prompt:
    user_query = st.text_area("TARGET QUERY / CONTEXT INPUT", placeholder="Specify target domain, code snippet, or architectural decision...", height=110)

with col_file:
    uploaded_file = st.file_uploader("ATTACH FILE / CONTEXT", type=["txt", "json", "py", "sh", "md", "log"])
    file_context = ""
    if uploaded_file is not None:
        file_context = uploaded_file.read().decode("utf-8", errors="ignore")
        st.caption(f"ATTACHED: {uploaded_file.name}")

run_execution = st.button("EXECUTE PARALLEL DEBATE", type="primary", use_container_width=True)

st.divider()

if run_execution:
    if not user_query:
        st.error("SYSTEM ERROR: INPUT QUERY IS REQUIRED.")
    elif len(st.session_state.council_members) == 0:
        st.error("SYSTEM ERROR: AT LEAST ONE COUNCIL MEMBER IS REQUIRED.")
    else:
        st.markdown("### LIVE PARALLEL PANELS")
        
        num_members = len(st.session_state.council_members)
        cols = st.columns(num_members)
        
        with st.spinner("DISPATCHING REQUESTS TO AGENTS..."):
            results = asyncio.run(execute_council_session(st.session_state.council_members, user_query, file_context, api_keys))
            st.session_state.debate_results = results

        for idx, (agent_name, agent_output) in enumerate(results.items()):
            with cols[idx]:
                st.markdown(f"#### {agent_name}")
                st.markdown("<span class='status-badge-success'>STATUS: COMPLETED</span>", unsafe_allow_html=True)
                st.markdown("---")
                st.markdown(agent_output)

if st.session_state.debate_results:
    st.divider()
    st.markdown("### HUMAN-IN-THE-LOOP // DECISION CHECKPOINT")
    
    col_acc, col_rej = st.columns(2)
    with col_acc:
        if st.button("APPROVE SYNTHESIS", use_container_width=True):
            with st.spinner("CHAIRMAN IS SYNTHESIZING RESULTS..."):
                synthesis = asyncio.run(
                    execute_chairman_synthesis(chairman_provider, chairman_model, user_query, st.session_state.debate_results, api_keys)
                )
                st.markdown("### CHAIRMAN SYNTHESIS REPORT")
                st.markdown(synthesis)
                
    with col_rej:
        if st.button("ABORT / CLEAR SESSION", use_container_width=True):
            st.session_state.debate_results = None
            st.rerun()

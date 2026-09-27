import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.markdown("### COUNCIL // CONTROL CENTER")
        st.caption("SYSTEM CONFIGURATION & API MANAGEMENT")
        
        # --- DYNAMIC API KEYS & ENDPOINTS ---
        st.markdown("### DYNAMIC API KEYS & ENDPOINTS")
        
        if "api_keys_list" not in st.session_state:
            st.session_state.api_keys_list = [
                {"name": "OpenRouter", "value": ""},
                {"name": "Groq", "value": ""},
                {"name": "OpenAI", "value": ""},
                {"name": "Ollama_URL", "value": "http://localhost:11434"}
            ]

        if st.button("ADD NEW API KEY / ENDPOINT", use_container_width=True):
            st.session_state.api_keys_list.append({"name": "CUSTOM_KEY", "value": ""})
            st.rerun()

        api_keys_dict = {}
        for idx, k_item in enumerate(st.session_state.api_keys_list):
            with st.expander(f"KEY: {k_item['name']}", expanded=False):
                k_item["name"] = st.text_input(f"Key Identifier #{idx+1}", value=k_item["name"], key=f"kname_{idx}")
                is_secret = "url" not in k_item["name"].lower()
                k_item["value"] = st.text_input(f"Value / Endpoint #{idx+1}", value=k_item["value"], type="password" if is_secret else "default", key=f"kval_{idx}")
                
                # Dynamic dict mapping with normalized lower-case keys
                api_keys_dict[k_item["name"].lower()] = k_item["value"]
                
                if st.button(f"REMOVE KEY #{idx+1}", key=f"kdel_{idx}"):
                    st.session_state.api_keys_list.pop(idx)
                    st.rerun()

        st.divider()

        # --- DYNAMIC MEMBERS SETUP ---
        st.markdown("### DYNAMIC MEMBERS SETUP")
        
        if st.button("ADD COUNCIL MEMBER", use_container_width=True):
            new_id = len(st.session_state.council_members) + 1
            st.session_state.council_members.append({
                "id": new_id,
                "name": f"AGENT_{new_id}",
                "provider": "OpenRouter",
                "model": "google/gemini-2.0-flash-001",
                "role": "You are a technical security analyst."
            })
            st.rerun()

        for idx, member in enumerate(st.session_state.council_members):
            with st.expander(f"MEMBER: {member['name']} [{member['provider']}]", expanded=False):
                member["name"] = st.text_input(f"Name #{idx+1}", value=member["name"], key=f"n_{idx}")
                member["provider"] = st.selectbox(f"Provider #{idx+1}", ["OpenRouter", "Groq", "OpenAI", "Ollama (Local)"], index=0 if member["provider"] not in ["OpenRouter", "Groq", "OpenAI", "Ollama (Local)"] else ["OpenRouter", "Groq", "OpenAI", "Ollama (Local)"].index(member["provider"]), key=f"p_{idx}")
                member["model"] = st.text_input(f"Model ID #{idx+1}", value=member["model"], key=f"m_{idx}")
                member["role"] = st.text_area(f"System Prompt #{idx+1}", value=member["role"], key=f"r_{idx}")
                
                if st.button(f"REMOVE MEMBER #{idx+1}", key=f"d_{idx}"):
                    st.session_state.council_members.pop(idx)
                    st.rerun()

        st.divider()

        # --- CHAIRMAN CONFIG ---
        st.markdown("### CHAIRMAN CONFIG")
        chairman_provider = st.selectbox("Chairman Provider", ["OpenRouter", "Groq", "OpenAI", "Ollama (Local)"])
        chairman_model = st.text_input("Chairman Model ID", value="google/gemini-2.0-flash-001")

        return api_keys_dict, chairman_provider, chairman_model

import asyncio
from core.providers import fetch_llm_response

async def execute_council_session(members: list, query: str, context: str, api_keys: dict):
    tasks = []
    for member in members:
        task = fetch_llm_response(
            provider=member["provider"],
            model_name=member["model"],
            system_prompt=member["role"],
            user_prompt=query,
            context=context,
            api_keys=api_keys
        )
        tasks.append(task)
    
    results = await asyncio.gather(*tasks)
    
    output_map = {}
    for idx, member in enumerate(members):
        output_map[member["name"]] = results[idx]
        
    return output_map

async def execute_chairman_synthesis(provider: str, model: str, query: str, debates: dict, api_keys: dict):
    combined_context = "\n\n".join([f"=== MEMBER [{name}] DEBATE OUTPUT ===\n{resp}" for name, resp in debates.items()])
    
    system_prompt = (
        "You are the Chairman of the AI Council. Review all member perspectives, "
        "identify inconsistencies, resolve debates, and output a unified, highly-actionable decision report."
    )
    
    return await fetch_llm_response(
        provider=provider,
        model_name=model,
        system_prompt=system_prompt,
        user_prompt=f"Target/Query: {query}\n\nCouncil Arguments:\n{combined_context}",
        api_keys=api_keys
    )

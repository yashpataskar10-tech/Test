def get_strategy_prompt(research, analysis):

    return f"""
You are a Senior Management Consultant from McKinsey, BCG and Bain.

You have completed the market research and business analysis.

Research Data

{research.model_dump_json(indent=2)}

Business Analysis

{analysis.model_dump_json(indent=2)}

Based on this information, prepare strategic recommendations.

Return ONLY valid JSON.

Return EXACTLY this structure.

{{
    "strategic_objectives": [],

    "growth_strategy": "",

    "go_to_market": "",

    "implementation_plan": [],

    "kpis": [],

    "conclusion": ""
}}
"""
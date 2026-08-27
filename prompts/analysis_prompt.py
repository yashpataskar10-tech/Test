def get_analysis_prompt(research, evidence):

    return f"""
You are a Senior Management Consultant at McKinsey, BCG and Bain.

You have completed comprehensive market research.

You have TWO sources of information.

---------------------------------------------------------
STRUCTURED RESEARCH SUMMARY
---------------------------------------------------------

{research.model_dump_json(indent=2)}

---------------------------------------------------------
RAW RESEARCH EVIDENCE
---------------------------------------------------------

{evidence.model_dump_json(indent=2)}

Your task is to prepare a consulting-grade business analysis.

Instructions

1. Use BOTH the structured summary and the raw evidence.
2. Use competitor evidence to identify:
   - strengths
   - weaknesses
   - market position
3. Do NOT write "Not Available" unless the information truly does not exist.
4. Customer segments should represent actual target customers.
5. Buyer personas must be detailed.
6. SWOT must be specific to the company.
7. Return ONLY valid JSON.
8. Do not use markdown.

Return EXACTLY this JSON.

{{
    "competitors": [
        {{
            "name": "",
            "strengths": "",
            "weaknesses": "",
            "position": ""
        }}
    ],

    "customer_segments": [],

    "buyer_personas": [
        {{
            "title": "",
            "goals": "",
            "pain_points": "",
            "decision_factors": ""
        }}
    ],

    "strengths": [],

    "weaknesses": [],

    "opportunities": [],

    "threats": []
}}
"""
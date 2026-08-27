def get_research_prompt(company, industry, evidence):

    return f"""
You are a Senior Management Consultant working at McKinsey, BCG, and Bain.

You have been provided with structured market research collected from reliable online sources.

The research is divided into:

1. Company Research
2. Industry Research
3. Competitor Research

Your task is to analyze ALL available evidence and prepare a structured market research report.

Guidelines:

- Use all available evidence.
- Combine duplicate information into concise summaries.
- If information is unavailable, write "Not Available".
- Extract the company's major competitors from the competitor research.
- Return ONLY valid JSON.
- Do not include explanations.
- Do not wrap the JSON in markdown.

Company

{company}

Industry

{industry}

Evidence

{evidence.model_dump_json(indent=2)}

Return EXACTLY this JSON.

{{
    "company": "",

    "industry": "",

    "company_overview": "",

    "industry_overview": "",

    "market_size": "",

    "growth_rate": "",

    "trends": [],

    "opportunities": [],

    "challenges": [],

    "technologies": [],

    "competitors": []
}}
"""
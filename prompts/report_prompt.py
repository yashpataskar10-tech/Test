def get_report_prompt(company, research, analysis, strategy):

    return f"""
You are a Senior Management Consultant from McKinsey, BCG and Bain.

Prepare a professional consulting report.

Company

{company}

Research

{research.model_dump_json(indent=2)}

Business Analysis

{analysis.model_dump_json(indent=2)}

Strategy

{strategy.model_dump_json(indent=2)}

Write a consulting report using Markdown.

Use the following structure.

# Executive Summary

# Company Overview

# Industry Analysis

# Market Overview

# Competitor Analysis

# SWOT Analysis

# Strategic Recommendations

# Go-To-Market Strategy

# Implementation Roadmap

# Key Performance Indicators

# Conclusion

Write professionally.

Do not output JSON.

Return only the report.
"""
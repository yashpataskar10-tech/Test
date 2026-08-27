from pathlib import Path


class MarkdownGenerator:

    def generate(
        self,
        company,
        industry,
        research,
        analysis,
        strategy
    ):

        report = f"""# AI Strategy Consulting Report

---

# Company

**Name:** {company}

**Industry:** {industry}

---

# Executive Summary

{research.company_overview}

---

# Industry Overview

{research.industry_overview}

---

# Market Size

{research.market_size}

---

# Market Growth Rate

{research.growth_rate}

---

# Industry Trends

"""

        for trend in research.trends:
            report += f"- {trend}\n"

        report += "\n---\n"

        report += "# Opportunities\n\n"

        for item in research.opportunities:
            report += f"- {item}\n"

        report += "\n---\n"

        report += "# Challenges\n\n"

        for item in research.challenges:
            report += f"- {item}\n"

        report += "\n---\n"

        report += "# Technologies\n\n"

        for item in research.technologies:
            report += f"- {item}\n"

        report += "\n---\n"

        report += "# SWOT Analysis\n\n"

        report += "## Strengths\n\n"

        for item in analysis.strengths:
            report += f"- {item}\n"

        report += "\n## Weaknesses\n\n"

        for item in analysis.weaknesses:
            report += f"- {item}\n"

        report += "\n## Opportunities\n\n"

        for item in analysis.opportunities:
            report += f"- {item}\n"

        report += "\n## Threats\n\n"

        for item in analysis.threats:
            report += f"- {item}\n"

        report += "\n---\n"

        report += "# Competitor Analysis\n\n"

        for competitor in analysis.competitors:

            report += f"## {competitor.name}\n\n"

            report += f"**Strengths:** {competitor.strengths}\n\n"

            report += f"**Weaknesses:** {competitor.weaknesses}\n\n"

            report += f"**Market Position:** {competitor.position}\n\n"

        report += "\n---\n"

        report += "# Customer Segments\n\n"

        for segment in analysis.customer_segments:
            report += f"- {segment}\n"

        report += "\n---\n"

        report += "# Buyer Personas\n\n"

        for persona in analysis.buyer_personas:

            report += f"## {persona.title}\n\n"

            report += f"**Goals:** {persona.goals}\n\n"

            report += f"**Pain Points:** {persona.pain_points}\n\n"

            report += (
                f"**Decision Factors:** {persona.decision_factors}\n\n"
            )

        report += "\n---\n"

        report += "# Strategic Objectives\n\n"

        for objective in strategy.strategic_objectives:
            report += f"- {objective}\n"

        report += "\n---\n"

        report += "# Growth Strategy\n\n"

        report += strategy.growth_strategy

        report += "\n\n---\n"

        report += "# Go-To-Market Strategy\n\n"

        report += strategy.go_to_market

        report += "\n\n---\n"

        report += "# Implementation Roadmap\n\n"

        for step in strategy.implementation_plan:
            report += f"- {step}\n"

        report += "\n---\n"

        report += "# Key Performance Indicators\n\n"

        for kpi in strategy.kpis:
            report += f"- {kpi}\n"

        report += "\n---\n"

        report += "# Conclusion\n\n"

        report += strategy.conclusion

        output_folder = Path("outputs")
        output_folder.mkdir(exist_ok=True)

        filename = output_folder / f"{company.replace(' ', '_')}_Strategy_Report.md"

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(report)

        return report
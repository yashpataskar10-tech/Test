from pathlib import Path

from agents.base_agent import BaseAgent
from prompts.report_prompt import get_report_prompt


class ReportAgent(BaseAgent):

    def __init__(self):
        super().__init__()

    def run(
        self,
        company,
        industry,
        research,
        analysis,
        strategy
    ):

        print("\n" + "=" * 70)
        print("REPORT AGENT")
        print("=" * 70)

        prompt = get_report_prompt(
            company,
            industry,
            research,
            analysis,
            strategy
        )

        report = self.generate(prompt)

        output_folder = Path("outputs")
        output_folder.mkdir(exist_ok=True)

        filename = f"{company.replace(' ', '_')}_Strategy_Report.md"

        output_path = output_folder / filename

        with open(
            output_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(report)

        print(f"\n✓ Report saved to {output_path}")

        return report
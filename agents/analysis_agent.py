from agents.base_agent import BaseAgent

from models.schemas import AnalysisData

from prompts.analysis_prompt import get_analysis_prompt


class AnalysisAgent(BaseAgent):

    def __init__(self):

        super().__init__()

    def run(
        self,
        research,
        evidence
    ):

        print("\n" + "=" * 70)
        print("ANALYSIS AGENT")
        print("=" * 70)

        prompt = get_analysis_prompt(

            research,

            evidence

        )

        analysis_json = self.generate_json(
            prompt
        )

        analysis = AnalysisData(
            **analysis_json
        )

        print("✓ Analysis Completed")

        print(f"\nCompetitors Analyzed : {len(analysis.competitors)}")

        print(f"Customer Segments    : {len(analysis.customer_segments)}")

        print(f"Buyer Personas       : {len(analysis.buyer_personas)}")

        return analysis
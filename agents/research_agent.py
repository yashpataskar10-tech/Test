from agents.base_agent import BaseAgent

from models.schemas import ResearchData

from prompts.research_prompt import get_research_prompt


class ResearchAgent(BaseAgent):

    def __init__(self):

        super().__init__()

    def run(
        self,
        company,
        industry,
        evidence
    ):

        print("\n" + "=" * 70)
        print("RESEARCH AGENT")
        print("=" * 70)

        prompt = get_research_prompt(
            company,
            industry,
            evidence
        )

        research_json = self.generate_json(
            prompt
        )

        research = ResearchData(
            **research_json
        )

        print("✓ Research Completed")

        print(f"\nDetected Competitors: {', '.join(research.competitors)}")

        return research
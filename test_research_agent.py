from services.research_service import ResearchService
from agents.research_agent import ResearchAgent


def main():

    company = "TCS"
    industry = "IT Services"

    print("=" * 70)
    print("TESTING RESEARCH AGENT")
    print("=" * 70)

    research_service = ResearchService()

    evidence = research_service.collect(
        company,
        industry
    )

    print(f"\nCollected {len(evidence.evidence)} evidence items")

    research_agent = ResearchAgent()

    research = research_agent.run(
        company,
        industry,
        evidence
    )

    print("\n")
    print("=" * 70)
    print("RESEARCH RESULT")
    print("=" * 70)

    print(research.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
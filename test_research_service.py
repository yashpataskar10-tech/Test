from services.research_service import ResearchService


service = ResearchService()

evidence = service.collect(

    "TCS",

    "IT Services"

)

print()

print("=" * 80)

print("Evidence Collected")

print("=" * 80)

print()

print(evidence.model_dump_json(indent=2))
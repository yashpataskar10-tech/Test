from services.research_service import ResearchService

from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent


company = "TCS"
industry = "IT Services"

research_service = ResearchService()

evidence = research_service.collect(
    company,
    industry
)

research = ResearchAgent().run(
    company,
    industry,
    evidence
)

analysis = AnalysisAgent().run(
    research
)

print(analysis.model_dump_json(indent=2))
from services.research_service import ResearchService

from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.strategy_agent import StrategyAgent

from report.markdown_generator import MarkdownGenerator
from report.pdf_generator import PDFGenerator


class ConsultantOrchestrator:

    def __init__(self):

        self.research_service = ResearchService()

        self.research_agent = ResearchAgent()

        self.analysis_agent = AnalysisAgent()

        self.strategy_agent = StrategyAgent()

        self.markdown_generator = MarkdownGenerator()

        self.pdf_generator = PDFGenerator()

    def execute(
        self,
        company,
        industry
    ):

        print("\n" + "=" * 70)
        print("STEP 1 : COLLECTING MARKET RESEARCH")
        print("=" * 70)

        evidence = self.research_service.collect(
            company,
            industry
        )

        print("\n" + "=" * 70)
        print("STEP 2 : RESEARCH AGENT")
        print("=" * 70)

        research = self.research_agent.run(
            company,
            industry,
            evidence
        )

        print("\n" + "=" * 70)
        print("STEP 3 : ANALYSIS AGENT")
        print("=" * 70)

        analysis = self.analysis_agent.run(
            research,
            evidence
        )

        print("\n" + "=" * 70)
        print("STEP 4 : STRATEGY AGENT")
        print("=" * 70)

        strategy = self.strategy_agent.run(
            research,
            analysis
        )

        print("\n" + "=" * 70)
        print("STEP 5 : GENERATING MARKDOWN REPORT")
        print("=" * 70)

        markdown_report = self.markdown_generator.generate(
            company,
            industry,
            research,
            analysis,
            strategy
        )

        print("\n" + "=" * 70)
        print("STEP 6 : GENERATING PDF REPORT")
        print("=" * 70)

        pdf_path = self.pdf_generator.generate(
            company,
            markdown_report
        )

        return {

            "company": company,

            "industry": industry,

            "research": research,

            "analysis": analysis,

            "strategy": strategy,

            "markdown": markdown_report,

            "pdf_path": pdf_path

        }
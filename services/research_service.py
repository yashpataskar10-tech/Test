from models.schemas import (
    EvidenceItem,
    EvidencePackage,
    CompetitorEvidence,
)

from prompts.search_queries import (
    COMPANY_QUERIES,
    INDUSTRY_QUERIES,
    COMPETITOR_DISCOVERY_QUERY,
)

from prompts.competitor_queries import (
    COMPETITOR_QUERIES,
)

from tools.search_tool import SearchTool
from services.gemini_service import GeminiService


class ResearchService:

    def __init__(self):

        self.search_tool = SearchTool()

        self.llm = GeminiService()

    def _search_queries(self, queries):

        evidence = []

        visited_urls = set()

        for query in queries:

            print(f"Searching : {query}")

            try:

                results = self.search_tool.search(
                    query,
                    max_results=3
                )

                for result in results:

                    url = result.get("url", "")

                    if not url:
                        continue

                    if url in visited_urls:
                        continue

                    visited_urls.add(url)

                    evidence.append(

                        EvidenceItem(

                            query=query,

                            title=result.get(
                                "title",
                                ""
                            ),

                            url=url,

                            content=result.get(
                                "content",
                                ""
                            )

                        )

                    )

            except Exception as e:

                print(f"Search failed: {e}")

        return evidence

    def discover_competitors(
        self,
        company
    ):

        print("\nDiscovering Competitors...\n")

        query = COMPETITOR_DISCOVERY_QUERY.format(
            company=company
        )

        results = self.search_tool.search(
            query,
            max_results=5
        )

        search_text = ""

        for result in results:

            search_text += (
                f"Title: {result.get('title','')}\n"
            )

            search_text += (
                f"Content: {result.get('content','')}\n\n"
            )

        prompt = f"""
You are a senior market research analyst.

Below are search results discussing competitors of {company}.

Identify ONLY the direct competitors.

Rules:

- Return ONLY valid JSON.
- No markdown.
- Maximum 10 competitors.
- Company names only.
- Ignore partners, customers and subsidiaries.

Search Results

{search_text}

Return EXACTLY:

{{
    "competitors":[]
}}
"""

        response = self.llm.generate_json(
            prompt
        )

        competitors = response.get(
            "competitors",
            []
        )

        competitors = [

            c.strip()

            for c in competitors

            if c.strip()

        ]

        competitors = list(
            dict.fromkeys(competitors)
        )

        print(
            f"Found {len(competitors)} competitors:"
        )

        for competitor in competitors:

            print(
                f"• {competitor}"
            )

        return competitors

    def research_competitors(
        self,
        competitors
    ):

        competitor_evidence = []

        for competitor in competitors:

            print(
                f"\nResearching {competitor}..."
            )

            queries = [

                query.format(
                    competitor=competitor
                )

                for query in COMPETITOR_QUERIES

            ]

            evidence = self._search_queries(
                queries
            )

            competitor_evidence.append(

                CompetitorEvidence(

                    competitor=competitor,

                    evidence=evidence

                )

            )

        return competitor_evidence

    def collect(
        self,
        company,
        industry
    ):

        print(
            "\nCollecting Company Research...\n"
        )

        company_queries = [

            query.format(
                company=company
            )

            for query in COMPANY_QUERIES

        ]

        company_evidence = self._search_queries(
            company_queries
        )

        print(
            "\nCollecting Industry Research...\n"
        )

        industry_queries = [

            query.format(
                industry=industry
            )

            for query in INDUSTRY_QUERIES

        ]

        industry_evidence = self._search_queries(
            industry_queries
        )

        competitors = self.discover_competitors(
            company
        )

        competitor_evidence = self.research_competitors(
            competitors
        )

        total_company = len(
            company_evidence
        )

        total_industry = len(
            industry_evidence
        )

        total_competitor = sum(

            len(
                competitor.evidence
            )

            for competitor in competitor_evidence

        )

        total = (

            total_company

            + total_industry

            + total_competitor

        )

        print("\n" + "=" * 70)

        print("RESEARCH SUMMARY")

        print("=" * 70)

        print(
            f"Company Evidence     : {total_company}"
        )

        print(
            f"Industry Evidence    : {total_industry}"
        )

        print(
            f"Competitor Evidence  : {total_competitor}"
        )

        print(
            f"Total Evidence       : {total}"
        )

        print(
            f"Competitors Found    : {len(competitors)}"
        )

        print("=" * 70)

        return EvidencePackage(

            company=company,

            industry=industry,

            company_evidence=company_evidence,

            industry_evidence=industry_evidence,

            competitor_evidence=competitor_evidence

        )
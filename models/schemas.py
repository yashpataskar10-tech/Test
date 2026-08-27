from typing import Dict, List

from pydantic import BaseModel


class EvidenceItem(BaseModel):
    query: str
    title: str
    url: str
    content: str


class CompetitorEvidence(BaseModel):
    competitor: str
    evidence: List[EvidenceItem]


class EvidencePackage(BaseModel):

    company: str

    industry: str

    company_evidence: List[EvidenceItem]

    industry_evidence: List[EvidenceItem]

    competitor_evidence: List[CompetitorEvidence]


class ResearchData(BaseModel):

    company: str

    industry: str

    company_overview: str

    industry_overview: str

    market_size: str

    growth_rate: str

    trends: List[str]

    opportunities: List[str]

    challenges: List[str]

    technologies: List[str]

    competitors: List[str]


class Competitor(BaseModel):

    name: str

    strengths: str

    weaknesses: str

    position: str


class BuyerPersona(BaseModel):

    title: str

    goals: str

    pain_points: str

    decision_factors: str


class AnalysisData(BaseModel):

    competitors: List[Competitor]

    customer_segments: List[str]

    buyer_personas: List[BuyerPersona]

    strengths: List[str]

    weaknesses: List[str]

    opportunities: List[str]

    threats: List[str]


class StrategyData(BaseModel):

    strategic_objectives: List[str]

    growth_strategy: str

    go_to_market: str

    implementation_plan: List[str]

    kpis: List[str]

    conclusion: str
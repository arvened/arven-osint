import os
from typing import Dict, List, Optional
from pydantic import BaseModel

from .core.claude_osint import ClaudeOSINT
from .core.graphify_engine import GraphifyEngine
from .core.public_apis_client import PublicAPIsClient


class OSINTResult(BaseModel):
    company: str
    data: Dict
    risk_score: float
    signals: List[str]
    tech_stack: List[str]


class ArvenOSINT:
    """Unified OSINT platform for ARVEN products"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        self.claude_osint = ClaudeOSINT(api_key=self.api_key)
        self.graphify = GraphifyEngine()
        self.public_apis = PublicAPIsClient()
    
    async def analyze_company(self, domain: str) -> OSINTResult:
        """Full company intelligence pipeline"""
        
        osint_data = await self.claude_osint.recon(domain)
        tech_graph = await self.graphify.analyze(domain, osint_data)
        enriched = await self.public_apis.enrich(
            domain=domain,
            osint_data=osint_data,
            tech_data=tech_graph
        )
        
        risk_score = self._calculate_risk(enriched)
        signals = self._extract_signals(enriched)
        
        return OSINTResult(
            company=domain,
            data=enriched,
            risk_score=risk_score,
            signals=signals,
            tech_stack=tech_graph.get("technologies", [])
        )
    
    def _calculate_risk(self, data: Dict) -> float:
        """Score company risk (0.0 - 1.0)"""
        risk = 0.0
        
        if data.get("breaches"):
            risk += 0.3
        if data.get("exposed_assets"):
            risk += 0.25
        if data.get("outdated_tech"):
            risk += 0.15
        if data.get("no_firewall"):
            risk += 0.3
        
        return min(risk, 1.0)
    
    def _extract_signals(self, data: Dict) -> List[str]:
        """Extract growth/risk signals"""
        signals = []
        
        if data.get("recent_hiring"):
            signals.append(f"Hiring {data['recent_hiring']} engineers")
        if data.get("funding_round"):
            signals.append(f"Raised {data['funding_round']}")
        if data.get("new_tech"):
            signals.append(f"Migrated to {data['new_tech']}")
        if data.get("breaches"):
            signals.append("⚠️ Data breach detected")
        
        return signals

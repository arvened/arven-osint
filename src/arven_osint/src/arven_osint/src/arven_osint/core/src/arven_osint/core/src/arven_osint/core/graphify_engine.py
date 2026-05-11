from typing import Dict, List


class GraphifyEngine:
    """Knowledge graph for tech stack & relationships"""
    
    async def analyze(self, domain: str, osint_data: Dict) -> Dict:
        """Build knowledge graph from OSINT data"""
        
        tech_graph = {
            "domain": domain,
            "technologies": [],
            "relationships": [],
            "vulnerabilities": [],
            "architecture": {}
        }
        
        if "tech_stack" in osint_data:
            tech_graph["technologies"] = osint_data["tech_stack"]
        
        tech_graph["architecture"] = self._infer_architecture(
            osint_data.get("tech_stack", [])
        )
        
        return tech_graph
    
    def _infer_architecture(self, techs: List[str]) -> Dict:
        """Infer architecture from tech choices"""
        patterns = {}
        
        if "AWS" in techs:
            patterns["cloud"] = "AWS"
        if "Kubernetes" in techs:
            patterns["container"] = "K8s"
        if "PostgreSQL" in techs or "MySQL" in techs:
            patterns["database"] = "SQL"
        
        return patterns

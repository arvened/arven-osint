from typing import Dict, List, Optional
from anthropic import Anthropic


class ClaudeOSINT:
    """Claude-OSINT integration (90+ modules)"""
    
    MODULES = {
        "linkedin": "Analyze LinkedIn footprint & employee discovery",
        "domain": "DNS, whois, subdomain enumeration",
        "email": "Email finding & validation",
        "tech_stack": "Technology detection & versions",
        "github": "Repository analysis & code secrets",
        "credentials": "Breach data & credential validation",
        "certificates": "SSL/TLS certificate analysis",
        "asn": "ASN & IP range analysis",
        "dns": "DNS records & history",
        "whois": "WHOIS data & registrar info",
    }
    
    def __init__(self, api_key: str):
        self.client = Anthropic(api_key=api_key)
        self.model = "claude-opus-4-1"
    
    async def recon(self, domain: str) -> Dict:
        """Run 90+ OSINT modules on domain"""
        
        prompt = f"""
        Run complete OSINT reconnaissance on: {domain}
        
        Use these modules (select relevant ones):
        {chr(10).join(f"- {k}: {v}" for k, v in self.MODULES.items())}
        
        Return structured JSON with:
        {{
            "domain": "{domain}",
            "linkedin": {{"employees": [...], "funding": "..."}},
            "tech_stack": ["tech1", "tech2"],
            "dns_records": [...],
            "subdomains": [...],
            "breaches": [...],
            "exposed_assets": [...],
            "risk_signals": [...]
        }}
        """
        
        response = self.client.messages.create(
            model=self.model,
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return {
            "raw": response.content[0].text,
            "domain": domain
        }

import pytest
from arven_osint.core.public_apis_client import PublicAPIsClient


@pytest.fixture
def public_apis():
    return PublicAPIsClient()


@pytest.mark.asyncio
async def test_enrich(public_apis):
    """Test data enrichment"""
    osint_data = {"domain": "example.com"}
    tech_data = {"technologies": ["AWS"]}
    
    result = await public_apis.enrich("example.com", osint_data, tech_data)
    
    assert "github_repos" in result
    assert "company_info" in result
    assert "certificates" in result


def test_apis_config(public_apis):
    """Test API configuration"""
    assert "github" in PublicAPIsClient.APIS
    assert "crunchbase" in PublicAPIsClient.APIS
    assert "opencorporates" in PublicAPIsClient.APIS

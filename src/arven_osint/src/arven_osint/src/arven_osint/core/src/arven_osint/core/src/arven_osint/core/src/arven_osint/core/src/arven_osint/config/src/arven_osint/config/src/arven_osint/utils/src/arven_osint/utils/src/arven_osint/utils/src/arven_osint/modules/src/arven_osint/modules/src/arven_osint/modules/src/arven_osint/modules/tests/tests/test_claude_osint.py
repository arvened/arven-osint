import pytest
from arven_osint.core.claude_osint import ClaudeOSINT


@pytest.fixture
def claude_osint():
    return ClaudeOSINT(api_key="test_key")


@pytest.mark.asyncio
async def test_recon(claude_osint):
    """Test OSINT reconnaissance"""
    result = await claude_osint.recon("example.com")
    assert result["domain"] == "example.com"


def test_modules():
    """Test available modules"""
    assert "linkedin" in ClaudeOSINT.MODULES
    assert "domain" in ClaudeOSINT.MODULES
    assert "tech_stack" in ClaudeOSINT.MODULES

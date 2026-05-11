import pytest
from arven_osint.core.graphify_engine import GraphifyEngine


@pytest.fixture
def graphify():
    return GraphifyEngine()


@pytest.mark.asyncio
async def test_analyze(graphify):
    """Test knowledge graph analysis"""
    osint_data = {"tech_stack": ["AWS", "Kubernetes", "PostgreSQL"]}
    result = await graphify.analyze("example.com", osint_data)
    
    assert result["domain"] == "example.com"
    assert "architecture" in result


def test_infer_architecture(graphify):
    """Test architecture inference"""
    techs = ["AWS", "Kubernetes", "PostgreSQL"]
    arch = graphify._infer_architecture(techs)
    
    assert arch["cloud"] == "AWS"
    assert arch["container"] == "K8s"
    assert arch["database"] == "SQL"

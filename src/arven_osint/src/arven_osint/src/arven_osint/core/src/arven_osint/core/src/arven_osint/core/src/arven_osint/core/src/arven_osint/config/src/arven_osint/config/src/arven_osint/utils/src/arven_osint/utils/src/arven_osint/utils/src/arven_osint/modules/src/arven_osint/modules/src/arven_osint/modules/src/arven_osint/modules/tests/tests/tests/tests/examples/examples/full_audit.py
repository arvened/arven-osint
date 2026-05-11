import asyncio
from arven_osint import ArvenOSINT


async def full_audit(domain: str):
    """Full company intelligence audit"""
    
    osint = ArvenOSINT()
    
    print(f"\n🔍 Starting full audit for: {domain}\n")
    
    result = await osint.analyze_company(domain)
    
    print(f"━━━ COMPANY AUDIT ━━━")
    print(f"Domain: {result.company}")
    print(f"\n⚠️  Risk Score: {result.risk_score:.2f}/1.0")
    
    print(f"\n📈 Growth Signals:")
    for signal in result.signals:
        print(f"  • {signal}")
    
    print(f"\n🛠️  Tech Stack:")
    for tech in result.tech_stack:
        print(f"  • {tech}")
    
    print(f"\n📊 Full Data:")
    print(result.data)


if __name__ == "__main__":
    domain = "example.com"
    asyncio.run(full_audit(domain))

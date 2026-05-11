import asyncio
from arven_osint import ArvenOSINT


async def main():
    """Basic OSINT reconnaissance example"""
    
    osint = ArvenOSINT()
    
    # Analyze a company
    result = await osint.analyze_company("example.com")
    
    print(f"Company: {result.company}")
    print(f"Risk Score: {result.risk_score}")
    print(f"Signals: {result.signals}")
    print(f"Tech Stack: {result.tech_stack}")


if __name__ == "__main__":
    asyncio.run(main())

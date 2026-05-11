from setuptools import setup, find_packages

setup(
    name="arven-osint",
    version="0.1.0",
    description="Universal OSINT & intelligence platform for ARVEN products",
    author="ARVEN AI",
    author_email="tech@arven.ai",
    url="https://github.com/arvened/arven-osint",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=[
        "anthropic>=0.7.0",
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
        "pydantic>=2.0.0",
        "aiohttp>=3.8.0",
        "beautifulsoup4>=4.12.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-asyncio>=0.21",
        ]
    },
)

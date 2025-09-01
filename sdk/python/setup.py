from setuptools import setup, find_packages
import os

# Read the contents of your README file
# This will be used as the long description
with open(os.path.join(os.path.dirname(__file__), '../../README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="sheikh-sdk",
    version="1.2.3",  # Auto-updated by CI/CD
    description="Python SDK for Sheikh LLM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Sheikh Development Team",
    url="https://github.com/username/sheikh-llm",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "pydantic>=1.8.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)

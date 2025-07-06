from setuptools import setup, find_packages

setup(
    name="code_monster",
    version="1.0.0",
    description="Das kompromissloseste Clean-Code Toolkit für Python-Projekte",
    long_description=open("README_Wissensdatenbank.md").read(),
    long_description_content_type="text/markdown",
    author="Philipp",
    author_email="code@monster.dev",
    url="https://github.com/code-monster",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "requests",
        "aiohttp",
        "pydantic>=2.0",
    ],
    extras_require={
        "dev": [
            "pytest",
            "black",
            "ruff",
            "mypy",
            "isort",
            "coverage",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
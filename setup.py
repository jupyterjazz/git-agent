from setuptools import find_packages, setup

setup(
    name="git-agent",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "langchain>=0.0.200",
        "openai",
        "colorama",
    ],
    entry_points={
        "console_scripts": [
            "git-agent = git_agent.main:main",
        ],
    },
)

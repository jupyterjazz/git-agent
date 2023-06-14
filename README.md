# Git Agent
Langchain-based Agent utilizing OpenAI Functions to help you with a couple of Git commands



https://github.com/jupyterjazz/git-agent/assets/45267439/c1c524bb-a42f-49b0-940a-7e5a4c722217


## Install

1. Install `git-agent`

```shell
pip install git+https://github.com/jupyterjazz/git-agent.git
```

2. Set your OPENAI_API_KEY

```shell
export OPENAI_API_KEY=<your key>
```

## Usage

Move to any repository you have locally, and ask `git-agent` to show diffs, stage/restore files in natural language!

```shell
git-agent show me all changes I made on docarray files
```


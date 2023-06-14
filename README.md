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
git-agent <your instruction>
```

In this example, `git-agent` will locate files associated with `docarray` and provide the corresponding diffs only for those files.

<img width="823" alt="Screenshot 2023-06-14 at 13 34 44" src="https://github.com/jupyterjazz/git-agent/assets/45267439/6c9c662b-f03a-442f-a2d4-19e43604be65">



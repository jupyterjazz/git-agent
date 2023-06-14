# Git Agent
Langchain-based Agent utilizing OpenAI Functions to help you with a couple of Git commands



https://github.com/jupyterjazz/git-agent/assets/45267439/c1c524bb-a42f-49b0-940a-7e5a4c722217


## Install

1. Clone the repository
```shell
git clone https://github.com/jupyterjazz/git-agent.git
```

2. Move to the project dir
```shell
cd git-agent
```

3. Create a venv
```shell
python3 -m venv venv
source venv/bin/activate
```

4. Set your OPENAI_API_KEY

```shell
export OPENAI_API_KEY=<your key>
```

5. Pip install `git-agent`
```shell
pip install -e .
```

## Usage

Move to any repository you have locally, and ask `git-agent` to show diffs, stage/restore files in natural language!

```shell
git-agent show me all changes I made on docarray files
```


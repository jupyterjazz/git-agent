import json
import sys

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from langchain.tools import format_tool_to_openai_function

from git_agent.tools import GitAddTool, GitDiffTool, GitRestoreTool, git_status


def execute(prompt, model):
    tools = [GitAddTool(), GitDiffTool(), GitRestoreTool()]
    functions = [format_tool_to_openai_function(t) for t in tools]
    context = git_status()
    message = model.predict_messages(
        [
            HumanMessage(
                content=f'For your output, utilize the provided project status information below. '
                        f'This will aid in effectively carrying out the instructions '
                        f'requested subsequently: \n """ \n {context} \n """ \n Instruction: {prompt}'
            )
        ],
        functions=functions,
    )
    fn_name = message.additional_kwargs["function_call"]["name"]
    files = json.loads(message.additional_kwargs["function_call"]["arguments"]).get("files")
    for tool in tools:
        if fn_name == tool.name:
            tool._run(files)


def main():
    prompt = " ".join(sys.argv[1:])
    model = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-0613")
    execute(prompt, model)


if __name__ == "__main__":
    main()

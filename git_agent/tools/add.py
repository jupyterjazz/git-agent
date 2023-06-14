import os
import subprocess
from typing import List, Optional, Type

from colorama import Fore, Style
from langchain.callbacks.manager import (AsyncCallbackManagerForToolRun,
                                         CallbackManagerForToolRun)
from langchain.tools.base import BaseTool
from pydantic import BaseModel, Field


class GitAddInput(BaseModel):
    """Input for GitAddTool."""

    files: List[str] = Field(
        ...,
        description="Collection of file paths intended for staging through the 'git add' operation.",
    )


class GitAddTool(BaseTool):
    name: str = "git_add"
    args_schema: Type[BaseModel] = GitAddInput
    description: str = "Facilitates the staging of file modifications within your working directory, preparing them for the next git commit."

    def _run(
        self,
        files: List[str],
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> None:
        try:
            repo_path = os.getcwd()
            subprocess.run(
                ["git", "add", *files], cwd=repo_path, capture_output=True, text=True
            )

            # The "stdout" attribute contains the output
            print("Staging:")
            for file in files:
                print(Fore.GREEN + file)

        except Exception as e:
            print(f"An error occurred: {e}")

    async def _arun(
        self,
        source_path: str,
        destination_path: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        # TODO: Add aiofiles method
        raise NotImplementedError

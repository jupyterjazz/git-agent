import os
import subprocess
from typing import List, Optional, Type

from colorama import Fore, Style
from langchain.callbacks.manager import (AsyncCallbackManagerForToolRun,
                                         CallbackManagerForToolRun)
from langchain.tools.base import BaseTool
from pydantic import BaseModel, Field


class GitDiffInput(BaseModel):
    """Input for GitDiffTool."""

    files: Optional[List[str]] = Field(
        None,
        description="Optional collection of file paths to display differences. If not provided, differences for all tracked files will be shown.",
    )


class GitDiffTool(BaseTool):
    name: str = "git_diff"
    args_schema: Type[BaseModel] = GitDiffInput
    description: str = "Generates a summary of changes between the working directory and the last commit, or between specified files if provided."

    def _run(
        self,
        files: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> None:
        try:
            repo_path = os.getcwd()
            if not files:
                files = []
            result = subprocess.run(
                ["git", "diff", *files], cwd=repo_path, capture_output=True, text=True
            )

            lines = result.stdout.split("\n")
            for line in lines:
                if line.startswith("diff --git"):
                    print(Fore.CYAN + line)
                elif line.startswith("---") or line.startswith("+++"):
                    print(Fore.MAGENTA + line)
                elif line.startswith("@@"):
                    print(Fore.YELLOW + line)
                elif line.startswith("-"):
                    print(Fore.RED + line)
                elif line.startswith("+"):
                    print(Fore.GREEN + line)
                else:
                    print(Style.RESET_ALL + line)

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

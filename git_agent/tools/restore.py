import os
import subprocess
from typing import List, Optional, Type

from colorama import Fore, Style
from langchain.callbacks.manager import (AsyncCallbackManagerForToolRun,
                                         CallbackManagerForToolRun)
from langchain.tools.base import BaseTool
from pydantic import BaseModel, Field


class GitRestoreInput(BaseModel):
    """Input for GitRestoreTool."""

    files: List[str] = Field(
        ...,
        description="Collection of file paths intended for restoration to their state in the last commit.",
    )


class GitRestoreTool(BaseTool):
    name: str = "git_restore"
    args_schema: Type[BaseModel] = GitRestoreInput
    description: str = (
        "Restores the specified files to their state at the time of the last commit."
    )

    def _run(
        self,
        files: List[str],
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        try:
            repo_path = os.getcwd()
            subprocess.run(
                ["git", "restore", *files],
                cwd=repo_path,
                capture_output=True,
                text=True,
            )
            print("Restoring:")
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

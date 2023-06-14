import os
import subprocess


def git_status():
    try:
        # Change 'your_directory_path' to your git repository path
        repo_path = os.getcwd()

        # the "cwd" parameter is used to set the current working directory
        result = subprocess.run(
            ["git", "status"], cwd=repo_path, capture_output=True, text=True
        )

        # The "stdout" attribute contains the output
        return result.stdout

    except Exception as e:
        print(f"An error occurred: {e}")

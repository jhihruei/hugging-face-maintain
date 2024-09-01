import argparse
import subprocess
import sys

from config import SPACE_CONFIG
from model import Space


def force_push_to_remote(space: Space, username: str, token: str, branch_name: str):
    proc = subprocess.run(
        [
            "git",
            "push",
            "--force",
            f"https://{username}:{token}@huggingface.co/spaces/{space.owner}/{space.name}",
            f"{branch_name}:main",
        ],
        capture_output=True,
    )

    if proc.returncode == 0:
        # NOTE: `git push` output always goes to stderr
        results = proc.stderr.decode("utf-8")
        return results

    print(f"Failed to push remote: {proc.stderr.decode('utf-8')}")
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deploy to Hugging Face spaces.")
    parser.add_argument("--branch_name", required=True)
    parser.add_argument("--username", required=True)
    parser.add_argument("--user_token", required=True)
    args = parser.parse_args()

    space = Space(SPACE_CONFIG["default"])

    push_result = force_push_to_remote(
        space, args.username, args.user_token, args.branch_name
    )
    if not push_result:
        sys.exit(1)
    print(push_result)
    sys.exit(0)

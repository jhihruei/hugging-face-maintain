import argparse
import sys

from config import DEV_SPACE_CONFIG, PRODUCTION_SPACE_CONFIG
from model import ReadMe, Space

DEFAULT_USER = "jy-raychen"


def readme_template(readme: ReadMe):
    return f"""---
title: {readme.title}
emoji: {readme.emoji}
colorFrom: {readme.color_from}
colorTo: {readme.color_to}
sdk: {readme.sdk}
sdk_version: {readme.sdk_version}
app_file: {readme.app_file}
pinned: {readme.pinned}
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate Hugging Face space config file (i.e. README.md)."
    )
    parser.add_argument("--mode", required=True, choices=["prod", "dev"])
    parser.add_argument(
        "--deployer",
        help="The actor in Github Actions, it used to choose space config in dev mode.",
    )
    args = parser.parse_args()

    try:
        if args.mode == "prod":
            space = Space(PRODUCTION_SPACE_CONFIG["production"])
        elif args.mode == "dev":
            space_config = DEV_SPACE_CONFIG.get(
                args.deployer, DEV_SPACE_CONFIG["default"]
            )
            space = Space(space_config)
    except Exception:
        print("Error: The space is not set correctly!")
        sys.exit(1)

    readme = readme_template(space.readme)
    print(readme)
    sys.exit(0)

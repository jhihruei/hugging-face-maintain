import argparse
import sys

from config import PRODUCTION_SPACE_CONFIG
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
    args = parser.parse_args()

    if args.mode == "prod":
        space = Space(PRODUCTION_SPACE_CONFIG["default"])
    elif args.mode == "dev":
        # TODO: Use dev space config when deploy to dev environment.
        space = Space(PRODUCTION_SPACE_CONFIG["default"])

    readme = readme_template(space.readme)
    print(readme)
    sys.exit(0)

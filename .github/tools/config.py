from typing import Dict, Literal

from model import Config

UserName = Literal["default"]

SPACE_CONFIG: Dict[UserName, Config] = {
    "default": {
        "space_name": "example",
        "space_owner": "jy-raychen",
        "space_readme": {
            "title": "Hugging Face Maintain",
            "emoji": "🏢",
            "color_from": "blue",
            "color_to": "indigo",
            "sdk": "gradio",
            "sdk_version": "4.36.0",
            "app_file": "app.py",
            "pinned": False,
        },
    }
}

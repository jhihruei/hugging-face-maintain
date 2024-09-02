from typing import Dict, Literal

from model import Config

ProductionSpace = Literal["production"]

PRODUCTION_SPACE_CONFIG: Dict[ProductionSpace, Config] = {
    "production": {
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

UserName = Literal["default", "jhihruei"]

DEV_SPACE_CONFIG: Dict[UserName, Config] = {
    "default": {
        "space_name": "dev-space",
        "space_owner": "jy-raychen",
        "space_readme": {
            "title": "Hugging Face Developing",
            "emoji": "🏢",
            "color_from": "blue",
            "color_to": "indigo",
            "sdk": "gradio",
            "sdk_version": "4.36.0",
            "app_file": "app.py",
            "pinned": False,
        },
    },
    "jhihruei": {
        "space_name": "personal-dev",
        "space_owner": "jy-raychen",
        "space_readme": {
            "title": "Personal Developing",
            "emoji": "🏢",
            "color_from": "yellow",
            "color_to": "indigo",
            "sdk": "gradio",
            "sdk_version": "4.21.0",
            "app_file": "app.py",
            "pinned": False,
        },
    },
}

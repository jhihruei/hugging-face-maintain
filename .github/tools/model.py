from typing import TypedDict


class ReadMeConfig(TypedDict):
    title: str
    emoji: str
    color_from: str
    color_to: str
    sdk: str
    sdk_version: str
    app_file: str
    pinned: bool


class ReadMe:
    title: str
    emoji: str
    color_from: str
    color_to: str
    sdk: str
    sdk_version: str
    app_file: str
    pinned: str

    def __init__(self, readme_config: ReadMeConfig):
        self.title = readme_config["title"]
        self.emoji = readme_config["emoji"]
        self.color_from = readme_config["color_from"]
        self.color_to = readme_config["color_to"]
        self.sdk = readme_config["sdk"]
        self.sdk_version = readme_config["sdk_version"]
        self.app_file = readme_config["app_file"]
        self.pinned = str(readme_config["pinned"]).lower()


class Config(TypedDict):
    space_name: str
    space_owner: str
    space_readme: ReadMe


class Space:
    name: str
    owner: str
    readme: ReadMeConfig

    def __init__(self, config: Config):
        self.name = config["space_name"]
        self.owner = config["space_owner"]
        self.readme = ReadMe(config["space_readme"])

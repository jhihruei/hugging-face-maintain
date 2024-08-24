from typing import TypedDict


class Config(TypedDict):
    space_name: str
    space_owner: str


class Space:
    name: str
    owner: str

    def __init__(self, config: Config):
        self.name = config["space_name"]
        self.owner = config["space_owner"]

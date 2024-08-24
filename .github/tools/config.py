from typing import Dict, Literal

from model import Config

UserName = Literal["default"]

SPACE_CONFIG: Dict[UserName, Config] = {
    "default": {"space_name": "example", "space_owner": "jy-raychen"}
}

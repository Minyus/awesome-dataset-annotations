from pathlib import Path
from smalldict import SmallDict


for p in Path(".").rglob("*.json"):
    print(p)
    SmallDict(str(p)).get(
        list_limit=10,
        json_out=str(p) + "_samples.json",
        yaml_out=str(p) + "_samples.yaml",
    )

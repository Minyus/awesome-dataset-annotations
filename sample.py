from pathlib import Path
from smalldict import SmallDict


for p in Path(".").rglob("*.json"):
    if "_samples" not in str(p):
        print("[Processing] {}".format(p))
        try:
            SmallDict(str(p)).get(
                list_limit=10,
                json_out=str(p) + "_samples.json",
                yaml_out=str(p) + "_samples.yaml",
            )
        except Exception:
            import traceback

            print(traceback.format_exc())

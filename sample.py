from pathlib import Path
from smalldict import SmallDict


for p in Path(".").rglob("*.json"):
    if p.is_file() and "_samples" not in str(p):
        print("[Processing] {}".format(p))
        try:
            SmallDict(str(p)).get(
                dict_limit=100,
                list_limit=100,
                json_out=str(p) + "_samples.json",
                yaml_out=str(p) + "_samples.yaml",
            )
        except Exception:
            import traceback

            print(traceback.format_exc())

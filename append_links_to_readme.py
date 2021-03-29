from pathlib import Path, PurePosixPath

dirs = set()

out = ""
for p in Path(".").rglob("*"):
    if p.is_file() and "_samples" in p.name:
        dir = p.parts[0]
        if dir not in dirs:
            out += "\n- {}".format(dir)
            dirs.add(dir)
        out += "\n  - [{}]({})".format(p.name, PurePosixPath(p))
out += "\n"

with open("README.md", mode="a") as f:
    f.write(out)

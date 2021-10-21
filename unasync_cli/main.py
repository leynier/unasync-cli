from distutils.dir_util import copy_tree
from os import system
from os.path import exists, join
from pathlib import Path
from shutil import rmtree
from typing import List

from typer import Argument, Typer

app = Typer()


@app.command()
def run(
    paths: List[Path] = Argument(
        ...,
        exists=True,
        file_okay=False,
        writable=True,
        resolve_path=True,
    )
):
    if exists("build"):
        rmtree("build")
    system("python build_sync.py build")
    folders = [
        folder
        for path in paths
        for folder in Path(str(path)).glob("**/_sync")
        if folder.is_dir()
    ]
    for folder in folders:
        rmtree(str(folder))
    folders = [
        folder
        for path in paths
        for folder in Path(
            join("build", "lib", str(path.relative_to(Path.cwd())))
        ).glob("**/_sync")
        if folder.is_dir()
    ]
    print("=====================================", folders)
    for folder in folders:
        source = str(folder)
        target = str(folder).removeprefix(join("build", "lib"))[1:]
        copy_tree(source, target)
    if exists("build"):
        rmtree("build")

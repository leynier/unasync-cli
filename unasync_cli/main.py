from distutils.dir_util import copy_tree
from os import remove, system
from os.path import exists, join
from pathlib import Path
from random import randint
from shutil import rmtree
from typing import List

from typer import Argument, Typer

app = Typer()

build_sync_content = """
from setuptools import find_packages, setup
from unasync import cmdclass_build_py

setup(
    packages=find_packages(),
    cmdclass={"build_py": cmdclass_build_py()},  # type: ignore
)
"""


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
    build_sync_name = f"build_sync_{randint(1, 10**6)}.py"
    with open(build_sync_name, "w") as f:
        f.write(build_sync_content)
    python = "python3"
    if system(f"{python} --version"):
        python = "python"
    system(f"{python} {build_sync_name} build")
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
    for folder in folders:
        source = str(folder)
        target = str(folder).removeprefix(join("build", "lib"))[1:]
        copy_tree(source, target)
    if exists("build"):
        rmtree("build")
    if exists(build_sync_name):
        remove(build_sync_name)

from pathlib import Path
import shutil


def bare_web(path, appname):
    print(f'{path=}')
    print(f'{appname=}')
    print(f'{(path / appname)=}')
    print(f"{((Path(__file__).parent / 'template', path / appname))=}")
    shutil.copytree(Path(__file__).parent / 'template', path / appname)

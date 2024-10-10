from pathlib import Path
import shutil
import subprocess


def bare_web(path, appname):
    print(f'{path=}')
    print(f'{appname=}')
    print(f'{(path / appname)=}')
    print(f"{((Path(__file__).parent / 'template', path / appname))=}")
    shutil.copytree(Path(__file__).parent / 'template', path / appname)
    subprocess.run('npx create-vue frontend --default', shell=True, cwd=path / appname)

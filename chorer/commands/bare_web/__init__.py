from pathlib import Path
import shutil
import subprocess


def invoke(path, appname):
    shutil.copytree(Path(__file__).parent / 'template', path / appname)
    subprocess.run('npx create-vue frontend --default', shell=True, cwd=path / appname)


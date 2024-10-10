from pathlib import Path
import shutil
import subprocess


def invoke(path, appname):
    shutil.copytree(Path(__file__).parent / 'template', path / appname)
    subprocess.run('PIPENV_VENV_IN_PROJECT=1 pipenv install -d', shell=True, cwd=path / appname / backend)
    subprocess.run('npx create-vue frontend --default', shell=True, cwd=path / appname)
    subprocess.run('npm install', shell=True, cwd=path / appname / 'frontend')


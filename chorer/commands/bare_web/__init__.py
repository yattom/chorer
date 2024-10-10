from pathlib import Path
import shutil
import subprocess


def invoke(path, appname):
    resource = Path(__file__).parent
    shutil.copytree(resource / 'template', path / appname)
    subprocess.run('PIPENV_IGNORE_VIRTUALENVS=1 PIPENV_VENV_IN_PROJECT=1 pipenv install -d', shell=True, cwd=path / appname / 'backend')
    subprocess.run('npx create-vue frontend --default', shell=True, cwd=path / appname)
    subprocess.run('npm install', shell=True, cwd=path / appname / 'frontend')
    shutil.copy(resource / 'Node.gitignore', path / appname / 'frontend')
    subprocess.run(f'patch < {(resource / "vite.config.js.diff").absolute()}', shell=True, cwd=path / appname / 'frontend')
    subprocess.run(f'git init', shell=True, cwd=path / appname)
    subprocess.run(f'git add .', shell=True, cwd=path / appname)
    subprocess.run(f'git commit -m init', shell=True, cwd=path / appname)

    guidance = '''
Bare minimum web application is built.

Compile front end asset with:
    $ cd frontend
    $ npm run build

Start service:
    $ cd backend
    $ pipenv run flask --app src run --debug
'''
    return guidance


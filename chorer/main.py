import sys
from click import command, option, argument
from pathlib import Path


@command
@option('--appname', default='webapp')
@argument('path')
def bare_web(path, appname):
    """build bare web application"""
    from .commands.bare_web import bare_web as m
    return m.bare_web(Path(path), appname)


if __name__=='__main__':
    print('specify a subcommand', file=sys.stderr)
    sys.exit(255)

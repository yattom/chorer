import sys
from click import command


@command
def bare_web():
    """build bare web application"""
    pass


if __name__=='__main__':
    print('specify a subcommand', file=sys.stderr)
    sys.exit(255)

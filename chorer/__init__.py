import sys
from click import command, option, argument, group, pass_context, echo, style
from pathlib import Path


@group
@pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        echo(click,style('specify a subcommand'))
        echo(cli.get_help(ctx))


@cli.command
@option('--appname', default='webapp')
@argument('path')
def bare_web(path, appname):
    """build bare web application"""
    from .commands.bare_web import invoke
    guidance = invoke(Path(path), appname)
    echo(guidance)



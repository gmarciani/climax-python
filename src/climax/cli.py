#!/bin/env python3

import click

from climax.commands import command1, command2
from climax.utils import guiutils, logutils

logger = logutils.get_logger(__name__)


@click.group(invoke_without_command=True, context_settings=dict(max_content_width=120))
@click.option("--debug/--no-debug", default=False, show_default=True, type=bool, help="Activate/Deactivate debug mode.")
@click.pass_context
@click.version_option(version="1.0.0")
def main(ctx, debug):
    print(guiutils.get_splash())
    if ctx.invoked_subcommand is None:
        print(ctx.get_help())
    else:
        logutils.set_log_level(logger, "DEBUG" if debug else "INFO")
        logger.debug("Debug Mode: {}".format("on" if debug else "off"))


@main.command(help="Executes the 1st command.")
@click.option(
    "-s",
    "--string",
    required=False,
    type=click.STRING,
    help="Not blank string.",
)
@click.option(
    "-l",
    "--list",
    required=False,
    type=click.STRING,
    help="Comma separated list of values.",
)
@click.option(
    "-f",
    "--file",
    required=False,
    type=click.Path(exists=True),
    help="Path to a readable file.",
)
@click.option(
    "-b",
    "--boolean",
    required=False,
    type=click.BOOL,
    help="Boolean flag.",
)
@click.pass_context
def command1(ctx, string, array, file, boolean):
    logger.debug("string=", string)
    logger.debug("array=", array)
    logger.debug("file=", file)
    logger.debug("boolean=", boolean)
    command1.run()


@main.command(help="Executes the 2nd command.")
@click.option(
    "-s",
    "--string",
    required=False,
    type=click.STRING,
    help="Not blank string.",
)
@click.option(
    "-l",
    "--list",
    required=False,
    type=click.STRING,
    help="Comma separated list of values.",
)
@click.option(
    "-f",
    "--file",
    required=False,
    type=click.Path(exists=True),
    help="Path to a readable file.",
)
@click.option(
    "-b",
    "--boolean",
    required=False,
    type=click.BOOL,
    help="Boolean flag.",
)
@click.pass_context
def command2(ctx, string, array, file, boolean):
    logger.debug("string=", string)
    logger.debug("array=", array)
    logger.debug("file=", file)
    logger.debug("boolean=", boolean)
    command2.run()


if __name__ == "__main__":
    main(obj={})

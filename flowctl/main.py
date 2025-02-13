import click
import sys
import logging
from flowctl.cli.check import run_check

# Configure logging inline with a simple format (only message)
logging.basicConfig(level=logging.INFO, format="%(message)s")


@click.group(context_settings=dict(help_option_names=["-H", "--help"]))
def cli():
    """Flowctl tool with multiple modes."""
    pass


@cli.command()
@click.option("--hostname", "-h", required=True, help="Hostname to check")
@click.option("--verbose", "-v", is_flag=True, help="Display detailed error messages")
def check(hostname, verbose):
    """
    Check mode: Validates whether a given hostname is legal.
    """
    if verbose:
        # Update logging to a detailed format and set level to DEBUG.
        logging.getLogger().setLevel(logging.DEBUG)
        detailed_formatter = logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        for handler in logging.getLogger().handlers:
            handler.setFormatter(detailed_formatter)
    exit_code = run_check(hostname, verbose)
    sys.exit(exit_code)


if __name__ == "__main__":
    cli()

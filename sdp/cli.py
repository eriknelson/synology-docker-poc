import click
from loguru import logger
from sdp.hello import hello

@click.command
def run():
    logger.debug('cli.run')
    hello()

def main():
    run()


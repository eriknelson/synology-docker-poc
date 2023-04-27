import click
from loguru import logger

@click.command
def run():
    logger.info('Hello world, this is sdp.')

def main():
    run()

import os
import click
import docker
from loguru import logger
from sdp.hello import hello

SDP_VOL_DEST_DIR='/var/sdp'
SDP_DOCKER_SOCK_FILE='/var/run/docker.sock'
SCRATCH_DIR_NAME = 'scratch'
FQIN = 'ghcr.io/eriknelson/synology-docker-poc'

@click.command
def run():
    logger.debug('cli.run')

    scratch_dir = os.path.join(SDP_VOL_DEST_DIR, SCRATCH_DIR_NAME)
    if not os.path.exists(scratch_dir):
        os.makedirs(scratch_dir)
    sdp_vol_src_dir = os.getenv('SDP_VOL_SRC_DIR')
    assert sdp_vol_src_dir

    docker_client = docker.DockerClient(base_url='unix://var/run/docker.sock')
    vols = {}
    vols[sdp_vol_src_dir] = { 'bind': SDP_VOL_DEST_DIR, 'mode': 'rw' }
    container_args = {
        'volumes': vols,
        'detach': True,
        'user': os.getuid(),
        'group_add': [os.getuid()],
        'command': 'sdp',
    }
    container = docker_client.containers.run(FQIN, **container_args)
    for log in container.logs(stream=True):
        print(log.decode('utf-8'))
    result = container.wait()
    container.remove()

def main():
    run()

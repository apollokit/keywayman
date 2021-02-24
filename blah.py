import logging

import click

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

form = "%(asctime)s %(levelname)-8s %(funcName)-15s %(message)s"
logging.basicConfig(format=form,
                    datefmt="%H:%M:%S")

@click.group()
def cli():
    """This function is necessary for the click CLI to work."""

@cli.command()
@click.option('--camera', type=int, default=None, 
    help='The integer camera identifier. 0 if only one camera connected.')
@click.option('--video', default=None, 
        help='Path to the video file. Only used if'
        'the camera argument is not supplied')
@click.option('--detector_type',
    default='darknet', 
    type=click.Choice([
        'darknet',
        'xnor'], case_sensitive=False),
    help='The detector type to use.')
@click.option("--use_existing/--no-use_existing",
    is_flag=True,
    default=False,
    help="Whether or not to reload existing file info and object counts.")

def go(
        camera: int,
        video: str,
        detector_type,
        use_existing: bool
    ):
    logger.info(f'hey')

if __name__ == '__main__':
    cli()
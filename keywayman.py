from concurrent.futures import ThreadPoolExecutor, as_completed
import logging
import queue

import click 
import yaml

from executor import executor_thread
from keyboard_listener import hotkey_listener

form = "%(asctime)s %(levelname)-8s %(name)-15s %(message)s"
logging.basicConfig(format=form,
                    datefmt="%H:%M:%S")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

@click.group()
def cli():
    pass

@cli.command()
@click.option("--keystrokes", type=str,
    default="keystrokes_default.yaml",
    help="File from which to import keystrokes.")
def go(
    keystrokes: str,
    ):
    logging.info('Running')

    keystrokes_file = keystrokes

    with open(keystrokes_file, 'r') as f:
        keystrokes_list = yaml.load(f, Loader=yaml.FullLoader)

    # need to start up the hotkey listener thread separately
    hotkey_listener.start()

    # start other threads
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        futures.append(executor.submit(
            executor_thread, 
            keystrokes_list))
        for future in as_completed(futures):
            logger.debug(f"Thread exit: {repr(future.exception())}")

if __name__ == '__main__':
    cli()

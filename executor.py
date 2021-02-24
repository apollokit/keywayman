import logging
import sys
import traceback
from typing import List

from events import event_mngr
from keystrokes import execute_keys 

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

form = "%(asctime)s %(levelname)-8s %(funcName)-15s %(message)s"
logging.basicConfig(format=form,
                    datefmt="%H:%M:%S")
    
def executor_thread(keystrokes_list: List[str]):
    """ Execution thread for typing keystrokes
    
    Args:
        keystrokes_list: list of keystroke commands
    """

    logger.info('Executor thread ready')
    
    # the main thread loop. Go forever.
    while True:
        # wait until triggered
        event_mngr.trigger.wait()

        logger.debug('Triggered')
        
        try:
            keys = keystrokes_list[0]['keys']
            execute_keys(keys)
        except Exception:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback)
            # logger.info("Parsing error: {}".format(str(e)))
        finally:
            event_mngr.trigger.clear()
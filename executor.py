import logging
import sys
import time
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
            # from testing, we need a delay between the triggering hotkey and
            # executing keystrokes, if the triggering hotkey uses modifiers.
            # one second was around the lowest number that guaranteed a
            # super+tab would actually execute and tab successfully between
            # windows. YMMV with keystrokes other than super+tab
            time.sleep(1.0) # seconds
            execute_keys(keys)
            logger.debug('Done')
        except Exception:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback)
            # logger.info("Parsing error: {}".format(str(e)))
        finally:
            event_mngr.trigger.clear()
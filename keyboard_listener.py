""" Functionality for dealing with keyboard interactions 
"""

import logging
import threading

from pynput import keyboard

from events import event_mngr
from globals import TRIGGER_HOTKEY

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

form = "%(asctime)s %(levelname)-8s %(funcName)-15s %(message)s"
logging.basicConfig(format=form,
                    datefmt="%H:%M:%S")

def on_trigger():
    """Handles hotkey triggering
    """
    logger.debug('Triggered')
    event_mngr.trigger.set()

# from https://pynput.readthedocs.io/en/latest/keyboard.html#monitoring-the-keyboard
hotkey_listener = keyboard.GlobalHotKeys({
        TRIGGER_HOTKEY: on_trigger})

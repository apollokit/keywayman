import threading

class EventManager:
    """A clearinghouse for coordinating events between threads"""
    
    def __init__(self):
        # indicates if command for executing keystrokes has been trigger
        self.trigger = threading.Event()

# # the global app manager instance
# app_mngr = AppManager()
# the global event manager instance
event_mngr = EventManager()
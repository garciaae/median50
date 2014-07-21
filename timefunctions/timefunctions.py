"""Contains functions for checking computing times"""

import time


def chronometer(funcion):
    """Counts how long does it take to compute a function"""
    def function_to_run(*args):
        """Inner function"""
        start_time = time.time()
        funcion(*args)
        end_time = time.time()
        time_elapsed = end_time - start_time
        return time_elapsed
    return function_to_run

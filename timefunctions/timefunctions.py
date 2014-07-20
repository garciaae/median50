"""Contains functions for checking computing times"""

import time


def chronometer(funcion):
    """Counts how long does it take to compute a function"""
    def function_to_run(*argumentos):
        """Inner function"""
        inicio = time.time()
        funcion(*argumentos)
        fin = time.time()
        tiempo_total = fin - inicio
        return tiempo_total
    return function_to_run

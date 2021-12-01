from functools import wraps
from threading import Thread


def threading_click_handler(daemon_mode: bool = True) -> callable:
    def inner_function(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> None:
            thread = Thread(target=func, args=args, kwargs=kwargs, daemon=daemon_mode)
            thread.start()

        return wrapper

    return inner_function

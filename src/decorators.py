import functools
from datetime import datetime


def log(filename=None):
    """Автоматически логирует начало и конец выполнения фукции и ее результаты или возникшие ошибки"""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:
                result = func(*args, **kwargs)
                log_message = f"{timestamp} - {func_name} ok\n"

                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message)
                else:
                    print(log_message, end="")

                return result

            except Exception as e:
                error_message = f"{timestamp} - {func_name} error: {type(e).__name__}. " f"Inputs: {args}, {kwargs}\n"

                if filename:
                    with open(filename, "a") as f:
                        f.write(error_message)
                else:
                    print(error_message, end="")

                raise  # Пробрасываем исключение дальше

        return wrapper

    return decorator

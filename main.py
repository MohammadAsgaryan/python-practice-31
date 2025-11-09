import json
import time
from functools import wraps
from logger_config import logger


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        exec_time = end - start

        logger.info(f"Function '{func.__name__}' executed in {exec_time:.6f} seconds")
        save_history(func.__name__, exec_time)

        return result
    return wrapper


def save_history(name, exec_time):
    record = {"function": name, "execution_time": exec_time}

    try:
        with open("history.json", "r") as f:
            data = json.load(f)
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        data = []

    data.append(record)

    with open("history.json", "w") as f:
        json.dump(data, f, indent=4)


@timer
def generate_list(n):
    return list(range(1, n+1))


if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        result = generate_list(num)
        print("List generated:", result[:10], "...")  # برای نمایش سریع
        logger.info("Program finished successfully")

    except ValueError:
        logger.error("User entered non-numeric value")
        print("Invalid input! Please enter a number.")

import time
import logging

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(':')


# simple match case statement
def run_match():
    num = int(input("Enter a number between 1 and 3: "))

    # match case
    match num:
        # pattern 1
        case 1:
            return "One"
        # pattern 2
        case 2:
            return "Two"
        # pattern 3
        case 3:
            return "Three"
        # pattern 0
        case 0:
            return False
        # default pattern
        case _:
            return "Number not between 1 and 3"


if __name__ == "__main__":
    while result := run_match():
        _logger.info(f'{result = }\n')
        time.sleep(1)

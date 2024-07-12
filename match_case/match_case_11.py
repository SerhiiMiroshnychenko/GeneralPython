# python match case with if condition
def run_match():
    num = int(input("Enter a number: "))

    # match case
    match num:
        # pattern 1
        case num if num > 0:
            print("Positive")
        # pattern 2
        case num if num < 0:
            print("Negative")
        # default pattern
        case _:
            print("Zero")


if __name__ == "__main__":
    run_match()


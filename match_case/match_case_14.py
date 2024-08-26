# match case with python dictionary
def run_match(dictionary):
    # match case
    match dictionary:
        # pattern 1
        case {"name": n, "age": a}:
            print(f"Name:{n}, Age:{a}")
        # pattern 2
        case {"name": n, "salary": s}:
            print(f"Name:{n}, Salary:{s}")
        # default pattern
        case _:
            print("Data does not exist")


if __name__ == "__main__":
    run_match({"name": "Jay", "age": 24})
    run_match({"name": "Ed", "salary": 25000})
    run_match({"name": "Al", "age": 27})
    run_match({})

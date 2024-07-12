# python match case with list
def run_match(input_data):
    # match case
    match input_data:
        # pattern 1
        case ["a"]:
            print("a")
        # pattern 2
        case ["a", *b]:
            print(f"a and {b}")
        # pattern 3
        case [*a, "e"] | (*a, "e"):
            print(f"{a} and e")
        # default pattern
        case _:
            print("No data")


if __name__ == "__main__":
    run_match([])
    run_match(["a"])
    run_match(["a", "b"])
    run_match(["b", "c", "d", "e"])


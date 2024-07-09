# Function for adding different type variables

def adding(a, b):
    try:
        # Try to add as usual
        return a + b
    except TypeError:
        # Convert to strings and add if above fails
        return str(a) + str(b)


if __name__ == "__main__":
    print(adding(1, 'a'))
    print(adding(1, (1, 2, 3)))
    print(adding({'one': 1, 'two': 2, 3: 'three'}, (1, 2, 3)))

def a_plus_b(a: int or float, b: int or float) -> int or float:
    a_plus_b.values = (a, b)
    a_plus_b.about = 'Return a + b'
    return a + b


if __name__ == "__main__":
    result_1 = a_plus_b(2, 3.0)
    print(f"{result_1 = }")
    result_2 = a_plus_b(3, 4)
    print(f"{result_2 = }")
    print(f"{a_plus_b.values = }")
    print(f"{a_plus_b.about = }")
    print(f"{a_plus_b.__annotations__ = }")
    print(f"{a_plus_b.__class__ = }")
    print(f"{a_plus_b.__name__ = }")
    print(f"{a_plus_b.__repr__() = }")
    print(f"{a_plus_b.__builtins__ = }")
    print(f"{a_plus_b.__code__ = }")
    print(f"{a_plus_b.__defaults__ = }")
    print(f"{a_plus_b.__dict__ = }")
    print(f"{a_plus_b.__dir__() = }")
    print(f"{a_plus_b.__globals__ = }")
    print(f"{a_plus_b.__hash__() = }")
    print(f"{a_plus_b.__kwdefaults__ = }")
    print(f"{a_plus_b.__module__ = }")
    print(f"{a_plus_b.__qualname__ = }")
    print(f"{a_plus_b.__str__() = }")
    print(f"{a_plus_b.__doc__ = }")
    print(f"{a_plus_b = }")


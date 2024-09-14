# match case with python classes
# import dataclass module
from dataclasses import dataclass


# Class 1
@dataclass
class Person:
    name: str
    age: int
    salary: int


# class 2
@dataclass
class Programmer:
    name: str
    language: str
    framework: str


def run_match(instance):
    # match case
    match instance:
        # pattern 1
        case Programmer("Om", language="Python", framework="Django"):
            print(f"Name: Om, Language:Python, Framework:Django")
        # pattern 2
        case Programmer("Rishabh", "C++"):
            print("Name:Rishabh, Language:C++")
        # pattern 3
        case Person("Vishal", age=5, salary=100):
            print("Name:Vishal")
        # pattern 4
        case Programmer(name, language, framework):
            print(f"Name:{name}, Language:{language}, Framework:{framework}")
        # pattern 5
        case Person():
            print("He is just a person !")
        # default case
        case _:
            print("This person is nothiing!")


if __name__ == "__main__":
    programmer1 = Programmer("Om", "Python", "Django")
    programmer2 = Programmer("Rishabh", "C++", None)
    programmer3 = Programmer("Sankalp", "Javascript", "React")
    person1 = Person("Vishal", 5, 100)
    run_match(programmer1)
    run_match(programmer2)
    run_match(person1)
    run_match(programmer3)

"""Simple calculator / greeter app used for coverage demos."""


def greet(name: str | None = None) -> str:
    if not name or not name.strip():
        return "Hello, World!"
    return f"Hello, {name.strip()}!"


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate(operation: str, a: float, b: float) -> float:
    ops = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }
    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")
    return ops[operation](a, b)


def grade(score: int) -> str:
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def main() -> None:
    print(greet("ATIS"))
    print(f"2 + 3 = {calculate('add', 2, 3)}")
    print(f"Grade for 85: {grade(85)}")


if __name__ == "__main__":
    main()

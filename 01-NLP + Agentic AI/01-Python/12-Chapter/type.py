from typing import List, Dict, Tuple

n : int = 66
name: str = "John Doe"

def sum(a: int, b: int) -> int:
    return a + b

result: int = sum(5, 10)

print(f"n: {n}, name: {name}, result: {result}")


number : list[int] = [1, 2, 3, 4, 5]

person: Dict[str, str] = {
    "name": "Alice",
    "email": "alice@example.com"
}
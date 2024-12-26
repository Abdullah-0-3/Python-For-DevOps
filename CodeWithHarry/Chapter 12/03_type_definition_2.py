from typing import List, Tuple, Dict

def fruite_basket(fruit: List[str]) -> None:
    for f in fruit:
        print(f)

fruite_basket(["Apple", "Banana", "Cherry"])

def fruite_basket(fruit: Tuple[str, str, str]) -> None:
    for f in fruit:
        print(f)

fruite_basket(("Apple", "Banana", "Cherry"))

def fruite_basket(fruit: Dict[str, str]) -> None:
    for f in fruit:
        print(f)

fruite_basket({"Apple": "Red", "Banana": "Yellow", "Cherry": "Red"})
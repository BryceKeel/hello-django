from typing import List, Tuple

# A property is a tuple with:
# - a name
# - a nightly price
# - a boolean indicating whether or not it is currently occupied (True means occupied)
Property = Tuple[str, int, bool]

#all less than
def find_all_properties_less_than(properties: List[Property],
                                  cost: int) -> List[Property]:
    return[property for property in properties if property[1] < cost]


#all
def find_all_available_properties(
        properties: List[Property]) -> List[Property]:
    return[property for property in properties if property[2] == False]

#print
def print_properties(properties: List[Property]) -> None:
    if not properties:
      print("NO PROPERTY")
    else:
      for name, price, occupied in properties:
        status = 'Occupied' if occupied else 'Available'
        print(f"{name}\n ${price}/night\n {status}")


# --------------- Do not change provided code.


def input_action() -> str:
    while True:
        action = input("[all]/[available]/[search] properties, or [quit]> ")
        if action in ('all', 'available', 'search', 'quit'):
            return action
        else:
            print("Please provide a valid action.")


def input_maximum_cost() -> int:
    while True:
        unit = input("Maximum Cost: ")
        if unit.isdigit() and int(unit) > 0:
            return int(unit)
        else:
            print("Please provide a valid maximum cost.")


def main() -> None:
    properties = [
        ("Pops Cabin - Lookout Mountain, City-Side", 135, True),
        ("NATURALIST BOUDOIR TOO, Brand New", 243, True),
        ("❤️ Off-Grid Socially Distanced Tiny House--PETS ✔️", 129, False),
        ("Lakefront Modern Tiny Home Getaway", 60, True),
        ("The East Fork Cottage— riverfront tiny home", 125, True),
        ("Tiny Cabin In the Woods", 108, False),
        ("\"Serenity Now\" Cabin is Perfect!", 202, True),
        ("The Tiny Juan! Unique tiny house on 30A -Seagrove!", 153, True),
        ("Tiny Luxury, beach living getaway", 134, False),
        ("Cricket by The Creek", 125, False),
        ("*The Honeysuckle House* - Tiny House, Big Living!", 115, True),
        ("Tiny House Columbia", 67, True),
        ("Old Algiers Garden House", 77, False),
        ("The Nest - Tiny Home Atop Lookout Mountain", 125, False),
        ("Eco-Friendly Tiny House - Modern & Bright", 171, False),
        ("Cozy, Quiet Tiny House- SO Close to Downtown!", 98, False),
        ("Cozy Casita Retreat with Big Backyard in Heart of the City", 127,
         False),
        ("Martha Cabin -Tiny Cabin close to everything", 120, False),
        ("Shangri-Little Tiny House (Live A Little Chatt)", 140, True),
        ("Stefan Cabin - Nature-Nested, City-Side", 116, False),
    ]

    while True:
        action = input_action()
        if action == "all":
            print_properties(properties)
        elif action == "available":
            print_properties(find_all_available_properties(properties))
        elif action == "search":
            maximum_cost = input_maximum_cost()
            print_properties(
                find_all_properties_less_than(properties, maximum_cost))
        elif action == "quit":
            break
        else:
            print("Invalid Action.")


if __name__ == "__main__":
    main()

import json
from datetime import datetime

# Global dictionary to hold stock data
stock_data = {}


def add_item(item: str = "default", qty: int = 0, logs=None):
    """
    FIX 1: Replaced mutable default argument 'logs=[]' with 'logs=None'.
    Mutable defaults (like lists) persist across calls and can cause bugs.
    Initialized a new list inside the function if None is provided.
    """
    if logs is None:
        logs = []

    """
    FIX 2: Added input validation for 'item' and 'qty' to ensure they have correct types.
    This prevents type-related runtime errors, e.g., passing strings as quantities.
    """
    if not isinstance(item, str) or not isinstance(qty, int):
        raise ValueError("Item must be a string and quantity must be an integer.")

    """
    FIX 3: Replaced old '%' string formatting with modern f-strings for better readability.
    """
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item: str, qty: int):
    """
    FIX 4: Replaced bare 'except:' with specific exception types.
    Bare except hides real errors and is considered bad practice.
    Now catches KeyError (missing item) and TypeError (wrong qty type).
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found in stock.")
    except TypeError:
        print(f"Invalid quantity type for removing '{item}'.")


def get_qty(item: str) -> int:
    return stock_data.get(item, 0)


def load_data(file: str = "inventory.json"):
    """
    FIX 5: Added 'with open(...)' context manager for safer file handling.
    FIX 6: Specified encoding='utf-8' to prevent encoding errors across systems.
    FIX 7: Added exception handling for FileNotFoundError to prevent crashes
    when the file does not exist.
    """
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        print(f"File '{file}' not found; starting with empty inventory.")


def save_data(file: str = "inventory.json"):
    """
    FIX 8: Used context manager 'with open(...)' for safe file writing.
    FIX 9: Specified encoding='utf-8' and added indentation for human-readable JSON.
    """
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)


def print_data():
    """
    FIX 10: Modernized print formatting using f-strings.
    """
    print("Items Report")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")


def check_low_items(threshold: int = 5):
    """
    FIX 11: Simplified function using list comprehension for cleaner, Pythonic style.
    """
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """
    FIX 12: Removed unsafe use of 'eval("print(...)")' found in the original code.
    'eval()' executes arbitrary code and is a major security risk.
    Replaced with a normal print statement.
    """
    add_item("apple", 10)
    add_item("banana", 2)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print("Low items:", check_low_items())

    """
    FIX 13: Functions 'save_data()' and 'load_data()' now safely handle files with
    proper context managers and encoding.
    """
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
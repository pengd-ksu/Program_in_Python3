#!/usr/bin/env python3

import os

YES = frozenset({"y", "Y", "yes", "Yes", "YES"})

def main():
    dirty = False
    
    filename, items = choose_file()
    if not filename:
        print("Cancelled")
        return

    while True:
        print("\n --- List Keeper --- \n")
        print_list(items)
        choice = user_choice(items, dirty)
        
        if choice in "Aa":
            dirty = add_item(items, dirty)
        elif choice in "Dd":
            dirty = delete_item(items, dirty)
        elif choice in "Ss":
            dirty = save_list(filename, items)
        elif choice in "Qq":
            if (dirty and (get_string("Save unsaved changes (y/n)",
                                      "yes/no", "y") in YES)):
                save_list(filename, items, True)
            break

def user_choice(items, dirty):
    while True:
        if items:
            if dirty:
                menu = "[A]dd  [D]elete  [S]ave  [Q]uit"
                valid_choices = "AaDdSsQq"
            else:
                menu = "[A]dd  [D]elete  [Q]uit"
                valid_choices = "AaDdQq"
        else:
            menu = "[A]dd  [Q]uit"
            valid_choices = "AaQq"

        choice = get_string(menu, "choice", "a")

        if choice not in valid_choices:
            print("ERROR: invalid choice--enter one of '{0}'".format(
                  valid_choices))
            input("Press Enter to continue...")
        else:
            return choice

def choose_file():
    files = filter_files()
    enter_filename = False

    if not files:
        enter_filename = True

    if not enter_filename:
        print_list(files)
        idx = get_integer("Specify file's number (or 0 to create "
                            "a new one)", "number", maximum=len(files),
                            allow_zero=True)
        if idx == 0:
            enter_filename = True
        else:
            filename = files[idx - 1]
            items = load_list(filename)

    if enter_filename:
        filename = get_string("Choose filename", "filename")
        if not filename.endswith(".lst"):
            filename += ".lst"
        items = []

    return filename, items


def load_list(filename):
    items = []
    fh = None
    try:
        fh = open(filename, "r")
        items = fh.readlines()
    except EnvironmentError as err:
        print(f"ERROR: failed to load {filename}: {err}")
        return []
    finally:
        if fh is not None:
            fh.close()
    return items

def add_item(items, dirty):
    new_item = get_string("Add item", "item")
    if new_item:
        items.append(new_item)
        items.sort(key=str.lower)
        return True
    return dirty

def delete_item(items, dirty):
    idx = get_integer("Delete item number (or 0 to cancel)",
                        "number", maximum=len(items),
                        allow_zero=True)
    if idx != 0:
        del items[idx - 1] # items.pop(idx - 1)
        return True
    return dirty

def save_list(filename, items, terminating=False):
    fh = None
    try:
        fh = open(filename, "w")
        fh.write("\n".join(items))
        fh.write("\n")
    except EnvironmentError as err:
        print(f"ERROR: failed to save {filename}: {err}")
        return True
    else:
        print(f"Saved {len(items)} item{'s' if len(items) != 1 else ''} to {filename}")
        if not terminating:
            input("Press Enter to continue...")
        return False
    finally:
        if fh is not None:
            fh.close()

def print_list(items):
    if not items:
        print("-- no items are in the list --")
    else:
        width = 1 if len(items) < 10 else 2 if len(items) < 100 else 3
        for i, file in enumerate(items, start = 1):
            print(f"Item {i:{width}}: {file}")
    print()

def filter_files():
    files = [file for file in os.listdir(".") if file.endswith(".lst")]
    return files

def get_string(message, name="string", default=None,
               minimum_length=0, maximum_length=80):
    message += ": " if default is None else f" [{default}]: "
    while True:
        try:
            line = input(message)
            if not line:
                if default is not None:
                    return default
                if minimum_length == 0:
                    return ""
                else:
                    raise ValueError(f"{name} may not be empty")
            if not (minimum_length <= len(line) <= maximum_length):
                raise ValueError(f"{name} must have at least "
                        "{minimum_length} and at most "
                        "{maximum_length} characters")
            return line
        except ValueError as err:
            print("ERROR", err)


def get_integer(message, name="integer", default=None, minimum=0,
                maximum=100, allow_zero=True):

    class RangeError(Exception): pass

    message += ": " if default is None else f" [{default}]: "
    while True:
        try:
            line = input(message)
            if not line and default is not None:
                return default
            i = int(line)
            if i == 0:
                if allow_zero:
                    return i
                else:
                    raise RangeError(f"{name} may not be 0")
            if not (minimum <= i <= maximum):
                raise RangeError("{name} must be between {minimum} "
                        "and {maximum} inclusive{0}".format(
                        " (or 0)" if allow_zero else "", **locals()))
            return i
        except RangeError as err:
            print("ERROR", err)
        except ValueError as err:
            print(f"ERROR {name} must be an integer")

if __name__ == "__main__":
    main()

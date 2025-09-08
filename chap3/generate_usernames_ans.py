#!/usr/bin/env python3

import collections
import sys


ID, FORENAME, MIDDLENAME, SURNAME, DEPARTMENT = range(5)

User = collections.namedtuple("User",
            "username forename middlename surname id")


def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print(f"usage: {sys.argv[0]} file1 [file2 [... fileN]]")
        sys.exit()

    usernames = set()
    users = {}
    for filename in sys.argv[1:]:
        with open(filename, encoding="utf8") as file:
            for line in file:
                line = line.rstrip()
                if line:
                    user = process_line(line, usernames)
                    users[(user.surname.lower(), user.forename.lower(),
                            user.id)] = user
    print_users(users)


def process_line(line, usernames):
    fields = line.split(":")
    username = generate_username(fields, usernames)
    user = User(username, fields[FORENAME], fields[MIDDLENAME],
                fields[SURNAME], fields[ID])
    return user


def generate_username(fields, usernames):
    username = ((fields[FORENAME][0] + fields[MIDDLENAME][:1] +
                 fields[SURNAME]).replace("-", "").replace("'", ""))
    username = original_name = username[:8].lower()
    count = 1
    while username in usernames:
        username = f"{original_name}{count}"
        count += 1
    usernames.add(username)
    return username


def by_surname_forename(user):
    return user.surname.lower(), user.forename.lower(), user.id


def print_users(users):
    namewidth = 17
    usernamewidth = 9
    columngap = " " * 2

    headline1 = f"{'Name':<{namewidth}} {'ID':^6} {'Username':<{usernamewidth}}"
    headline2 = f"{'':-<{namewidth}} {'':-<6} {'':-<{usernamewidth}}"
    header = (headline1 + columngap + headline1 + "\n" +
              headline2 + columngap + headline2)

    lines = []
    for key in sorted(users):
        user = users[key]
        initial = ""
        if user.middlename:
            initial = " " + user.middlename[0]
        name = f"{user.surname}, {user.forename}{initial}"
        lines.append(f"{name:.<{namewidth}.{namewidth}} ({user.id:4}) {user.username:<{usernamewidth}}")

    lines_per_page = 64
    lino = 0
    for left, right in zip(lines[::2], lines[1::2]):
        if lino == 0:
            print(header)
        print(left + columngap + right)
        lino += 1
        if lino == lines_per_page:
            print("\f")
            lino = 0
    if lines[-1] != right:
        print(lines[-1])

if __name__ == "__main__":
    main()

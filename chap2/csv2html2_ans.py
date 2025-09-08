#!/usr/bin/env python3

import sys

def main():
    maxwidth, format = process_options()
    if maxwidth is not None:
        print_start()
        count = 0
        while True:
            try:
                line = input()
                if count == 0:
                    color = "lightgreen"
                elif count % 2:
                    color = "white"
                else:
                    color = "lightyellow"
                print_line(line, color, maxwidth, format)
                count += 1
            except EOFError:
                break
        print_end()

def process_options():
    maxwidth_arg = "maxwidth="
    format_arg = "format="
    maxwidth = 100
    format = ".0f"
    for arg in sys.argv[1:]:
        if arg in ["-h", "--help"]:
            print(f"""\
usage:
csv2html.py [maxwidth=int] [format=str] < infile.csv > outfile.html

maxwidth is an optional integer; if specified, it sets the maximum
number of characters that can be output for string fields,
otherwise a default of {maxwidth} characters is used.

format is the format to use for numbers; if not specified it
defaults to "{format}".""")
            return None, None
        elif arg.startswith(maxwidth_arg):
            try:
                maxwidth = int(arg[len(maxwidth_arg):])
            except ValueError:
                pass
        elif arg.startswith(format_arg):
            format = arg[len(format_arg):]
    return maxwidth, format

def print_start():
    print("<table border='1'>")


def print_line(line, color, maxwidth, format):
    print(f"<tr bgcolor='{color}'>")
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                print(f"<td align='right'>{round(x):format}</td>")
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                if len(field) <= maxwidth:
                    field = escape_html(field)
                else:
                    field = f"{escape_html(field[:maxwidth])} ..."
                print(f"<td>{field}</td>")
    print("</tr>")


def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None: # start of quoted string
                quote = c
            elif quote == c:  # end of quoted string
                quote = None
            else:
                field += c    # other quote inside quoted string
            continue
        if quote is None and c == ",": # end of a field
            fields.append(field)
            field = ""
        else:
            field += c        # accumulating a field
    if field:
        fields.append(field)  # adding the last field
    return fields


def escape_html(text):
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    return text


def print_end():
    print("</table>")


main()

#!/usr/bin/env python3

import locale
locale.setlocale(locale.LC_ALL, "")

import datetime
import argparse   # modern replacement for optparse
import os


def main():
    counts = [0, 0]
    opts, paths = process_options()
    if not opts.recursive:
        filenames = []
        dirnames = []
        for path in paths:
            if os.path.isfile(path):
                filenames.append(path)
                continue
            for name in os.listdir(path):
                if not opts.hidden and name.startswith("."):
                    continue
                fullname = os.path.join(path, name)
                if fullname.startswith("./"):
                    fullname = fullname[2:]
                if os.path.isfile(fullname):
                    filenames.append(fullname)
                else:
                    dirnames.append(fullname)
        counts[0] += len(filenames)
        counts[1] += len(dirnames)
        process_lists(opts, filenames, dirnames)
    else:
        for path in paths:
            for root, dirs, files in os.walk(path):
                if not opts.hidden:
                    # Assignment of dirs will create a new list, while the iteration still refers to the original list
                    dirs[:] = [dir for dir in dirs
                               if not dir.startswith(".")]
                filenames = []
                for name in files:
                    if not opts.hidden and name.startswith("."):
                        continue
                    fullname = os.path.join(root, name)
                    if fullname.startswith("./"):
                        fullname = fullname[2:]
                    filenames.append(fullname)
                counts[0] += len(filenames)
                counts[1] += len(dirs)
                process_lists(opts, filenames, [])
    print(f"{counts[0]:,} file{'s' if counts[0] != 1 else ''}, "
        f"{counts[1]:,} director{'ies' if counts[1] != 1 else 'y'}")


def process_lists(opts, filenames, dirnames):
    keys_lines = []
    for name in filenames:
        modified = ""
        if opts.modified:
            try:
                modified = (datetime.datetime.fromtimestamp(
                                os.path.getmtime(name))
                                    .isoformat(" ")[:19] + " ")
            except OSError:   # EnvironmentError -> OSError (modern)
                modified = f"{'unknown':>19} "
        size = ""
        if opts.sizes:
            try:
                size = f"{os.path.getsize(name):>15,} "
            except OSError:   # EnvironmentError -> OSError (modern)
                size = f"{'unknown':>15} "
        if os.path.islink(name):
            name += " -> " + os.path.realpath(name)
        if opts.order in {"m", "modified"}:
            orderkey = modified
        elif opts.order in {"s", "size"}:
            orderkey = size
        else:
            orderkey = name
        keys_lines.append((orderkey, f"{modified}{size}{name}"))
    size = "" if not opts.sizes else " " * 15
    modified = "" if not opts.modified else " " * 20
    for name in sorted(dirnames):
        keys_lines.append((name, modified + size + name + "/"))
    for key, line in sorted(keys_lines):
        print(line)


def process_options():
    usage = """%(prog)s [options] [path1 [path2 [... pathN]]]

The paths are optional; if not given . is used."""

    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument("-H", "--hidden", dest="hidden",
            action="store_true",
            help=("show hidden files [default: off]"))
    parser.add_argument("-m", "--modified", dest="modified",
            action="store_true",
            help=("show last modified date/time [default: off]"))
    orderlist = ["name", "n", "modified", "m", "size", "s"]
    parser.add_argument("-o", "--order", dest="order",
            choices=orderlist, default=orderlist[0],
            help=("order by ({0}) [default: %(default)s]".format(
                  ", ".join(["'" + x + "'" for x in orderlist]))))
    parser.add_argument("-r", "--recursive", dest="recursive",
            action="store_true",
            help=("recurse into subdirectories [default: off]"))
    parser.add_argument("-s", "--sizes", dest="sizes",
            action="store_true",
            help=("show sizes [default: off]"))
    parser.add_argument("paths", nargs="*", default=["."])

    ns = parser.parse_args()
    # Keep the original return shape (opts, paths list)
    opts = ns
    paths = ns.paths if ns.paths else ["."]
    return opts, paths


main()

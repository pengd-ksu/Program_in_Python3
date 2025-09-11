#!/usr/bin/env python3

import argparse, os, datetime
from pathlib import Path

def main():
    counts = [0, 0] # [file, directory]
    opts, paths = parse_option()
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
                fullname = Path(path) / name 
                if os.path.isfile(fullname):
                    filenames.append(str(fullname))
                else:
                    dirnames.append(str(fullname))
        counts[0] += len(filenames)
        counts[1] += len(dirnames)
        print_lists(opts, filenames, dirnames)    
    else:
        for path in paths:
            for root, dirs, files in os.walk(path):
                if not opts.hidden:
                    # Assignment of dirs will create a new list, while the iteration still refers to the original list
                    dirs[:] = [dir for dir in dirs if not dir.startswith(".")]
                filenames = []
                for name in files:
                    if not opts.hidden and name.startswith("."):
                        continue
                    fullname = Path(root) / name
                    filenames.append(str(fullname))
                counts[0] += len(filenames)
                counts[1] += len(dirs)
                print_lists(opts, filenames, [])

    print(f"{counts[0]} file{'s' if counts[0] != 1 else ''} ,"
        f"{counts[1]} director{'ies' if counts[1] != 1 else 'y'}")

def print_lists(opts, filenames, dirnames):
    tuples = []
    for name in filenames:
        modified = ""
        # modified time and size are from the author's original code
        if opts.modified:
            try:
                modified = (datetime.datetime.fromtimestamp(
                                os.path.getmtime(name))
                                    .isoformat(" ")[:19] + " ")
            except OSError:   # EnvironmentError -> OSError (modern)
                modified = f"{'unknown':>19} "
        size = ""
        if opts.size:
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
        tuples.append((orderkey, f"{modified}{size}{name}"))
    size = "" if not opts.size else " " * 15
    modified = "" if not opts.modified else " " * 20
    for name in sorted(dirnames):
        tuples.append((name, modified + size + name + "/"))
    for key, line in sorted(tuples):
        print(line)
    

def parse_option():
    usage = """%(prog)s [options] [path1 [path2 [... pathN]]]

The paths are optional; if not given . is used."""
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument("-H", "--hidden", 
                        action="store_true", default=False,
                        help="show hidden files [default: off]")
    parser.add_argument("-m", "--modified",
                        action="store_true", default=False,
                        help="show last modified date/time [default: off]")
    orderlist = ["name", "n", "modified", "m", "size", "s"]
    parser.add_argument("-o", "--order", default=orderlist[0],
                        help=f"order by ({', '.join(orderlist)}) [default= name]")
    parser.add_argument("-r", "--recursive",
                        action="store_true", default=False,
                        help="recurse into subdirectories [default: off]")
    parser.add_argument("-s", "--size",
                        action="store_true", default=False,
                        help="show sizes [default: off]")
    parser.add_argument("paths", nargs="*", default=["."])
    args = parser.parse_args()
    paths = args.paths
    return args, paths

if __name__ == "__main__":
    main()

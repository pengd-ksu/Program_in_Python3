table = "".maketrans(
    "\N{bengali digit zero}"
    "\N{bengali digit one}\N{bengali digit two}"
    "\N{bengali digit three}\N{bengali digit four}"
    "\N{bengali digit five}\N{bengali digit six}"
    "\N{bengali digit seven}\N{bengali digit eight}"
    "\N{bengali digit nine}",
    "0123456789"
)

print(f"the table: \n{table}\n")
print("20749".translate(table))  # prints: 20749

print(
    "\N{bengali digit two}07\N{bengali digit four}"
    "\N{bengali digit nine}".translate(table)
)  # prints: 20749

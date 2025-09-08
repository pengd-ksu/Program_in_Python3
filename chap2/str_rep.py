from decimal import Decimal

x = Decimal("93.4")

print(f"default: {x}")
print(f"force str: {x!s}")
print(f"force repr: {x!r}")
print(f"force ascii: {x!a}")


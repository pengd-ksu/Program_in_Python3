from decimal import Decimal
import locale

# Example 1: Simple grouping
n = 2394321
print(f"{n:,}")
print(f"{n:*>13,}")

# Example 2: Locale-aware formatting
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
print(f"{n:n}")

locale.setlocale(locale.LC_ALL, "de_DE.UTF-8")
print(f"{n:n}")

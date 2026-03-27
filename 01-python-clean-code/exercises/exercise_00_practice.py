"""
=============================================================
GYAKORLÓ FELADATOK — Python alapok
=============================================================
"""

# @TASK 1. Változók és kiírás
# @DESC Hozz létre 3 változót: `my_name` (neved), `my_age` (korod), `my_city` (városod).
# Írasd ki f-stringgel: **"Szia! A nevem X, Y éves vagyok, Z-ban élek."**
# @HINT `print(f"Szia! A nevem {my_name}, {my_age} éves vagyok, {my_city}-ban élek.")`
# @CODE
# MEGOLDÁS IDE:



# ELLENŐRZÉS:
if my_name and my_age > 0 and my_city:
    print("✓ OK — változók rendben")
else:
    print("✗ Töltsd ki a neved, korod, városod!")
# @END

# @TASK 2. Műveletek
# @DESC Adott egy téglalap: `width = 5`, `height = 8`.
# Számold ki a **kerületet** (`perimeter = 2 * (a + b)`) és a **területet** (`area = a * b`).
# Írasd ki mindkettőt!
# @HINT `perimeter = 2 * (width + height)` és `area = width * height`
# @CODE
width = 5
height = 8

# MEGOLDÁS IDE:



# ELLENŐRZÉS:
if perimeter == 26 and area == 40:
    print("✓ OK — kerület:", perimeter, "terület:", area)
else:
    print("✗ Kerület = 26 és terület = 40 kéne legyen!")
# @END

# @TASK 3. Lista műveletek
# @DESC Adott egy bevásárlólista. **Adj hozzá 2 új elemet** (`.append()`),
# és **töröld a "kenyer" elemet** (`.remove()`)!
# @HINT `shopping_list.append("vaj")` és `shopping_list.remove("kenyer")`
# @CODE
shopping_list = ["tej", "kenyer", "sajt", "tojas"]

# MEGOLDÁS IDE:



# ELLENŐRZÉS:
if "kenyer" not in shopping_list and len(shopping_list) >= 5:
    print("✓ OK — lista:", shopping_list)
else:
    print("✗ Adj hozzá 2 elemet és töröld a 'kenyer'-t!")
    print("  Jelenlegi lista:", shopping_list)
# @END

# @TASK 4. Feltétel — páros vagy páratlan
# @DESC Írd meg az `even_or_odd` függvényt: ha a szám **páros**, adjon vissza `"paros"`,
# ha **páratlan**, adjon vissza `"paratlan"`.
# @HINT Ha `number % 2 == 0`, akkor páros. Használj `if/else`-t és `return`-t!
# @CODE
def even_or_odd(number):
    # MEGOLDÁS IDE:
    pass

# ELLENŐRZÉS:
if even_or_odd(4) == "paros" and even_or_odd(7) == "paratlan":
    print("✓ OK — even_or_odd működik")
else:
    print("✗ even_or_odd(4) = 'paros' és even_or_odd(7) = 'paratlan' kéne legyen!")
# @END

# @TASK 5. Ciklus — páros számok
# @DESC Írj egy `for` ciklust, ami kiírja a **páros számokat 1-től 10-ig** (2, 4, 6, 8, 10).
# @HINT `for i in range(1, 11):` és `if i % 2 == 0: print(i)`
# @CODE
print("Páros számok 1-10:")
# MEGOLDÁS IDE:

# @END

# @TASK 6. Függvény — átlag
# @DESC Írd meg a `calculate_average` függvényt, ami kap egy számlistát
# és **visszaadja az átlagot** (összeg / elemszám).
# @HINT `return sum(numbers) / len(numbers)`
# @CODE
def calculate_average(numbers):
    # MEGOLDÁS IDE:
    pass

# ELLENŐRZÉS:
if calculate_average([10, 20, 30]) == 20.0:
    print("✓ OK — átlag:", calculate_average([10, 20, 30]))
else:
    print("✗ calculate_average([10, 20, 30]) = 20.0 kéne legyen!")
# @END

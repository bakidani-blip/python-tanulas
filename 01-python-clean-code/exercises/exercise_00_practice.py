"""
=============================================================
GYAKORLO FELADATOK — Python alapok
=============================================================
"""

# @TASK 1. Valtozok es kiiras
# @DESC Hozz letre 3 valtozot: `my_name` (neved), `my_age` (korod), `my_city` (varosod).
# Irasd ki f-stringgel: **"Szia! A nevem X, Y eves vagyok, Z-ban elek."**
# @HINT `print(f"Szia! A nevem {my_name}, {my_age} eves vagyok, {my_city}-ban elek.")`
# @CODE
# MEGOLDAS IDE:



# ELLENORZES:
if my_name and my_age > 0 and my_city:
    print("✓ OK — valtozok rendben")
else:
    print("✗ Toltsd ki a neved, korod, varosod!")
# @END

# @TASK 2. Muveletek
# @DESC Adott egy teglalap: `width = 5`, `height = 8`.
# Szamold ki a **keruletet** (`perimeter = 2 * (a + b)`) es a **teruletet** (`area = a * b`).
# Irasd ki mindkettot!
# @HINT `perimeter = 2 * (width + height)` es `area = width * height`
# @CODE
width = 5
height = 8

# MEGOLDAS IDE:



# ELLENORZES:
if perimeter == 26 and area == 40:
    print("✓ OK — kerulet:", perimeter, "terulet:", area)
else:
    print("✗ Kerulet = 26 es terulet = 40 kene legyen!")
# @END

# @TASK 3. Lista muveletek
# @DESC Adott egy bevasarlolista. **Adj hozza 2 uj elemet** (`.append()`),
# es **torold a "kenyer" elemet** (`.remove()`)!
# @HINT `shopping_list.append("vaj")` es `shopping_list.remove("kenyer")`
# @CODE
shopping_list = ["tej", "kenyer", "sajt", "tojas"]

# MEGOLDAS IDE:



# ELLENORZES:
if "kenyer" not in shopping_list and len(shopping_list) >= 5:
    print("✓ OK — lista:", shopping_list)
else:
    print("✗ Adj hozza 2 elemet es torold a 'kenyer'-t!")
    print("  Jelenlegi lista:", shopping_list)
# @END

# @TASK 4. Feltetel — paros vagy paratlan
# @DESC Ird meg az `even_or_odd` fuggvenyt: ha a szam **paros**, adjon vissza `"paros"`,
# ha **paratlan**, adjon vissza `"paratlan"`.
# @HINT Ha `number % 2 == 0`, akkor paros. Hasznalj `if/else`-t es `return`-t!
# @CODE
def even_or_odd(number):
    # MEGOLDAS IDE:
    pass

# ELLENORZES:
if even_or_odd(4) == "paros" and even_or_odd(7) == "paratlan":
    print("✓ OK — even_or_odd mukodik")
else:
    print("✗ even_or_odd(4) = 'paros' es even_or_odd(7) = 'paratlan' kene legyen!")
# @END

# @TASK 5. Ciklus — paros szamok
# @DESC Irj egy `for` ciklust, ami kiirja a **paros szamokat 1-tol 10-ig** (2, 4, 6, 8, 10).
# @HINT `for i in range(1, 11):` es `if i % 2 == 0: print(i)`
# @CODE
print("Paros szamok 1-10:")
# MEGOLDAS IDE:

# @END

# @TASK 6. Fuggveny — atlag
# @DESC Ird meg a `calculate_average` fuggvenyt, ami kap egy szamlistat
# es **visszaadja az atlagot** (osszeg / elemszam).
# @HINT `return sum(numbers) / len(numbers)`
# @CODE
def calculate_average(numbers):
    # MEGOLDAS IDE:
    pass

# ELLENORZES:
if calculate_average([10, 20, 30]) == 20.0:
    print("✓ OK — atlag:", calculate_average([10, 20, 30]))
else:
    print("✗ calculate_average([10, 20, 30]) = 20.0 kene legyen!")
# @END

"""
=============================================================
1.4 GYAKORLAT: Type hints es docstringek
=============================================================
"""

# @TASK 1. Tipusjelzes valtozokhoz
# @DESC Add hozza a megfelelo **type hint**-et az alabbi valtozokhoz!
# Pelda: `name = "Dani"` → `name: str = "Dani"`
# Tipusok: `int` (egesz), `float` (tizedes), `str` (szoveg), `bool` (True/False)
# @HINT `player_name: str = "Hero123"`, `player_level: int = 42`, stb.
# @CODE
# Add hozza a tipusjelzeseket (: tipus):
player_name = "Hero123"
player_level = 42
player_health = 95.5
is_alive = True

# Irasd ki mindet:
print("Jatekos:", player_name)
print("Szint:", player_level)
print("Elet:", player_health)
print("El:", is_alive)
# @END

# @TASK 2. Fuggveny tipusjelzesek
# @DESC Add hozza a **parameterek** es a **visszateresi ertek** tipusat az alabbi fuggvenyekhez!
# Pelda: `def add(a, b)` → `def add(a: int, b: int) -> int:`
# @HINT `def join_words(first: str, second: str) -> str:` es hasonloan a tobbinel
# @CODE
# Add hozza a tipusjelzeseket:
def join_words(first, second):
    return first + " " + second

def calculate_area(width, height):
    return width * height

def is_old_enough(age, minimum_age):
    return age >= minimum_age

# ELLENORZES:
print("Szavak:", join_words("hello", "vilag"))
print("Terulet:", calculate_area(5.0, 3.0))
print("Eleg idos:", is_old_enough(20, 18))
print("✓ Ha a tipusjelzeseket hozzaadtad, a fuggvenyek ugyanugy mukodnek!")
# @END

# @TASK 3. Osszett tipusok
# @DESC Add hozza a tipusjelzeseket az alabbi valtozokhoz!
# `list[str]` = szoveglista, `list[int]` = szamlista, `dict[str, int]` = szotar, `str | None` = opcionalis
# @HINT `favorite_foods: list[str] = [...]`, `student_grades: dict[str, int] = {...}`
# @CODE
# Add hozza az osszetett tipusjelzeseket:
favorite_foods = ["pizza", "ramen", "turos csusza"]
weekly_temps = [18, 22, 25, 19, 21]
student_grades = {"Anna": 5, "Bela": 3, "Cecil": 4}
nickname = None

print("Etelek:", favorite_foods)
print("Homersekletek:", weekly_temps)
print("Jegyek:", student_grades)
print("Becenev:", nickname)
print("✓ Tipusjelzesek rendben, ha a kiiras mukodik!")
# @END

# @TASK 4. Docstring iras
# @DESC Az alabbi fuggvenynek **van** type hint-je, de **nincs docstring**-je.
# Irj hozza Google-style docstring-et: osszefoglalo, `Args:`, `Returns:` szekcio.
# @HINT A `pass`-t torold, es irj `"""..."""` docstring-et a `def` sor ala!
# @CODE
def celsius_to_fahrenheit(celsius: float) -> float:
    # MEGOLDAS IDE — irj docstring-et:
    pass
    return celsius * 9 / 5 + 32

# ELLENORZES:
result = celsius_to_fahrenheit(100)
if abs(result - 212.0) < 0.01:
    print("✓ OK — 100°C =", result, "°F")
else:
    print("✗ celsius_to_fahrenheit(100) = 212.0 kene!")
# @END

# @TASK 5. Komplett — type hints + docstring
# @DESC Irj egy TELJES fuggvenyt `calculate_shopping_total` neven:
# Kap egy **szotarat** (termek: ar) es egy **kedvezmeny szazalekot** (alapertelmezetten 0).
# Visszaadja a **vegosszeget** a kedvezmeny levonasa utan.
# Pelda: `{"kenyer": 500, "tej": 400}` 10% kedvezmeny → 810.0
# @HINT `def calculate_shopping_total(items: dict, discount: int = 0) -> float:`
# osszeg = `sum(items.values())`, vegosszeg = `osszeg * (1 - discount / 100)`
# @CODE
# MEGOLDAS IDE — irj type hint-eket, docstring-et, es a kodot:
def calculate_shopping_total():
    pass

# ELLENORZES:
items = {"kenyer": 500, "tej": 400, "sajt": 800}
try:
    r1 = calculate_shopping_total(items)
    r2 = calculate_shopping_total(items, 10)
    if r1 is not None and abs(r1 - 1700.0) < 0.01:
        if r2 is not None and abs(r2 - 1530.0) < 0.01:
            print("✓ OK — kedvezmeny nelkul:", r1, ", 10%-kal:", r2)
        else:
            print("✗ 10% kedvezmeny: 1530.0 kene, kaptam:", r2)
    else:
        print("✗ Kedvezmeny nelkul: 1700.0 kene, kaptam:", r1)
except TypeError as e:
    print("✗ A fuggvenynek 2 parametere legyen: (items, discount=0)")
# @END

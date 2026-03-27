"""
=============================================================
1.4 GYAKORLAT: Type hints és docstringek
=============================================================
"""

# @TASK 1. Típusjelzés változókhoz
# @DESC Add hozzá a megfelelő **type hint**-et az alábbi változókhoz!
# Példa: `name = "Dani"` → `name: str = "Dani"`
# Típusok: `int` (egész), `float` (tizedes), `str` (szöveg), `bool` (True/False)
# @HINT `player_name: str = "Hero123"`, `player_level: int = 42`, stb.
# @CODE
# Add hozzá a típusjelzéseket (: típus):
player_name = "Hero123"
player_level = 42
player_health = 95.5
is_alive = True

# Írasd ki mindet:
print("Játékos:", player_name)
print("Szint:", player_level)
print("Élet:", player_health)
print("Él:", is_alive)
# @END

# @TASK 2. Függvény típusjelzések
# @DESC Add hozzá a **paraméterek** és a **visszatérési érték** típusát az alábbi függvényekhez!
# Példa: `def add(a, b)` → `def add(a: int, b: int) -> int:`
# @HINT `def join_words(first: str, second: str) -> str:` és hasonlóan a többinél
# @CODE
# Add hozzá a típusjelzéseket:
def join_words(first, second):
    return first + " " + second

def calculate_area(width, height):
    return width * height

def is_old_enough(age, minimum_age):
    return age >= minimum_age

# ELLENŐRZÉS:
print("Szavak:", join_words("hello", "világ"))
print("Terület:", calculate_area(5.0, 3.0))
print("Elég idős:", is_old_enough(20, 18))
print("✓ Ha a típusjelzéseket hozzáadtad, a függvények ugyanúgy működnek!")
# @END

# @TASK 3. Összetett típusok
# @DESC Add hozzá a típusjelzéseket az alábbi változókhoz!
# `list[str]` = szöveglista, `list[int]` = számlista, `dict[str, int]` = szótár, `str | None` = opcionális
# @HINT `favorite_foods: list[str] = [...]`, `student_grades: dict[str, int] = {...}`
# @CODE
# Add hozzá az összetett típusjelzéseket:
favorite_foods = ["pizza", "ramen", "turos csusza"]
weekly_temps = [18, 22, 25, 19, 21]
student_grades = {"Anna": 5, "Bela": 3, "Cecil": 4}
nickname = None

print("Ételek:", favorite_foods)
print("Hőmérsékletek:", weekly_temps)
print("Jegyek:", student_grades)
print("Becenév:", nickname)
print("✓ Típusjelzések rendben, ha a kiírás működik!")
# @END

# @TASK 4. Docstring írás
# @DESC Az alábbi függvénynek **van** type hint-je, de **nincs docstring**-je.
# Írj hozzá Google-style docstring-et: összefoglaló, `Args:`, `Returns:` szekció.
# @HINT A `pass`-t töröld, és írj `"""..."""` docstring-et a `def` sor alá!
# @CODE
def celsius_to_fahrenheit(celsius: float) -> float:
    # MEGOLDÁS IDE — írj docstring-et:
    pass
    return celsius * 9 / 5 + 32

# ELLENŐRZÉS:
result = celsius_to_fahrenheit(100)
if abs(result - 212.0) < 0.01:
    print("✓ OK — 100°C =", result, "°F")
else:
    print("✗ celsius_to_fahrenheit(100) = 212.0 kéne!")
# @END

# @TASK 5. Komplett — type hints + docstring
# @DESC Írj egy TELJES függvényt `calculate_shopping_total` néven:
# Kap egy **szótárat** (termék: ár) és egy **kedvezmény százalékot** (alapértelmezetten 0).
# Visszaadja a **végösszeget** a kedvezmény levonása után.
# Példa: `{"kenyer": 500, "tej": 400}` 10% kedvezmény → 810.0
# @HINT `def calculate_shopping_total(items: dict, discount: int = 0) -> float:`
# összeg = `sum(items.values())`, végösszeg = `összeg * (1 - discount / 100)`
# @CODE
# MEGOLDÁS IDE — írj type hint-eket, docstring-et, és a kódot:
def calculate_shopping_total():
    pass

# ELLENŐRZÉS:
items = {"kenyer": 500, "tej": 400, "sajt": 800}
try:
    r1 = calculate_shopping_total(items)
    r2 = calculate_shopping_total(items, 10)
    if r1 is not None and abs(r1 - 1700.0) < 0.01:
        if r2 is not None and abs(r2 - 1530.0) < 0.01:
            print("✓ OK — kedvezmény nélkül:", r1, ", 10%-kal:", r2)
        else:
            print("✗ 10% kedvezmény: 1530.0 kéne, kaptam:", r2)
    else:
        print("✗ Kedvezmény nélkül: 1700.0 kéne, kaptam:", r1)
except TypeError as e:
    print("✗ A függvénynek 2 paramétere legyen: (items, discount=0)")
# @END

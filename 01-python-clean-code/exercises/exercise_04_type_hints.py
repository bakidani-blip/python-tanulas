"""
=============================================================
  1.4 GYAKORLAT: Type hints és docstringek
=============================================================

5 feladat vár rád:
  1. Típusjelzés hozzáadása változókhoz
  2. Függvény paraméterek típusjelzése
  3. Összetett típusok (lista, szótár)
  4. Docstring írása
  5. Komplett: type hints + docstring együtt

A kód végén automatikus ellenőrző fut.

Futtasd:
    python 01-python-clean-code/exercises/exercise_04_type_hints.py
"""


# ============================================================
# 1. feladat: Típusjelzés hozzáadása változókhoz
#
# Az alábbi 5 változó MŰKÖDIK, de nincs rajtuk típusjelzés.
# Add hozzá mindegyikhez a megfelelő type hint-et!
#
# Példa:
#   ELŐTTE:  name = "Dani"
#   UTÁNA:   name: str = "Dani"
#
# Emlékeztető:
#   int   → egész szám
#   float → tizedes szám
#   str   → szöveg
#   bool  → True/False
# ============================================================

# MEGOLDÁS IDE: add hozzá a típusjelzéseket!

player_name = "Hero123"
player_level = 42
player_health = 95.5
is_alive = True
guild_name = "DragonSlayers"


# ============================================================
# 2. feladat: Függvény paraméterek típusjelzése
#
# Az alábbi 3 függvény MŰKÖDIK, de hiányoznak a type hint-ek.
# Add hozzá:
#   - Minden paraméterhez a típust (: típus)
#   - A visszatérési típust (-> típus)
#
# Tipp: nézd meg a függvény belsejét, abból kitalálod a típust!
#   - Ha return-nel ad vissza szöveget → -> str
#   - Ha return-nel ad vissza számot → -> int vagy -> float
#   - Ha return-nel ad vissza True/False-t → -> bool
# ============================================================

# 2a) Ez a függvény két szöveget fűz össze szóközzel.
#     Mit kap? Két szöveget. Mit ad vissza? Szöveget.
# MEGOLDÁS IDE: add hozzá a típusjelzéseket!

def join_words(first, second):
    """Két szót összefűz egy szóközzel."""
    return first + " " + second


# 2b) Ez a függvény kiszámolja a téglalap területét.
#     Mit kap? Két tizedes számot. Mit ad vissza? Tizedes számot.
# MEGOLDÁS IDE: add hozzá a típusjelzéseket!

def calculate_area(width, height):
    """Kiszámolja egy téglalap területét."""
    return width * height


# 2c) Ez a függvény ellenőrzi, hogy elég idős-e valaki.
#     Mit kap? Egy egész számot és egy egész számot.
#     Mit ad vissza? True/False-t.
# MEGOLDÁS IDE: add hozzá a típusjelzéseket!

def is_old_enough(age, minimum_age):
    """Ellenőrzi, hogy az életkor eléri-e a minimumot."""
    return age >= minimum_age


# ============================================================
# 3. feladat: Összetett típusok
#
# Most összetett típusokkal dolgozol: lista és szótár.
#
# Emlékeztető:
#   list[str]       → szövegek listája
#   list[int]       → egész számok listája
#   dict[str, int]  → szótár, ahol kulcs: szöveg, érték: szám
#   str | None      → lehet szöveg VAGY None
# ============================================================

# 3a) Add hozzá a típusjelzéseket ezekhez a változókhoz!
# MEGOLDÁS IDE:

favorite_foods = ["pizza", "ramen", "túrós csusza"]
weekly_temperatures = [18, 22, 25, 19, 21, 23, 20]
student_grades = {"Anna": 5, "Béla": 3, "Cecil": 4}
nickname = None     # Ez egy opcionális szöveg — lehet str VAGY None


# 3b) Add hozzá a típusjelzéseket ehhez a függvényhez!
#     - names: szövegek listája
#     - visszatérési érték: szöveg
# MEGOLDÁS IDE:

def format_name_list(names):
    """A nevek listáját vesszővel elválasztott szöveggé alakítja."""
    return ", ".join(names)


# 3c) Add hozzá a típusjelzéseket ehhez a függvényhez!
#     - inventory: szótár (kulcs: szöveg, érték: egész szám)
#     - item_name: szöveg
#     - visszatérési érték: egész szám VAGY None
#       (mert ha nincs ilyen tárgy, None-t ad vissza)
# MEGOLDÁS IDE:

def get_item_count(inventory, item_name):
    """Megkeresi egy tárgy darabszámát a leltárból.

    Ha a tárgy nincs a leltárban, None-t ad vissza.
    """
    if item_name in inventory:
        return inventory[item_name]
    return None


# ============================================================
# 4. feladat: Docstring írása
#
# Az alábbi 2 függvénynek VAN type hint-je, de NINCS docstring-je.
# Írd meg a docstring-et Google-style formátumban!
#
# Emlékeztető — Google-style docstring:
#   """Egysoros összefoglaló.
#
#   Részletesebb leírás (ha kell).
#
#   Args:
#       param1: Mit jelent ez a paraméter.
#       param2: Mit jelent ez a paraméter.
#
#   Returns:
#       Mit ad vissza a függvény.
#   """
# ============================================================

# 4a) Írd meg a docstring-et!
# MEGOLDÁS IDE: a pass helyére írd a docstring-et!

def convert_celsius_to_fahrenheit(celsius: float) -> float:
    pass  # ← töröld a pass-t és írd meg a docstring-et!
    return celsius * 9 / 5 + 32


# 4b) Írd meg a docstring-et!
# MEGOLDÁS IDE: a pass helyére írd a docstring-et!

def find_longest_word(words: list[str]) -> str:
    pass  # ← töröld a pass-t és írd meg a docstring-et!
    longest: str = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


# ============================================================
# 5. feladat: KOMPLETT — Mindent együtt!
#
# Írj egy függvényt a semmiből, ami TELJESEN dokumentált:
#   - Type hint-ek a paramétereknél ÉS a visszatérési értéknél
#   - Google-style docstring
#
# A függvény neve: calculate_shopping_total
#
# Mit csináljon:
#   - Kap egy szótárat, ahol a kulcs a termék neve (str),
#     az érték a termék ára (int)
#   - Kap egy kedvezmény százalékot (int), alapértéke 0
#   - Visszaadja a végösszeget (float) a kedvezmény levonása után
#
# Példa:
#   items = {"kenyér": 500, "tej": 400, "sajt": 800}
#   calculate_shopping_total(items, 10)  → 1530.0
#   (mert 500+400+800 = 1700, abból 10% kedvezmény = 170, végösszeg = 1530.0)
# ============================================================

# MEGOLDÁS IDE: írd meg a teljes függvényt!

def calculate_shopping_total():
    pass


# ============================================================
# ELLENŐRZÉS — Ne módosítsd az alábbi részt!
# ============================================================

print("=" * 50)
print("  ELLENŐRZÉS")
print("=" * 50)
print()

total_score: int = 0
max_score: int = 0

def check(test_name: str, passed: bool, hint: str = "") -> None:
    """Egy teszt eredményét kiírja."""
    global total_score, max_score
    max_score += 1
    if passed:
        total_score += 1
        print(f"  ✅ {test_name}")
    else:
        print(f"  ❌ {test_name}")
        if hint:
            print(f"     💡 Tipp: {hint}")


# --- 1. feladat: Változók típusjelzése ---
print("1. feladat: Változók típusjelzése")
print("-" * 40)

# A type hint-ek a __annotations__ szótárban tárolódnak
# (modul szintű változóknál a globals-ban keressük az annotációkat)
try:
    annotations = {}
    # Python 3.10+ módszer: __annotations__ a modul szintjén
    import sys
    module = sys.modules[__name__]
    annotations = getattr(module, '__annotations__', {})

    check(
        "player_name típusjelzés (str)",
        annotations.get("player_name") == str,
        "Írd át így: player_name: str = \"Hero123\""
    )
    check(
        "player_level típusjelzés (int)",
        annotations.get("player_level") == int,
        "Írd át így: player_level: int = 42"
    )
    check(
        "player_health típusjelzés (float)",
        annotations.get("player_health") == float,
        "Írd át így: player_health: float = 95.5"
    )
    check(
        "is_alive típusjelzés (bool)",
        annotations.get("is_alive") == bool,
        "Írd át így: is_alive: bool = True"
    )
    check(
        "guild_name típusjelzés (str)",
        annotations.get("guild_name") == str,
        "Írd át így: guild_name: str = \"DragonSlayers\""
    )
except Exception as e:
    print(f"  ⚠️  Hiba a változók ellenőrzésekor: {e}")

print()

# --- 2. feladat: Függvény típusjelzések ---
print("2. feladat: Függvény típusjelzések")
print("-" * 40)

import inspect

# 2a) join_words
hints_2a = getattr(join_words, '__annotations__', {})
check(
    "join_words — 'first' típusa str",
    hints_2a.get("first") == str,
    "Írd át: def join_words(first: str, second: str) -> str:"
)
check(
    "join_words — 'second' típusa str",
    hints_2a.get("second") == str,
    "Írd át: def join_words(first: str, second: str) -> str:"
)
check(
    "join_words — visszatérési típus str",
    hints_2a.get("return") == str,
    "Add hozzá: -> str a zárójelek után"
)

# 2b) calculate_area
hints_2b = getattr(calculate_area, '__annotations__', {})
check(
    "calculate_area — 'width' típusa float",
    hints_2b.get("width") == float,
    "Írd át: def calculate_area(width: float, height: float) -> float:"
)
check(
    "calculate_area — 'height' típusa float",
    hints_2b.get("height") == float,
    "Írd át: def calculate_area(width: float, height: float) -> float:"
)
check(
    "calculate_area — visszatérési típus float",
    hints_2b.get("return") == float,
    "Add hozzá: -> float a zárójelek után"
)

# 2c) is_old_enough
hints_2c = getattr(is_old_enough, '__annotations__', {})
check(
    "is_old_enough — 'age' típusa int",
    hints_2c.get("age") == int,
    "Írd át: def is_old_enough(age: int, minimum_age: int) -> bool:"
)
check(
    "is_old_enough — 'minimum_age' típusa int",
    hints_2c.get("minimum_age") == int,
    "Írd át: def is_old_enough(age: int, minimum_age: int) -> bool:"
)
check(
    "is_old_enough — visszatérési típus bool",
    hints_2c.get("return") == bool,
    "Add hozzá: -> bool a zárójelek után"
)

print()

# --- 3. feladat: Összetett típusok ---
print("3. feladat: Összetett típusok")
print("-" * 40)

# 3a) Változók
check(
    "favorite_foods típusjelzés (list[str])",
    annotations.get("favorite_foods") == list[str],
    "Írd át: favorite_foods: list[str] = [...]"
)
check(
    "weekly_temperatures típusjelzés (list[int])",
    annotations.get("weekly_temperatures") == list[int],
    "Írd át: weekly_temperatures: list[int] = [...]"
)
check(
    "student_grades típusjelzés (dict[str, int])",
    annotations.get("student_grades") == dict[str, int],
    "Írd át: student_grades: dict[str, int] = {...}"
)
check(
    "nickname típusjelzés (str | None)",
    annotations.get("nickname") == (str | None),
    "Írd át: nickname: str | None = None"
)

# 3b) format_name_list
hints_3b = getattr(format_name_list, '__annotations__', {})
check(
    "format_name_list — 'names' típusa list[str]",
    hints_3b.get("names") == list[str],
    "Írd át: def format_name_list(names: list[str]) -> str:"
)
check(
    "format_name_list — visszatérési típus str",
    hints_3b.get("return") == str,
    "Add hozzá: -> str"
)

# 3c) get_item_count
hints_3c = getattr(get_item_count, '__annotations__', {})
check(
    "get_item_count — 'inventory' típusa dict[str, int]",
    hints_3c.get("inventory") == dict[str, int],
    "Írd át: def get_item_count(inventory: dict[str, int], ...)"
)
check(
    "get_item_count — 'item_name' típusa str",
    hints_3c.get("item_name") == str,
    "Írd át: ..., item_name: str) -> ..."
)
check(
    "get_item_count — visszatérési típus int | None",
    hints_3c.get("return") == (int | None),
    "Add hozzá: -> int | None"
)

print()

# --- 4. feladat: Docstring ---
print("4. feladat: Docstring írása")
print("-" * 40)

doc_4a = getattr(convert_celsius_to_fahrenheit, '__doc__', None)
check(
    "convert_celsius_to_fahrenheit — van docstring",
    doc_4a is not None and len(doc_4a.strip()) > 10,
    "Adj hozzá egy docstring-et a függvényhez: \"\"\"...\"\"\""
)
check(
    "convert_celsius_to_fahrenheit — tartalmaz 'Args' szekciót",
    doc_4a is not None and "Args" in doc_4a,
    "Adj hozzá Args szekciót: 'Args:\\n    celsius: ...'"
)
check(
    "convert_celsius_to_fahrenheit — tartalmaz 'Returns' szekciót",
    doc_4a is not None and "Returns" in doc_4a or doc_4a is not None and "Return" in doc_4a,
    "Adj hozzá Returns szekciót: 'Returns:\\n    ...'"
)

# A függvény működését is ellenőrizzük:
check(
    "convert_celsius_to_fahrenheit(100) == 212.0",
    abs(convert_celsius_to_fahrenheit(100) - 212.0) < 0.01,
    "A képlet: celsius * 9 / 5 + 32"
)

doc_4b = getattr(find_longest_word, '__doc__', None)
check(
    "find_longest_word — van docstring",
    doc_4b is not None and len(doc_4b.strip()) > 10,
    "Adj hozzá egy docstring-et a függvényhez: \"\"\"...\"\"\""
)
check(
    "find_longest_word — tartalmaz 'Args' szekciót",
    doc_4b is not None and "Args" in doc_4b,
    "Adj hozzá Args szekciót"
)

# A függvény működését is ellenőrizzük:
check(
    "find_longest_word(['alma', 'ananász', 'dió']) == 'ananász'",
    find_longest_word(["alma", "ananász", "dió"]) == "ananász",
    "A függvény a leghosszabb szót kell visszaadja"
)

print()

# --- 5. feladat: Komplett ---
print("5. feladat: Komplett függvény")
print("-" * 40)

# Ellenőrizzük, hogy a függvény működik-e
hints_5 = getattr(calculate_shopping_total, '__annotations__', {})
sig = inspect.signature(calculate_shopping_total)
params = list(sig.parameters.keys())

check(
    "calculate_shopping_total — van legalább 1 paramétere",
    len(params) >= 1,
    "A függvénynek kell kapnia egy items szótárat és egy discount_percent-et"
)

check(
    "calculate_shopping_total — van type hint a paramétereken",
    len(hints_5) >= 2,
    "Adj hozzá type hint-eket: (items: dict[str, int], discount_percent: int = 0) -> float"
)

check(
    "calculate_shopping_total — van visszatérési type hint",
    "return" in hints_5,
    "Add hozzá: -> float"
)

doc_5 = getattr(calculate_shopping_total, '__doc__', None)
check(
    "calculate_shopping_total — van docstring",
    doc_5 is not None and len(doc_5.strip()) > 10,
    "Írj egy Google-style docstring-et a függvényhez"
)

# Funkció tesztek
try:
    test_items: dict[str, int] = {"kenyér": 500, "tej": 400, "sajt": 800}
    result_no_discount = calculate_shopping_total(test_items)
    check(
        "calculate_shopping_total({'kenyér':500,'tej':400,'sajt':800}) == 1700.0",
        result_no_discount is not None and abs(result_no_discount - 1700.0) < 0.01,
        "Kedvezmény nélkül: az árak összege kell legyen (500+400+800 = 1700)"
    )

    result_with_discount = calculate_shopping_total(test_items, 10)
    check(
        "calculate_shopping_total({...}, 10) == 1530.0",
        result_with_discount is not None and abs(result_with_discount - 1530.0) < 0.01,
        "10% kedvezménnyel: 1700 - 170 = 1530.0"
    )
except TypeError as e:
    print(f"  ❌ A függvény nem hívható meg megfelelően: {e}")
    print(f"     💡 Tipp: Ellenőrizd a paramétereket: (items: dict[str, int], discount_percent: int = 0)")

print()

# --- Összesítés ---
print("=" * 50)
percentage: int = round(total_score / max_score * 100) if max_score > 0 else 0
print(f"  Eredmény: {total_score}/{max_score} ({percentage}%)")
print("=" * 50)

if percentage == 100:
    print("  🎉 TÖKÉLETES! Mindent hibátlanul megoldottál!")
    print("  Profi módon dokumentálod a kódod — így kell ezt csinálni!")
elif percentage >= 70:
    print("  👏 Szép munka! Már majdnem minden stimmel.")
    print("  Nézd meg a ❌ jelöléseket és a tippeket!")
elif percentage >= 40:
    print("  💪 Jó kezdet! Olvsd el újra a 04_type_hints_alapok.py leckét,")
    print("  és próbáld meg a hibás részeket javítani.")
else:
    print("  📖 Először olvasd el a 04_type_hints_alapok.py elméleti anyagot,")
    print("  és próbáld meg újra! A tippek segítenek.")

print()

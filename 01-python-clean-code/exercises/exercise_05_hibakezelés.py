"""
=============================================================
GYAKORLAT 05 — Hibakezelés (Error Handling)
=============================================================
"""

# @TASK 1. Alapvető try/except
# @DESC Írd meg a `safe_divide(a, b)` függvényt: **elosztja a-t b-vel**.
# Ha `b` nulla → adjon vissza `None`-t (ne szálljon el a program!).
# Ha nincs hiba → adja vissza az eredményt.
# @HINT Használj `try/except ZeroDivisionError`-t!
# @CODE
def safe_divide(a, b):
    # MEGOLDÁS IDE:
    pass

# ELLENŐRZÉS:
r1 = safe_divide(10, 2)
r2 = safe_divide(10, 0)
if r1 == 5.0 and r2 is None:
    print("✓ OK — safe_divide(10,2) =", r1, ", safe_divide(10,0) =", r2)
else:
    print("✗ safe_divide(10,2) = 5.0 és safe_divide(10,0) = None kéne!")
    print("  Kaptam:", r1, "és", r2)
# @END

# @TASK 2. IndexError kezelés
# @DESC Írd meg a `safe_list_access(items, index)` függvényt:
# Próbáld meg visszaadni a lista `index`-edik elemét.
# Ha **nincs ilyen index** → adj vissza: `"Hiba: Nincs ilyen index: {index}"`
# @HINT `try: return items[index]` / `except IndexError: return f"Hiba: ..."`
# @CODE
def safe_list_access(items, index):
    # MEGOLDÁS IDE:
    pass

# ELLENŐRZÉS:
r1 = safe_list_access(["a", "b", "c"], 1)
r2 = safe_list_access(["a", "b", "c"], 10)
if r1 == "b" and r2 == "Hiba: Nincs ilyen index: 10":
    print("✓ OK — lista elérés működik")
else:
    print("✗ index 1 = 'b' és index 10 = hibaüzenet kéne!")
    print("  Kaptam:", r1, "|", r2)
# @END

# @TASK 3. Szám konvertálás
# @DESC Írd meg a `safe_int_convert(value)` függvényt:
# Próbáld meg **szövegből számmá** alakítani (`int(value)`).
# Ha sikerül → add vissza a számot. Ha nem (`ValueError`) → add vissza `None`-t.
# @HINT `try: return int(value)` / `except ValueError: return None`
# @CODE
def safe_int_convert(value):
    # MEGOLDÁS IDE:
    pass

# ELLENŐRZÉS:
r1 = safe_int_convert("42")
r2 = safe_int_convert("hello")
r3 = safe_int_convert("")
if r1 == 42 and r2 is None and r3 is None:
    print("✓ OK — konvertálás működik")
else:
    print("✗ '42'=42, 'hello'=None, ''=None kéne!")
    print("  Kaptam:", r1, r2, r3)
# @END

# @TASK 4. Saját hiba dobása (raise)
# @DESC Írd meg a `create_profile(username, age)` függvényt:
# Ellenőrizd az inputot és **dobj hibát** ha:
# - `username` üres → `raise ValueError("A név nem lehet üres!")`
# - `username` rövid (< 3 kar.) → `raise ValueError("A név legalább 3 karakter legyen!")`
# - `age` nem pozitív → `raise ValueError("Az életkor pozitív szám kell legyen!")`
# Ha minden ok → add vissza: `{"username": username, "age": age}`
# @HINT `if username == "": raise ValueError("A név nem lehet üres!")`
# @CODE
def create_profile(username, age):
    # MEGOLDÁS IDE:
    pass

# ELLENŐRZÉS:
errors = 0

r = create_profile("Dani", 19)
if r == {"username": "Dani", "age": 19}:
    print("✓ create_profile('Dani', 19) — OK")
else:
    print("✗ create_profile('Dani', 19) szótár kéne!")
    errors += 1

try:
    create_profile("", 19)
    print("✗ Üres név — ValueError kéne!")
    errors += 1
except ValueError:
    print("✓ Üres név — ValueError OK")

try:
    create_profile("ab", 19)
    print("✗ Rövid név — ValueError kéne!")
    errors += 1
except ValueError:
    print("✓ Rövid név — ValueError OK")

try:
    create_profile("Dani", -5)
    print("✗ Negatív kor — ValueError kéne!")
    errors += 1
except ValueError:
    print("✓ Negatív kor — ValueError OK")

if errors == 0:
    print("MINDEN FELADAT KÉSZ!")
# @END

# @TASK 5. Mini bank
# @DESC Írj `get_balance(name)` és `transfer(sender, receiver, amount)` függvényeket.
# `get_balance`: visszaadja az egyenleget. Ha nincs ilyen személy → `raise KeyError("Ismeretlen: {name}")`.
# `transfer`: átutal pénzt. Hibák: nem létezik személy → `KeyError`, nincs elég pénz → `ValueError`.
# Siker → `"Sikeres utalás: {amount} Ft"` + módosítja az egyenlegeket.
# @HINT `if name not in accounts: raise KeyError(...)` / `accounts[sender] -= amount`
# @CODE
accounts = {"Anna": 10000, "Bela": 5000, "Cecil": 0}

def get_balance(name):
    # MEGOLDÁS IDE:
    pass

def transfer(sender, receiver, amount):
    # MEGOLDÁS IDE:
    pass

# ELLENŐRZÉS:
errors = 0

if get_balance("Anna") == 10000:
    print("✓ get_balance('Anna') — OK")
else:
    print("✗ get_balance('Anna') = 10000 kéne!")
    errors += 1

try:
    get_balance("Xyz")
    print("✗ Ismeretlen személy — KeyError kéne!")
    errors += 1
except KeyError:
    print("✓ Ismeretlen személy — KeyError OK")

accounts["Anna"] = 10000
accounts["Bela"] = 5000
result = transfer("Anna", "Bela", 3000)
if result is not None and "Sikeres" in result:
    if accounts["Anna"] == 7000 and accounts["Bela"] == 8000:
        print("✓ transfer — OK, egyenlegek stimmelnek")
    else:
        print("✗ Anna=7000, Bela=8000 kéne!")
        errors += 1
else:
    print("✗ transfer visszatérési értéke 'Sikeres...' kéne!")
    errors += 1

try:
    transfer("Cecil", "Anna", 1000)
    print("✗ Nincs fedezet — ValueError kéne!")
    errors += 1
except ValueError:
    print("✓ Nincs fedezet — ValueError OK")

if errors == 0:
    print("MINDEN FELADAT KÉSZ!")
# @END

"""
=============================================================
GYAKORLAT 05 — Hibakezeles (Error Handling)
=============================================================
"""

# @TASK 1. Alapveto try/except
# @DESC Ird meg a `safe_divide(a, b)` fuggvenyt: **elosztja a-t b-vel**.
# Ha `b` nulla → adjon vissza `None`-t (ne szalljon el a program!).
# Ha nincs hiba → adja vissza az eredmenyt.
# @HINT Hasznalj `try/except ZeroDivisionError`-t!
# @CODE
def safe_divide(a, b):
    # MEGOLDAS IDE:
    pass

# ELLENORZES:
r1 = safe_divide(10, 2)
r2 = safe_divide(10, 0)
if r1 == 5.0 and r2 is None:
    print("✓ OK — safe_divide(10,2) =", r1, ", safe_divide(10,0) =", r2)
else:
    print("✗ safe_divide(10,2) = 5.0 es safe_divide(10,0) = None kene!")
    print("  Kaptam:", r1, "es", r2)
# @END

# @TASK 2. IndexError kezeles
# @DESC Ird meg a `safe_list_access(items, index)` fuggvenyt:
# Probald meg visszaadni a lista `index`-edik elemet.
# Ha **nincs ilyen index** → adj vissza: `"Hiba: Nincs ilyen index: {index}"`
# @HINT `try: return items[index]` / `except IndexError: return f"Hiba: ..."`
# @CODE
def safe_list_access(items, index):
    # MEGOLDAS IDE:
    pass

# ELLENORZES:
r1 = safe_list_access(["a", "b", "c"], 1)
r2 = safe_list_access(["a", "b", "c"], 10)
if r1 == "b" and r2 == "Hiba: Nincs ilyen index: 10":
    print("✓ OK — lista eleres mukodik")
else:
    print("✗ index 1 = 'b' es index 10 = hibauzenet kene!")
    print("  Kaptam:", r1, "|", r2)
# @END

# @TASK 3. Szam konvertalas
# @DESC Ird meg a `safe_int_convert(value)` fuggvenyt:
# Probald meg **szovegbol szamma** alakitani (`int(value)`).
# Ha sikerul → add vissza a szamot. Ha nem (`ValueError`) → add vissza `None`-t.
# @HINT `try: return int(value)` / `except ValueError: return None`
# @CODE
def safe_int_convert(value):
    # MEGOLDAS IDE:
    pass

# ELLENORZES:
r1 = safe_int_convert("42")
r2 = safe_int_convert("hello")
r3 = safe_int_convert("")
if r1 == 42 and r2 is None and r3 is None:
    print("✓ OK — konvertalas mukodik")
else:
    print("✗ '42'=42, 'hello'=None, ''=None kene!")
    print("  Kaptam:", r1, r2, r3)
# @END

# @TASK 4. Sajat hiba dobasa (raise)
# @DESC Ird meg a `create_profile(username, age)` fuggvenyt:
# Ellenorizd az inputot es **dobj hibat** ha:
# - `username` ures → `raise ValueError("A nev nem lehet ures!")`
# - `username` rovid (< 3 kar.) → `raise ValueError("A nev legalabb 3 karakter legyen!")`
# - `age` nem pozitiv → `raise ValueError("Az eletkor pozitiv szam kell legyen!")`
# Ha minden ok → add vissza: `{"username": username, "age": age}`
# @HINT `if username == "": raise ValueError("A nev nem lehet ures!")`
# @CODE
def create_profile(username, age):
    # MEGOLDAS IDE:
    pass

# ELLENORZES:
errors = 0

r = create_profile("Dani", 19)
if r == {"username": "Dani", "age": 19}:
    print("✓ create_profile('Dani', 19) — OK")
else:
    print("✗ create_profile('Dani', 19) szotar kene!")
    errors += 1

try:
    create_profile("", 19)
    print("✗ Ures nev — ValueError kene!")
    errors += 1
except ValueError:
    print("✓ Ures nev — ValueError OK")

try:
    create_profile("ab", 19)
    print("✗ Rovid nev — ValueError kene!")
    errors += 1
except ValueError:
    print("✓ Rovid nev — ValueError OK")

try:
    create_profile("Dani", -5)
    print("✗ Negativ kor — ValueError kene!")
    errors += 1
except ValueError:
    print("✓ Negativ kor — ValueError OK")

if errors == 0:
    print("MINDEN FELADAT KESZ!")
# @END

# @TASK 5. Mini bank
# @DESC Irj `get_balance(name)` es `transfer(sender, receiver, amount)` fuggvenyeket.
# `get_balance`: visszaadja az egyenleget. Ha nincs ilyen szemely → `raise KeyError("Ismeretlen: {name}")`.
# `transfer`: atutal penzt. Hibak: nem letezik szemely → `KeyError`, nincs eleg penz → `ValueError`.
# Siker → `"Sikeres utalas: {amount} Ft"` + modositja az egyenlegeket.
# @HINT `if name not in accounts: raise KeyError(...)` / `accounts[sender] -= amount`
# @CODE
accounts = {"Anna": 10000, "Bela": 5000, "Cecil": 0}

def get_balance(name):
    # MEGOLDAS IDE:
    pass

def transfer(sender, receiver, amount):
    # MEGOLDAS IDE:
    pass

# ELLENORZES:
errors = 0

if get_balance("Anna") == 10000:
    print("✓ get_balance('Anna') — OK")
else:
    print("✗ get_balance('Anna') = 10000 kene!")
    errors += 1

try:
    get_balance("Xyz")
    print("✗ Ismeretlen szemely — KeyError kene!")
    errors += 1
except KeyError:
    print("✓ Ismeretlen szemely — KeyError OK")

accounts["Anna"] = 10000
accounts["Bela"] = 5000
result = transfer("Anna", "Bela", 3000)
if result is not None and "Sikeres" in result:
    if accounts["Anna"] == 7000 and accounts["Bela"] == 8000:
        print("✓ transfer — OK, egyenlegek stimmelnek")
    else:
        print("✗ Anna=7000, Bela=8000 kene!")
        errors += 1
else:
    print("✗ transfer visszateresi erteke 'Sikeres...' kene!")
    errors += 1

try:
    transfer("Cecil", "Anna", 1000)
    print("✗ Nincs fedezet — ValueError kene!")
    errors += 1
except ValueError:
    print("✓ Nincs fedezet — ValueError OK")

if errors == 0:
    print("MINDEN FELADAT KESZ!")
# @END

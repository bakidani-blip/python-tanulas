"""
=============================================================
  GYAKORLÓ FELADATOK — Python alapok
=============================================================

Oldd meg az alábbi feladatokat!
Minden feladatnál a "# MEGOLDÁS IDE" részt írd át.
Ha kész vagy, futtasd a fájlt — a végén ellenőrzi magát.

Futtasd:
    python 01-python-clean-code/exercises/exercise_00_practice.py
"""


# ============================================================
# 1. feladat: Változók
# Hozz létre 3 változót a saját adataiddal!
# ============================================================

my_name = "Dani"         # ← írd be a neved (szöveg)
my_age = 19           # ← írd be a korod (szám)
my_city = "Budapest"         # ← írd be a városod (szöveg)

# Írd ki egy f-string-gel: "Szia! A nevem X, Y éves vagyok, Z-ban élek."
# MEGOLDÁS IDE: 
print(f"Szia, a nevem {my_name}, {my_age} éves vagyok, {my_city}-ben élek")



# ============================================================
# 2. feladat: Műveletek
# Számold ki egy téglalap kerületét és területét!
# Kerület = 2 * (a + b)
# Terület = a * b
# ============================================================

width = 5
height = 8

perimeter = (width + height) * 2   # ← számold ki a kerületet
area = width * height        # ← számold ki a területet

# MEGOLDÁS IDE:


print(f"A téglalap területe: {area}, kerülete: {perimeter}")


# ============================================================
# 3. feladat: Lista
# Van egy bevásárlólista. Adj hozzá 2 új elemet,
# és töröld a "kenyér" elemet!
# ============================================================

shopping_list = ["tej", "kenyér", "sajt", "tojás"]

# MEGOLDÁS IDE (használd az .append() és .remove() metódusokat):

shopping_list.remove("kenyér")
shopping_list.append("vaj")
shopping_list.append("liszt")

print(f"Bevásárlólista: {shopping_list}")


# ============================================================
# 4. feladat: Feltételek
# Írd meg az alábbi függvényt, ami eldönti,
# hogy egy szám páros vagy páratlan!
# Tipp: ha a szám 2-vel osztva 0 maradékot ad → páros
# ============================================================

def even_or_odd(number):
    """Visszaadja, hogy "páros" vagy "páratlan"."""
    # MEGOLDÁS IDE:
    if number % 2 == 0:
        return "páros"
    else:
        return "páratlan"  # ← töröld ezt a sort és írd meg a megoldást


# ============================================================
# 5. feladat: Ciklus
# Írd ki a számokat 1-től 10-ig, de csak a párosakat!
# Tipp: használj for ciklust és if feltételt
# ============================================================

print("Páros számok 1-10:")
# MEGOLDÁS IDE:
for i in range(2, 11, 2):
    print(i)


# ============================================================
# 6. feladat: Függvény
# Írj egy függvényt, ami kiszámolja egy lista átlagát!
# Tipp: összeg / elemek száma → használd sum() és len()
# ============================================================

def calculate_average(numbers):
    """Kiszámolja és visszaadja a számok átlagát."""
    # MEGOLDÁS IDE:
    return sum(numbers) / len(numbers)    # ← töröld ezt a sort és írd meg a megoldást

# ============================================================
# 7. feladat: Szótár
# Hozz létre egy szótárat egy filmről! Legyen benne:
# title, year, director, rating (1-10)
# Aztán írd ki szépen formázva.
# ============================================================

movie = {
    "title": "Interstellar",
    "year": 2014,
    "director": "Christopher Nolan",
    "rating": 9.1
}  # ← töltsd ki a szótárat

# MEGOLDÁS IDE:



# ============================================================
# ELLENŐRZÉS — ne módosítsd ezt a részt!
# ============================================================

print("\n" + "=" * 50)
print("EREDMÉNYEK")
print("=" * 50)

errors = 0

# 1. feladat
if my_name and my_age > 0 and my_city:
    print("✓ 1. feladat: Változók — OK")
else:
    print("✗ 1. feladat: Változók — töltsd ki a neved, korod, városod!")
    errors += 1

# 2. feladat
if perimeter == 2 * (width + height) and area == width * height:
    print("✓ 2. feladat: Műveletek — OK")
else:
    print(f"✗ 2. feladat: Műveletek — kerület={perimeter} (helyes: {2*(width+height)}), terület={area} (helyes: {width*height})")
    errors += 1

# 3. feladat
if "kenyér" not in shopping_list and len(shopping_list) >= 5:
    print("✓ 3. feladat: Lista — OK")
else:
    print("✗ 3. feladat: Lista — adj hozzá 2 elemet és töröld a 'kenyér'-t!")
    errors += 1

# 4. feladat
if even_or_odd(4) == "páros" and even_or_odd(7) == "páratlan":
    print("✓ 4. feladat: Feltételek — OK")
else:
    print("✗ 4. feladat: Feltételek — a függvény nem ad jó eredményt!")
    errors += 1

# 6. feladat
if calculate_average([10, 20, 30]) == 20.0:
    print("✓ 6. feladat: Függvény — OK")
else:
    print("✗ 6. feladat: Függvény — az átlag nem stimmel!")
    errors += 1

# 7. feladat
if movie.get("title") and movie.get("year") and movie.get("director") and movie.get("rating"):
    print("✓ 7. feladat: Szótár — OK")
else:
    print("✗ 7. feladat: Szótár — töltsd ki a title, year, director, rating mezőket!")
    errors += 1

print("=" * 50)
if errors == 0:
    print("🎉 MINDEN FELADAT KÉSZ! Szólj nekem, és megnézem!")
else:
    print(f"Még {errors} feladat van hátra. Hajrá!")

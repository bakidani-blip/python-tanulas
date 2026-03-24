"""
=============================================================
  1.2 GYAKORLAT: Függvények — Egy feladat, egy függvény
=============================================================

Két típusú feladat vár rád:
  A) Függvény SZÉTBONTÁS: egy nagy függvényt kell kis részekre vágni
  B) Függvény ÍRÁS: saját függvényeket kell írnod

A kód végén automatikus ellenőrző fut.

Futtasd:
    python 01-python-clean-code/exercises/exercise_02_fuggvenyek.py
"""


# ============================================================
# 1. feladat: Írd meg a hiányzó függvényt
#
# Írj egy függvényt, ami kiszámolja egy kör KERÜLETÉT.
#
# Képlet: kerület = 2 * pi * sugár
# A PI legyen konstans (3.14159).
#
# A függvény:
#   - KAPJA: a kör sugarát (egy szám)
#   - VISSZAADJA: a kerületet (return-nel!)
#   - NE írjon ki semmit (ne használj print-et benne!)
#
# Tipp: a függvény neve legyen igés és beszédes.
# ============================================================

PI = 3.14159

def calculate_circle_circumference(radius):
    """Kiszámolja egy kör kerületét a sugár alapján."""
    pass    # ← töröld és írd meg a megoldást


# ============================================================
# 2. feladat: Írd meg a hiányzó függvényt
#
# Írj egy függvényt, ami eldönti, hogy egy diák ÁTMENT-E
# a vizsgán.
#
# Szabály: ha a pontszám >= 50, akkor átment.
#
# A függvény:
#   - KAPJA: a diák pontszámát (egy szám, 0-100)
#   - VISSZAADJA: True ha átment, False ha nem
#   - NE írjon ki semmit!
#
# Tipp: boolean függvénynél → is_ vagy has_ előtag
# ============================================================

def is_passing_grade(score):
    """Eldönti, hogy a diák átment-e (pontszám >= 50)."""
    pass    # ← töröld és írd meg a megoldást


# ============================================================
# 3. feladat: Bontsd szét a nagy függvényt!
#
# Az alábbi függvény 3 dolgot csinál egyszerre:
#   1. Kiszámolja a diákok átlagát
#   2. Megszámolja hány diák bukott meg (< 50 pont)
#   3. Kiírja az eredményt
#
# A te feladatod:
#   Írd meg az alábbi 3 KÜLÖN függvényt, amik EGY-EGY dolgot csinálnak.
#   A nagy függvényt NE módosítsd — alatta dolgozz!
#
# Tipp: nézd meg a kommenteket a nagy függvényben,
#       azok mutatják a határokat.
# ============================================================

# --- EZT a függvényt NE módosítsd, csak nézd meg mit csinál: ---
def process_exam_results_bad(scores):
    """ROSSZ: túl sokat csinál egyszerre."""
    # Átlag számolás
    total = 0
    for score in scores:
        total = total + score
    average = total / len(scores)

    # Bukottak számolása
    failed_count = 0
    for score in scores:
        if score < 50:
            failed_count = failed_count + 1

    # Eredmény kiírása
    print(f"  Átlag: {average}")
    print(f"  Bukott: {failed_count} diák")

# --- IDE írd meg a 3 külön függvényt: ---

# 3a) Átlag számolás
#     Neve: calculate_average_score
#     Kapja: pontszámok listáját (pl. [85, 42, 73])
#     Visszaadja: az átlagot (return)
#     NE írjon ki semmit!

def calculate_average_score(scores):
    """Kiszámolja a pontszámok átlagát."""
    pass    # ← töröld és írd meg a megoldást


# 3b) Bukottak számolása
#     Neve: count_failed_students
#     Kapja: pontszámok listáját
#     Visszaadja: a bukott diákok számát (akiknek pontszáma < 50)
#     NE írjon ki semmit!

def count_failed_students(scores):
    """Megszámolja hány diák bukott meg (pontszám < 50)."""
    pass    # ← töröld és írd meg a megoldást


# 3c) Eredmény kiírása
#     Neve: print_exam_summary
#     Kapja: pontszámok listáját
#     HASZNÁLJA a fenti két függvényt (calculate_average_score, count_failed_students)
#     Kiírja az átlagot és a bukottak számát
#     NEM ad vissza semmit (nincs return)

def print_exam_summary(scores):
    """Kiírja a vizsga összesítőt a fenti függvények segítségével."""
    pass    # ← töröld és írd meg a megoldást


# ============================================================
# 4. feladat: Függvény alapértelmezett paraméterrel
#
# Írj egy függvényt, ami KÖSZÖNT egy felhasználót.
#
# A függvény:
#   - KAPJA: a nevet (kötelező) ÉS az időszakot (opcionális)
#   - Az időszak alapértelmezetten "reggel"
#   - VISSZAADJA a köszönést szövegként (return!)
#
# Visszatérési értékek időszak szerint:
#   "reggel"  → "Jó reggelt, {név}!"
#   "este"    → "Jó estét, {név}!"
#   bármi más → "Szia, {név}!"
#
# Példák:
#   create_greeting("Anna")           → "Jó reggelt, Anna!"
#   create_greeting("Béla", "este")   → "Jó estét, Béla!"
#   create_greeting("Cecil", "dél")   → "Szia, Cecil!"
# ============================================================

def create_greeting(name, time_of_day="reggel"):
    """Köszönést hoz létre a név és időszak alapján."""
    pass    # ← töröld és írd meg a megoldást


# ============================================================
# 5. feladat: Bontsd szét — Pizzarendelés
#
# Az alábbi függvény egy teljes pizzarendelést kezel.
# Szedd szét 3 függvényre!
#
# A nagy függvényt NE módosítsd — alatta dolgozz!
# ============================================================

DELIVERY_FEE = 500  # kiszállítási díj (Ft)

# --- EZT NE módosítsd: ---
def order_pizza_bad(pizza_name, size, quantity, is_delivery):
    """ROSSZ: túl sokat csinál."""
    # Ár kiszámolás
    base_prices = {"kicsi": 1500, "közepes": 2200, "nagy": 2900}
    base_price = base_prices[size]
    total_price = base_price * quantity
    if is_delivery:
        total_price = total_price + DELIVERY_FEE

    # Rendelés kiírása
    print(f"  Pizza: {pizza_name} ({size})")
    print(f"  Darab: {quantity}")
    print(f"  Kiszállítás: {'igen' if is_delivery else 'nem'}")
    print(f"  Összesen: {total_price} Ft")

# --- IDE írd meg a függvényeket: ---

# 5a) Ár kiszámolás
#     Neve: calculate_pizza_price
#     Kapja: size (méret szövegként: "kicsi"/"közepes"/"nagy"),
#            quantity (darabszám),
#            is_delivery (True/False — kiszállítás kell-e)
#     Visszaadja: a végösszeget
#     Tipp: a base_prices szótárat használd!

def calculate_pizza_price(size, quantity, is_delivery):
    """Kiszámolja a pizza rendelés végösszegét."""
    pass    # ← töröld és írd meg a megoldást


# 5b) Rendelés kiírása
#     Neve: print_order_summary
#     Kapja: pizza_name, size, quantity, is_delivery, total_price
#     Kiírja a rendelés adatait (pont úgy, mint a rossz verzióban)
#     NEM ad vissza semmit

def print_order_summary(pizza_name, size, quantity, is_delivery, total_price):
    """Kiírja a rendelés összesítőjét."""
    pass    # ← töröld és írd meg a megoldást


# 5c) Összerakás
#     Neve: process_pizza_order
#     Kapja: pizza_name, size, quantity, is_delivery
#     HASZNÁLJA a calculate_pizza_price és print_order_summary függvényeket
#     NEM ad vissza semmit

def process_pizza_order(pizza_name, size, quantity, is_delivery):
    """Feldolgoz egy pizza rendelést a fenti függvények segítségével."""
    pass    # ← töröld és írd meg a megoldást


# ============================================================
# ELLENŐRZÉS — ne módosítsd ezt a részt!
# ============================================================

print("\n" + "=" * 50)
print("EREDMÉNYEK")
print("=" * 50)

errors = 0

# 1. feladat
try:
    r1 = calculate_circle_circumference(10)
    expected1 = 2 * PI * 10
    if r1 is not None and abs(r1 - expected1) < 0.01:
        print("✓ 1. feladat: Kör kerülete — OK")
    else:
        print(f"✗ 1. feladat: Kör kerülete — eredmény: {r1}, elvárt: {expected1:.2f}")
        errors += 1
except Exception as e:
    print(f"✗ 1. feladat: Kör kerülete — hiba: {e}")
    errors += 1

# 2. feladat
try:
    if is_passing_grade(75) == True and is_passing_grade(50) == True and is_passing_grade(49) == False:
        print("✓ 2. feladat: Átment-e — OK")
    else:
        print("✗ 2. feladat: Átment-e — 50 felett True, alatta False kell legyen!")
        errors += 1
except Exception as e:
    print(f"✗ 2. feladat: Átment-e — hiba: {e}")
    errors += 1

# 3. feladat
test_scores = [85, 42, 73, 91, 38, 67]

try:
    avg = calculate_average_score(test_scores)
    expected_avg = sum(test_scores) / len(test_scores)
    if avg is not None and abs(avg - expected_avg) < 0.01:
        print("✓ 3a. feladat: Átlag számolás — OK")
    else:
        print(f"✗ 3a. feladat: Átlag — eredmény: {avg}, elvárt: {expected_avg:.2f}")
        errors += 1
except Exception as e:
    print(f"✗ 3a. feladat: Átlag — hiba: {e}")
    errors += 1

try:
    failed = count_failed_students(test_scores)
    if failed == 2:
        print("✓ 3b. feladat: Bukottak száma — OK")
    else:
        print(f"✗ 3b. feladat: Bukottak — eredmény: {failed}, elvárt: 2")
        errors += 1
except Exception as e:
    print(f"✗ 3b. feladat: Bukottak — hiba: {e}")
    errors += 1

try:
    import io
    import sys
    captured = io.StringIO()
    sys.stdout = captured
    print_exam_summary(test_scores)
    sys.stdout = sys.__stdout__
    output = captured.getvalue()
    if "66" in output and "2" in output:
        print("✓ 3c. feladat: Összesítő kiírás — OK")
    else:
        print("✗ 3c. feladat: Összesítő — használd a calculate_average_score és count_failed_students függvényeket!")
        errors += 1
except Exception as e:
    sys.stdout = sys.__stdout__
    print(f"✗ 3c. feladat: Összesítő — hiba: {e}")
    errors += 1

# 4. feladat
try:
    g1 = create_greeting("Anna")
    g2 = create_greeting("Béla", "este")
    g3 = create_greeting("Cecil", "dél")
    if g1 == "Jó reggelt, Anna!" and g2 == "Jó estét, Béla!" and g3 == "Szia, Cecil!":
        print("✓ 4. feladat: Köszönés — OK")
    else:
        print(f"✗ 4. feladat: Köszönés — ellenőrizd a visszatérési értékeket!")
        if g1 != "Jó reggelt, Anna!":
            print(f"  create_greeting('Anna') → '{g1}' (elvárt: 'Jó reggelt, Anna!')")
        if g2 != "Jó estét, Béla!":
            print(f"  create_greeting('Béla', 'este') → '{g2}' (elvárt: 'Jó estét, Béla!')")
        if g3 != "Szia, Cecil!":
            print(f"  create_greeting('Cecil', 'dél') → '{g3}' (elvárt: 'Szia, Cecil!')")
        errors += 1
except Exception as e:
    print(f"✗ 4. feladat: Köszönés — hiba: {e}")
    errors += 1

# 5. feladat
try:
    p1 = calculate_pizza_price("kicsi", 2, False)
    p2 = calculate_pizza_price("nagy", 1, True)
    if p1 == 3000 and p2 == 3400:
        print("✓ 5a. feladat: Pizza ár — OK")
    else:
        print(f"✗ 5a. feladat: Pizza ár — kicsi×2 kiszállítás nélkül={p1} (elvárt: 3000), nagy×1 kiszállítással={p2} (elvárt: 3400)")
        errors += 1
except Exception as e:
    print(f"✗ 5a. feladat: Pizza ár — hiba: {e}")
    errors += 1

try:
    captured = io.StringIO()
    sys.stdout = captured
    print_order_summary("Margherita", "közepes", 2, True, 4900)
    sys.stdout = sys.__stdout__
    output = captured.getvalue()
    if "Margherita" in output and "4900" in output:
        print("✓ 5b. feladat: Rendelés kiírás — OK")
    else:
        print("✗ 5b. feladat: Rendelés kiírás — írd ki a pizza nevét, méretet, darabszámot és árat!")
        errors += 1
except Exception as e:
    sys.stdout = sys.__stdout__
    print(f"✗ 5b. feladat: Rendelés kiírás — hiba: {e}")
    errors += 1

try:
    captured = io.StringIO()
    sys.stdout = captured
    process_pizza_order("Hawaii", "nagy", 3, True)
    sys.stdout = sys.__stdout__
    output = captured.getvalue()
    if "Hawaii" in output and "9200" in output:
        print("✓ 5c. feladat: Rendelés feldolgozás — OK")
    else:
        print("✗ 5c. feladat: Rendelés feldolgozás — használd a calculate_pizza_price és print_order_summary függvényeket!")
        errors += 1
except Exception as e:
    sys.stdout = sys.__stdout__
    print(f"✗ 5c. feladat: Rendelés feldolgozás — hiba: {e}")
    errors += 1

print("=" * 50)
if errors == 0:
    print("🎉 MINDEN FELADAT KÉSZ! Szólj nekem, és megnézem!")
else:
    print(f"Még {errors} feladat van hátra. Hajrá!")

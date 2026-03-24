"""
=============================================================
  1.3 GYAKORLAT: DRY és KISS — Ne ismételd magad, legyen egyszerű!
=============================================================

Öt feladat vár rád, egyre nehezebbek:
  1. Ismétlődő kód felismerése és függvénybe emelése
  2. Mágikus szám kiemelése konstansba
  3. Túlbonyolított kód egyszerűsítése (KISS)
  4. Komplex refaktorálás (DRY + KISS együtt)
  5. Saját függvény írása az ismétlődés kiváltására

A kód végén automatikus ellenőrző fut.

Futtasd:
    python 01-python-clean-code/exercises/exercise_03_dry_kiss.py
"""


# ============================================================
# 1. feladat: Ismétlődő kód → függvénybe emelés
#
# Az alábbi kód 3x csinálja UGYANAZT: kiszámolja egy téglalap
# területét és kiírja. Írd meg a calculate_rectangle_area()
# függvényt, hogy kiválthassa az ismétlődést!
#
# A függvény:
#   - KAPJA: a téglalap nevét (szöveg), szélességét (szám),
#            magasságát (szám)
#   - KIÍRJA: "{név} területe: {terület} cm²"
#   - VISSZAADJA: a területet (szám)
#
# Tipp: a terület = szélesség × magasság
# ============================================================

# --- EZT az ismétlődő kódot kell kiváltanod: ---
# width_1 = 10
# height_1 = 5
# area_1 = width_1 * height_1
# print(f"  Asztal területe: {area_1} cm²")
#
# width_2 = 3
# height_2 = 7
# area_2 = width_2 * height_2
# print(f"  Könyv területe: {area_2} cm²")
#
# width_3 = 20
# height_3 = 15
# area_3 = width_3 * height_3
# print(f"  Ablak területe: {area_3} cm²")

# --- IDE írd meg a függvényt: ---

def calculate_rectangle_area(name, width, height):
    """Kiszámolja egy téglalap területét, kiírja, és visszaadja."""
    pass    # ← töröld és írd meg a megoldást


# ============================================================
# 2. feladat: Mágikus szám → konstansba emelés
#
# Az alábbi kódban az ÁFA értéke (0.27) 5 helyen szerepel
# szám formában. Ez "mágikus szám" — ha az ÁFA változna,
# 5 helyen kellene átírni (és könnyen elfelejtenéd az egyiket).
#
# A te feladatod:
#   1. Hozz létre egy VAT_RATE konstanst a fájl tetején
#      (a függvény FELETT), aminek értéke 0.27
#   2. Írd meg a calculate_gross_price() függvényt,
#      ami HASZNÁLJA a VAT_RATE konstanst
#
# A függvény:
#   - KAPJA: a nettó árat (szám)
#   - VISSZAADJA: az áfás árat (nettó * (1 + VAT_RATE))
#   - NE írjon ki semmit!
#
# Tipp: az áfás ár = nettó ár × (1 + áfakulcs)
#       pl. 1000 Ft × 1.27 = 1270 Ft
# ============================================================

# --- EZT a kódot kell kiváltanod: ---
# price_a = 1000 * 1.27    # 1.27 = mágikus szám!
# price_b = 2500 * 1.27    # megint...
# price_c = 500 * 1.27     # megint...
# price_d = 8900 * 1.27    # megint...
# price_e = 3200 * 1.27    # ötödször is!

# --- IDE írd a konstanst: ---

# VAT_RATE = ???    # ← írd be az ÁFA kulcsot

# --- IDE írd meg a függvényt: ---

def calculate_gross_price(net_price):
    """Kiszámolja az áfás árat a nettó árból, a VAT_RATE konstans alapján."""
    pass    # ← töröld és írd meg a megoldást


# ============================================================
# 3. feladat: Túlbonyolított kód → egyszerűsítés (KISS)
#
# Az alábbi függvény eldönti, hogy egy szám pozitív, negatív,
# vagy nulla. De TÚLBONYOLÍTVA van — 15 sor, holott 3-4 sorban
# is megoldható!
#
# Írd meg a classify_number_simple() függvényt, ami UGYANAZT
# csinálja, de sokkal egyszerűbben.
#
# A függvény:
#   - KAPJA: egy számot
#   - VISSZAADJA: "pozitív", "negatív", vagy "nulla" (szövegként)
#   - NE írjon ki semmit!
#
# Tipp: if/elif/else — ennyi elég!
# ============================================================

# --- EZT a túlbonyolított kódot kell EGYSZERŰSÍTENED: ---
def classify_number_bad(number):
    """ROSSZ: Túlbonyolított szám-osztályozás."""
    result = ""
    is_positive = False
    is_negative = False
    is_zero = False
    if number > 0:
        is_positive = True
    if number < 0:
        is_negative = True
    if number == 0:
        is_zero = True
    if is_positive == True and is_negative == False and is_zero == False:
        result = "pozitív"
    elif is_negative == True and is_positive == False and is_zero == False:
        result = "negatív"
    elif is_zero == True and is_positive == False and is_negative == False:
        result = "nulla"
    return result

# --- IDE írd meg az egyszerű verziót: ---

def classify_number_simple(number):
    """Eldönti, hogy a szám pozitív, negatív, vagy nulla."""
    pass    # ← töröld és írd meg a megoldást (3-5 sor elég!)


# ============================================================
# 4. feladat: Komplex refaktorálás (DRY + KISS együtt)
#
# Az alábbi kód 3 termék kedvezményes árát számolja ki.
# Két problémája is van:
#   - DRY: ugyanaz a kedvezmény-számítás 3x le van írva
#   - KISS: a kedvezmény logika túl bonyolítva van
#
# A te feladatod:
#   1. Hozz létre egy DISCOUNT_PERCENT konstanst (értéke: 20)
#   2. Írd meg a calculate_discounted_price() függvényt
#
# A függvény:
#   - KAPJA: az eredeti árat (szám)
#   - VISSZAADJA: a kedvezményes árat (szám)
#   - NE írjon ki semmit!
#
# Tipp: kedvezményes ár = eredeti ár × (1 - kedvezmény/100)
#       pl. 10000 Ft × (1 - 20/100) = 10000 × 0.8 = 8000 Ft
# ============================================================

# --- EZT a kódot kell kiváltanod: ---
# # Laptop
# original_1 = 250000
# discount_1 = 20
# discount_amount_1 = original_1 / 100
# discount_amount_1 = discount_amount_1 * discount_1
# discounted_1 = original_1 - discount_amount_1
#
# # Telefon
# original_2 = 180000
# discount_2 = 20
# discount_amount_2 = original_2 / 100
# discount_amount_2 = discount_amount_2 * discount_2
# discounted_2 = original_2 - discount_amount_2
#
# # Tablet
# original_3 = 120000
# discount_3 = 20
# discount_amount_3 = original_3 / 100
# discount_amount_3 = discount_amount_3 * discount_3
# discounted_3 = original_3 - discount_amount_3

# --- IDE írd a konstanst: ---

# DISCOUNT_PERCENT = ???    # ← írd be a kedvezmény százalékot

# --- IDE írd meg a függvényt: ---

def calculate_discounted_price(original_price):
    """Kiszámolja a kedvezményes árat a DISCOUNT_PERCENT konstans alapján."""
    pass    # ← töröld és írd meg a megoldást


# ============================================================
# 5. feladat: Saját függvény az ismétlődés kiváltására
#
# Az alábbi kódban 4 diák adatait dolgozzuk fel ugyanúgy:
# kiszámoljuk az átlagát és kiírjuk, hogy átment-e (átlag >= 2.0).
#
# Írd meg a print_student_result() függvényt, ami KIVÁLTJA
# az ismétlődő kódot.
#
# A függvény:
#   - KAPJA: a diák nevét (szöveg) és a jegyeit (számok listája)
#   - KISZÁMOLJA: a jegyek átlagát
#   - KIÍRJA: "{név}: átlag {átlag:.1f} - {'átment' vagy 'megbukott'}"
#   - VISSZAADJA: True ha átment (átlag >= 2.0), False ha megbukott
#
# Tipp az átlaghoz: sum(lista) / len(lista)
#
# Például:
#   print_student_result("Anna", [5, 4, 3])
#   → kiírja: "Anna: átlag 4.0 - átment"
#   → visszaadja: True
# ============================================================

# --- EZT az ismétlődő kódot kell kiváltanod: ---
# total_anna = (5 + 4 + 3) / 3
# if total_anna >= 2.0:
#     print(f"  Anna: átlag {total_anna:.1f} - átment")
# else:
#     print(f"  Anna: átlag {total_anna:.1f} - megbukott")
#
# total_bela = (2 + 1 + 3) / 3
# if total_bela >= 2.0:
#     print(f"  Béla: átlag {total_bela:.1f} - átment")
# else:
#     print(f"  Béla: átlag {total_bela:.1f} - megbukott")
#
# total_cecil = (1 + 1 + 2) / 3
# if total_cecil >= 2.0:
#     print(f"  Cecil: átlag {total_cecil:.1f} - átment")
# else:
#     print(f"  Cecil: átlag {total_cecil:.1f} - megbukott")
#
# total_dora = (5 + 5 + 4) / 3
# if total_dora >= 2.0:
#     print(f"  Dóra: átlag {total_dora:.1f} - átment")
# else:
#     print(f"  Dóra: átlag {total_dora:.1f} - megbukott")

# --- IDE írd meg a függvényt: ---

def print_student_result(name, grades):
    """Kiírja a diák átlagát és hogy átment-e, visszaadja True/False."""
    pass    # ← töröld és írd meg a megoldást


# ============================================================
# ELLENŐRZÉS — ne módosítsd ezt a részt!
# ============================================================

import io
import sys

print("\n" + "=" * 50)
print("EREDMÉNYEK")
print("=" * 50)

errors = 0

# 1. feladat: calculate_rectangle_area
try:
    captured = io.StringIO()
    sys.stdout = captured
    result_1 = calculate_rectangle_area("Teszt", 10, 5)
    sys.stdout = sys.__stdout__
    output_1 = captured.getvalue()

    if result_1 is None:
        print("✗ 1. feladat: Téglalap terület — a függvény None-t ad vissza.")
        print("  Tipp: használj return-t a terület visszaadásához!")
        errors += 1
    elif result_1 != 50:
        print(f"✗ 1. feladat: Téglalap terület — eredmény: {result_1}, elvárt: 50")
        print("  Tipp: terület = szélesség × magasság (10 × 5 = 50)")
        errors += 1
    elif "Teszt" not in output_1 or "50" not in output_1:
        print("✗ 1. feladat: Téglalap terület — a kiírás nem tartalmazza a nevet vagy a területet.")
        print("  Tipp: print(f\"{name} területe: {area} cm²\")")
        errors += 1
    else:
        # Teszteljük másik mérettel is
        captured2 = io.StringIO()
        sys.stdout = captured2
        result_1b = calculate_rectangle_area("Ablak", 20, 15)
        sys.stdout = sys.__stdout__
        if result_1b == 300:
            print("✓ 1. feladat: Téglalap terület — OK")
        else:
            print(f"✗ 1. feladat: Téglalap terület — 20×15 = {result_1b}, elvárt: 300")
            errors += 1
except Exception as e:
    sys.stdout = sys.__stdout__
    print(f"✗ 1. feladat: Téglalap terület — hiba: {e}")
    errors += 1

# 2. feladat: VAT_RATE + calculate_gross_price
try:
    # Ellenőrizzük, hogy létezik-e a VAT_RATE konstans
    try:
        vat = VAT_RATE
        if vat is None or vat == 0:
            raise ValueError("VAT_RATE nincs beállítva")
    except NameError:
        print("✗ 2. feladat: ÁFA számítás — a VAT_RATE konstans nem létezik!")
        print("  Tipp: a függvény FELETT hozd létre: VAT_RATE = 0.27")
        errors += 1
        raise

    result_2 = calculate_gross_price(1000)

    if result_2 is None:
        print("✗ 2. feladat: ÁFA számítás — a függvény None-t ad vissza.")
        print("  Tipp: használj return-t! return net_price * (1 + VAT_RATE)")
        errors += 1
    elif abs(result_2 - 1270) > 0.01:
        print(f"✗ 2. feladat: ÁFA számítás — 1000 Ft áfásan = {result_2}, elvárt: 1270.0")
        print("  Tipp: áfás ár = nettó × (1 + 0.27) = nettó × 1.27")
        errors += 1
    else:
        # Teszteljük más értékkel is
        result_2b = calculate_gross_price(2500)
        if abs(result_2b - 3175) < 0.01:
            print("✓ 2. feladat: ÁFA számítás — OK")
        else:
            print(f"✗ 2. feladat: ÁFA számítás — 2500 Ft áfásan = {result_2b}, elvárt: 3175.0")
            errors += 1
except NameError:
    pass  # Már kiírtuk a hibát fentebb
except Exception as e:
    sys.stdout = sys.__stdout__
    print(f"✗ 2. feladat: ÁFA számítás — hiba: {e}")
    errors += 1

# 3. feladat: classify_number_simple
try:
    r_pos = classify_number_simple(42)
    r_neg = classify_number_simple(-7)
    r_zero = classify_number_simple(0)

    if r_pos is None and r_neg is None and r_zero is None:
        print("✗ 3. feladat: Szám osztályozás — a függvény None-t ad vissza.")
        print("  Tipp: használj return-t! Pl.: return \"pozitív\"")
        errors += 1
    elif r_pos == "pozitív" and r_neg == "negatív" and r_zero == "nulla":
        print("✓ 3. feladat: Szám osztályozás — OK")
    else:
        print("✗ 3. feladat: Szám osztályozás — helytelen eredmény:")
        if r_pos != "pozitív":
            print(f"  42 → \"{r_pos}\", elvárt: \"pozitív\"")
        if r_neg != "negatív":
            print(f"  -7 → \"{r_neg}\", elvárt: \"negatív\"")
        if r_zero != "nulla":
            print(f"  0 → \"{r_zero}\", elvárt: \"nulla\"")
        print("  Tipp: if number > 0 → \"pozitív\", elif number < 0 → \"negatív\", else → \"nulla\"")
        errors += 1
except Exception as e:
    print(f"✗ 3. feladat: Szám osztályozás — hiba: {e}")
    errors += 1

# 4. feladat: DISCOUNT_PERCENT + calculate_discounted_price
try:
    try:
        disc = DISCOUNT_PERCENT
        if disc is None or disc == 0:
            raise ValueError("DISCOUNT_PERCENT nincs beállítva")
    except NameError:
        print("✗ 4. feladat: Kedvezmény — a DISCOUNT_PERCENT konstans nem létezik!")
        print("  Tipp: a függvény FELETT hozd létre: DISCOUNT_PERCENT = 20")
        errors += 1
        raise

    result_4 = calculate_discounted_price(250000)

    if result_4 is None:
        print("✗ 4. feladat: Kedvezmény — a függvény None-t ad vissza.")
        print("  Tipp: return original_price * (1 - DISCOUNT_PERCENT / 100)")
        errors += 1
    elif abs(result_4 - 200000) > 0.01:
        print(f"✗ 4. feladat: Kedvezmény — 250000 Ft 20% kedvezménnyel = {result_4}, elvárt: 200000")
        print("  Tipp: kedvezményes = eredeti × (1 - 20/100) = eredeti × 0.8")
        errors += 1
    else:
        result_4b = calculate_discounted_price(180000)
        if abs(result_4b - 144000) < 0.01:
            print("✓ 4. feladat: Kedvezmény — OK")
        else:
            print(f"✗ 4. feladat: Kedvezmény — 180000 Ft kedvezménnyel = {result_4b}, elvárt: 144000")
            errors += 1
except NameError:
    pass  # Már kiírtuk a hibát fentebb
except Exception as e:
    sys.stdout = sys.__stdout__
    print(f"✗ 4. feladat: Kedvezmény — hiba: {e}")
    errors += 1

# 5. feladat: print_student_result
try:
    # Anna: [5, 4, 3] → átlag 4.0 → átment (True)
    captured = io.StringIO()
    sys.stdout = captured
    result_5a = print_student_result("Anna", [5, 4, 3])
    sys.stdout = sys.__stdout__
    output_5a = captured.getvalue()

    if result_5a is None:
        print("✗ 5. feladat: Diák eredmény — a függvény None-t ad vissza.")
        print("  Tipp: return True ha átment (átlag >= 2.0), return False ha megbukott")
        errors += 1
    elif result_5a != True:
        print(f"✗ 5. feladat: Diák eredmény — Anna [5,4,3] átlaga 4.0, átment → True kell, de {result_5a}")
        errors += 1
    elif "Anna" not in output_5a:
        print("✗ 5. feladat: Diák eredmény — a kiírásban nem szerepel a diák neve.")
        print("  Tipp: print(f\"{name}: átlag {average:.1f} - átment\")")
        errors += 1
    else:
        # Teszteljük bukott diákkal is
        captured2 = io.StringIO()
        sys.stdout = captured2
        result_5b = print_student_result("Teszt", [1, 1, 1])
        sys.stdout = sys.__stdout__
        output_5b = captured2.getvalue()

        if result_5b == False and "megbukott" in output_5b:
            print("✓ 5. feladat: Diák eredmény — OK")
        elif result_5b != False:
            print(f"✗ 5. feladat: Diák eredmény — [1,1,1] átlaga 1.0, bukott → False kell, de {result_5b}")
            errors += 1
        else:
            print("✗ 5. feladat: Diák eredmény — ha megbukott, a kiírásban legyen benne: \"megbukott\"")
            errors += 1
except Exception as e:
    sys.stdout = sys.__stdout__
    print(f"✗ 5. feladat: Diák eredmény — hiba: {e}")
    errors += 1

print("=" * 50)
if errors == 0:
    print("🎉 MINDEN FELADAT KÉSZ! Szólj nekem, és megnézem!")
else:
    print(f"Még {errors} feladat van hátra. Hajrá!")

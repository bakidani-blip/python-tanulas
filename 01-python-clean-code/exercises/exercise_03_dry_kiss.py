"""
=============================================================
1.3 GYAKORLAT: DRY és KISS — Ne ismételd magad!
=============================================================
"""

# @TASK 1. Ismétlődő kód → függvénybe emelés
# @DESC Az alábbi 3 sor UGYANAZT csinálja: téglalap területét számolja és kiírja.
# Írd meg a `calculate_rectangle_area(name, width, height)` függvényt,
# ami kiírja **"{név} területe: {terület} cm2"** és **visszaadja** a területet.
# @HINT `area = width * height`, `print(f"{name} területe: {area} cm2")`, `return area`
# @CODE
# Ezt az ismétlődő kódot kell kiváltanod egy függvénnyel:
# area_1 = 10 * 5    → print("Asztal területe: 50 cm2")
# area_2 = 3 * 7     → print("Könyv területe: 21 cm2")
# area_3 = 20 * 15   → print("Ablak területe: 300 cm2")

def calculate_rectangle_area(name, width, height):
    # MEGOLDÁS IDE:
    pass

# ELLENŐRZÉS:
r1 = calculate_rectangle_area("Teszt", 10, 5)
if r1 == 50:
    r2 = calculate_rectangle_area("Ablak", 20, 15)
    if r2 == 300:
        print("✓ OK — függvény működik!")
    else:
        print("✗ calculate_rectangle_area('Ablak', 20, 15) = 300 kéne!")
else:
    print("✗ calculate_rectangle_area('Teszt', 10, 5) = 50 kéne! Kaptam:", r1)
# @END

# @TASK 2. Mágikus szám → konstansba
# @DESC Az ÁFA értéke (0.27) több helyen szerepel számként — ez "mágikus szám".
# Hozz létre egy `VAT_RATE = 0.27` konstanst, és írd meg a
# `calculate_gross_price(net_price)` függvényt, ami visszaadja az **áfás árat**.
# @HINT Áfás ár = `net_price * (1 + VAT_RATE)`. Példa: 1000 * 1.27 = 1270
# @CODE
# MEGOLDÁS IDE — először a konstans, aztán a függvény:


# ELLENŐRZÉS:
r = calculate_gross_price(1000)
if r is not None and abs(r - 1270) < 0.01:
    print("✓ OK — 1000 Ft áfásan:", r)
else:
    print("✗ calculate_gross_price(1000) = 1270 kéne!")
# @END

# @TASK 3. Túlbonyolított kód → egyszerűsítés (KISS)
# @DESC Az alábbi függvény 15 sorban dönti el, hogy egy szám pozitív, negatív vagy nulla.
# Írd meg a `classify_number(number)` függvényt **3-4 sorban**! Visszaadja: `"pozitiv"`, `"negativ"`, vagy `"nulla"`.
# @HINT `if number > 0: return "pozitiv"` — `elif number < 0: return "negativ"` — `else: return "nulla"`
# @CODE
def classify_number(number):
    # MEGOLDÁS IDE (3-4 sor elég!):
    pass

# ELLENŐRZÉS:
r1 = classify_number(42)
r2 = classify_number(-7)
r3 = classify_number(0)
if r1 == "pozitiv" and r2 == "negativ" and r3 == "nulla":
    print("✓ OK — classify_number működik")
else:
    print("✗ 42='pozitiv', -7='negativ', 0='nulla' kéne!")
    print("  Kaptam:", r1, r2, r3)
# @END

# @TASK 4. Kedvezmény számítás (DRY + KISS)
# @DESC Hozz létre egy `DISCOUNT_PERCENT = 20` konstanst és írd meg a
# `calculate_discounted_price(original_price)` függvényt.
# Képlet: **kedvezményes ár = eredeti ár * (1 - kedvezmény/100)**
# @HINT `return original_price * (1 - DISCOUNT_PERCENT / 100)` → 250000 * 0.8 = 200000
# @CODE
# MEGOLDÁS IDE — konstans + függvény:


# ELLENŐRZÉS:
r = calculate_discounted_price(250000)
if r is not None and abs(r - 200000) < 0.01:
    print("✓ OK — 250000 Ft 20% kedvezmény:", r)
else:
    print("✗ calculate_discounted_price(250000) = 200000 kéne!")
# @END

# @TASK 5. Diák eredmény kiírás
# @DESC Írd meg a `print_student_result(name, grades)` függvényt.
# Számolja ki a jegyek **átlagát**, írja ki: **"{név}: átlag {átlag:.1f} - átment/megbukott"**
# (átment ha átlag >= 2.0). **Visszaadja**: `True` ha átment, `False` ha megbukott.
# @HINT `avg = sum(grades) / len(grades)`, `if avg >= 2.0: ... return True else: ... return False`
# @CODE
def print_student_result(name, grades):
    # MEGOLDÁS IDE:
    pass

# ELLENŐRZÉS:
r1 = print_student_result("Anna", [5, 4, 3])
r2 = print_student_result("Bela", [1, 1, 1])
if r1 == True and r2 == False:
    print("✓ OK — függvény működik!")
else:
    print("✗ Anna [5,4,3] → True, Bela [1,1,1] → False kéne!")
# @END

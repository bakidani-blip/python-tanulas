"""
=============================================================
1.3 GYAKORLAT: DRY es KISS — Ne ismeteld magad!
=============================================================
"""

# @TASK 1. Ismetlodo kod → fuggvenybe emeles
# @DESC Az alabbi 3 sor UGYANAZT csinalja: teglalap teruletet szamolja es kiirja.
# Ird meg a `calculate_rectangle_area(name, width, height)` fuggvenyt,
# ami kiirja **"{nev} terulete: {terulet} cm2"** es **visszaadja** a teruletet.
# @HINT `area = width * height`, `print(f"{name} terulete: {area} cm2")`, `return area`
# @CODE
# Ezt az ismetlodo kodot kell kivaltanod egy fuggvennyel:
# area_1 = 10 * 5    → print("Asztal terulete: 50 cm2")
# area_2 = 3 * 7     → print("Konyv terulete: 21 cm2")
# area_3 = 20 * 15   → print("Ablak terulete: 300 cm2")

def calculate_rectangle_area(name, width, height):
    # MEGOLDAS IDE:
    pass

# ELLENORZES:
r1 = calculate_rectangle_area("Teszt", 10, 5)
if r1 == 50:
    r2 = calculate_rectangle_area("Ablak", 20, 15)
    if r2 == 300:
        print("✓ OK — fuggveny mukodik!")
    else:
        print("✗ calculate_rectangle_area('Ablak', 20, 15) = 300 kene!")
else:
    print("✗ calculate_rectangle_area('Teszt', 10, 5) = 50 kene! Kaptam:", r1)
# @END

# @TASK 2. Magikus szam → konstansba
# @DESC Az AFA erteke (0.27) tobb helyen szerepel szamkent — ez "magikus szam".
# Hozz letre egy `VAT_RATE = 0.27` konstanst, es ird meg a
# `calculate_gross_price(net_price)` fuggvenyt, ami visszaadja az **afas arat**.
# @HINT Afas ar = `net_price * (1 + VAT_RATE)`. Pelda: 1000 * 1.27 = 1270
# @CODE
# MEGOLDAS IDE — eloszor a konstans, aztan a fuggveny:


# ELLENORZES:
r = calculate_gross_price(1000)
if r is not None and abs(r - 1270) < 0.01:
    print("✓ OK — 1000 Ft afasan:", r)
else:
    print("✗ calculate_gross_price(1000) = 1270 kene!")
# @END

# @TASK 3. Tulbonyolitott kod → egyszerusites (KISS)
# @DESC Az alabbi fuggveny 15 sorban donti el, hogy egy szam pozitiv, negativ vagy nulla.
# Ird meg a `classify_number(number)` fuggvenyt **3-4 sorban**! Visszaadja: `"pozitiv"`, `"negativ"`, vagy `"nulla"`.
# @HINT `if number > 0: return "pozitiv"` — `elif number < 0: return "negativ"` — `else: return "nulla"`
# @CODE
def classify_number(number):
    # MEGOLDAS IDE (3-4 sor eleg!):
    pass

# ELLENORZES:
r1 = classify_number(42)
r2 = classify_number(-7)
r3 = classify_number(0)
if r1 == "pozitiv" and r2 == "negativ" and r3 == "nulla":
    print("✓ OK — classify_number mukodik")
else:
    print("✗ 42='pozitiv', -7='negativ', 0='nulla' kene!")
    print("  Kaptam:", r1, r2, r3)
# @END

# @TASK 4. Kedvezmeny szamitas (DRY + KISS)
# @DESC Hozz letre egy `DISCOUNT_PERCENT = 20` konstanst es ird meg a
# `calculate_discounted_price(original_price)` fuggvenyt.
# Keplet: **kedvezmenyes ar = eredeti ar * (1 - kedvezmeny/100)**
# @HINT `return original_price * (1 - DISCOUNT_PERCENT / 100)` → 250000 * 0.8 = 200000
# @CODE
# MEGOLDAS IDE — konstans + fuggveny:


# ELLENORZES:
r = calculate_discounted_price(250000)
if r is not None and abs(r - 200000) < 0.01:
    print("✓ OK — 250000 Ft 20% kedvezmeny:", r)
else:
    print("✗ calculate_discounted_price(250000) = 200000 kene!")
# @END

# @TASK 5. Diak eredmeny kiiras
# @DESC Ird meg a `print_student_result(name, grades)` fuggvenyt.
# Szamolja ki a jegyek **atlaga**t, irja ki: **"{nev}: atlag {atlag:.1f} - atment/megbukott"**
# (atment ha atlag >= 2.0). **Visszaadja**: `True` ha atment, `False` ha megbukott.
# @HINT `avg = sum(grades) / len(grades)`, `if avg >= 2.0: ... return True else: ... return False`
# @CODE
def print_student_result(name, grades):
    # MEGOLDAS IDE:
    pass

# ELLENORZES:
r1 = print_student_result("Anna", [5, 4, 3])
r2 = print_student_result("Bela", [1, 1, 1])
if r1 == True and r2 == False:
    print("✓ OK — fuggveny mukodik!")
else:
    print("✗ Anna [5,4,3] → True, Bela [1,1,1] → False kene!")
# @END

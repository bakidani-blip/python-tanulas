"""
=============================================================
1.2 GYAKORLAT: Függvények — Egy feladat, egy függvény
=============================================================
"""

# @TASK 1. Kör kerülete
# @DESC Írj egy függvényt `calculate_circumference` néven, ami kiszámolja egy **kör kerületét**.
# Képlet: **kerület = 2 * 3.14159 * sugár**. A függvény VISSZAADJA az eredményt (`return`).
# @HINT `def calculate_circumference(radius): return 2 * 3.14159 * radius`
# @CODE
PI = 3.14159

def calculate_circumference(radius):
    # MEGOLDÁS IDE:
    pass

# ELLENŐRZÉS:
result = calculate_circumference(10)
expected = 2 * PI * 10
if result is not None and abs(result - expected) < 0.01:
    print("✓ OK — kerület:", round(result, 2))
else:
    print("✗ calculate_circumference(10) =", round(expected, 2), "kéne legyen!")
# @END

# @TASK 2. Átment-e a vizsgán?
# @DESC Írj egy függvényt `is_passing` néven: ha a pontszám **>= 50**, adjon vissza `True`,
# különben `False`. Boolean függvény → `is_` előtag!
# @HINT `return score >= 50`
# @CODE
def is_passing(score):
    # MEGOLDÁS IDE:
    pass

# ELLENŐRZÉS:
if is_passing(75) == True and is_passing(50) == True and is_passing(49) == False:
    print("✓ OK — is_passing működik")
else:
    print("✗ is_passing(75)=True, is_passing(50)=True, is_passing(49)=False kéne!")
# @END

# @TASK 3. Átlag számolás
# @DESC Írj egy függvényt `calculate_average` néven: kap egy **számlistát**,
# és visszaadja az **átlagot** (összeg / elemszám).
# @HINT `return sum(scores) / len(scores)`
# @CODE
def calculate_average(scores):
    # MEGOLDÁS IDE:
    pass

# ELLENŐRZÉS:
test = [85, 42, 73, 91, 38, 67]
avg = calculate_average(test)
if avg is not None and abs(avg - 66.0) < 0.01:
    print("✓ OK — átlag:", round(avg, 1))
else:
    print("✗ calculate_average([85,42,73,91,38,67]) = 66.0 kéne legyen!")
# @END

# @TASK 4. Köszöntés alapértelmezett paraméterrel
# @DESC Írj egy függvényt `create_greeting` néven:
# Kapja a **nevet** (kötelező) és az **időszakot** (alapértelmezetten `"reggel"`).
# `"reggel"` → `"Jo reggelt, X!"`, `"este"` → `"Jo estet, X!"`, bármi más → `"Szia, X!"`
# @HINT `def create_greeting(name, time_of_day="reggel"):` és használj `if/elif/else`-t
# @CODE
def create_greeting(name, time_of_day="reggel"):
    # MEGOLDÁS IDE:
    pass

# ELLENŐRZÉS:
g1 = create_greeting("Anna")
g2 = create_greeting("Bela", "este")
g3 = create_greeting("Cecil", "del")
errors = 0
if g1 == "Jo reggelt, Anna!":
    print("✓ create_greeting('Anna') — OK")
else:
    print("✗ Várt: 'Jo reggelt, Anna!', kaptam:", g1)
    errors += 1
if g2 == "Jo estet, Bela!":
    print("✓ create_greeting('Bela', 'este') — OK")
else:
    print("✗ Várt: 'Jo estet, Bela!', kaptam:", g2)
    errors += 1
if g3 == "Szia, Cecil!":
    print("✓ create_greeting('Cecil', 'del') — OK")
else:
    print("✗ Várt: 'Szia, Cecil!', kaptam:", g3)
    errors += 1
if errors == 0:
    print("MINDEN FELADAT KÉSZ!")
# @END

# @TASK 5. Pizza ár számítás
# @DESC Írj egy függvényt `calculate_pizza_price` néven.
# Kapja: `size` ("kicsi"/"kozepes"/"nagy"), `quantity` (darabszám), `is_delivery` (True/False).
# Árak: kicsi=1500, közepes=2200, nagy=2900. Ha kiszállítás: +500 Ft.
# @HINT Használj szótárat: `prices = {"kicsi": 1500, "kozepes": 2200, "nagy": 2900}`
# @CODE
DELIVERY_FEE = 500

def calculate_pizza_price(size, quantity, is_delivery):
    # MEGOLDÁS IDE:
    pass

# ELLENŐRZÉS:
p1 = calculate_pizza_price("kicsi", 2, False)
p2 = calculate_pizza_price("nagy", 1, True)
if p1 == 3000 and p2 == 3400:
    print("✓ OK — kicsi x2 =", p1, ", nagy x1 + kiszállítás =", p2)
else:
    print("✗ kicsi x2 = 3000 és nagy x1 + kiszállítás = 3400 kéne!")
    print("  Kaptam:", p1, "és", p2)
# @END

"""
=============================================================
1.2 GYAKORLAT: Fuggvenyek — Egy feladat, egy fuggveny
=============================================================
"""

# @TASK 1. Kor kerulete
# @DESC Irj egy fuggvenyt `calculate_circumference` neven, ami kiszamolja egy **kor keruletet**.
# Keplet: **kerulet = 2 * 3.14159 * sugar**. A fuggveny VISSZAADJA az eredmenyt (`return`).
# @HINT `def calculate_circumference(radius): return 2 * 3.14159 * radius`
# @CODE
PI = 3.14159

def calculate_circumference(radius):
    # MEGOLDAS IDE:
    pass

# ELLENORZES:
result = calculate_circumference(10)
expected = 2 * PI * 10
if result is not None and abs(result - expected) < 0.01:
    print("✓ OK — kerulet:", round(result, 2))
else:
    print("✗ calculate_circumference(10) =", round(expected, 2), "kene legyen!")
# @END

# @TASK 2. Atment-e a vizsgán?
# @DESC Irj egy fuggvenyt `is_passing` neven: ha a pontszam **>= 50**, adjon vissza `True`,
# kulonben `False`. Boolean fuggveny → `is_` elotag!
# @HINT `return score >= 50`
# @CODE
def is_passing(score):
    # MEGOLDAS IDE:
    pass

# ELLENORZES:
if is_passing(75) == True and is_passing(50) == True and is_passing(49) == False:
    print("✓ OK — is_passing mukodik")
else:
    print("✗ is_passing(75)=True, is_passing(50)=True, is_passing(49)=False kene!")
# @END

# @TASK 3. Atlag szamolas
# @DESC Irj egy fuggvenyt `calculate_average` neven: kap egy **szamlistat**,
# es visszaadja az **atlagot** (osszeg / elemszam).
# @HINT `return sum(scores) / len(scores)`
# @CODE
def calculate_average(scores):
    # MEGOLDAS IDE:
    pass

# ELLENORZES:
test = [85, 42, 73, 91, 38, 67]
avg = calculate_average(test)
if avg is not None and abs(avg - 66.0) < 0.01:
    print("✓ OK — atlag:", round(avg, 1))
else:
    print("✗ calculate_average([85,42,73,91,38,67]) = 66.0 kene legyen!")
# @END

# @TASK 4. Koszontes alapertelmezett parameterrel
# @DESC Irj egy fuggvenyt `create_greeting` neven:
# Kapja a **nevet** (kotelezo) es az **idoszakot** (alapertelmezetten `"reggel"`).
# `"reggel"` → `"Jo reggelt, X!"`, `"este"` → `"Jo estet, X!"`, barmi mas → `"Szia, X!"`
# @HINT `def create_greeting(name, time_of_day="reggel"):` es hasznalj `if/elif/else`-t
# @CODE
def create_greeting(name, time_of_day="reggel"):
    # MEGOLDAS IDE:
    pass

# ELLENORZES:
g1 = create_greeting("Anna")
g2 = create_greeting("Bela", "este")
g3 = create_greeting("Cecil", "del")
errors = 0
if g1 == "Jo reggelt, Anna!":
    print("✓ create_greeting('Anna') — OK")
else:
    print("✗ Vart: 'Jo reggelt, Anna!', kaptam:", g1)
    errors += 1
if g2 == "Jo estet, Bela!":
    print("✓ create_greeting('Bela', 'este') — OK")
else:
    print("✗ Vart: 'Jo estet, Bela!', kaptam:", g2)
    errors += 1
if g3 == "Szia, Cecil!":
    print("✓ create_greeting('Cecil', 'del') — OK")
else:
    print("✗ Vart: 'Szia, Cecil!', kaptam:", g3)
    errors += 1
if errors == 0:
    print("MINDEN FELADAT KESZ!")
# @END

# @TASK 5. Pizza ar szamitas
# @DESC Irj egy fuggvenyt `calculate_pizza_price` neven.
# Kapja: `size` ("kicsi"/"kozepes"/"nagy"), `quantity` (darabszam), `is_delivery` (True/False).
# Arak: kicsi=1500, kozepes=2200, nagy=2900. Ha kiszallitas: +500 Ft.
# @HINT Hasznalj szotarat: `prices = {"kicsi": 1500, "kozepes": 2200, "nagy": 2900}`
# @CODE
DELIVERY_FEE = 500

def calculate_pizza_price(size, quantity, is_delivery):
    # MEGOLDAS IDE:
    pass

# ELLENORZES:
p1 = calculate_pizza_price("kicsi", 2, False)
p2 = calculate_pizza_price("nagy", 1, True)
if p1 == 3000 and p2 == 3400:
    print("✓ OK — kicsi x2 =", p1, ", nagy x1 + kiszallitas =", p2)
else:
    print("✗ kicsi x2 = 3000 es nagy x1 + kiszallitas = 3400 kene!")
    print("  Kaptam:", p1, "es", p2)
# @END

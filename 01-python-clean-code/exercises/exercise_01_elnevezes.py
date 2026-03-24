"""
=============================================================
  1.1 GYAKORLAT: Változók és elnevezések — Clean Code
=============================================================

Az alábbi kódokban SZÁNDÉKOSAN rossz nevek vannak.
A te feladatod: írd át MINDEN nevet a Python konvenciók szerint.

Szabályok:
  - Változók, függvények → snake_case
  - Konstansok → UPPER_SNAKE_CASE
  - Osztályok → PascalCase
  - Boolean → is_/has_/can_ előtaggal
  - Beszédes, értelmes nevek (ne rövidíts!)

A kód LOGIKÁJÁT ne változtasd — csak a neveket!

Futtasd:
    python 01-python-clean-code/exercises/exercise_01_elnevezes.py
"""


# ============================================================
# 1. feladat: Változók átnevezése
#
# Az alábbi változóknál rossz az elnevezés.
# Nevezd át MINDEGYIKET a konvencióknak megfelelően.
# A hozzájuk rendelt értéket NE változtasd!
#
# Tipp: gondolj bele, mit TÁROL a változó,
#       és adj neki olyan nevet, amiből ez kiderül.
# ============================================================

user_name = "Kiss Péter"           # ← ez egy személy neve
user_age = 42                     # ← ez egy életkor
user_city = "Budapest"             # ← ez egy város
body_temperature = 36.6                   # ← ez egy testhőmérséklet
days_left = 7                      # ← ez a hátralevő napok száma

# MEGOLDÁS IDE — írd felül a fenti sorokat jó nevekkel:



# ============================================================
# 2. feladat: Konstansok átnevezése
#
# Ezek az értékek a program futása során SOHA nem változnak.
# Nevezd át őket a konstansok konvenciója szerint (UPPER_SNAKE_CASE).
# Az értékeket NE változtasd!
# ============================================================

MAX_ATTEMPTS = 5                     # ← max próbálkozások száma
TAX_RATE = 0.27                  # ← adókulcs
API_URL = "https://api.example.com/v2"  # ← API webcím
PI = 3.14159                # ← pi értéke (matematikai állandó)

# MEGOLDÁS IDE — írd felül a fenti sorokat:



# ============================================================
# 3. feladat: Boolean változók átnevezése
#
# Boolean = igaz/hamis érték.
# A konvenció: a nevük KÉRDÉS legyen (is_, has_, can_ előtag).
# Példa: active → is_active ("aktív-e?")
#
# Nevezd át mindegyiket!
# ============================================================

is_active = True               # ← aktív-e a felhasználó?
is_admin = False               # ← adminisztrátor-e?
is_logged_in = True             # ← be van-e jelentkezve?
has_items = False               # ← van-e termék a kosarában?

# MEGOLDÁS IDE — írd felül a fenti sorokat:



# ============================================================
# 4. feladat: Függvény átnevezése
#
# Az alábbi függvénynek rossz a neve ÉS a paramétereinek neve is.
# Nevezd át a függvényt ÉS a paramétereit is.
#
# Mi a függvény neve most? "calc" — de MIT számol?
# Mi az "a" és "b"? Ránézésre nem tudom.
#
# Tipp: a függvény kiszámolja a téglalap területét.
#       A két paraméter a szélesség és a magasság.
#       A függvények neve IGÉVEL kezdődik!
# ============================================================

def calculate_area(width, height):
    return width * height

# MEGOLDÁS IDE — írd újra a függvényt jó névvel és paraméternevekkel:



# ============================================================
# 5. feladat: Vegyes — javítsd ki az egész kódrészletet
#
# Az alábbi kód egy bevásárlást számol ki.
# MINDEN elnevezés rossz benne.
# Írd át az ÖSSZESET — változókat, konstanst, függvényt!
#
# A kód logikáját NE változtasd, csak a neveket.
# ============================================================

TAX_RATE = 0.27                   # ez az áfa

def calculate_total_price(net_price, quantity):
    """Kiszámolja a végösszeget áfával."""
    net_total = net_price * quantity               # nettó összeg
    tax_amount = net_total * TAX_RATE              # áfa összeg
    return net_total + tax_amount            # bruttó összeg



# MEGOLDÁS IDE — írd újra az egész kódrészletet jó nevekkel:



# ============================================================
# ELLENŐRZÉS — ne módosítsd ezt a részt!
# ============================================================

print("\n" + "=" * 50)
print("EREDMÉNYEK")
print("=" * 50)

errors = 0

# 1. feladat — változónevek ellenőrzése
# (Az ellenőrző a "jó" neveket keresi a globális névtérben)
g = globals()

task1_names = {
    "személy neve": ["person_name", "user_name", "full_name", "name"],
    "életkor": ["age", "person_age", "user_age"],
    "város": ["city", "person_city", "user_city", "home_city"],
    "testhőmérséklet": ["body_temperature", "temperature", "body_temp"],
    "hátralevő napok": ["days_until_deadline", "days_remaining", "remaining_days", "days_left"],
}

task1_ok = True
for desc, valid_names in task1_names.items():
    found = any(name in g for name in valid_names)
    if not found:
        task1_ok = False

if task1_ok:
    print("✓ 1. feladat: Változók — OK")
else:
    print("✗ 1. feladat: Változók — adj beszédes snake_case neveket (pl. person_name, age, city...)")
    errors += 1

# 2. feladat — konstansok
task2_names = ["MAX_RETRIES", "MAX_ATTEMPTS", "TAX_RATE", "API_URL", "PI"]
task2_found = sum(1 for name in task2_names if name in g)
if task2_found >= 4:
    print("✓ 2. feladat: Konstansok — OK")
else:
    print("✗ 2. feladat: Konstansok — használj UPPER_SNAKE_CASE-t (pl. MAX_RETRIES, TAX_RATE...)")
    errors += 1

# 3. feladat — boolean
task3_prefixes = ["is_", "has_", "can_"]
task3_bools = [name for name, val in g.items()
               if isinstance(val, bool) and any(name.startswith(p) for p in task3_prefixes)]
if len(task3_bools) >= 4:
    print("✓ 3. feladat: Boolean változók — OK")
else:
    print(f"✗ 3. feladat: Boolean — {len(task3_bools)}/4 jó. Használj is_/has_/can_ előtagot!")
    errors += 1

# 4. feladat — függvény
task4_good_names = ["calculate_area", "calculate_rectangle_area", "get_rectangle_area", "compute_area"]
task4_ok = any(name in g and callable(g[name]) for name in task4_good_names)
if task4_ok:
    # Teszteljük is, hogy működik-e
    func = next(g[name] for name in task4_good_names if name in g and callable(g[name]))
    if func(5, 3) == 15:
        print("✓ 4. feladat: Függvény — OK")
    else:
        print("✗ 4. feladat: Függvény — a név jó, de az eredmény nem stimmel!")
        errors += 1
else:
    print("✗ 4. feladat: Függvény — adj igével kezdődő, beszédes nevet (pl. calculate_rectangle_area)")
    errors += 1

# 5. feladat — vegyes
task5_ok = True
# Van-e konstans az áfának?
if "TAX_RATE" not in g:
    task5_ok = False
# Van-e jól elnevezett függvény?
task5_func_names = ["calculate_total_price", "calculate_gross_price", "calculate_total",
                     "calculate_total_with_tax", "calculate_price_with_tax"]
if not any(name in g and callable(g[name]) for name in task5_func_names):
    task5_ok = False

if task5_ok:
    func = next(g[name] for name in task5_func_names if name in g and callable(g[name]))
    expected = 2500 * 3 * (1 + 0.27)
    result = func(2500, 3)
    if abs(result - expected) < 0.01:
        print("✓ 5. feladat: Vegyes — OK")
    else:
        print("✗ 5. feladat: Vegyes — a nevek jók, de az eredmény nem stimmel!")
        errors += 1
else:
    print("✗ 5. feladat: Vegyes — használj TAX_RATE konstanst és beszédes függvénynevet!")
    errors += 1

print("=" * 50)
if errors == 0:
    print("🎉 MINDEN FELADAT KÉSZ! Szólj nekem, és megnézem!")
else:
    print(f"Még {errors} feladat van hátra. Hajrá!")

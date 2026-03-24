"""
=============================================================
  1.2 LECKE: Függvények — Egy feladat, egy függvény
=============================================================

Eddig tanultál:
  - Változókat, típusokat, ciklusokat (0. lecke)
  - Jó elnevezéseket (1.1 lecke)

Most megtanulod:
  - Miért fontos, hogy egy függvény CSAK EGY dolgot csináljon
  - Hogyan bontsd szét a nagy, bonyolult kódot kis függvényekre
  - Mikor kell új függvényt írni

Futtasd:
    python 01-python-clean-code/exercises/02_fuggvenyek_alapok.py
"""


# ============================================================
# 1. MI A FÜGGVÉNY ÉS MIÉRT JÓ?
# ============================================================

# Képzeld el, hogy süteményt sütsz.
# Két lehetőséged van:
#
# A) Minden alkalommal újra leírod a teljes receptet az elejétől
# B) Egyszer leírod a receptet, és utána csak annyit mondasz:
#    "Csináld meg a csokitortát!"
#
# A függvény = a recept.
# Egyszer megírod, utána bármikor "meghívod" (használod) a nevével.

print("--- 1. Miért jó a függvény? ---")
print()

# FÜGGVÉNY NÉLKÜL — mindig újra leírod:
print("Szia, Anna! Üdv a rendszerben!")
print("Szia, Béla! Üdv a rendszerben!")
print("Szia, Cecil! Üdv a rendszerben!")
# Ha változtatni akarod az üdvözlést, 3 helyen kell átírni!

print()

# FÜGGVÉNNYEL — egyszer megírod, háromszor használod:
def greet_user(name):
    """Üdvözli a felhasználót."""
    print(f"Szia, {name}! Üdv a rendszerben!")

greet_user("Anna")      # meghívjuk Anna-val
greet_user("Béla")      # meghívjuk Béla-val
greet_user("Cecil")     # meghívjuk Cecil-lel
# Ha változtatni akarod az üdvözlést, CSAK 1 helyen kell!

print()


# ============================================================
# 2. EGY FÜGGVÉNY = EGY FELADAT (Single Responsibility)
# ============================================================

# Ez a lecke LEGFONTOSABB szabálya:
#
#   ╔══════════════════════════════════════════════╗
#   ║  Egy függvény CSAK EGY dolgot csináljon,    ║
#   ║  és azt csinálja JÓL.                       ║
#   ╚══════════════════════════════════════════════╝
#
# Miért? Gondolj bele:
# - Ha egy függvény 10 dolgot csinál, és valami elromlik,
#   10 helyen kell keresgélned a hibát.
# - Ha egy függvény 1 dolgot csinál, és valami elromlik,
#   AZONNAL tudod hol a baj.
#
# Hasonlat: egy svájci bicska 20 dolgot tud, de egyiket sem
# csinálja olyan jól, mint egy rendes kés, olló, vagy csavarhúzó.

print("--- 2. Egy függvény = egy feladat ---")
print()

# ---- ROSSZ PÉLDA: mindent egy függvénybe zsúfolunk ----

def process_order_bad(product_name, price, quantity, customer_email):
    """EZ ROSSZ — túl sok mindent csinál egyszerre!"""
    # 1. Kiszámolja az árat
    total = price * quantity
    tax = total * 0.27
    grand_total = total + tax

    # 2. Ellenőrzi az emailt
    if "@" not in customer_email:
        print("HIBA: érvénytelen email!")
        return None

    # 3. Kiírja a számlát
    print(f"--- SZÁMLA ---")
    print(f"Termék: {product_name}")
    print(f"Darab: {quantity}")
    print(f"Nettó: {total} Ft")
    print(f"ÁFA: {tax} Ft")
    print(f"Összesen: {grand_total} Ft")
    print(f"Vásárló: {customer_email}")

    # 4. "Elküldi" az emailt
    print(f"Email elküldve: {customer_email}")

    return grand_total

# Ez a függvény 4 dolgot csinál:
# árat számol, emailt ellenőriz, számlát nyomtat, emailt "küld".
# Ha bármelyikben hiba van, az egész kusza.

print("ROSSZ megoldás (egy nagy függvény):")
process_order_bad("Laptop", 250000, 2, "anna@example.com")
print()

# ---- JÓ PÉLDA: minden feladatnak saját függvénye van ----

TAX_RATE = 0.27

def calculate_order_total(price, quantity):
    """Kiszámolja a megrendelés bruttó végösszegét.

    Paraméterek:
        price: egy darab nettó ára (Ft)
        quantity: darabszám

    Visszatérési érték:
        A bruttó végösszeg (nettó + ÁFA)
    """
    net_total = price * quantity
    tax_amount = net_total * TAX_RATE
    return net_total + tax_amount
    # ↑ Ez a függvény CSAK számol. Nem ír ki semmit, nem küld emailt.
    # Visszaadja (return) az eredményt, és kész.


def is_valid_email(email):
    """Ellenőrzi, hogy az email cím tartalmaz-e @-ot.

    Paraméterek:
        email: az ellenőrzendő email cím (szöveg)

    Visszatérési érték:
        True ha van benne @, False ha nincs
    """
    return "@" in email
    # ↑ Ez a függvény CSAK ellenőriz. Egy kérdésre válaszol: érvényes-e?


def print_invoice(product_name, quantity, net_total, tax_amount, grand_total):
    """Kiírja a számlát a képernyőre.

    Paraméterek:
        product_name: a termék neve
        quantity: darabszám
        net_total: nettó összeg
        tax_amount: ÁFA összeg
        grand_total: bruttó végösszeg
    """
    print(f"--- SZÁMLA ---")
    print(f"Termék: {product_name}")
    print(f"Darab: {quantity}")
    print(f"Nettó: {net_total} Ft")
    print(f"ÁFA: {tax_amount} Ft")
    print(f"Összesen: {grand_total} Ft")
    # ↑ Ez a függvény CSAK kiír. Nem számol, nem ellenőriz.


def send_confirmation_email(email, grand_total):
    """Visszaigazoló emailt küld a vásárlónak.

    Paraméterek:
        email: a vásárló email címe
        grand_total: a fizetendő összeg
    """
    print(f"Email elküldve ({email}): Rendelésed összege {grand_total} Ft")
    # ↑ Ez a függvény CSAK "küld". (Most csak kiírja, de igazi appban
    # tényleg emailt küldene.)


# És most ÖSSZERAKJUK őket — mint LEGO kockákat:

print("JÓ megoldás (kis függvények összerakva):")

customer_email = "anna@example.com"
product_price = 250000
order_quantity = 2

# 1. lépés: email ellenőrzés
if not is_valid_email(customer_email):
    print("HIBA: érvénytelen email!")
else:
    # 2. lépés: ár kiszámolása
    grand_total = calculate_order_total(product_price, order_quantity)
    net_total = product_price * order_quantity
    tax_amount = grand_total - net_total

    # 3. lépés: számla kiírása
    print_invoice("Laptop", order_quantity, net_total, tax_amount, grand_total)

    # 4. lépés: email küldés
    send_confirmation_email(customer_email, grand_total)

print()

# Miért jobb ez?
# - Ha az ár számolás hibás → CSAK a calculate_order_total-t nézed
# - Ha a számla csúnya → CSAK a print_invoice-t javítod
# - Ha az email küldés nem megy → CSAK a send_confirmation_email-lel foglalkozol
# - Bármelyik függvényt ÚJRA tudod használni más programban is!


# ============================================================
# 3. HONNAN TUDOM, HOGY SZÉT KELL BONTANI?
# ============================================================

print("--- 3. Mikor kell szétbontani? ---")
print()

# Van pár egyszerű jel, ami arra utal, hogy a függvényed túl sokat csinál:
#
# 1. A függvény neve tartalmazza az "és" szót (vagy "and"):
#    calculate_and_print()  → szedd szét: calculate() + print()
#
# 2. A függvény 15 sornál hosszabb:
#    Valószínűleg több dolgot csinál. Keresd a logikai határokat.
#
# 3. Kommentekkel választod el a részeket:
#    # Kiszámoljuk az árat
#    ...
#    # Ellenőrizzük az emailt
#    ...
#    # Kiírjuk a számlát
#    ↑ Minden komment = egy lehetséges új függvény!
#
# 4. Több behúzási szint (if-ben if-ben for...):
#    Ha 3-nál mélyebb, ideje szétbontani.

# ---- PÉLDA: kommentek mint jelek ----

# ROSSZ — a kommentek jelzik, hogy ez igazából 3 függvény:
def process_student_grades_bad(students):
    """Rossz: túl sok feladatot lát el."""
    # Átlagot számolunk
    total = 0
    for student in students:
        total = total + student["grade"]
    average = total / len(students)

    # Megkeressük a legjobbat
    best = students[0]
    for student in students:
        if student["grade"] > best["grade"]:
            best = student

    # Kiírjuk az eredményt
    print(f"Átlag: {average}")
    print(f"Legjobb: {best['name']} ({best['grade']})")

# JÓ — minden kommentből önálló függvény lett:
def calculate_average_grade(students):
    """Kiszámolja a diákok jegyeinek átlagát."""
    total = 0
    for student in students:
        total = total + student["grade"]
    return total / len(students)


def find_best_student(students):
    """Megkeresi a legjobb jegyű diákot."""
    best = students[0]
    for student in students:
        if student["grade"] > best["grade"]:
            best = student
    return best


def print_grade_report(students):
    """Kiírja az osztályzat összesítőt."""
    average = calculate_average_grade(students)
    best = find_best_student(students)
    print(f"Átlag: {average}")
    print(f"Legjobb: {best['name']} ({best['grade']})")


# Kipróbáljuk:
students = [
    {"name": "Anna", "grade": 5},
    {"name": "Béla", "grade": 3},
    {"name": "Cecil", "grade": 4},
]

print("Rossz (egy nagy függvény):")
process_student_grades_bad(students)
print()
print("Jó (kis függvények):")
print_grade_report(students)
print()


# ============================================================
# 4. PARAMÉTEREK ÉS VISSZATÉRÉSI ÉRTÉKEK
# ============================================================

print("--- 4. Paraméterek és return ---")
print()

# Két fontos fogalom:
#
# PARAMÉTER = amit a függvény KAP (a bemenete)
#   Olyan, mint egy recept hozzávalói: "adj nekem lisztet és tojást"
#
# VISSZATÉRÉSI ÉRTÉK (return) = amit a függvény VISSZAAD (a kimenete)
#   Olyan, mint a kész sütemény: "tessék, itt a torta"

# ---- Függvény RETURN nélkül ----
# Ezek csak CSINÁLNAK valamit (pl. kiírnak), de nem adnak vissza semmit.

def say_hello(name):
    """Csak kiír — nem ad vissza semmit."""
    print(f"Hello, {name}!")

say_hello("Péter")

# Ha megpróbálod elmenteni az eredményt:
result = say_hello("Anna")
print(f"A say_hello visszatérési értéke: {result}")
# ↑ None-t ír ki! Mert a függvényben nincs return.
# A None = "semmi", "nincs érték".

print()

# ---- Függvény RETURN-nel ----
# Ezek VISSZAADNAK egy értéket, amit el tudsz menteni egy változóba.

def add_numbers(a, b):
    """Összeadja a két számot és VISSZAADJA az eredményt."""
    return a + b
    # ↑ A return azt mondja: "itt az eredmény, tessék!"

result = add_numbers(10, 20)
print(f"10 + 20 = {result}")
# ↑ Most result = 30, nem None!

# A return-ös függvényekkel ÉPÍTKEZHETSZ:
price = add_numbers(1000, 500)          # 1500
total = add_numbers(price, 270)         # 1770
print(f"Ár: {price}, Végösszeg ÁFA-val: {total}")
print()

# ---- SZABÁLY: melyiket mikor? ----
#
# RETURN-nel: ha a függvény KISZÁMOL vagy MEGÁLLAPÍT valamit
#   calculate_total() → return total
#   is_valid_email() → return True/False
#   find_best_student() → return best_student
#
# RETURN nélkül: ha a függvény MEGJELENÍT vagy VÉGREHAJT valamit
#   print_invoice() → kiír a képernyőre
#   send_email() → elküld egy emailt
#   save_to_file() → ment egy fájlba


# ============================================================
# 5. ALAPÉRTELMEZETT PARAMÉTEREK
# ============================================================

print("--- 5. Alapértelmezett paraméterek ---")
print()

# Néha egy paraméternek van egy "szokásos" értéke,
# amit legtöbbször nem akarsz megváltoztatni.
# Ilyenkor adhatsz neki ALAPÉRTELMEZETT értéket.

# PÉLDA: kedvezmény számolás
# A legtöbb vásárlónak nincs kedvezménye (0%),
# de néhányan kapnak.

def calculate_discounted_price(price, discount_percent=0):
    """Kiszámolja az árat kedvezménnyel.

    Paraméterek:
        price: az eredeti ár
        discount_percent: kedvezmény százalékban (alapból 0, vagyis nincs)
                          ↑ ez az alapértelmezett érték!
    """
    discount_amount = price * (discount_percent / 100)
    return price - discount_amount

# Használat alapértelmezetten (nincs kedvezmény):
normal_price = calculate_discounted_price(10000)
print(f"Kedvezmény nélkül: {normal_price} Ft")
# ↑ Nem adtunk meg discount_percent-et, ezért 0 lesz automatikusan.

# Használat kedvezménnyel:
sale_price = calculate_discounted_price(10000, 20)
print(f"20% kedvezménnyel: {sale_price} Ft")
# ↑ Most megadtuk: 20%

# Még egy példa — üdvözlés, ami alapból magyarul köszön:
def greet(name, language="hu"):
    """Köszönt a megadott nyelven. Alapból magyarul."""
    if language == "hu":
        print(f"Szia, {name}!")
    elif language == "en":
        print(f"Hello, {name}!")
    else:
        print(f"Hi, {name}!")

greet("Péter")               # → "Szia, Péter!" (alapértelmezett: hu)
greet("John", "en")          # → "Hello, John!" (angol)
print()


# ============================================================
# 6. ÖSSZEFOGLALÓ
# ============================================================

print("--- 6. Összefoglaló ---")
print("""
Amit megtanultál:

  1. Egy függvény = egy feladat
     Ha a függvényed neve "és"-t tartalmaz → bontsd szét!

  2. Jelek, hogy szét kell bontani:
     - 15 sornál hosszabb
     - Kommentekkel választod el a részeket
     - A neve tartalmaz "és/and" szót

  3. Paraméter = bemenet, Return = kimenet
     - return-nel: ha KISZÁMOL valamit
     - return nélkül: ha MEGJELENÍT vagy VÉGREHAJT valamit

  4. Alapértelmezett paraméterek:
     def func(param=alapérték) — ha nem adod meg, az alapérték érvényes

  5. Kis függvények előnyei:
     - Könnyebb megérteni
     - Könnyebb hibát keresni
     - Újra tudod használni más programban

Következő lépés: oldd meg az exercise_02_fuggvenyek.py feladatait!
""")

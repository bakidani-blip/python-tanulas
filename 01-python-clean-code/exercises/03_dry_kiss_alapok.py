"""
=============================================================
  1.3 LECKE: DRY és KISS — Ne ismételd magad, legyen egyszerű!
=============================================================

Eddig tanultál:
  - Változókat, típusokat, listákat, szótárakat (0. lecke)
  - Jó elnevezéseket (1.1 lecke)
  - Függvényeket (1.2 lecke)

Most megtanulod:
  - Mi az a DRY (Don't Repeat Yourself) és miért fontos
  - Mi az a KISS (Keep It Simple, Stupid) és miért fontos
  - Hogyan ismerd fel az ismétlődő vagy túlbonyolított kódot
  - Hogyan refaktorálj (alakíts át) egy kódot szebbé

Futtasd:
    python 01-python-clean-code/exercises/03_dry_kiss_alapok.py
"""


# ============================================================
# 1. MI AZ A DRY? — Don't Repeat Yourself (Ne ismételd magad!)
# ============================================================

# Képzeld el, hogy van egy barátod telefonszáma: 06-30-123-4567.
#
# Két lehetőséged van:
#
# A) Leírod ezt a számot 10 különböző helyre:
#    - a hűtőre, a naptáradba, az asztalodra, a füzetedbe...
#    Ha megváltozik a száma, mind a 10 helyen át kell írni!
#    (És garantáltan elfelejted az egyiket.)
#
# B) Beírod a telefonkönyvbe EGYSZER, és mindenhol onnan nézed.
#    Ha változik a szám, egyetlen helyen javítod, és kész.
#
# A DRY elv = a B) megoldás.
# Minden információ EGYETLEN helyen legyen a kódodban.
# Ha valamit másolsz-beillesztesz, az szinte mindig baj.

print("=" * 55)
print("  1. MI AZ A DRY? — Ne ismételd magad!")
print("=" * 55)
print()

# --- ROSSZ PÉLDA: Ugyanazt a számítást 3x leírtuk ---

print("--- ROSSZ: Ismétlődő kód ---")

# Tegyük fel, hogy áfás árat számolunk 3 termékre.
# Az ÁFA 27%, tehát az áfás ár = nettó ár * 1.27

# 1. termék
net_price_1 = 1000                     # nettó ár
gross_price_1 = net_price_1 * 1.27     # áfás ár kiszámítva
print(f"  Toll: {gross_price_1:.0f} Ft")  # kiírjuk

# 2. termék — UGYANAZ a számítás, copy-paste!
net_price_2 = 2500
gross_price_2 = net_price_2 * 1.27     # megint 1.27... mi van ha változik?
print(f"  Füzet: {gross_price_2:.0f} Ft")

# 3. termék — megint!
net_price_3 = 800
gross_price_3 = net_price_3 * 1.27     # harmadszor is 1.27...
print(f"  Radír: {gross_price_3:.0f} Ft")

# Mi a baj ezzel?
# - A 1.27-es szám 3 helyen szerepel.
# - Ha az ÁFA változik (pl. 25%-ra), 3 helyen kell átírni.
# - Ha az egyiket elfelejted → a programod hibás lesz, de nem szól!

print()

# --- JÓ PÉLDA: Függvénybe kiemelve, konstans használatával ---

print("--- JÓ: DRY megoldás ---")

VAT_RATE = 0.27   # ÁFA kulcs — EGYETLEN helyen definiálva (konstans)

def calculate_gross_price(net_price):
    """Kiszámolja az áfás árat a nettó árból."""
    return net_price * (1 + VAT_RATE)  # a konstanst használjuk, nem számot

# Most bármennyi terméket feldolgozhatunk:
print(f"  Toll: {calculate_gross_price(1000):.0f} Ft")   # függvényt hívunk
print(f"  Füzet: {calculate_gross_price(2500):.0f} Ft")  # ugyanazt a függvényt
print(f"  Radír: {calculate_gross_price(800):.0f} Ft")   # harmadszor is

# Ha az ÁFA változik → EGYETLEN helyen írjuk át (VAT_RATE), és kész!

print()
print()


# ============================================================
# 2. HOGYAN ISMERED FEL AZ ISMÉTLŐDÉST?
# ============================================================

# 3 figyelmeztető jel, hogy DRY problémád van:
#
# 1. "Ctrl+C, Ctrl+V érzés" — Ha copy-paste-elni akarod a kódot,
#    az szinte mindig azt jelenti, hogy függvényt kellene írni.
#
# 2. "Egy javítás = sok módosítás" — Ha egy hibát javítasz,
#    és 3-4 helyen kell átírni → az ismétlődő kód jele.
#
# 3. "Mágikus számok" — Ha ugyanaz a szám (pl. 0.27, 100, 3.14)
#    többször szerepel a kódban, és nem tudod miért annyi →
#    emeld ki konstansba és adj neki beszédes nevet!

print("=" * 55)
print("  2. HOGYAN ISMERED FEL AZ ISMÉTLŐDÉST?")
print("=" * 55)
print()

# --- Előtte-Utána #1: Ismétlődő kiírás ---

print("--- Előtte: Ismétlődő köszönés ---")

# ROSSZ — Ugyanaz a minta 4x:
print("  **********************")
print("  * Üdv, Anna!         *")
print("  **********************")
print("  **********************")
print("  * Üdv, Béla!         *")
print("  **********************")

# Ha meg akarod változtatni a keretet (pl. ### legyen *** helyett),
# 4 sort kell átírni — és könnyen elrontod.

print()
print("--- Utána: Függvénnyel ---")

def print_welcome_box(name):
    """Keretes üdvözlőt ír ki a megadott névvel."""
    border = "*" * 22                   # a keret egyszer van definiálva
    print(f"  {border}")               # felső keret
    print(f"  * Üdv, {name + '!':13s}*")  # üdvözlés (13 karakter széles)
    print(f"  {border}")               # alsó keret

print_welcome_box("Anna")    # 1 sor a hívás
print_welcome_box("Béla")    # 1 sor a hívás
# Ha változtatni akarod a keretet → 1 helyen írod át.

print()

# --- Előtte-Utána #2: Mágikus számok ---

print("--- Előtte: Mágikus számok ---")

# ROSSZ — Mi az a 9.81? Mi az a 0.5? Miért szerepel 3x?
distance_1 = 0.5 * 9.81 * 2 ** 2      # valami fizikai számítás
distance_2 = 0.5 * 9.81 * 5 ** 2      # de mi ez pontosan?
distance_3 = 0.5 * 9.81 * 10 ** 2     # ha 9.81 változna, 3 helyen kell javítani

print(f"  2 mp: {distance_1:.1f} m")
print(f"  5 mp: {distance_2:.1f} m")
print(f"  10 mp: {distance_3:.1f} m")

print()
print("--- Utána: Konstans + függvény ---")

# JÓ — Beszédes konstans + függvény
GRAVITY = 9.81  # gravitációs gyorsulás (m/s²) — egyszer definiálva

def calculate_free_fall_distance(time_seconds):
    """Kiszámolja a szabadesés távolságát a megadott idő alapján."""
    # Képlet: d = 0.5 * g * t²
    return 0.5 * GRAVITY * time_seconds ** 2   # GRAVITY-t használjuk

print(f"  2 mp: {calculate_free_fall_distance(2):.1f} m")   # hívjuk a függvényt
print(f"  5 mp: {calculate_free_fall_distance(5):.1f} m")
print(f"  10 mp: {calculate_free_fall_distance(10):.1f} m")
# Ha a gravitáció változna (pl. Holdon) → 1 helyen módosítod.

print()

# --- Előtte-Utána #3: Ismétlődő ellenőrzés ---

print("--- Előtte: Ismétlődő ellenőrzés ---")

# ROSSZ — Ugyanaz a logika 3x:
age_1 = 15
if age_1 >= 18:                        # korhatár ellenőrzés
    print(f"  {age_1} éves: beléphet")
else:
    print(f"  {age_1} éves: NEM léphet be")

age_2 = 22
if age_2 >= 18:                        # UGYANAZ az ellenőrzés
    print(f"  {age_2} éves: beléphet")
else:
    print(f"  {age_2} éves: NEM léphet be")

age_3 = 17
if age_3 >= 18:                        # MEGINT ugyanaz
    print(f"  {age_3} éves: beléphet")
else:
    print(f"  {age_3} éves: NEM léphet be")

print()
print("--- Utána: Függvénnyel ---")

MINIMUM_AGE = 18   # korhatár — egyszer definiálva

def check_entry_permission(age):
    """Kiírja, hogy az adott életkorral be lehet-e lépni."""
    if age >= MINIMUM_AGE:                           # a konstanst használjuk
        print(f"  {age} éves: beléphet")
    else:
        print(f"  {age} éves: NEM léphet be")

check_entry_permission(15)   # 1 sor — tiszta, átlátható
check_entry_permission(22)
check_entry_permission(17)
# Ha a korhatár 21-re változna → 1 helyen írod át (MINIMUM_AGE).

print()
print()


# ============================================================
# 3. MI AZ A KISS? — Keep It Simple, Stupid (Legyen egyszerű!)
# ============================================================

# Képzeld el, hogy el akarsz menni a boltba, ami 200 méterre van.
#
# A) Megépítesz egy űrhajót, kiszámolod a röppályát, felszállsz,
#    belépsz a légkörbe, landolsz a bolt előtt.
#    → Működik? Igen. De teljesen feleslegesen bonyolult!
#
# B) Elsétálsz.
#    → Működik? Igen. És sokkal egyszerűbb.
#
# A KISS elv = a B) megoldás.
# Ne bonyolítsd túl a kódot! Az egyszerű megoldás szinte mindig jobb.
#
# Miért?
# - Egyszerű kódot könnyebb MEGÉRTENI (neked is, 2 hét múlva is!)
# - Egyszerű kódot könnyebb JAVÍTANI (kevesebb a hiba esélye)
# - Egyszerű kódot könnyebb MÓDOSÍTANI (ha változik a feladat)

print("=" * 55)
print("  3. MI AZ A KISS? — Legyen egyszerű!")
print("=" * 55)
print()

# --- ROSSZ PÉLDA: Túlbonyolított megoldás ---

print("--- ROSSZ: Túlbonyolított 'páros szám?' ellenőrzés ---")

def is_even_complicated(number):
    """ROSSZ: Túlbonyolított módja annak, hogy páros-e egy szám."""
    # Végigmegyünk 0-tól a számig, és nézzük melyik osztható 2-vel...
    even_numbers = []                  # üres lista a páros számoknak
    for i in range(number + 1):        # 0-tól number-ig
        if i % 2 == 0:                 # ha i páros
            even_numbers.append(i)     # betesszük a listába
    # Megnézzük benne van-e a szám a páros számok listájában
    if number in even_numbers:         # keresés a listában
        return True                    # ha benne van → páros
    else:
        return False                   # ha nincs benne → páratlan

result = is_even_complicated(42)       # ennyi munkát végez egy egyszerű kérdésre...
print(f"  42 páros? {result}")

print()

# --- JÓ PÉLDA: Egyszerű megoldás ---

print("--- JÓ: KISS megoldás ---")

def is_even_simple(number):
    """JÓ: Egyszerű módja annak, hogy páros-e egy szám."""
    return number % 2 == 0    # ha 2-vel osztva 0 a maradék → páros

result = is_even_simple(42)            # 1 sor — tiszta, egyértelmű
print(f"  42 páros? {result}")

# Mindkettő UGYANAZT csinálja, de a második:
# - 1 sor a lényeg (nem 8)
# - Azonnal érthető
# - Nincs felesleges lista, ciklus, keresés

print()

# --- Még egy KISS példa: Osztályozás ---

print("--- ROSSZ: Túlbonyolított osztályozás ---")

def get_grade_complicated(score):
    """ROSSZ: Feleslegesen sok feltétel."""
    if score >= 90 and score <= 100:     # 90-100 → ez jó
        grade = 5
        return grade                     # miért nem rögtön return 5?
    elif score >= 80 and score < 90:     # 80-89
        grade = 4
        return grade
    elif score >= 70 and score < 80:     # 70-79
        grade = 3
        return grade
    elif score >= 50 and score < 70:     # 50-69
        grade = 2
        return grade
    elif score >= 0 and score < 50:      # 0-49
        grade = 1
        return grade

print(f"  85 pont = {get_grade_complicated(85)}")

print()
print("--- JÓ: KISS osztályozás ---")

def get_grade_simple(score):
    """JÓ: Egyszerű, tiszta osztályozás."""
    # Felülről lefelé haladunk — ha a feltétel igaz, azonnal visszatér.
    # Nem kell felső határ, mert a sorrend garantálja!
    if score >= 90:        # ha 90+ → 5 (és kilép a függvényből)
        return 5
    if score >= 80:        # ide csak akkor jut → ha < 90
        return 4
    if score >= 70:        # ide → ha < 80
        return 3
    if score >= 50:        # ide → ha < 70
        return 2
    return 1               # minden más → 1

print(f"  85 pont = {get_grade_simple(85)}")

# A második verzió:
# - Kevesebb feltétel (nem kell "and score < X")
# - Nem kell felesleges "grade" változó
# - Azonnal érthető a logika

print()
print()


# ============================================================
# 4. DRY + KISS EGYÜTT — Nagyobb példa
# ============================================================

# Képzeld el, hogy egy iskola adminisztrátor vagy, és
# ki kell számolnod 3 osztály átlagát, a legjobb diákot,
# és el kell döntened ki kapjon dicséretet (4.5+ átlag).

print("=" * 55)
print("  4. DRY + KISS EGYÜTT — Diákok feldolgozása")
print("=" * 55)
print()

# --- ROSSZ VERZIÓ: Ismétlődő + túlbonyolított ---

print("--- ROSSZ: Ismétlődő és túlbonyolított ---")

# 9. A osztály
grades_9a = {"Anna": 4, "Béla": 3, "Cecil": 5, "Dóra": 4}
total_9a = 0                           # összeg nullázás
count_9a = 0                           # számláló nullázás
for name in grades_9a:                 # minden diákon végigmegyünk
    total_9a = total_9a + grades_9a[name]  # hozzáadjuk a jegyét
    count_9a = count_9a + 1            # növeljük a számlálót
average_9a = total_9a / count_9a       # osztunk
best_student_9a = ""                   # legjobb diák keresése...
best_grade_9a = 0
for name in grades_9a:
    if grades_9a[name] > best_grade_9a:
        best_grade_9a = grades_9a[name]
        best_student_9a = name
print(f"  9.A átlag: {average_9a:.1f}, legjobb: {best_student_9a}")

# 9. B osztály — COPY-PASTE! Ugyanaz a kód, más adattal
grades_9b = {"Ede": 5, "Feri": 2, "Gizi": 4, "Hanna": 5}
total_9b = 0
count_9b = 0
for name in grades_9b:
    total_9b = total_9b + grades_9b[name]
    count_9b = count_9b + 1
average_9b = total_9b / count_9b
best_student_9b = ""
best_grade_9b = 0
for name in grades_9b:
    if grades_9b[name] > best_grade_9b:
        best_grade_9b = grades_9b[name]
        best_student_9b = name
print(f"  9.B átlag: {average_9b:.1f}, legjobb: {best_student_9b}")

# Látod a problémát? 20 sor kód, KÉTSZER leírva, szinte betűre ugyanaz.
# Ha 10 osztály lenne, 100 sor lenne — és ha egy hibát találsz, 10x javítanád!

print()

# --- JÓ VERZIÓ: DRY + KISS ---

print("--- JÓ: DRY + KISS ---")

PRAISE_THRESHOLD = 4.5   # efelett kap dicséretet — konstansba kiemelve

def calculate_class_average(student_grades):
    """Kiszámolja egy osztály átlagát.

    Kapja: szótár, pl. {"Anna": 4, "Béla": 3}
    Visszaadja: az átlagot (szám)
    """
    total = sum(student_grades.values())     # a values() a jegyeket adja
    return total / len(student_grades)       # összeg / darabszám = átlag

def find_best_student(student_grades):
    """Megkeresi a legjobb jegyű diákot.

    Kapja: szótár, pl. {"Anna": 4, "Béla": 3}
    Visszaadja: a legjobb diák nevét (szöveg)
    """
    best_name = ""             # itt tároljuk a legjobb nevét
    best_grade = 0             # itt a legjobb jegyét
    for name in student_grades:                    # végigmegyünk minden diákon
        if student_grades[name] > best_grade:      # ha jobb jegye van
            best_grade = student_grades[name]      # megjegyezzük a jegyét
            best_name = name                       # és a nevét
    return best_name           # visszaadjuk a legjobb nevét

def print_class_report(class_name, student_grades):
    """Kiírja egy osztály összesítőjét.

    Kapja: az osztály nevét (szöveg) és a jegyeket (szótár)
    Nem ad vissza semmit, csak kiír.
    """
    average = calculate_class_average(student_grades)  # átlag kiszámolása
    best = find_best_student(student_grades)           # legjobb diák keresése

    praise = ""                                        # dicséret szöveg
    if average >= PRAISE_THRESHOLD:                    # ha az átlag elég magas
        praise = " ⭐ Dicséretet kap!"                 # dicséret hozzáadása

    print(f"  {class_name} átlag: {average:.1f}, legjobb: {best}{praise}")

# Használjuk a függvényeket — minden osztály 1 sor!
grades_9a = {"Anna": 4, "Béla": 3, "Cecil": 5, "Dóra": 4}
grades_9b = {"Ede": 5, "Feri": 2, "Gizi": 4, "Hanna": 5}
grades_9c = {"Irén": 5, "János": 5, "Kata": 4, "Laci": 5}

print_class_report("9.A", grades_9a)   # egyetlen hívás — tiszta, rövid
print_class_report("9.B", grades_9b)   # ugyanaz a logika, más adattal
print_class_report("9.C", grades_9c)   # ha 50 osztály lenne, 50 sor

# Ha az átlagszámítás logikáját változtatni kell → 1 függvényben javítod.
# Ha a dicséret küszöbértéke változik → 1 konstanst módosítasz.
# Ha új riportot kell kiírni → 1 függvényt bővítesz.

print()
print()


# ============================================================
# 5. ÖSSZEFOGLALÓ
# ============================================================

print("=" * 55)
print("  5. ÖSSZEFOGLALÓ")
print("=" * 55)
print()
print("  DRY — Don't Repeat Yourself (Ne ismételd magad!)")
print("  ─────────────────────────────────────────────────")
print("  • Ha copy-paste-elsz kódot → függvényt kellene írni")
print("  • Ha egy szám többször szerepel → emeld ki konstansba")
print("  • Ha 1 javítás = sok módosítás → ismétlődő kód van")
print()
print("  KISS — Keep It Simple, Stupid (Legyen egyszerű!)")
print("  ─────────────────────────────────────────────────")
print("  • Ne bonyolítsd túl — az egyszerű megoldás a jó")
print("  • Ha 3 sor elég, ne írj 15 sort")
print("  • Ha nem érted 5 mp alatt → valószínűleg túl bonyolult")
print()
print("  EGYÜTT:")
print("  • DRY + KISS = tiszta, karbantartható, érthető kód")
print("  • Nem tökéletest kell írni, hanem érthetőt!")
print("  • Ha javítanod kell, 1 helyen legyen elég.")
print()
print("  Következő lecke: Gyakorlás! → exercise_03_dry_kiss.py")

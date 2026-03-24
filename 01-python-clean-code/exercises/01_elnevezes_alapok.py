"""
=============================================================
  1.1 LECKE: Változók és elnevezések — Clean Code
=============================================================

Eddig megtanultad, hogyan hozz létre változókat és függvényeket.
Most megtanuljuk, hogyan NEVEZZÜK EL őket JÓL.

Miért fontos ez?
Mert a kódot sokkal többször OLVASSÁK, mint ahányszor ÍRJÁK.
Ha jól nevezed el a dolgokat, a kód szinte önmagát magyarázza.

Futtasd:
    python 01-python-clean-code/exercises/01_elnevezes_alapok.py
"""


# ============================================================
# 1. MI AZ A "CLEAN CODE" (TISZTA KÓD)?
# ============================================================

# Képzeld el, hogy írsz egy levelet valakinek.
# Két verzió:
#
# ROSSZ levél:  "Szja! H v? É j v. Cs m lgylj."
# JÓ levél:    "Szia! Hogy vagy? Én jól vagyok. Csütörtökön majd legyél ott."
#
# Mindkettő ugyanazt mondja, de az elsőt nem érti senki.
# A kóddal PONTOSAN ugyanez a helyzet.
#
# A "clean code" (tiszta kód) azt jelenti:
# olyan kódot írsz, amit MÁS EMBEREK is könnyen megértenek.
# (És te magad is, 3 hónap múlva, amikor már elfelejtetted mit csináltál.)

print("--- 1. Miért fontos a jó elnevezés? ---")
print()

# ROSSZ kód — mit csinál ez? Fogalmad sincs ránézésre:
x = 30
y = 1000
z = x * y
print(f"ROSSZ: x={x}, y={y}, z={z}")
# Mi az x? Mi az y? Mi a z? Senki nem tudja...

# JÓ kód — UGYANAZ a számítás, de most érted:
hourly_wage = 30                        # órabér dollárban
work_hours_per_year = 1000              # munkaórák száma évente
yearly_salary = hourly_wage * work_hours_per_year  # éves fizetés
print(f"JÓ:   órabér={hourly_wage}, órák={work_hours_per_year}, fizetés={yearly_salary}")

# Látod? UGYANAZ a kód, UGYANAZ az eredmény.
# De a második verziót olvasva AZONNAL érted, miről van szó.
print()


# ============================================================
# 2. PYTHON ELNEVEZÉSI SZABÁLYOK (KONVENCIÓK)
# ============================================================

# A Python közösség kitalált szabályokat, hogy mindenki
# UGYANÚGY nevezze el a dolgokat. Ezt PEP 8-nak hívják.
# (PEP = Python Enhancement Proposal, vagyis "Python Fejlesztési Javaslat")
#
# Nem kötelező, de ha betartod:
# - Más programozók azonnal értik a kódodat
# - Profinak tűnik a munkád
# - Könnyebb csapatban dolgozni

print("--- 2. Elnevezési konvenciók ---")
print()

# ---- SZABÁLY 1: Változók és függvények → snake_case ----
#
# "snake_case" = minden kisbetű, szavakat alulvonás (_) választja el
# Azért hívják "snake"-nek (kígyó), mert a kígyó is a földön csúszik :)

# JÓ (snake_case):
user_name = "Kiss Péter"
total_price = 4500
is_active = True                  # boolean (igaz/hamis) változóknál: is_, has_, can_

# ROSSZ (ezeket NE csináld):
# UserName = "Kiss Péter"         ← ez osztályoknak van fenntartva (később)
# username = "Kiss Péter"         ← ha egy szó, ez még OK, de két szónál mindig _
# user_Name = "Kiss Péter"        ← keverés, csúnya
# USERNAME = "Kiss Péter"         ← ez konstansoknak van fenntartva (később)

print(f"Felhasználó: {user_name}")
print(f"Végösszeg: {total_price} Ft")
print(f"Aktív: {is_active}")
print()


# ---- SZABÁLY 2: Konstansok → UPPER_SNAKE_CASE ----
#
# Mi az a konstans?
# Egy olyan érték, amit a program elején beállítasz, és SOHA nem változtatod meg.
# Például: az adókulcs, a maximális próbálkozások száma, egy API URL.
#
# Ezeket CSUPA NAGYBETŰVEL írjuk, szavakat alulvonás (_) választja el.
# Így bárki ránéz és tudja: "aha, ez fix, nem változik."

MAX_RETRIES = 3                   # maximum újrapróbálkozások száma
TAX_RATE = 0.27                   # áfa kulcs (27%)
API_URL = "https://api.example.com"
DATABASE_NAME = "my_app_db"

# ROSSZ:
# maxRetries = 3                  ← ez nem Python stílus (ez JavaScript stílus)
# max_retries = 3                 ← ez kisbetűs, tehát változónak tűnik
#                                   (senki nem tudja, hogy nem szabad változtatni)

print(f"Max próbálkozás: {MAX_RETRIES}")
print(f"ÁFA: {TAX_RATE * 100}%")
print()


# ---- SZABÁLY 3: Osztályok → PascalCase ----
#
# Az osztályokat majd később tanulod meg részletesen.
# Most elég annyit tudni: az osztály egy "tervrajz",
# amiből "példányokat" (objektumokat) készítesz.
#
# PascalCase = minden szó nagybetűvel kezdődik, NINCS alulvonás.

# JÓ (PascalCase):
# class UserAccount:
# class ShoppingCart:
# class DatabaseConnection:

# ROSSZ:
# class user_account:             ← ez snake_case, változónak/függvénynek való
# class useraccount:              ← nem látni hol van a szóhatár

print("Osztályok: PascalCase (pl. UserAccount, ShoppingCart)")
print()


# ============================================================
# 3. BESZÉDES NEVEK — A LEGFONTOSABB SZABÁLY
# ============================================================

# Az elnevezés legyen olyan, hogy OLVASVA megértsd, mit tárol/csinál.
# Nem kell komment mellé, ha jó a név.

print("--- 3. Beszédes nevek ---")
print()

# ---- 3a: Változóknál ----

# ROSSZ → nem tudom mi ez:
d = 7
# JÓ → azonnal értem:
days_until_deadline = 7

# ROSSZ → mi az a "t"?
t = 36.6
# JÓ → áhá, testhőmérséklet:
body_temperature = 36.6

# ROSSZ → semmitmondó:
data = [85, 92, 78, 95, 88]
# JÓ → tudom mit tartalmaz:
exam_scores = [85, 92, 78, 95, 88]

print(f"Határidő: {days_until_deadline} nap múlva")
print(f"Testhő: {body_temperature}°C")
print(f"Vizsgaeredmények: {exam_scores}")
print()


# ---- 3b: Függvényeknél ----
#
# A függvény CSINÁL valamit, ezért a neve IGÉVEL kezdődjön.
# Gondolj úgy rá, mint egy parancsra: "csináld ezt!"


# ROSSZ — nem tudom mit csinál:
def process(a, b):
    return a + b

# JÓ — a névből tudom mit csinál:
def calculate_total_price(item_price, quantity):
    """Kiszámolja a teljes árat (egységár × darabszám)."""
    return item_price * quantity

# ROSSZ — mi az, hogy "data"? Milyen adatot ellenőriz?
def check(data):
    return len(data) > 0

# JÓ — azonnal értem:
def is_list_empty(items):
    """Visszaadja True-t ha a lista üres, False-t ha nem."""
    return len(items) == 0

# Tipikus JÓ ige-kezdetek függvényeknél:
# get_...     → valamit lekér        get_user_name()
# calculate_... → valamit kiszámol   calculate_average()
# is_...      → igaz/hamis kérdés    is_valid_email()
# has_...     → van-e valami         has_permission()
# create_...  → valamit létrehoz     create_new_account()
# send_...    → valamit elküld       send_email()
# validate_.. → valamit ellenőriz    validate_password()

total = calculate_total_price(1500, 3)
print(f"3 db × 1500 Ft = {total} Ft")
print(f"Üres lista? {is_list_empty([])}")
print(f"Üres lista? {is_list_empty([1, 2, 3])}")
print()


# ---- 3c: Boolean (igaz/hamis) változóknál ----
#
# Ha egy változó True vagy False értéket tárol,
# a neve legyen KÉRDÉS formájú — mintha kérdeznéd:
# "Aktív? Igen." / "Van jogosultsága? Nem."

# ROSSZ:
active = True               # "active" önmagában nem kérdés
login = False               # "login" egy főnév, nem tudom igaz/hamis-e

# JÓ:
is_active = True            # "aktív-e?" → igen
is_logged_in = False        # "be van-e jelentkezve?" → nem
has_permission = True       # "van-e jogosultsága?" → igen
can_edit = False            # "szerkeszthet-e?" → nem

print(f"Aktív: {is_active}")
print(f"Bejelentkezve: {is_logged_in}")
print(f"Van joga: {has_permission}")
print(f"Szerkeszthet: {can_edit}")
print()


# ============================================================
# 4. KERÜLENDŐ DOLGOK
# ============================================================

print("--- 4. Amit NE csinálj ---")
print()

# ---- 4a: Egybetűs nevek ----
# SOHA ne használj egybetűs változónevet (kivéve ciklusváltozó: i, j)

# ROSSZ:
n = "Kiss Péter"
a = 25
c = "Budapest"

# JÓ:
name = "Kiss Péter"
age = 25
city = "Budapest"

# Ciklusban az i, j elfogadott — mert mindenki tudja, ez a "sorszám":
for i in range(3):
    print(f"  {i + 1}. kör")

print()


# ---- 4b: Rövidítések ----
# Ne rövidíts, hacsak nem közismert rövidítés (pl. URL, API, ID)

# ROSSZ:
usr_nm = "Kiss Péter"       # user_name rövidítve — nehéz olvasni
calc_ttl = 4500             # calculate_total rövidítve — érthetetlen
btn_clr = "blue"            # button_color — mi??

# JÓ:
user_name = "Kiss Péter"    # teljes, érthető
calculated_total = 4500     # teljes, érthető
button_color = "blue"       # teljes, érthető

# Elfogadott rövidítések (mert mindenki ismeri):
user_id = 42                # ID = identifier (azonosító)
api_url = "https://..."     # API, URL — közismert
max_hp = 100                # HP — ha játékfejlesztésben vagy

print(f"Felhasználó: {user_name} (ID: {user_id})")
print()


# ---- 4c: Félrevezető nevek ----

# A NÉV mindig tükrözze a TARTALMAT!

# ROSSZ — félrevezető:
user_list = {"name": "Anna", "age": 25}
# ↑ "list"-nek hívja, de ez egy szótár (dict)! Félrevezető!

# JÓ:
user_data = {"name": "Anna", "age": 25}
# ↑ "data" nem hazudik — ez tényleg adat


# ============================================================
# 5. ÖSSZEFOGLALÓ TÁBLÁZAT
# ============================================================

print("--- 5. Összefoglaló ---")
print()
print("┌────────────────────┬──────────────────┬────────────────────────┐")
print("│ Típus              │ Konvenció        │ Példa                  │")
print("├────────────────────┼──────────────────┼────────────────────────┤")
print("│ Változó            │ snake_case       │ user_name              │")
print("│ Függvény           │ snake_case       │ calculate_total()      │")
print("│ Konstans           │ UPPER_SNAKE_CASE │ MAX_RETRIES            │")
print("│ Osztály            │ PascalCase       │ UserAccount            │")
print("│ Boolean változó    │ is_/has_/can_    │ is_active              │")
print("├────────────────────┼──────────────────┼────────────────────────┤")
print("│ KERÜLENDŐ          │                  │                        │")
print("│ Egybetűs nevek     │ ✗               │ x, n, d                │")
print("│ Rövidítések         │ ✗               │ calc_ttl, usr_nm       │")
print("│ Félrevezető nevek   │ ✗               │ user_list (ha dict)    │")
print("└────────────────────┴──────────────────┴────────────────────────┘")
print()
print("Következő lépés: oldd meg az exercise_01_elnevezes.py feladatait!")

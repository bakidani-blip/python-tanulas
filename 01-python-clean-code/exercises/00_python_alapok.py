"""
=============================================================
  PYTHON ALAPOK — Lexikális tudás
  Olvasd végig, futtasd, kísérletezz!
=============================================================

Futtasd ezt a fájlt a terminálban:
    cd tanulás
    source .venv/bin/activate
    python 01-python-clean-code/exercises/00_python_alapok.py

Vagy VS Code-ban: jobb klikk → "Run Python File in Terminal"
"""


# ============================================================
# 1. VÁLTOZÓK — dobozok, amikbe értékeket raksz
# ============================================================

# Szöveg (string) — idézőjelbe tesszük
name = "Kiss Péter"
greeting = 'Szia!'          # egyszeres idézőjel is jó

# Egész szám (integer)
age = 25
year = 2026

# Tizedes szám (float)
height = 1.78
temperature = 36.6

# Igaz/hamis (boolean) — nagybetűvel!
is_student = True
has_car = False

# Kiírás a képernyőre
print("--- 1. Változók ---")
print(name)
print(age)
print(is_student)


# ============================================================
# 2. PRINT — kiírás a képernyőre
# ============================================================

print("\n--- 2. Print ---")

# Egyszerű kiírás
print("Hello, világ!")

# Több dolog egymás mellé
print("Név:", name, "- Kor:", age)

# f-string — a legmodernebb és legolvashatóbb módszer
# A {} kapcsos zárójelbe változókat rakhatsz
print(f"Szia, {name}! Te {age} éves vagy.")
print(f"Magasság: {height} méter")


# ============================================================
# 3. TÍPUSOK — minden értéknek van típusa
# ============================================================

print("\n--- 3. Típusok ---")

# A type() megmondja, mi a típusa
print(type(name))         # <class 'str'>     → szöveg
print(type(age))          # <class 'int'>     → egész szám
print(type(height))       # <class 'float'>   → tizedes szám
print(type(is_student))   # <class 'bool'>    → igaz/hamis


# ============================================================
# 4. MŰVELETEK — mit csinálhatsz az értékekkel
# ============================================================

print("\n--- 4. Műveletek ---")

# Számokkal: matematika
a = 10
b = 3
print(f"{a} + {b} = {a + b}")      # összeadás → 13
print(f"{a} - {b} = {a - b}")      # kivonás → 7
print(f"{a} * {b} = {a * b}")      # szorzás → 30
print(f"{a} / {b} = {a / b}")      # osztás → 3.333...
print(f"{a} // {b} = {a // b}")    # egész osztás → 3
print(f"{a} % {b} = {a % b}")      # maradék → 1
print(f"{a} ** {b} = {a ** b}")    # hatványozás → 1000

# Szövegekkel
first = "Hello"
second = "Világ"
together = first + " " + second    # összefűzés
print(together)                    # "Hello Világ"
print(first * 3)                   # "HelloHelloHello"


# ============================================================
# 5. LISTA (list) — több érték egy helyen
# ============================================================

print("\n--- 5. Lista ---")

# Lista létrehozása — szögletes zárójel
fruits = ["alma", "körte", "szilva", "barack"]
numbers = [10, 20, 30, 40, 50]
mixed = ["szöveg", 42, True, 3.14]   # vegyes is lehet

# Elem elérése — indexelés 0-tól indul!
print(fruits[0])    # "alma"     ← első elem
print(fruits[1])    # "körte"    ← második elem
print(fruits[-1])   # "barack"   ← utolsó elem

# Lista hossza
print(f"Gyümölcsök száma: {len(fruits)}")

# Elem hozzáadása
fruits.append("meggy")
print(fruits)       # ["alma", "körte", "szilva", "barack", "meggy"]

# Elem törlése
fruits.remove("körte")
print(fruits)       # ["alma", "szilva", "barack", "meggy"]


# ============================================================
# 6. SZÓTÁR (dict) — kulcs-érték párok
# ============================================================

print("\n--- 6. Szótár ---")

# Szótár létrehozása — kapcsos zárójel
person = {
    "name": "Kiss Péter",
    "age": 25,
    "city": "Budapest"
}

# Értékek elérése
print(person["name"])       # "Kiss Péter"
print(person["age"])        # 25

# Új kulcs hozzáadása
person["email"] = "peter@example.com"
print(person)

# Biztonságos elérés — .get() nem dob hibát, ha nincs a kulcs
print(person.get("phone", "nincs megadva"))


# ============================================================
# 7. FELTÉTELEK (if/elif/else) — döntéshozatal
# ============================================================

print("\n--- 7. Feltételek ---")

age = 25

if age < 18:
    print("Kiskorú")
elif age < 65:
    print("Felnőtt")
else:
    print("Nyugdíjas")

# Összehasonlító operátorok:
# ==  egyenlő          !=  nem egyenlő
# <   kisebb            >   nagyobb
# <=  kisebb-egyenlő   >=  nagyobb-egyenlő

# Logikai operátorok: and, or, not
score = 85
if score >= 80 and score < 90:
    print("Jó eredmény!")

has_ticket = True
if not has_ticket:
    print("Nincs jegyed!")
else:
    print("Van jegyed, mehetsz!")


# ============================================================
# 8. CIKLUSOK (for, while) — ismétlés
# ============================================================

print("\n--- 8. Ciklusok ---")

# FOR ciklus — végigmegy egy listán
print("Gyümölcsök:")
for fruit in ["alma", "körte", "szilva"]:
    print(f"  - {fruit}")

# FOR ciklus számokkal — range()
print("Számok 1-től 5-ig:")
for i in range(1, 6):       # 1, 2, 3, 4, 5 (a 6 már nincs benne!)
    print(f"  {i}")

# WHILE ciklus — amíg igaz a feltétel
print("Visszaszámlálás:")
counter = 5
while counter > 0:
    print(f"  {counter}...")
    counter = counter - 1    # counter -= 1 is jó
print("  Start!")


# ============================================================
# 9. FÜGGVÉNYEK (def) — újrahasználható kódrészletek
# ============================================================

print("\n--- 9. Függvények ---")


# Függvény definiálása
def greet(name):
    """Köszönti a megadott személyt."""
    print(f"Szia, {name}!")


# Függvény hívása
greet("Anna")
greet("Béla")


# Visszatérési értékkel (return)
def add(a, b):
    """Összeadja a két számot és visszaadja az eredményt."""
    return a + b


result = add(10, 20)
print(f"10 + 20 = {result}")


# Több paraméter, alapértelmezett érték
def introduce(name, age, city="Budapest"):
    """Bemutatkozás — a város opcionális, alapból Budapest."""
    print(f"A nevem {name}, {age} éves vagyok, {city}-ban élek.")


introduce("Péter", 25)
introduce("Anna", 30, "Debrecen")


# ============================================================
# 10. ÖSSZEFOGLALÓ
# ============================================================

print("\n--- Összefoglaló ---")
print("""
Amit megtanultál:
  1. Változók: name = "érték"
  2. Print és f-string: print(f"Szia, {name}!")
  3. Típusok: str, int, float, bool
  4. Műveletek: +, -, *, /, //, %, **
  5. Lista: [1, 2, 3] — indexelés 0-tól
  6. Szótár: {"kulcs": "érték"}
  7. Feltételek: if/elif/else
  8. Ciklusok: for, while
  9. Függvények: def my_function():

Következő lépés: nyisd meg az exercise_00_practice.py fájlt
és oldd meg a gyakorló feladatokat!
""")

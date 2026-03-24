"""
=============================================================
  1.4 LECKE: Type hints (típusjelzések) és docstringek
=============================================================

Eddig tanultál:
  - Változókat, típusokat, listákat, szótárakat (0. lecke)
  - Jó elnevezéseket (1.1 lecke)
  - Függvényeket (1.2 lecke)
  - DRY/KISS elveket

Most megtanulod:
  - Mi az a type hint és miért hasznos
  - Hogyan jelöld meg a típusokat változóknál és függvényeknél
  - Mi az a docstring és hogyan írd meg
  - Hogyan kombináld a kettőt profin

Futtasd:
    python 01-python-clean-code/exercises/04_type_hints_alapok.py
"""


# ============================================================
# 1. MI AZ A TYPE HINT (TÍPUSJELZÉS)?
# ============================================================

# Képzeld el, hogy költözöl. Dobozokba pakolsz mindent.
#
# Ha a dobozra NEM írsz semmit:
#   → Aki később kinyitja, fogalma sincs mi van benne.
#   → Lehet benne pohár, könyv, vagy akár macskaeledel.
#
# Ha a dobozra RÁÍROD: "TÖRÉKENY — POHARAK":
#   → Bárki azonnal tudja, mit talál benne.
#   → Óvatosan fog bánni vele.
#
# A type hint pontosan ez: FELIRATOZOD a kódodat,
# hogy mindenki (és te magad is!) tudja, milyen típusú
# adatot vár és ad vissza egy függvény.

print("=" * 50)
print("  1. MI AZ A TYPE HINT?")
print("=" * 50)
print()

# --- TYPE HINT NÉLKÜL ---
# Mi az a és b? Szám? Szöveg? Lista? Fogalmunk sincs!
def calculate_bad(a, b):
    return a * b

# Ez működik számmal:
print(calculate_bad(5, 3))       # 15

# De szöveggel is "működik", pedig nem biztos hogy ezt akartad:
print(calculate_bad("ha", 3))    # "hahaha"

print()

# --- TYPE HINT-TEL ---
# Azonnal látod: árat (int) és mennyiséget (int) vár,
# és egy int-et ad vissza!
def calculate_total(price: int, quantity: int) -> int:
    """Kiszámolja a végösszeget."""
    return price * quantity                    # ár szorozva mennyiséggel

print(f"5 darab 300 Ft-os termék: {calculate_total(300, 5)} Ft")
# Kimenet: 5 darab 300 Ft-os termék: 1500 Ft

print()

# FONTOS: A type hint csak JELZÉS, nem kényszer!
# A Python NEM akadályozza meg, hogy rossz típust adj.
# De a szerkesztőd (VS Code) figyelmeztet rá,
# és te magad is azonnal látod, mit vár a függvény.


# ============================================================
# 2. ALAP TÍPUSOK
# ============================================================

# A Python 5 leggyakoribb alaptípusa:
#   int   — egész szám (pl. 1, 42, -7)
#   float — tizedes szám (pl. 3.14, -0.5)
#   str   — szöveg (pl. "Hello", "alma")
#   bool  — igaz/hamis (True vagy False)
#   None  — "semmi" / "nincs érték"

print("=" * 50)
print("  2. ALAP TÍPUSOK")
print("=" * 50)
print()

# --- Változóknál ---
# A változó neve után kettőspont, utána a típus:

age: int = 19                       # egész szám: életkor
height: float = 1.75                # tizedes szám: magasság méterben
username: str = "Dani"              # szöveg: felhasználónév
is_student: bool = True             # igaz/hamis: diák-e?

print(f"Név: {username}, Kor: {age}, Magasság: {height}m, Diák: {is_student}")

print()

# --- Függvény paramétereknél ---
# Ugyanúgy kettőspont a paraméter után:

def greet_user(name: str) -> str:   # str-t kap, str-t ad vissza
    """Üdvözlő szöveget ad vissza."""
    return f"Szia, {name}!"         # visszaadja az üdvözlést

message: str = greet_user("Dani")   # a visszatérési értéket eltároljuk
print(message)                      # Kimenet: Szia, Dani!

print()

# --- float visszatérési érték ---

def calculate_average(a: float, b: float) -> float:
    """Két szám átlagát számolja ki."""
    return (a + b) / 2              # az osztás mindig float-ot ad

result: float = calculate_average(8.0, 6.0)
print(f"8 és 6 átlaga: {result}")  # Kimenet: 8 és 6 átlaga: 7.0

print()

# --- bool visszatérési érték ---

def is_adult(age: int) -> bool:
    """Megmondja, hogy nagykorú-e valaki (18+)."""
    return age >= 18                # True ha 18 vagy több, False ha kevesebb

print(f"19 éves nagykorú? {is_adult(19)}")   # True
print(f"15 éves nagykorú? {is_adult(15)}")   # False

print()

# --- None visszatérési érték ---
# Ha a függvény NEM ad vissza semmit (nincs return, vagy return None):

def print_welcome(name: str) -> None:
    """Kiírja az üdvözlést. Nem ad vissza semmit."""
    print(f"Üdvözöllek, {name}!")   # csak kiír, nem return-öl

print_welcome("Dani")              # Kimenet: Üdvözöllek, Dani!

print()


# ============================================================
# 3. ÖSSZETETT TÍPUSOK
# ============================================================

# Az alaptípusokon kívül vannak "összetett" típusok is.
# Ezek olyanok, mint a doboz a dobozban:
#   - Van egy nagy dobozod (lista), amiben kis dobozok vannak (str-ek).
#   - A type hint-tel meg tudod mondani: "ez egy lista, AMIBEN szövegek vannak"

print("=" * 50)
print("  3. ÖSSZETETT TÍPUSOK")
print("=" * 50)
print()

# --- Lista típusjelzés ---
# list[str] = lista, amiben szövegek vannak
# list[int] = lista, amiben egész számok vannak

fruit_names: list[str] = ["alma", "körte", "barack"]   # szövegek listája
exam_scores: list[int] = [85, 92, 78, 95]              # számok listája

print(f"Gyümölcsök: {fruit_names}")
print(f"Vizsgapontok: {exam_scores}")

print()

# --- Szótár típusjelzés ---
# dict[str, int] = szótár, ahol a kulcs szöveg, az érték szám
# Gondolj rá úgy: dict[KULCS_TÍPUSA, ÉRTÉK_TÍPUSA]

student_scores: dict[str, int] = {   # kulcs: diák neve (str), érték: pont (int)
    "Anna": 92,
    "Béla": 78,
    "Cecil": 85,
}

print(f"Diákok pontjai: {student_scores}")

print()

# --- Függvényben összetett típusokkal ---

def get_best_student(scores: dict[str, int]) -> str:
    """Visszaadja a legjobb diák nevét."""
    best_name: str = ""             # ide gyűjtjük a legjobb nevét
    best_score: int = 0             # ide gyűjtjük a legjobb pontját

    for name, score in scores.items():     # végigmegyünk a szótáron
        if score > best_score:             # ha ez jobb, mint az eddigi legjobb
            best_name = name               # megjegyezzük a nevét
            best_score = score             # és a pontját

    return best_name                       # visszaadjuk a legjobb nevét

print(f"Legjobb diák: {get_best_student(student_scores)}")

print()

# --- Tuple típusjelzés ---
# tuple[str, int] = rendezett pár, ahol az első szöveg, a második szám
# A tuple olyan mint a lista, de NEM lehet módosítani!

coordinates: tuple[float, float] = (47.497, 19.040)   # Budapest GPS koordinátái
print(f"Budapest koordinátái: {coordinates}")

print()

# --- Lehet None is: str | None ---
# Néha egy érték LEHET szöveg, de LEHET semmi (None) is.
# Például: a felhasználó középső neve — nem mindenkinek van.
#
# Python 3.10+ szintaxis: str | None
# Olvasd így: "vagy str, VAGY None"

middle_name: str | None = None         # nincs középső neve
print(f"Középső név: {middle_name}")   # Kimenet: Középső név: None

middle_name = "István"                 # de lehet, hogy van
print(f"Középső név: {middle_name}")   # Kimenet: Középső név: István

print()

# --- Függvényben Optional használata ---

def find_student_score(scores: dict[str, int], name: str) -> int | None:
    """Megkeresi a diák pontszámát. Ha nincs ilyen diák, None-t ad vissza."""
    if name in scores:                  # ha megtaláljuk a diákot
        return scores[name]             # visszaadjuk a pontszámát
    return None                         # ha nincs ilyen diák, None

anna_score: int | None = find_student_score(student_scores, "Anna")
xyz_score: int | None = find_student_score(student_scores, "XYZ")

print(f"Anna pontja: {anna_score}")    # Kimenet: Anna pontja: 92
print(f"XYZ pontja: {xyz_score}")      # Kimenet: XYZ pontja: None

print()


# ============================================================
# 4. MI AZ A DOCSTRING?
# ============================================================

# Emlékszel a dobozhasonlatra?
#
# A TYPE HINT = a doboz KÜLSŐ felirata
#   → Ránézel és tudod: "POHARAK" (típus: str)
#
# A DOCSTRING = a HASZNÁLATI ÚTMUTATÓ a doboz BELSEJÉBEN
#   → Kinyitod és megtudod: "Kézzel mosogatni! Max 6 db fér bele."
#
# Miért fontos a docstring?
# Mert 3 HÓNAP MÚLVA te sem fogod érteni a saját kódodat.
# Komolyan. Mindenki azt hiszi, hogy "de én biztosan emlékezni fogok."
# Aztán 3 hónap múlva: "Ki írta ezt?! ...ja, én."

print("=" * 50)
print("  4. MI AZ A DOCSTRING?")
print("=" * 50)
print()

# A docstring háromszoros idézőjelek közé írt szöveg,
# rögtön a függvény definiálása UTÁN.
# A Python ezt speciálisan kezeli: a help() paranccsal elérheted.

# --- ROSSZ docstring ---
# Nem mond többet, mint amit a kódból amúgy is látsz:

def add_numbers_bad(a: int, b: int) -> int:
    """Összeadja a-t és b-t."""     # ← EZ SEMMIT NEM SEGÍT
    return a + b                     # a kódból is látod, hogy összeadja

# --- JÓ docstring ---
# Megmondja a MIÉRT-et, a szabályokat, példát ad:

def calculate_discount(price: float, discount_percent: float) -> float:
    """Kiszámolja a kedvezményes árat.

    Az eredeti árból levonja a megadott százalékos kedvezményt.
    Ha a kedvezmény 100%-nál nagyobb, 0-t ad vissza (nem lehet negatív ár).

    Args:
        price: Az eredeti ár forintban. Pozitív szám kell legyen.
        discount_percent: A kedvezmény mértéke százalékban (pl. 20 = 20%).

    Returns:
        A kedvezményes ár forintban.

    Examples:
        >>> calculate_discount(1000, 20)
        800.0
        >>> calculate_discount(500, 100)
        0.0
    """
    discount_amount: float = price * (discount_percent / 100)   # kedvezmény összege
    final_price: float = price - discount_amount                # kedvezményes ár

    if final_price < 0:        # ha a kedvezmény túl nagy volt
        return 0.0             # ne legyen negatív ár

    return final_price         # visszaadjuk a kedvezményes árat

print(f"1000 Ft, 20% kedvezmény: {calculate_discount(1000, 20)} Ft")
print(f"500 Ft, 100% kedvezmény: {calculate_discount(500, 100)} Ft")

print()

# --- Google-style docstring formátum ---
#
# Ez a legelterjedtebb formátum. Így épül fel:
#
#   def függvény_neve(param1: típus, param2: típus) -> visszatérési_típus:
#       """Egysoros összefoglaló — mit csinál a függvény.
#
#       Részletesebb leírás, ha kell. Ide írhatsz több mondatot is.
#       Magyarázhatod a logikát, a szabályokat, a korlátokat.
#
#       Args:
#           param1: Mit jelent ez a paraméter.
#           param2: Mit jelent ez a paraméter.
#
#       Returns:
#           Mit ad vissza a függvény.
#
#       Examples:
#           >>> függvény_neve(1, 2)
#           3
#       """

# Tippek a jó docstring-hez:
# 1. Az első sor MINDIG egysoros összefoglaló (mit csinál)
# 2. Utána üres sor, majd részletes leírás (ha kell)
# 3. Args: — minden paraméter rövid leírása
# 4. Returns: — mit ad vissza
# 5. Examples: — egy-két példa (opcionális, de nagyon hasznos)

print("A docstring formátumot lásd a forráskódban!")
print()


# ============================================================
# 5. TYPE HINTS + DOCSTRING EGYÜTT — KOMPLETT PÉLDA
# ============================================================

# Most nézzük meg, hogyan néz ki egy TELJESEN PROFESSZIONÁLISAN
# dokumentált függvény. Ez a "gold standard" — így érdemes írni!

print("=" * 50)
print("  5. TYPE HINTS + DOCSTRING EGYÜTT")
print("=" * 50)
print()


def create_student_report(
    name: str,                         # a diák neve
    scores: list[int],                 # a diák jegyeinek listája
    is_scholarship: bool = False       # ösztöndíjas-e (alapból nem)
) -> dict[str, str | float | bool]:
    """Létrehoz egy diák jelentést az eredményei alapján.

    Kiszámolja a diák átlagát és meghatározza, hogy átment-e
    (az átlag legalább 2.0 kell legyen). Ha ösztöndíjas, azt is
    feltünteti a jelentésben.

    Args:
        name: A diák teljes neve.
        scores: A diák jegyeinek listája (1-5 skálán).
        is_scholarship: Ösztöndíjas-e a diák. Alapértelmezetten False.

    Returns:
        Egy szótár a következő kulcsokkal:
        - "name": a diák neve
        - "average": a jegyek átlaga
        - "passed": átment-e (True/False)
        - "scholarship": ösztöndíjas-e

    Examples:
        >>> create_student_report("Anna", [5, 4, 5, 3])
        {'name': 'Anna', 'average': 4.25, 'passed': True, 'scholarship': False}
    """
    # Átlag kiszámítása: összeg osztva a jegyek számával
    average: float = sum(scores) / len(scores)

    # Átment-e: az átlag legalább 2.0 kell legyen
    passed: bool = average >= 2.0

    # Jelentés összeállítása szótárként
    report: dict[str, str | float | bool] = {
        "name": name,                  # diák neve
        "average": round(average, 2),  # átlag, 2 tizedesre kerekítve
        "passed": passed,              # átment-e
        "scholarship": is_scholarship, # ösztöndíjas-e
    }

    return report                      # visszaadjuk a kész jelentést


# --- Használat ---
anna_report = create_student_report("Anna", [5, 4, 5, 3])
bela_report = create_student_report("Béla", [2, 1, 2, 1], is_scholarship=True)

print(f"Anna jelentése: {anna_report}")
print(f"Béla jelentése: {bela_report}")

print()


# ============================================================
# 6. ÖSSZEFOGLALÓ
# ============================================================

print("=" * 50)
print("  6. ÖSSZEFOGLALÓ")
print("=" * 50)
print()

print("""
MIT TANULTÁL MA:

1. TYPE HINT = feliratozás a kódra
   - Változónál:    age: int = 19
   - Paraméternél:  def greet(name: str)
   - Visszatérésnél: def greet(name: str) -> str

2. ALAP TÍPUSOK:
   - int, float, str, bool, None

3. ÖSSZETETT TÍPUSOK:
   - list[str]         — szövegek listája
   - dict[str, int]    — szótár (kulcs: str, érték: int)
   - tuple[int, int]   — módosíthatatlan pár
   - str | None        — lehet szöveg VAGY semmi

4. DOCSTRING = használati útmutató a függvényhez
   - Háromszoros idézőjelek: \"""...\"""
   - Google-style: Args, Returns, Examples
   - A MIÉRT-et írd le, ne azt, amit a kódból amúgy is látsz!

5. A KETTŐ EGYÜTT = profin dokumentált kód
   - Type hint: a típusokat jelzi
   - Docstring: a logikát magyarázza

KÖVETKEZŐ LÉPÉS:
   → Oldd meg a exercise_04_type_hints.py gyakorlatot!
""")

"""
=================================================================
  GYAKORLAT 05 - HIBAKEZELÉS (Error Handling)
  Szint: Kezdő
  Előfeltétel: 05_hibakezelés_alapok.py elolvasása
=================================================================

  5 feladat vár rád. Minden feladatnál megvan a leírás,
  a függvény váza, és a végén automatikus ellenőrzés.

  SZABÁLYOK:
  - A "# MEGOLDÁS IDE:" komment alá írd a kódodat
  - Ne töröld a pass-t, amíg nem írod be a saját megoldásod
  - Futtasd le a fájlt, és nézd meg az ellenőrzés eredményét

  TIPP: Ha elakadsz, olvasd újra az elméleti anyagot!
        (05_hibakezelés_alapok.py)
=================================================================
"""


# =============================================================
# 1. FELADAT: ALAPVETŐ TRY/EXCEPT
# =============================================================
#
# Adott egy függvény ami két számot oszt el egymással.
# A probléma: ha a második szám 0, a program elszáll!
#
# Feladat:
#   - Kezeld le a ZeroDivisionError-t
#   - Ha 0-val próbálnak osztani, a függvény adjon vissza None-t
#   - Ha nincs hiba, adja vissza az osztás eredményét (float)
#
# Példák:
#   safe_divide(10, 2)  -> 5.0
#   safe_divide(10, 0)  -> None
#   safe_divide(7, 3)   -> 2.3333...

def safe_divide(a: int, b: int) -> float | None:
    """Biztonságosan eloszt két számot. Ha b nulla, None-t ad vissza."""
    # MEGOLDÁS IDE:
    pass


# =============================================================
# 2. FELADAT: KONKRÉT HIBATÍPUS (IndexError)
# =============================================================
#
# Adott egy lista és egy index.
# A feladat: próbáld meg visszaadni a lista adott indexű elemét.
#
# Ha az index NEM létezik (IndexError), adj vissza egy
# hibaüzenetet szövegként: "Hiba: Nincs ilyen index: {index}"
#
# Példák:
#   safe_list_access(["a", "b", "c"], 1)  -> "b"
#   safe_list_access(["a", "b", "c"], 10) -> "Hiba: Nincs ilyen index: 10"
#   safe_list_access([], 0)               -> "Hiba: Nincs ilyen index: 0"

def safe_list_access(items: list, index: int) -> str:
    """Biztonságosan hozzáfér egy lista eleméhez index alapján."""
    # MEGOLDÁS IDE:
    pass


# =============================================================
# 3. FELADAT: SZÁM KONVERTÁLÁS
# =============================================================
#
# Írj egy függvényt ami egy szöveget (str) egész számmá (int)
# próbál meg alakítani.
#
# Ha sikerül: adja vissza a számot (int)
# Ha NEM sikerül (mert a szöveg nem szám): adjon vissza None-t
#
# Tipp: A megfelelő hibatípus a ValueError.
#
# Példák:
#   safe_int_convert("42")    -> 42
#   safe_int_convert("hello") -> None
#   safe_int_convert("3.14")  -> None  (a "3.14" nem int!)
#   safe_int_convert("")      -> None

def safe_int_convert(value: str) -> int | None:
    """Szöveget számmá alakít. Ha nem sikerül, None-t ad vissza."""
    # MEGOLDÁS IDE:
    pass


# =============================================================
# 4. FELADAT: SAJÁT HIBA DOBÁSA (raise)
# =============================================================
#
# Írj egy függvényt ami létrehoz egy felhasználói profilt.
# A függvény ellenőrizze az inputot és DOBJON HIBÁT ha:
#
#   - A username üres szöveg ("") -> raise ValueError("A felhasználónév nem lehet üres!")
#   - A username rövidebb mint 3 karakter -> raise ValueError("A felhasználónév legalább 3 karakter legyen!")
#   - Az age nem pozitív szám (0 vagy negatív) -> raise ValueError("Az életkor pozitív szám kell legyen!")
#   - Az age nagyobb mint 150 -> raise ValueError("Az életkor nem lehet 150-nél nagyobb!")
#
# Ha minden rendben van, adja vissza a szótárat:
#   {"username": username, "age": age}
#
# Példák:
#   create_profile("Dani", 19)  -> {"username": "Dani", "age": 19}
#   create_profile("", 19)      -> ValueError: "A felhasználónév nem lehet üres!"
#   create_profile("ab", 19)    -> ValueError: "A felhasználónév legalább 3 karakter legyen!"
#   create_profile("Dani", -5)  -> ValueError: "Az életkor pozitív szám kell legyen!"

def create_profile(username: str, age: int) -> dict:
    """Létrehoz egy felhasználói profilt az adatok ellenőrzése után."""
    # MEGOLDÁS IDE:
    pass


# =============================================================
# 5. FELADAT: KOMPLEX — MINI BANKI ALKALMAZÁS
# =============================================================
#
# Készíts egy egyszerű "bankszámlát" ami szótárként tárolja
# a számlákat, és két műveletet támogat:
#   - Egyenleg lekérdezés
#   - Utalás (pénz átvitele egyik számláról a másikra)
#
# A számlák szótára ilyen formátumú:
#   accounts = {"Anna": 10000, "Béla": 5000, "Cecil": 0}
#
# --- get_balance ---
# Visszaadja az adott személy egyenlegét.
# Ha a személy NEM létezik: raise KeyError("Ismeretlen számlatulajdonos: {name}")
#
# --- transfer ---
# Átutal pénzt az egyik számláról a másikra.
# Ellenőrzések:
#   - Ha a küldő NEM létezik: raise KeyError("Ismeretlen küldő: {sender}")
#   - Ha a fogadó NEM létezik: raise KeyError("Ismeretlen fogadó: {receiver}")
#   - Ha az összeg nem pozitív: raise ValueError("Az összeg pozitív szám kell legyen!")
#   - Ha nincs elég pénz: raise ValueError("Nincs elég fedezet! Egyenleg: {egyenleg} Ft")
#   - Ha minden rendben: vonja le a küldőtől, adja hozzá a fogadóhoz
#   - Adja vissza: "Sikeres utalás: {amount} Ft, {sender} -> {receiver}"

# Ezt a szótárat használd a függvényeidben:
accounts: dict[str, int] = {
    "Anna": 10000,
    "Béla": 5000,
    "Cecil": 0,
}


def get_balance(name: str) -> int:
    """Visszaadja az adott személy egyenlegét."""
    # MEGOLDÁS IDE:
    pass


def transfer(sender: str, receiver: str, amount: int) -> str:
    """Pénzt utal át egyik számláról a másikra."""
    # MEGOLDÁS IDE:
    pass


# =============================================================
#                     ELLENŐRZÉS
# =============================================================
# Ez a rész automatikusan lefut és ellenőrzi a megoldásaidat.
# NE módosítsd ezt a részt!
# =============================================================

def run_tests() -> None:
    """Lefuttatja az összes tesztet és kiírja az eredményeket."""

    print("=" * 60)
    print("  ELLENŐRZÉS — Hibakezelés gyakorlat")
    print("=" * 60)

    passed = 0       # hány teszt sikerült
    total = 0        # hány teszt volt összesen
    failed_info = [] # elbukott tesztek infói

    def check(test_name: str, condition: bool, hint: str = "") -> None:
        """Egy teszt ellenőrzése."""
        nonlocal passed, total
        total += 1
        if condition:
            passed += 1
            print(f"  [SIKER] {test_name}")
        else:
            print(f"  [HIBA]  {test_name}")
            if hint:
                print(f"          Tipp: {hint}")
            failed_info.append(test_name)

    # --- 1. feladat tesztek ---
    print("\n--- 1. feladat: safe_divide ---")
    check(
        "safe_divide(10, 2) == 5.0",
        safe_divide(10, 2) == 5.0,
        "A 10 / 2 eredménye 5.0 kell legyen."
    )
    check(
        "safe_divide(10, 0) is None",
        safe_divide(10, 0) is None,
        "Ha 0-val osztunk, None-t kell visszaadni (try/except ZeroDivisionError)."
    )
    check(
        "safe_divide(7, 3) közelítőleg 2.333",
        safe_divide(7, 3) is not None and abs(safe_divide(7, 3) - 2.3333333) < 0.001,
        "A 7 / 3 eredménye kb. 2.333 kell legyen."
    )
    check(
        "safe_divide(0, 5) == 0.0",
        safe_divide(0, 5) == 0.0,
        "A 0 / 5 eredménye 0.0 kell legyen."
    )

    # --- 2. feladat tesztek ---
    print("\n--- 2. feladat: safe_list_access ---")
    check(
        'safe_list_access(["a", "b", "c"], 1) == "b"',
        safe_list_access(["a", "b", "c"], 1) == "b",
        "Az 1-es indexen a 'b' van."
    )
    check(
        'safe_list_access(["a", "b", "c"], 10) hibaüzenetet ad',
        safe_list_access(["a", "b", "c"], 10) == "Hiba: Nincs ilyen index: 10",
        "Ha nincs ilyen index, adj vissza: 'Hiba: Nincs ilyen index: {index}'"
    )
    check(
        'safe_list_access([], 0) hibaüzenetet ad',
        safe_list_access([], 0) == "Hiba: Nincs ilyen index: 0",
        "Üres lista esetén sincs 0-s index!"
    )

    # --- 3. feladat tesztek ---
    print("\n--- 3. feladat: safe_int_convert ---")
    check(
        'safe_int_convert("42") == 42',
        safe_int_convert("42") == 42,
        "A '42' szöveg int-té alakítva 42."
    )
    check(
        'safe_int_convert("hello") is None',
        safe_int_convert("hello") is None,
        "A 'hello' nem szám, None-t kell visszaadni."
    )
    check(
        'safe_int_convert("3.14") is None',
        safe_int_convert("3.14") is None,
        "A '3.14' nem egész szám (int), None-t kell visszaadni."
    )
    check(
        'safe_int_convert("") is None',
        safe_int_convert("") is None,
        "Üres szöveg nem szám, None-t kell visszaadni."
    )

    # --- 4. feladat tesztek ---
    print("\n--- 4. feladat: create_profile ---")
    check(
        'create_profile("Dani", 19) helyes szótárat ad',
        create_profile("Dani", 19) == {"username": "Dani", "age": 19},
        'Jó input esetén: {"username": "Dani", "age": 19}'
    )

    # Üres username teszt
    got_error = False
    try:
        create_profile("", 19)
    except ValueError as e:
        got_error = "nem lehet üres" in str(e)
    check(
        'create_profile("", 19) ValueError-t dob (üres név)',
        got_error,
        'Üres username esetén raise ValueError("A felhasználónév nem lehet üres!")'
    )

    # Rövid username teszt
    got_error = False
    try:
        create_profile("ab", 19)
    except ValueError as e:
        got_error = "legalább 3" in str(e)
    check(
        'create_profile("ab", 19) ValueError-t dob (rövid név)',
        got_error,
        'Rövid username esetén raise ValueError("A felhasználónév legalább 3 karakter legyen!")'
    )

    # Negatív kor teszt
    got_error = False
    try:
        create_profile("Dani", -5)
    except ValueError as e:
        got_error = "pozitív" in str(e).lower()
    check(
        'create_profile("Dani", -5) ValueError-t dob (negatív kor)',
        got_error,
        'Negatív kor esetén raise ValueError("Az életkor pozitív szám kell legyen!")'
    )

    # Túl nagy kor teszt
    got_error = False
    try:
        create_profile("Dani", 200)
    except ValueError as e:
        got_error = "150" in str(e)
    check(
        'create_profile("Dani", 200) ValueError-t dob (túl nagy kor)',
        got_error,
        'Túl nagy kor esetén raise ValueError("Az életkor nem lehet 150-nél nagyobb!")'
    )

    # --- 5. feladat tesztek ---
    print("\n--- 5. feladat: Mini banki alkalmazás ---")

    # Egyenleg reset a tesztek előtt
    accounts["Anna"] = 10000
    accounts["Béla"] = 5000
    accounts["Cecil"] = 0

    check(
        "get_balance('Anna') == 10000",
        get_balance("Anna") == 10000,
        "Anna egyenlege 10000 Ft kell legyen."
    )

    # Nem létező személy
    got_error = False
    try:
        get_balance("Xyz")
    except KeyError as e:
        got_error = "Ismeretlen" in str(e)
    check(
        "get_balance('Xyz') KeyError-t dob",
        got_error,
        "Nem létező személynél raise KeyError('Ismeretlen számlatulajdonos: Xyz')"
    )

    # Sikeres utalás
    accounts["Anna"] = 10000
    accounts["Béla"] = 5000
    result = None
    try:
        result = transfer("Anna", "Béla", 3000)
    except Exception:
        pass
    check(
        "transfer('Anna', 'Béla', 3000) sikeres",
        result is not None and "Sikeres" in result,
        "Sikeres utalás esetén: 'Sikeres utalás: 3000 Ft, Anna -> Béla'"
    )
    check(
        "Utalás után Anna egyenlege 7000",
        accounts.get("Anna") == 7000,
        "10000 - 3000 = 7000 kell legyen Anna egyenlege."
    )
    check(
        "Utalás után Béla egyenlege 8000",
        accounts.get("Béla") == 8000,
        "5000 + 3000 = 8000 kell legyen Béla egyenlege."
    )

    # Nincs elég fedezet
    accounts["Cecil"] = 0
    got_error = False
    try:
        transfer("Cecil", "Anna", 1000)
    except ValueError as e:
        got_error = "fedezet" in str(e).lower()
    check(
        "transfer('Cecil', 'Anna', 1000) ValueError (nincs fedezet)",
        got_error,
        "Ha nincs elég pénz: raise ValueError('Nincs elég fedezet! Egyenleg: 0 Ft')"
    )

    # Negatív összeg
    got_error = False
    try:
        transfer("Anna", "Béla", -500)
    except ValueError as e:
        got_error = "pozitív" in str(e).lower()
    check(
        "transfer('Anna', 'Béla', -500) ValueError (negatív összeg)",
        got_error,
        "Negatív összeg esetén: raise ValueError('Az összeg pozitív szám kell legyen!')"
    )

    # Nem létező küldő
    got_error = False
    try:
        transfer("Xyz", "Anna", 100)
    except KeyError as e:
        got_error = "küldő" in str(e).lower() or "Ismeretlen" in str(e)
    check(
        "transfer('Xyz', 'Anna', 100) KeyError (nem létező küldő)",
        got_error,
        "Nem létező küldő esetén raise KeyError('Ismeretlen küldő: Xyz')"
    )

    # --- Végeredmény ---
    print("\n" + "=" * 60)
    print(f"  EREDMÉNY: {passed}/{total} teszt sikerült")
    print("=" * 60)

    if passed == total:
        print("\n  TÖKÉLETES! Minden feladatot megoldottál!")
        print("  A hibakezelés mostantól a fegyvertárad része.")
    elif passed >= total * 0.7:
        print("\n  Szép munka! Már majdnem minden stimmel.")
        print("  Nézd meg a [HIBA] jelzésű teszteket és javítsd ki!")
    elif passed >= total * 0.4:
        print("\n  Jó irány! De még van mit javítani.")
        print("  Olvasd újra az elméleti anyagot (05_hibakezelés_alapok.py)")
        print("  és próbáld újra a hibás feladatokat.")
    else:
        print("\n  Ne csüggedj! Ez egy új téma, gyakorlás kell hozzá.")
        print("  Tipp: Kezdd az 1. feladattal, és haladj sorban.")
        print("  Az elméleti anyagban (05_hibakezelés_alapok.py) minden benne van!")


# Futtatás
if __name__ == "__main__":
    run_tests()

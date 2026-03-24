"""
=================================================================
  05 - HIBAKEZELÉS ALAPOK (Error Handling)
  Szint: Kezdő
  Előfeltétel: változók, típusok, listák, szótárak, ciklusok,
                feltételek, függvények, type hints
=================================================================

  Képzeld el, hogy főzöl egy recept alapján.
  A recept azt mondja: "Adj hozzá 3 tojást."
  De mi van, ha NINCS tojásod?

  Ha a recept nem szól erről, te ott állsz tanácstalanul.
  A főzés megáll, a vacsora elmarad.

  A programozásban UGYANEZ történik:
  - A kódod csinál valamit (receptet követ)
  - Valami váratlan történik (nincs tojás = hiba)
  - Ha NEM készülsz fel rá, a program LEÁLL

  A hibakezelés = felkészülsz arra, hogy mi lehet a baj,
  és megmondod a programnak, mit csináljon ilyenkor.

=================================================================
"""


# =============================================================
# 1. SZEKCIÓ: MI AZ A HIBA (EXCEPTION)?
# =============================================================

# A Python-ban a hibákat "exception"-nek (kivételnek) hívjuk.
# Amikor valami "rosszul sül el", a Python dob egy hibát,
# és ha nem kapod el, a programod azonnal megáll.

# Nézzük meg, milyen gyakori hibák vannak:

# --- ZeroDivisionError ---
# Nullával nem lehet osztani, ezt matekból is tudod.
# Ha mégis megpróbálod, a Python hibát dob:

print("--- ZeroDivisionError példa ---")
# Ha ezt lefuttatnád komment nélkül, leállna a program:
# result = 10 / 0   # <-- HIBA! Ezt NEM szabad csinálni kezelés nélkül

# Helyette biztonságosan mutatjuk meg:
try:
    result = 10 / 0                   # megpróbáljuk az osztást
except ZeroDivisionError:             # ha nullával osztanánk...
    print("Hiba: Nullával nem lehet osztani!")  # ...ezt írjuk ki helyette


# --- TypeError ---
# Amikor össze nem illő típusokat próbálsz használni.
# Olyan, mintha almát és körtét akarnál összeadni, de úgy,
# hogy az egyik egy szám, a másik meg egy szöveg.

print("\n--- TypeError példa ---")
try:
    result = "5" + 3                  # szöveget és számot NEM lehet összeadni
except TypeError:
    print("Hiba: Szöveget és számot nem lehet összeadni!")


# --- ValueError ---
# Amikor a típus jó, de az ÉRTÉK nem megfelelő.
# Olyan, mintha azt mondanád: "Hány éves vagy?" és a válasz: "alma".
# A válasz szöveg (az jó), de NEM alakítható számmá.

print("\n--- ValueError példa ---")
try:
    number = int("alma")              # az "alma" szöveget nem lehet számmá alakítani
except ValueError:
    print("Hiba: Az 'alma' nem szám, nem lehet int-té alakítani!")


# --- KeyError ---
# Amikor egy szótárban (dict) olyan kulcsot keresel, ami nem létezik.
# Olyan, mintha a telefonkönyvben keresnéd "Darth Vader" számát.

print("\n--- KeyError példa ---")
phone_book = {"Anna": "06301234567", "Béla": "06709876543"}  # telefonkönyv
try:
    number = phone_book["Darth Vader"]   # ilyen személy nincs a szótárban
except KeyError:
    print("Hiba: 'Darth Vader' nincs a telefonkönyvben!")


# --- IndexError ---
# Amikor egy lista olyan elemét kéred, ami nem létezik.
# Olyan, mintha 3 fős sorban a 10. embert keresnéd.

print("\n--- IndexError példa ---")
fruits = ["alma", "banán", "citrom"]  # 3 elemű lista (indexek: 0, 1, 2)
try:
    print(fruits[10])                 # a 10-es index nem létezik
except IndexError:
    print("Hiba: Nincs 10-es indexű elem a listában!")


# =============================================================
# 2. SZEKCIÓ: TRY/EXCEPT ALAPOK
# =============================================================

# A try/except a legfontosabb hibakezelő szerkezet.
#
# Gondolj rá így:
#   try    = "Próbáld meg ezt csinálni..."
#   except = "...és ha nem sikerül, csináld ezt helyette."
#   else   = "...de ha sikerült, csináld ezt is."
#   finally = "...és MINDENKÉPP csináld ezt, akár sikerült, akár nem."
#
# Hasonlat:
#   try:     Megpróbálom kinyitni az ajtót.
#   except:  Ha zárva van, becsöngetek.
#   else:    Ha nyitva volt, bemegyek.
#   finally: Akárhogy is, letörlöm a cipőm.

print("\n" + "=" * 50)
print("2. SZEKCIÓ: try/except alapok")
print("=" * 50)

# --- Alap try/except ---

print("\n--- Alap try/except ---")

try:                                  # próbáljuk meg...
    number = int("42")                # a "42" szöveget számmá alakítani
    print(f"Sikerült! A szám: {number}")  # ha sikerült, kiírjuk
except ValueError:                    # ha nem sikerült (mert nem szám volt)...
    print("Ez nem egy érvényes szám!")     # ...ezt írjuk ki helyette


# --- try/except/else ---
# Az "else" ág CSAK AKKOR fut le, ha NEM volt hiba.

print("\n--- try/except/else ---")

user_input = "25"                     # tegyük fel, ezt írta be a felhasználó

try:
    age = int(user_input)             # megpróbáljuk számmá alakítani
except ValueError:                    # ha nem sikerült...
    print("Kérlek számot írj be!")
else:                                 # ha SIKERÜLT (nem volt hiba)...
    print(f"A korod: {age} év")       # ...akkor használjuk a számot


# --- try/except/finally ---
# A "finally" ág MINDIG lefut, volt hiba vagy sem.
# Hasznos takarításra (fájl bezárás, kapcsolat lezárás stb.)

print("\n--- try/except/finally ---")

try:
    result = 100 / 5                  # ez most sikerülni fog (nem 0-val osztunk)
    print(f"Az eredmény: {result}")
except ZeroDivisionError:
    print("Nullával nem lehet osztani!")
finally:                              # ez MINDIG lefut
    print("A számítás befejeződött (akár sikerült, akár nem).")


# --- Teljes szerkezet egyben ---

print("\n--- Teljes try/except/else/finally ---")

user_input = "abc"                    # ez nem szám, szándékosan "rossz" input

try:
    number = int(user_input)          # megpróbáljuk számmá alakítani
except ValueError:                    # ha nem sikerült...
    print(f"'{user_input}' nem alakítható számmá!")
else:                                 # ha sikerült...
    print(f"A szám: {number}")
finally:                              # mindenképp lefut
    print("Feldolgozás kész.")


# =============================================================
# 3. SZEKCIÓ: KONKRÉT HIBATÍPUS ELKAPÁSA
# =============================================================

# Nagyon fontos szabály:
# SOHA ne írj sima "except:" -et (konkrét hibatípus nélkül)!
#
# Miért?
# Mert az MINDENT elkap — még azokat a hibákat is,
# amikről nem is tudsz. Elfedi a valódi problémát.
#
# Hasonlat:
#   Rossz: "Ha BÁRMI baj van, ne szólj semmit."
#          (Mi van ha leég a ház? Arról se szólsz?)
#
#   Jó:   "Ha NINCS TOJÁS, használj helyette banánt."
#          (Pontosan tudjuk, mire készülünk fel.)

print("\n" + "=" * 50)
print("3. SZEKCIÓ: Konkrét hibatípus elkapása")
print("=" * 50)

# --- ROSSZ PÉLDA (NE csináld így!) ---

print("\n--- ROSSZ: sima except (kerüld!) ---")

try:
    number = int("abc")
except:                               # <-- ROSSZ! Nem tudod, milyen hibát kapsz
    print("Valami hiba történt...")    # Semmitmondó üzenet, nem segít

# --- JÓ PÉLDA (így csináld!) ---

print("\n--- JÓ: konkrét except ---")

try:
    number = int("abc")
except ValueError:                    # <-- JÓ! Pontosan tudjuk, mire figyelünk
    print("ValueError: A megadott szöveg nem alakítható számmá!")

# Ha a hibaobjektumot is látni akarod (pl. naplózáshoz):

print("\n--- Hibaobjektum kiírása ---")

try:
    number = int("hello")
except ValueError as error:          # az "as error" elmenti a hiba részleteit
    print(f"Hiba típusa: ValueError")
    print(f"Hiba üzenete: {error}")   # kiírja: invalid literal for int()...


# =============================================================
# 4. SZEKCIÓ: TÖBB HIBATÍPUS KEZELÉSE
# =============================================================

# Néha egy kódrészletben többféle hiba is előfordulhat.
# Ilyenkor többféleképpen kezelheted:
#
# a) Külön-külön except ágakkal (ha máshogy kezeled őket)
# b) Egy except ágban összefogva (ha ugyanúgy kezeled őket)

print("\n" + "=" * 50)
print("4. SZEKCIÓ: Több hibatípus kezelése")
print("=" * 50)

# --- a) Külön-külön kezelés ---

print("\n--- Külön-külön except ágak ---")


def read_and_convert(file_name: str, index: int) -> str:
    """Egy fájlt olvas és a tartalmát számmá alakítja.

    Ez a függvény bemutatja, hogy egy műveletsor során
    többféle hiba is előfordulhat, és mindegyiket
    másképp kell kezelni.
    """
    # Szimulált fájltartalom (mintha fájlból olvasnánk)
    fake_files: dict[str, list[str]] = {
        "adatok.txt": ["42", "alma", "100"],
        "szamok.txt": ["10", "20", "30"],
    }

    try:
        file_content = fake_files[file_name]   # fájl "megnyitása" (szótárból)
        text_value = file_content[index]        # adott sor kiválasztása
        number = int(text_value)                # szöveget számmá alakítjuk
        return f"Siker! A szám: {number}"

    except KeyError:                           # ha a fájl nem létezik
        return f"Hiba: A '{file_name}' fájl nem található!"

    except IndexError:                         # ha az index túl nagy
        return f"Hiba: Nincs {index}. sor a fájlban!"

    except ValueError:                         # ha a szöveg nem szám
        return f"Hiba: A szöveg nem alakítható számmá!"


# Teszteljük a függvényt különböző esetekkel:
print(read_and_convert("adatok.txt", 0))       # Siker! A szám: 42
print(read_and_convert("nincs.txt", 0))         # KeyError - fájl nem létezik
print(read_and_convert("adatok.txt", 99))       # IndexError - túl nagy index
print(read_and_convert("adatok.txt", 1))        # ValueError - "alma" nem szám


# --- b) Összevont kezelés ---

print("\n--- Összevont except (több típus egyben) ---")

# Ha többféle hibát UGYANÚGY akarsz kezelni,
# zárójelben felsorolhatod őket:

user_data = "nem_szám"                         # rossz input

try:
    number = int(user_data)                    # ValueError lehet
    result = 100 / number                      # ZeroDivisionError lehet
except (ValueError, ZeroDivisionError) as error:  # mindkettőt ugyanúgy kezeljük
    print(f"Hiba történt: {error}")


# =============================================================
# 5. SZEKCIÓ: SAJÁT HIBAÜZENETEK (raise)
# =============================================================

# Eddig a Python dobta a hibákat, mi meg elkaptuk őket.
# De TE IS DOBHATSZ hibát a "raise" kulcsszóval!
#
# Mikor érdemes?
# Amikor TE tudod, hogy valami nem stimmel,
# és meg akarod mondani a felhasználónak, MI a baj.
#
# Hasonlat:
#   A Python azt mondaná: "ValueError" (semmitmondó)
#   TE azt mondod: "Az ár nem lehet negatív!" (segítőkész)
#
# Olyan, mintha a boltos NEM csak annyit mondana, hogy
# "Hiba a fizetésnél", hanem: "A kártyád lejárt!"

print("\n" + "=" * 50)
print("5. SZEKCIÓ: Saját hibaüzenetek (raise)")
print("=" * 50)


def set_age(age: int) -> str:
    """Beállítja egy felhasználó korát, de ellenőrzi az értéket.

    A kor nem lehet negatív és nem lehet irreálisan nagy.
    Ha rossz értéket kap, saját hibaüzenetet dob.
    """
    if age < 0:                                # negatív kor nincs
        raise ValueError("A kor nem lehet negatív szám!")  # MI dobjuk a hibát
    if age > 150:                              # 150 évnél idősebb ember nincs
        raise ValueError("A kor nem lehet 150-nél nagyobb!")
    return f"Kor beállítva: {age} év"


# Teszteljük:
print("\n--- Saját hiba dobása ---")

# Jó eset:
try:
    print(set_age(25))                         # 25 éves - ez rendben van
except ValueError as error:
    print(f"Hiba: {error}")

# Rossz eset - negatív:
try:
    print(set_age(-5))                         # -5 éves - nem létezik
except ValueError as error:
    print(f"Hiba: {error}")                    # "A kor nem lehet negatív szám!"

# Rossz eset - túl nagy:
try:
    print(set_age(200))                        # 200 éves - irreális
except ValueError as error:
    print(f"Hiba: {error}")                    # "A kor nem lehet 150-nél nagyobb!"


# --- Még egy példa: termék ár ellenőrzés ---

print("\n--- Termék ár ellenőrzés ---")


def set_product_price(name: str, price: int) -> str:
    """Beállítja egy termék árát.

    Az ár nem lehet negatív és nem lehet nulla,
    mert ingyen nem adunk el semmit.
    """
    if not isinstance(price, (int, float)):    # ellenőrizzük, hogy szám-e
        raise TypeError("Az ár csak szám lehet!")
    if price < 0:                              # negatív ár nincs
        raise ValueError("Az ár nem lehet negatív!")
    if price == 0:                             # nulla ár sincs
        raise ValueError("Az ár nem lehet nulla — ingyen nem adunk el semmit!")
    return f"'{name}' ára beállítva: {price} Ft"


# Teszteljük:
try:
    print(set_product_price("Laptop", 250000))   # rendben van
except (TypeError, ValueError) as error:
    print(f"Hiba: {error}")

try:
    print(set_product_price("Egér", -500))       # negatív ár
except (TypeError, ValueError) as error:
    print(f"Hiba: {error}")

try:
    print(set_product_price("Pendrive", 0))      # nulla ár
except (TypeError, ValueError) as error:
    print(f"Hiba: {error}")


# =============================================================
# 6. SZEKCIÓ: ÖSSZEFOGLALÓ
# =============================================================

print("\n" + "=" * 50)
print("6. SZEKCIÓ: Összefoglaló")
print("=" * 50)

print("""
MIKOR HASZNÁLJ try/except-et:
  1. Felhasználói input feldolgozásakor (mert a user bármit beírhat)
  2. Fájl műveletekkor (mert a fájl lehet hogy nem létezik)
  3. Hálózati műveleteknél (mert az internet kiszámíthatatlan)
  4. Szótár/lista elérésekor (ha nem biztos, hogy létezik a kulcs/index)

MIKOR NE HASZNÁLJ try/except-et:
  1. Simán ellenőrizhető dolgokra — használj if/else-t helyette!
     Rossz:  try: x = lista[5]  except: ...
     Jó:     if len(lista) > 5: x = lista[5]
  2. Ne kapj el MINDEN hibát — csak amiket vársz!
  3. Ne használd programlogika helyett (try/except nem if/else!)

ARANYSZABÁLYOK:
  - Mindig KONKRÉT hibatípust kapj el (except ValueError, NE except:)
  - A try blokkba CSAK azt a kódot tedd, ami hibázhat
  - Adj ÉRTELMES hibaüzenetet, ne csak annyit hogy "hiba történt"
  - Ha TE tudod hogy valami nem stimmel, használj raise-t
""")

print("Gratulálok! Most már tudod, hogyan kezeld a hibákat Python-ban!")
print("Következő lépés: próbáld ki a gyakorló feladatokat!")
print("Fájl: exercise_05_hibakezelés.py")

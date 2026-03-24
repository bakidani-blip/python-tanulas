"""
1.1 Feladat: Változók és elnevezések

Javítsd ki az összes változó-, függvény- és osztálynevet a Python konvenciók szerint:
- Változók és függvények: snake_case
- Konstansok: UPPER_SNAKE_CASE
- Osztályok: PascalCase
- Használj beszédes, értelmes neveket

A kód logikáját NE változtasd, csak a neveket!
"""

# --- Konstansok ---
maxretries = 3
apiurl = "https://api.example.com"
t = 30  # timeout másodpercben


# --- Függvények ---
def calcTtl(lst):
    """Kiszámítja a lista elemeinek összegét."""
    r = 0
    for x in lst:
        r = r + x
    return r


def chkUsr(n, a):
    """Ellenőrzi, hogy a felhasználó érvényes-e."""
    if len(n) < 2:
        return False
    if a < 0 or a > 150:
        return False
    return True


def FetchData(ApiUrl, maxretries):
    """Adatokat tölt le egy API-ról, újrapróbálkozással."""
    for I in range(maxretries):
        print(f"Próbálkozás {I + 1}...")
        # Szimuláljuk a letöltést
        Data = {"status": "ok", "items": [1, 2, 3]}
        if Data["status"] == "ok":
            return Data
    return None


# --- Osztály ---
class usraccount:
    def __init__(self, N, E, a):
        self.N = N  # név
        self.E = E  # email
        self.a = a  # aktív-e

    def getFullInfo(self):
        s = "aktív" if self.a else "inaktív"
        return f"{self.N} ({self.E}) - {s}"

    def deactivateaccount(self):
        self.a = False


# --- Használat ---
if __name__ == "__main__":
    u = usraccount("Kiss Péter", "peter@example.com", True)
    print(u.getFullInfo())

    nums = [10, 20, 30, 40]
    t2 = calcTtl(nums)
    print(f"Összeg: {t2}")

    ok = chkUsr("Anna", 25)
    print(f"Érvényes felhasználó: {ok}")

    d = FetchData(apiurl, maxretries)
    print(f"Letöltött adat: {d}")

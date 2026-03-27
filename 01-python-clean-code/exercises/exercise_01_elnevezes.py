"""
=============================================================
1.1 GYAKORLAT: Változók és elnevezések — Clean Code
=============================================================
"""

# @TASK 1. Változók átnevezése
# @DESC Az alábbi változóknak **rossz a nevük**. Nevezd át őket értelmes, `snake_case` nevekre!
# Az értéküket **NE változtasd**, csak a nevet! Gondolj bele: mit TÁROL a változó?
# @HINT Példa: `n` → `user_name`, `x` → `user_age`, `c` → `user_city`
# @CODE
# Nevezd át ezeket értelmes nevekre:
n = "Kiss Peter"           # ez egy személy neve
x = 42                     # ez egy életkor
c = "Budapest"             # ez egy város

# Írasd ki az új nevű változókat:
# MEGOLDÁS IDE:

# @END

# @TASK 2. Konstansok
# @DESC Az alábbi értékek **SOHA nem változnak** — konstansok.
# Nevezd át őket **UPPER_SNAKE_CASE** konvenció szerint!
# @HINT Példa: `mr` → `MAX_RETRIES`, `tax` → `TAX_RATE`
# @CODE
# Nevezd át UPPER_SNAKE_CASE-re:
mr = 5                     # max próbálkozások száma
tax = 0.27                 # adókulcs
url = "https://api.example.com/v2"  # API webcím

# Írasd ki mindet:
# MEGOLDÁS IDE:

# @END

# @TASK 3. Boolean változók
# @DESC Boolean változók neve mindig **kérdés** legyen: `is_`, `has_`, `can_` előtaggal.
# Nevezd át az alábbiakat!
# @HINT Példa: `active` → `is_active`, `admin` → `is_admin`
# @CODE
# Nevezd át is_/has_/can_ előtaggal:
active = True               # aktív-e a felhasználó?
admin = False               # adminisztrátor-e?
logged = True               # be van-e jelentkezve?
items = False               # van-e termék a kosarában?

# Írasd ki mindet:
# MEGOLDÁS IDE:

# @END

# @TASK 4. Függvény átnevezése
# @DESC Az alábbi függvénynek rossz a neve ÉS a paramétereinek neve is.
# A függvény egy **téglalap területét** számolja ki (szélesség * magasság).
# Nevezd át a függvényt és a paramétereit is!
# @HINT Függvénynevek igével kezdődnek: `calculate_area(width, height)`
# @CODE
# Nevezd át a függvényt és a paramétereit:
def calc(a, b):
    return a * b

# Teszteld az új nevű függvényt:
# MEGOLDÁS IDE:

# @END

# @TASK 5. Vegyes — teljes kód átírás
# @DESC Az alábbi kód egy vásárlást számol ki. **MINDEN elnevezés rossz** benne.
# Írd át az ÖSSZES nevet — változót, konstanst, függvényt! A **logika** maradjon!
# @HINT `t` → `TAX_RATE`, `f` → `calculate_total_price(net_price, quantity)`
# @CODE
t = 0.27

def f(p, q):
    s = p * q
    a = s * t
    return s + a

# MEGOLDÁS IDE — írd újra az egészet jó nevekkel:


# Teszteld: calculate_total_price(1000, 3) = 3810.0
# @END

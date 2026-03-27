"""
=============================================================
1.1 GYAKORLAT: Valtozok es elnevezesek — Clean Code
=============================================================
"""

# @TASK 1. Valtozok atnevezese
# @DESC Az alabbi valtozoknak **rossz a nevuk**. Nevezd at oket ertelmes, `snake_case` nevekre!
# Az ertekuket **NE valtoztasd**, csak a nevet! Gondolj bele: mit TAROL a valtozo?
# @HINT Pelda: `n` → `user_name`, `x` → `user_age`, `c` → `user_city`
# @CODE
# Nevezd at ezeket ertelmes nevekre:
n = "Kiss Peter"           # ez egy szemely neve
x = 42                     # ez egy eletkor
c = "Budapest"             # ez egy varos

# Irasd ki az uj nevu valtozokat:
# MEGOLDAS IDE:

# @END

# @TASK 2. Konstansok
# @DESC Az alabbi ertekek **SOHA nem valtoznak** — konstansok.
# Nevezd at oket **UPPER_SNAKE_CASE** konvencio szerint!
# @HINT Pelda: `mr` → `MAX_RETRIES`, `tax` → `TAX_RATE`
# @CODE
# Nevezd at UPPER_SNAKE_CASE-re:
mr = 5                     # max probalkozasok szama
tax = 0.27                 # adokulcs
url = "https://api.example.com/v2"  # API webcim

# Irasd ki mindet:
# MEGOLDAS IDE:

# @END

# @TASK 3. Boolean valtozok
# @DESC Boolean valtozok neve mindig **kerdes** legyen: `is_`, `has_`, `can_` elotaggal.
# Nevezd at az alabbiakat!
# @HINT Pelda: `active` → `is_active`, `admin` → `is_admin`
# @CODE
# Nevezd at is_/has_/can_ elotaggal:
active = True               # aktiv-e a felhasznalo?
admin = False               # adminisztrator-e?
logged = True               # be van-e jelentkezve?
items = False               # van-e termek a kosaraban?

# Irasd ki mindet:
# MEGOLDAS IDE:

# @END

# @TASK 4. Fuggveny atnevezese
# @DESC Az alabbi fuggvenynek rossz a neve ES a parametereinek neve is.
# A fuggveny egy **teglalap teruletet** szamolja ki (szelesseg * magassag).
# Nevezd at a fuggvenyt es a parametereit is!
# @HINT Fuggvenynevek igevel kezdodnek: `calculate_area(width, height)`
# @CODE
# Nevezd at a fuggvenyt es a parametereit:
def calc(a, b):
    return a * b

# Teszteld az uj nevu fuggvenyt:
# MEGOLDAS IDE:

# @END

# @TASK 5. Vegyes — teljes kod atiras
# @DESC Az alabbi kod egy vasarlast szamol ki. **MINDEN elnevezes rossz** benne.
# Ird at az OSSZES nevet — valtozot, konstanst, fuggvenyt! A **logika** maradjon!
# @HINT `t` → `TAX_RATE`, `f` → `calculate_total_price(net_price, quantity)`
# @CODE
t = 0.27

def f(p, q):
    s = p * q
    a = s * t
    return s + a

# MEGOLDAS IDE — ird ujra az egeszet jo nevekkel:


# Teszteld: calculate_total_price(1000, 3) = 3810.0
# @END

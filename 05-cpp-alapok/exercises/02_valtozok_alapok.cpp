/*
=============================================================
2. LECKE: Változók és típusok — adatok tárolása C++-ban
Futtasd: a böngészőben a Futtatás gombbal
=============================================================
*/

#include <iostream>
#include <string>
using namespace std;

// ============================================================
// MI AZ A VÁLTOZÓ?
// ============================================================

// A változó olyan, mint egy **címkézett doboz**.
// Beleteszel valamit (egy számot, szöveget), és később
// a címke (a név) alapján előkeresheted.
//
// Pythonban csak írtad: `age = 25` és kész.
// C++-ban meg kell mondanod a **típust** is:
//
//   int age = 25;
//   ^   ^     ^
//   |   |     +-- érték (mit teszel a dobozba)
//   |   +-------- név (a címke a dobozon)
//   +------------ típus (milyen doboz — számnak? szövegnek?)
//
// Miért kell típus? Mert a gép így tudja, mennyi helyet
// foglaljon a memóriában és hogyan kezelje az adatot.

// ============================================================
// EGÉSZ SZÁMOK: int
// ============================================================

// Az `int` (integer = egész szám) a leggyakoribb típusok egyike.
// Egész számokat tárol: 0, 1, -5, 42, 1000000

int main() {
    int age = 25;
    int score = 100;
    int temperature = -3;

    cout << "Kor: " << age << endl;
    cout << "Pontszám: " << score << endl;
    cout << "Hőmérséklet: " << temperature << " fok" << endl;

    // Számolás változókkal — ugyanúgy mint matek:
    int sum = age + score;
    cout << "Összeg: " << sum << endl;

    // ============================================================
    // TÖRTEK: double
    // ============================================================

    // Ha tizedesjegyekre van szükséged, használj `double`-t.
    // (Van `float` is, de a `double` pontosabb — használd azt.)

    double pi = 3.14159;
    double price = 990.5;
    double height = 1.75;

    cout << endl;
    cout << "Pi: " << pi << endl;
    cout << "Ár: " << price << " Ft" << endl;
    cout << "Magasság: " << height << " m" << endl;

    // **VIGYÁZZ**: int / int = int (levágja a törtet!)
    int a = 7;
    int b = 2;
    cout << endl;
    cout << "7 / 2 int-tel: " << a / b << endl;         // 3 (nem 3.5!)
    cout << "7.0 / 2 double-lel: " << 7.0 / 2 << endl;  // 3.5 (ez a helyes)

    // ============================================================
    // SZÖVEG: string
    // ============================================================

    // Szöveget a `string` típussal tárolunk.
    // Ehhez kell a `#include <string>` a fájl elején.

    string name = "Kata";
    string city = "Budapest";

    cout << endl;
    cout << "Név: " << name << endl;
    cout << "Város: " << city << endl;

    // Szövegek összefűzése a `+` operátorral:
    string greeting = "Hello, " + name + "!";
    cout << greeting << endl;

    // ============================================================
    // EGYETLEN KARAKTER: char
    // ============================================================

    // A `char` egyetlen karaktert tárol. Aposztróftal adjuk meg!
    // (Nem idézőjellel — az a string!)

    char grade = 'A';
    char initial = 'K';

    cout << endl;
    cout << "Jegy: " << grade << endl;
    cout << "Kezdőbetű: " << initial << endl;

    // ============================================================
    // IGAZ/HAMIS: bool
    // ============================================================

    // A `bool` (boolean) csak két értéket vehet fel: true vagy false.
    // Olyan, mint egy villanykapcsoló: be vagy ki.

    bool is_student = true;
    bool has_license = false;

    cout << endl;
    cout << "Diák? " << is_student << endl;       // 1 = true
    cout << "Van jogsi? " << has_license << endl;  // 0 = false

    // Megjegyzés: C++-ban a true = 1, false = 0 jelenik meg.
    // Ha "true"/"false" szöveget akarsz, használj feltételt (következő lecke).

    // ============================================================
    // KONSTANSOK: const
    // ============================================================

    // Ha egy érték SOHA nem változik, tedd elé a `const` szót.
    // Ez megvédi a véletlenszerű felülírástól.

    const double GRAVITY = 9.81;
    const int MAX_PLAYERS = 4;

    cout << endl;
    cout << "Gravitáció: " << GRAVITY << " m/s2" << endl;
    cout << "Max játékos: " << MAX_PLAYERS << endl;

    // Ha megpróbálnád megváltoztatni, fordítási hibát kapnál:
    // GRAVITY = 10.0;  // HIBA! const-ot nem lehet módosítani!

    // ============================================================
    // ÖSSZEFOGLALÁS
    // ============================================================

    // Típusok amit ma megtanultál:
    //
    // | Típus    | Mire jó           | Példa              |
    // |----------|-------------------|--------------------|
    // | int      | Egész számok      | int age = 25;      |
    // | double   | Törtek/tizedesek  | double pi = 3.14;  |
    // | string   | Szöveg            | string s = "Hello";|
    // | char     | Egy karakter      | char c = 'A';      |
    // | bool     | Igaz/hamis        | bool ok = true;    |
    // | const    | Változhatatlan    | const int X = 10;  |
    //
    // A következő leckében feltételek jönnek: if, else, switch!

    return 0;
}

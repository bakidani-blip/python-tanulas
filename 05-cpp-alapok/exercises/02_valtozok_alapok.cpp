/*
=============================================================
2. LECKE: Valtozok es tipusok — adatok tarolasa C++-ban
Futtasd: a bongeszoben a Futtatas gombbal
=============================================================
*/

#include <iostream>
#include <string>
using namespace std;

// ============================================================
// MI AZ A VALTOZO?
// ============================================================

// A valtozo olyan, mint egy **cimkezett doboz**.
// Beleteszel valamit (egy szamot, szoveget), es kesobb
// a cimke (a nev) alapjan elokeresheted.
//
// Pythonban csak irtad: `age = 25` es kesz.
// C++-ban meg kell mondanod a **tipust** is:
//
//   int age = 25;
//   ^   ^     ^
//   |   |     +-- ertek (mit teszel a dobozba)
//   |   +-------- nev (a cimke a dobozon)
//   +------------ tipus (milyen doboz — szamnak? szovegnek?)
//
// Miert kell tipus? Mert a gep igy tudja, mennyi helyet
// foglaljon a memoriaban es hogyan kezelje az adatot.

// ============================================================
// EGESZ SZAMOK: int
// ============================================================

// Az `int` (integer = egesz szam) a leggyakoribb tipusok egyike.
// Egesz szamokat tarol: 0, 1, -5, 42, 1000000

int main() {
    int age = 25;
    int score = 100;
    int temperature = -3;

    cout << "Kor: " << age << endl;
    cout << "Pontszam: " << score << endl;
    cout << "Homerseklet: " << temperature << " fok" << endl;

    // Szamolas valtozokkal — ugyanugy mint matek:
    int sum = age + score;
    cout << "Osszeg: " << sum << endl;

    // ============================================================
    // TORTEK: double
    // ============================================================

    // Ha tizedesjegyekre van szukseged, hasznalj `double`-t.
    // (Van `float` is, de a `double` pontosabb — hasznald azt.)

    double pi = 3.14159;
    double price = 990.5;
    double height = 1.75;

    cout << endl;
    cout << "Pi: " << pi << endl;
    cout << "Ar: " << price << " Ft" << endl;
    cout << "Magassag: " << height << " m" << endl;

    // **VIGYAZZ**: int / int = int (levagja a tortet!)
    int a = 7;
    int b = 2;
    cout << endl;
    cout << "7 / 2 int-tel: " << a / b << endl;         // 3 (nem 3.5!)
    cout << "7.0 / 2 double-lel: " << 7.0 / 2 << endl;  // 3.5 (ez a helyes)

    // ============================================================
    // SZOVEG: string
    // ============================================================

    // Szoveget a `string` tipussal tarolunk.
    // Ehhez kell a `#include <string>` a fajl elejen.

    string name = "Kata";
    string city = "Budapest";

    cout << endl;
    cout << "Nev: " << name << endl;
    cout << "Varos: " << city << endl;

    // Szovegek osszefuzese a `+` operatorral:
    string greeting = "Hello, " + name + "!";
    cout << greeting << endl;

    // ============================================================
    // EGYETLEN KARAKTER: char
    // ============================================================

    // A `char` egyetlen karaktert tarol. Aposztroffal adjuk meg!
    // (Nem idezojellel — az a string!)

    char grade = 'A';
    char initial = 'K';

    cout << endl;
    cout << "Jegy: " << grade << endl;
    cout << "Kezdobetu: " << initial << endl;

    // ============================================================
    // IGAZ/HAMIS: bool
    // ============================================================

    // A `bool` (boolean) csak ket erteket vehet fel: true vagy false.
    // Olyan, mint egy villanykapcsolo: be vagy ki.

    bool is_student = true;
    bool has_license = false;

    cout << endl;
    cout << "Diak? " << is_student << endl;       // 1 = true
    cout << "Van jogsi? " << has_license << endl;  // 0 = false

    // Megjegyzes: C++-ban a true = 1, false = 0 jelenik meg.
    // Ha "true"/"false" szoveget akarsz, hasznalj feltetelt (kovetkezo lecke).

    // ============================================================
    // KONSTANSOK: const
    // ============================================================

    // Ha egy ertek SOHA nem valtozik, tedd ele a `const` szot.
    // Ez megvedi a veletlenszeru felulirástol.

    const double GRAVITY = 9.81;
    const int MAX_PLAYERS = 4;

    cout << endl;
    cout << "Gravitacio: " << GRAVITY << " m/s2" << endl;
    cout << "Max jatekos: " << MAX_PLAYERS << endl;

    // Ha megprobalnad megvaltoztatni, fordítasi hibat kapnal:
    // GRAVITY = 10.0;  // HIBA! const-ot nem lehet modositani!

    // ============================================================
    // OSSZEFOGLALAS
    // ============================================================

    // Tipusok amit ma megtanultal:
    //
    // | Tipus    | Mire jo           | Pelda              |
    // |----------|-------------------|--------------------|
    // | int      | Egesz szamok      | int age = 25;      |
    // | double   | Tortek/tizedesek  | double pi = 3.14;  |
    // | string   | Szoveg            | string s = "Hello";|
    // | char     | Egy karakter      | char c = 'A';      |
    // | bool     | Igaz/hamis        | bool ok = true;    |
    // | const    | Valtozhatatlan    | const int X = 10;  |
    //
    // A kovetkezo leckeben feltetelek jonnek: if, else, switch!

    return 0;
}

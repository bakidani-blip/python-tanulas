/*
=============================================================
5. LECKE: Függvények — saját parancsok készítése
Futtasd: a böngészőben a Futtatás gombbal
=============================================================
*/

#include <iostream>
#include <string>
using namespace std;

// ============================================================
// MI AZ A FÜGGVÉNY?
// ============================================================

// Képzeld el, hogy van egy receptkönyved.
// Minden recept egy "függvény": megmondja,
// MIT kell csinálni, MIBŐL (alapanyagok), és MI lesz az eredmény.
//
// Programozásban ugyanez:
//   - A függvény egy NEVET kap (pl. "add" = összeadás)
//   - Kap BEMENETEKET (paraméter = alapanyagok)
//   - Ad egy EREDMÉNYT (visszatérési érték = a kész étel)
//
// Miért jó?
//   1. Nem kell újra és újra megírni ugyanazt a kódot
//   2. A program áttekinthetőbb, rendezettebb
//   3. Ha hiba van, csak egy helyen kell javítani

// ============================================================
// 1. LEGEGYSZERŰBB FÜGGVÉNY — nincs bemenet, nincs kimenet
// ============================================================

// A `void` szó azt jelenti: "nem ad vissza semmit".
// Ez a függvény csak kiír valamit, de nem számol eredményt.

void say_hello() {
    cout << "Hello! Üdv a C++ függvények leckében!" << endl;
}

// A függvényt DEFINIÁLOD (megírod, mint fent),
// majd MEGHÍVOD (használod, mint lent a main()-ben).
// A definíciót a main() ELÉ kell írni C++-ban!

// ============================================================
// 2. FÜGGVÉNY PARAMÉTERREL — bemenet
// ============================================================

// A paraméterek a zárójelben vannak.
// Ezek a függvény "alapanyagai" — amit kap, azzal dolgozik.

void greet(string name) {
    // A `name` változó azt az értéket veszi fel, amit meghíváskor adsz.
    cout << "Szia, " << name << "! Örülök, hogy itt vagy!" << endl;
}

// Több paraméter is lehet, vesszővel elválasztva:

void introduce(string name, int age) {
    cout << name << " vagyok, " << age << " éves." << endl;
}

// ============================================================
// 3. FÜGGVÉNY VISSZATÉRÉSI ÉRTÉKKEL — kimenet
// ============================================================

// Ha a függvény SZÁMOL valamit, visszaadja az eredményt.
// Ilyenkor a `void` helyett a visszatérési érték TÍPUSÁT írjuk.

int add(int a, int b) {
    // A `return` szó küldi vissza az eredményt
    return a + b;
}

// A függvény típusa megmondja, MIT ad vissza:
//   int add(...)    → egész számot ad vissza
//   double area(...) → törtet ad vissza
//   string greet(...) → szöveget ad vissza
//   void print_stuff(...) → semmit nem ad vissza

double calculate_average(int a, int b, int c) {
    // Figyelem: int / int = int! Ezért 3.0-val osztunk (double)
    double avg = (a + b + c) / 3.0;
    return avg;
}

// ============================================================
// 4. FÜGGVÉNY BOOL VISSZATÉRÉSSEL — igen/nem válasz
// ============================================================

// Nagyon hasznos, ha a függvény egy KÉRDÉST válaszol meg:
// "Igaz ez?" → true/false

bool is_adult(int age) {
    return age >= 18;
    // Ha age >= 18, visszaad true-t, különben false-t
}

bool is_even(int number) {
    return number % 2 == 0;
}

// ============================================================
// 5. FÜGGVÉNYEK HASZNÁLATA EGYMÁSBAN
// ============================================================

// Függvények hívhatnak MÁS függvényeket!
// Ez a programozás igazi ereje.

int square(int n) {
    return n * n;
}

int sum_of_squares(int a, int b) {
    // Felhasználjuk a `square` függvényt!
    return square(a) + square(b);
}

// ============================================================
// MAIN — itt hívjuk meg a függvényeket
// ============================================================

int main() {

    // ============================================================
    // Függvények meghívása
    // ============================================================

    // 1. Egyszerű meghívás (void, nincs paraméter)
    say_hello();

    cout << endl;

    // 2. Paraméterrel
    greet("Kata");
    greet("Péter");
    introduce("Anna", 15);

    cout << endl;

    // 3. Visszatérési értékkel — az eredményt elmentjük változóba
    int result = add(10, 25);
    cout << "10 + 25 = " << result << endl;

    // Vagy közvetlenül használhatjuk:
    cout << "3 + 7 = " << add(3, 7) << endl;

    double avg = calculate_average(80, 90, 70);
    cout << "Átlag: " << avg << endl;

    cout << endl;

    // 4. Bool függvények — döntésekhez
    int my_age = 16;
    if (is_adult(my_age)) {
        cout << my_age << " éves: felnőtt" << endl;
    } else {
        cout << my_age << " éves: még nem felnőtt" << endl;
    }

    cout << "7 páros? " << is_even(7) << endl;   // 0 = false
    cout << "12 páros? " << is_even(12) << endl;  // 1 = true

    cout << endl;

    // 5. Függvények egymásban
    cout << "3 négyzete: " << square(3) << endl;
    cout << "3^2 + 4^2 = " << sum_of_squares(3, 4) << endl;  // 9 + 16 = 25

    // ============================================================
    // ÖSSZEFOGLALÁS
    // ============================================================

    // | Típus          | Példa                           | Mit csinál             |
    // |----------------|---------------------------------|------------------------|
    // | void           | void greet() { ... }            | Nem ad vissza semmit   |
    // | int/double/... | int add(int a, int b) { ... }   | Visszaad egy értéket   |
    // | bool           | bool is_even(int n) { ... }     | Igaz/hamis választ ad  |
    //
    // Fontos szabályok:
    // - Függvényt a main() ELÉ kell írni (vagy deklarálni)
    // - A `return` VISSZAKÜLDI az eredményt és KILÉP a függvényből
    // - A paraméterek típusát meg kell adni: int a, string name
    // - Adj a függvénynek ÉRTELMES nevet: `calculate_area`, nem `f1`
    //
    // Gratulálok! Ezzel elvégezted a C++ alapok 5 leckéjét!
    // Most már ismered: változók, feltételek, ciklusok, függvények.

    return 0;
}

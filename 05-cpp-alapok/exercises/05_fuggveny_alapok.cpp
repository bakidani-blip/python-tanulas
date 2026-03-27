/*
=============================================================
5. LECKE: Fuggvenyek — sajat parancsok keszitese
Futtasd: a bongeszoben a Futtatas gombbal
=============================================================
*/

#include <iostream>
#include <string>
using namespace std;

// ============================================================
// MI AZ A FUGGVENY?
// ============================================================

// Kepzeld el, hogy van egy receptkonyved.
// Minden recept egy "fuggveny": megmondja,
// MIT kell csinalni, MIBOL (alapanyagok), es MI lesz az eredmeny.
//
// Programozasban ugyanez:
//   - A fuggveny egy NEVET kap (pl. "add" = osszeadas)
//   - Kap BEMENETEKET (parameter = alapanyagok)
//   - Ad egy EREDMENYT (visszateresi ertek = a kész etel)
//
// Miert jo?
//   1. Nem kell ujra es ujra megirni ugyanazt a kodot
//   2. A program attekinthetobb, rendezettebb
//   3. Ha hiba van, csak egy helyen kell javitani

// ============================================================
// 1. LEGEGYSZERÜBB FUGGVENY — nincs bemenet, nincs kimenet
// ============================================================

// A `void` szo azt jelenti: "nem ad vissza semmit".
// Ez a fuggveny csak kiir valamit, de nem szamol eredmenyt.

void say_hello() {
    cout << "Hello! Udv a C++ fuggvenyek leckeben!" << endl;
}

// A fuggvenyt DEFINIALOD (megírod, mint fent),
// majd MEGHIVOD (használod, mint lent a main()-ben).
// A definiciót a main() ELÉ kell irni C++-ban!

// ============================================================
// 2. FUGGVENY PARAMETERREL — bemenet
// ============================================================

// A parameterek a zarojelben vannak.
// Ezek a fuggveny "alapanyagai" — amit kap, azzal dolgozik.

void greet(string name) {
    // A `name` valtozo azt az erteket veszi fel, amit meghivaskor adsz.
    cout << "Szia, " << name << "! Orulok, hogy itt vagy!" << endl;
}

// Tobb parameter is lehet, vesszoval elvalasztva:

void introduce(string name, int age) {
    cout << name << " vagyok, " << age << " eves." << endl;
}

// ============================================================
// 3. FUGGVENY VISSZATERESI ERTEKKEL — kimenet
// ============================================================

// Ha a fuggveny SZAMOL valamit, visszaadja az eredmenyt.
// Ilyenkor a `void` helyett a visszateresi ertek TIPUSAT irjuk.

int add(int a, int b) {
    // A `return` szo kuldi vissza az eredmenyt
    return a + b;
}

// A fuggveny tipusa megmondja, MIT ad vissza:
//   int add(...)    → egesz szamot ad vissza
//   double area(...) → tortet ad vissza
//   string greet(...) → szoveget ad vissza
//   void print_stuff(...) → semmit nem ad vissza

double calculate_average(int a, int b, int c) {
    // Figyelem: int / int = int! Ezert 3.0-val osztunk (double)
    double avg = (a + b + c) / 3.0;
    return avg;
}

// ============================================================
// 4. FUGGVENY BOOL VISSZATERESSEL — igen/nem valasz
// ============================================================

// Nagyon hasznos, ha a fuggveny egy KERDEST valaszol meg:
// "Igaz ez?" → true/false

bool is_adult(int age) {
    return age >= 18;
    // Ha age >= 18, visszaad true-t, kulonben false-t
}

bool is_even(int number) {
    return number % 2 == 0;
}

// ============================================================
// 5. FUGGVENYEK HASZNALATA EGYMASBAN
// ============================================================

// Fuggvenyek hivhatnak MAS fuggvenyeket!
// Ez a programozas igazi ereje.

int square(int n) {
    return n * n;
}

int sum_of_squares(int a, int b) {
    // Felhasznaljuk a `square` fuggvenyt!
    return square(a) + square(b);
}

// ============================================================
// MAIN — itt hivjuk meg a fuggvenyeket
// ============================================================

int main() {

    // ============================================================
    // Fuggvenyek meghivasa
    // ============================================================

    // 1. Egyszerü meghivas (void, nincs parameter)
    say_hello();

    cout << endl;

    // 2. Parameterrel
    greet("Kata");
    greet("Peter");
    introduce("Anna", 15);

    cout << endl;

    // 3. Visszateresi ertekkel — az eredmenyt elmentjuk valtozoba
    int result = add(10, 25);
    cout << "10 + 25 = " << result << endl;

    // Vagy kozvetlenul hasznalhatjuk:
    cout << "3 + 7 = " << add(3, 7) << endl;

    double avg = calculate_average(80, 90, 70);
    cout << "Atlag: " << avg << endl;

    cout << endl;

    // 4. Bool fuggvenyek — dontesekhez
    int my_age = 16;
    if (is_adult(my_age)) {
        cout << my_age << " eves: felnoett" << endl;
    } else {
        cout << my_age << " eves: meg nem felnoett" << endl;
    }

    cout << "7 paros? " << is_even(7) << endl;   // 0 = false
    cout << "12 paros? " << is_even(12) << endl;  // 1 = true

    cout << endl;

    // 5. Fuggvenyek egymasban
    cout << "3 negyzete: " << square(3) << endl;
    cout << "3^2 + 4^2 = " << sum_of_squares(3, 4) << endl;  // 9 + 16 = 25

    // ============================================================
    // OSSZEFOGLALAS
    // ============================================================

    // | Tipus          | Pelda                           | Mit csinal             |
    // |----------------|---------------------------------|------------------------|
    // | void           | void greet() { ... }            | Nem ad vissza semmit   |
    // | int/double/... | int add(int a, int b) { ... }   | Visszaad egy erteket   |
    // | bool           | bool is_even(int n) { ... }     | Igaz/hamis valaszt ad  |
    //
    // Fontos szabalyok:
    // - Fuggvenyt a main() ELE kell irni (vagy deklaralni)
    // - A `return` VISSZAKULDI az eredmenyt es KILEP a fuggvenybol
    // - A parameterek tipusat meg kell adni: int a, string name
    // - Adj a fuggvenynek ERTELMES nevet: `calculate_area`, nem `f1`
    //
    // Gratulalok! Ezzel elvegezted a C++ alapok 5 leckéjét!
    // Most mar ismered: valtozok, feltetelek, ciklusok, fuggvenyek.

    return 0;
}

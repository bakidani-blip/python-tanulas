/*
=============================================================
GYAKORLO FELADATOK — C++ fuggvenyek
Ird meg a megoldasokat a MEGOLDAS IDE reszekhez!
Futtasd a Futtatas gombbal az ellenorzeshez.
=============================================================
*/

#include <iostream>
#include <string>
using namespace std;

// ============================================================
// 1. feladat: Teglalap terulete
//
// Irj egy fuggvenyt `rectangle_area` neven, ami:
//   - Kap ket int parametert: `width` (szelesseg) es `height` (magassag)
//   - Visszaadja a teruletüket (szelesseg * magassag) int-kent
//
// Pelda: rectangle_area(5, 3) → 15
// Tipp: int rectangle_area(int width, int height) { return ...; }
// ============================================================

// MEGOLDAS IDE:


// ============================================================
// 2. feladat: Nagyobb szam
//
// Irj egy fuggvenyt `bigger` neven, ami:
//   - Kap ket int parametert: `a` es `b`
//   - Visszaadja a NAGYOBBAT a ketto kozul
//
// Pelda: bigger(10, 7) → 10
// Tipp: hasznalj if-else-t a fuggvenyen belul!
// ============================================================

// MEGOLDAS IDE:


// ============================================================
// 3. feladat: Udvozlo uzenet
//
// Irj egy fuggvenyt `create_greeting` neven, ami:
//   - Kap egy string parametert: `name`
//   - Visszaad EGY stringet: "Udvozollek, [name]!"
//
// Pelda: create_greeting("Kata") → "Udvozollek, Kata!"
// Tipp: return "Udvozollek, " + name + "!";
// ============================================================

// MEGOLDAS IDE:


// ============================================================
// 4. feladat: Szam oszthato-e?
//
// Irj egy fuggvenyt `is_divisible` neven, ami:
//   - Kap ket int parametert: `number` es `divisor`
//   - Visszaad true-t ha `number` oszthato `divisor`-ral,
//     kulonben false-t
//
// Pelda: is_divisible(10, 5) → true
//        is_divisible(10, 3) → false
// Tipp: hasznald a % (modulo) operatort!
// ============================================================

// MEGOLDAS IDE:


// ============================================================
// 5. feladat: Faktorialis
//
// Irj egy fuggvenyt `factorial` neven, ami:
//   - Kap egy int parametert: `n`
//   - Visszaadja n! (n faktorialis) erteket
//   - n! = 1 * 2 * 3 * ... * n
//
// Pelda: factorial(5) → 120 (mert 1*2*3*4*5 = 120)
//        factorial(1) → 1
// Tipp: hasznalj for ciklust! Kezdj result = 1 ertekkel.
// ============================================================

// MEGOLDAS IDE:


// ============================================================
// MAIN — itt fut az ellenorzes
// ============================================================

int main() {

    // ============================================================
    // ELLENORZES — ne modositsd ezt a reszt!
    // ============================================================

    cout << endl;
    cout << "==================================================" << endl;
    cout << "EREDMENYEK" << endl;
    cout << "==================================================" << endl;

    int errors = 0;

    // 1. feladat
    if (rectangle_area(5, 3) == 15 && rectangle_area(10, 10) == 100) {
        cout << "✓ 1. feladat: rectangle_area — OK" << endl;
    } else {
        cout << "✗ 1. feladat: rectangle_area — Szelesseg * magassag! rectangle_area(5,3) = 15 kene legyen." << endl;
        errors++;
    }

    // 2. feladat
    if (bigger(10, 7) == 10 && bigger(3, 9) == 9 && bigger(5, 5) == 5) {
        cout << "✓ 2. feladat: bigger — OK" << endl;
    } else {
        cout << "✗ 2. feladat: bigger — A nagyobbat kell visszaadni! Hasznalj if-else-t." << endl;
        errors++;
    }

    // 3. feladat
    if (create_greeting("Kata") == "Udvozollek, Kata!" && create_greeting("Peter") == "Udvozollek, Peter!") {
        cout << "✓ 3. feladat: create_greeting — OK" << endl;
    } else {
        cout << "✗ 3. feladat: create_greeting — \"Udvozollek, \" + name + \"!\" legyen az eredmeny!" << endl;
        errors++;
    }

    // 4. feladat
    if (is_divisible(10, 5) == true && is_divisible(10, 3) == false && is_divisible(15, 3) == true) {
        cout << "✓ 4. feladat: is_divisible — OK" << endl;
    } else {
        cout << "✗ 4. feladat: is_divisible — Hasznald: return number % divisor == 0;" << endl;
        errors++;
    }

    // 5. feladat
    if (factorial(5) == 120 && factorial(1) == 1 && factorial(3) == 6) {
        cout << "✓ 5. feladat: factorial — OK" << endl;
    } else {
        cout << "✗ 5. feladat: factorial — 5! = 120, 3! = 6. Hasznalj for ciklust!" << endl;
        errors++;
    }

    cout << "==================================================" << endl;
    if (errors == 0) {
        cout << "MINDEN FELADAT KESZ! Szolj nekem, es megnezem!" << endl;
    } else {
        cout << "Meg " << errors << " feladat van hatra. Hajra!" << endl;
    }

    return 0;
}

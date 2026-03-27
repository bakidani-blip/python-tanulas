/*
=============================================================
GYAKORLO FELADATOK — C++ ciklusok (for, while)
Ird meg a megoldasokat a MEGOLDAS IDE reszekhez!
Futtasd a Futtatas gombbal az ellenorzeshez.
=============================================================
*/

#include <iostream>
#include <string>
using namespace std;

int main() {

    // ============================================================
    // 1. feladat: Szamolas 1-tol 10-ig
    //
    // Irj egy for ciklust, ami kiirja a szamokat 1-tol 10-ig!
    // Kozben szamold ossze oket a `sum` valtozoba.
    //
    // Vart eredmeny: sum = 55 (1+2+3+...+10)
    // Tipp: for (int i = 1; i <= 10; i++) { ... }
    // ============================================================

    int sum = 0;

    // MEGOLDAS IDE:


    // ============================================================
    // 2. feladat: Paros szamok
    //
    // Irj egy for ciklust, ami vegigmegy 1-tol 20-ig,
    // de CSAK a paros szamokat adja hozza az `even_sum`-hoz.
    //
    // Vart eredmeny: even_sum = 110 (2+4+6+8+10+12+14+16+18+20)
    // Tipp: hasznald az if-et a cikluson belul: if (i % 2 == 0)
    // ============================================================

    int even_sum = 0;

    // MEGOLDAS IDE:


    // ============================================================
    // 3. feladat: Visszaszamlalas
    //
    // Irj egy for ciklust, ami visszafele szamol 10-tol 1-ig,
    // es osszeepiti a `countdown` stringet.
    // Minden szamot irj bele a countdown-ba ugy:
    //   countdown = countdown + to_string(i) + " ";
    //
    // Vart eredmeny: countdown = "10 9 8 7 6 5 4 3 2 1 "
    // Tipp: for (int i = 10; i >= 1; i--) { ... }
    // ============================================================

    string countdown = "";

    // MEGOLDAS IDE:


    // ============================================================
    // 4. feladat: Hatvanyozas while ciklussal
    //
    // Adott a `base` valtozo (erteke 2).
    // Irj egy while ciklust, ami addig szorozza `power` erteket
    // `base`-zel, amig az el nem eri vagy meghaladja az 1000-et.
    // Szamold meg, hanyszor szorzotal (`steps` valtozoba).
    //
    // Vart eredmeny: power = 1024, steps = 10
    // (mert 2^10 = 1024, ami az elso 2-hatvany >= 1000)
    // Tipp: while (power < 1000) { power = power * base; steps++; }
    // ============================================================

    int base = 2;
    int power = 1;
    int steps = 0;

    // MEGOLDAS IDE:


    // ============================================================
    // 5. feladat: Csillag piramis
    //
    // Irj egymasba agyazott for ciklusokat, amik felépitik
    // a `pyramid` stringet igy (5 sor):
    //   "*\n"
    //   "**\n"
    //   "***\n"
    //   "****\n"
    //   "*****\n"
    //
    // A kulso ciklus a sorokon megy (1-tol 5-ig).
    // A belso ciklus annyi *-ot ir, ahany a sorszam.
    // Minden sor vegen adj hozza "\n"-t (ujsor karakter).
    //
    // Tipp:
    //   for (int row = 1; row <= 5; row++) {
    //       for (int col = 1; col <= row; col++) { ... }
    //       pyramid = pyramid + "\n";
    //   }
    // ============================================================

    string pyramid = "";

    // MEGOLDAS IDE:


    // ============================================================
    // ELLENORZES — ne modositsd ezt a reszt!
    // ============================================================

    cout << endl;
    cout << "==================================================" << endl;
    cout << "EREDMENYEK" << endl;
    cout << "==================================================" << endl;

    int errors = 0;

    // 1. feladat
    if (sum == 55) {
        cout << "✓ 1. feladat: Osszeg 1-10 — OK (sum = " << sum << ")" << endl;
    } else {
        cout << "✗ 1. feladat: Osszeg 1-10 — Vart: 55, kaptam: " << sum << endl;
        errors++;
    }

    // 2. feladat
    if (even_sum == 110) {
        cout << "✓ 2. feladat: Paros osszeg — OK (even_sum = " << even_sum << ")" << endl;
    } else {
        cout << "✗ 2. feladat: Paros osszeg — Vart: 110, kaptam: " << even_sum << endl;
        errors++;
    }

    // 3. feladat
    if (countdown == "10 9 8 7 6 5 4 3 2 1 ") {
        cout << "✓ 3. feladat: Visszaszamlalas — OK" << endl;
    } else {
        cout << "✗ 3. feladat: Visszaszamlalas — Ellenorizd a ciklust! Kaptam: \"" << countdown << "\"" << endl;
        errors++;
    }

    // 4. feladat
    if (power == 1024 && steps == 10) {
        cout << "✓ 4. feladat: Hatvanyozas — OK (2^" << steps << " = " << power << ")" << endl;
    } else {
        cout << "✗ 4. feladat: Hatvanyozas — Vart: power=1024, steps=10. Kaptam: " << power << ", " << steps << endl;
        errors++;
    }

    // 5. feladat
    string expected_pyramid = "*\n**\n***\n****\n*****\n";
    if (pyramid == expected_pyramid) {
        cout << "✓ 5. feladat: Piramis — OK" << endl;
        cout << pyramid;
    } else {
        cout << "✗ 5. feladat: Piramis — Ellenorizd a ket egymasba agyazott ciklust!" << endl;
        if (pyramid.length() > 0) {
            cout << "  Kaptam:" << endl << pyramid;
        }
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

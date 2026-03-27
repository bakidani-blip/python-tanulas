/*
=============================================================
GYAKORLO FELADATOK — C++ feltetelek (if/else, switch)
Ird meg a megoldasokat a MEGOLDAS IDE reszekhez!
Futtasd a Futtatas gombbal az ellenorzeshez.
=============================================================
*/

#include <iostream>
#include <string>
using namespace std;

int main() {

    // ============================================================
    // 1. feladat: Paros vagy paratlan?
    //
    // Adott egy `number` valtozo (erteke 7).
    // Ird meg az if-else feltetelt, ami:
    //   - Ha paros: kiirja "Paros"
    //   - Ha paratlan: kiirja "Paratlan"
    //
    // Tipp: a % (modulo) operator megadja az osztás maradekát.
    //       Ha number % 2 == 0, akkor paros!
    // ============================================================

    int number = 7;
    string number_result = "";

    // MEGOLDAS IDE:


    // ============================================================
    // 2. feladat: Jegyezes
    //
    // Adott egy `points` valtozo (erteke 73).
    // Ird meg az if / else if / else lancot, ami beallitja
    // a `grade` valtozo erteket:
    //   90-100 pont → grade = "Jeles"
    //   75-89  pont → grade = "Jo"
    //   60-74  pont → grade = "Kozepes"
    //   40-59  pont → grade = "Elegseges"
    //   0-39   pont → grade = "Elegtelen"
    //
    // Tipp: felulrol lefele vizsgald, a >= operatorral!
    // ============================================================

    int points = 73;
    string grade = "";

    // MEGOLDAS IDE:


    // ============================================================
    // 3. feladat: Beleptetés
    //
    // Adott ket valtozo: `visitor_age` (22) es `has_id` (true).
    // Ird meg a feltetelt:
    //   - Ha 18 vagy idosebb ÉS van igazolványa → result = "Belephet"
    //   - Kulonben → result = "Nem lephet be"
    //
    // Tipp: hasznald az && (ÉS) operatort!
    // ============================================================

    int visitor_age = 22;
    bool has_id = true;
    string entry_result = "";

    // MEGOLDAS IDE:


    // ============================================================
    // 4. feladat: Evszak
    //
    // Adott a `month` valtozo (erteke 8, azaz augusztus).
    // Hasznalj switch-et, es allitsd be a `season` valtozot:
    //   12, 1, 2  → season = "Tel"
    //   3, 4, 5   → season = "Tavasz"
    //   6, 7, 8   → season = "Nyar"
    //   9, 10, 11 → season = "Osz"
    //
    // Tipp: tobb case-t is irhatsz egymas ala break nelkul,
    //       hogy "atfolyjanak" ugyanarra az eredmenyre:
    //       case 6: case 7: case 8: ... break;
    // ============================================================

    int month = 8;
    string season = "";

    // MEGOLDAS IDE:


    // ============================================================
    // 5. feladat: Hany eves vagy kategoria
    //
    // Adott a `cat_age` valtozo (erteke 10).
    // Ird meg a feltetelt:
    //   - Ha 0-2   → category = "Csecsemo"
    //   - Ha 3-5   → category = "Ovodas"
    //   - Ha 6-14  → category = "Iskolás"
    //   - Ha 15-17 → category = "Tinedzser"
    //   - Ha 18+   → category = "Felnott"
    //
    // Tipp: hasznalj else if lancot!
    // ============================================================

    int cat_age = 10;
    string category = "";

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
    if (number_result == "Paratlan") {
        cout << "✓ 1. feladat: Paros/paratlan — OK" << endl;
    } else {
        cout << "✗ 1. feladat: Paros/paratlan — A 7 paratlan! Hasznald: number % 2" << endl;
        errors++;
    }

    // 2. feladat
    if (grade == "Kozepes") {
        cout << "✓ 2. feladat: Jegyezes — OK (73 pont = " << grade << ")" << endl;
    } else {
        cout << "✗ 2. feladat: Jegyezes — 73 pont Kozepes kene legyen! Ellenorizd a hataroket." << endl;
        errors++;
    }

    // 3. feladat
    if (entry_result == "Belephet") {
        cout << "✓ 3. feladat: Beleptetes — OK" << endl;
    } else {
        cout << "✗ 3. feladat: Beleptetes — 22 eves + van ID = Belephet! Hasznald az && operatort." << endl;
        errors++;
    }

    // 4. feladat
    if (season == "Nyar") {
        cout << "✓ 4. feladat: Evszak — OK (8. honap = " << season << ")" << endl;
    } else {
        cout << "✗ 4. feladat: Evszak — Augusztus (8) = Nyar! Hasznalj switch-et." << endl;
        errors++;
    }

    // 5. feladat
    if (category == "Iskolás" || category == "Iskolas") {
        cout << "✓ 5. feladat: Korkategoria — OK (10 eves = " << category << ")" << endl;
    } else {
        cout << "✗ 5. feladat: Korkategoria — 10 eves = Iskolas! Ellenorizd az else if lancot." << endl;
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

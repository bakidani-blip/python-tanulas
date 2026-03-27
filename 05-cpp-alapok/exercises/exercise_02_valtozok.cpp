/*
=============================================================
GYAKORLO FELADATOK — C++ valtozok es tipusok
Ird meg a megoldasokat a MEGOLDAS IDE reszekhez!
Futtasd a Futtatas gombbal az ellenorzeshez.
=============================================================
*/

#include <iostream>
#include <string>
using namespace std;

int main() {

    // ============================================================
    // 1. feladat: Egesz szam valtozo
    // Hozz letre egy `my_age` nevu int valtozot a koroddal!
    // ============================================================

    // MEGOLDAS IDE:


    // ============================================================
    // 2. feladat: Tort szam
    // Hozz letre egy `my_height` nevu double valtozot
    // a magassagoddal meterben (pl. 1.72)!
    // ============================================================

    // MEGOLDAS IDE:


    // ============================================================
    // 3. feladat: Szoveg
    // Hozz letre egy `my_name` nevu string valtozot a neveddel!
    // Tipp: string my_name = "...";
    // ============================================================

    // MEGOLDAS IDE:


    // ============================================================
    // 4. feladat: Bemutatkozas
    // Irasd ki EGYETLEN sorba:
    //   "Szia! Nevem [nev], [kor] eves vagyok."
    // Hasznald a fenti valtozokat (my_name, my_age)!
    // Tipp: cout << "szoveg" << valtozo << "szoveg" << endl;
    // ============================================================

    // MEGOLDAS IDE:


    // ============================================================
    // 5. feladat: Szamolas
    // Hozz letre ket int valtozot: `a` erteke 15, `b` erteke 4.
    // Szamold ki es irasd ki:
    //   - az osszeguket (a + b)
    //   - a kulonbseguket (a - b)
    //   - a szorzatukat (a * b)
    // Mindegyiket kulon sorba, peldaul: "Osszeg: 19"
    // ============================================================

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
    if (my_age > 0 && my_age < 120) {
        cout << "✓ 1. feladat: my_age — OK (" << my_age << ")" << endl;
    } else {
        cout << "✗ 1. feladat: my_age — Adj meg egy valos kort!" << endl;
        errors++;
    }

    // 2. feladat
    if (my_height > 0.5 && my_height < 2.5) {
        cout << "✓ 2. feladat: my_height — OK (" << my_height << " m)" << endl;
    } else {
        cout << "✗ 2. feladat: my_height — Adj meg valos magassagot meterben!" << endl;
        errors++;
    }

    // 3. feladat
    if (my_name.length() > 0) {
        cout << "✓ 3. feladat: my_name — OK (\"" << my_name << "\")" << endl;
    } else {
        cout << "✗ 3. feladat: my_name — Ne hagyd uresen a neved!" << endl;
        errors++;
    }

    // 4. feladat — vizualis ellenorzes
    cout << "? 4. feladat: Nezd meg fentebb, megjelent-e a bemutatkozas!" << endl;

    // 5. feladat
    if (a == 15 && b == 4) {
        cout << "✓ 5. feladat: a es b — OK" << endl;
    } else {
        cout << "✗ 5. feladat: a legyen 15, b legyen 4!" << endl;
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

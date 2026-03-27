/*
=============================================================
4. LECKE: Ciklusok — ismetles a programban
Futtasd: a bongeszoben a Futtatas gombbal
=============================================================
*/

#include <iostream>
#include <string>
using namespace std;

// ============================================================
// MIERT KELLENEK CIKLUSOK?
// ============================================================

// Kepzeld el, hogy 10-szer ki akarod irni: "Hello!"
// Irhatnal 10 darab cout sort... de az borzaszto lenne.
//
// A ciklus (loop) megoldja ezt: megmondod MIT csinaljon,
// es HANYSZOR — a gep megcsinalja helyetted.
//
// Ket fo ciklus letezik C++-ban:
//   - `for`   — ha tudod, hanyszor kell ismetelni
//   - `while` — ha nem tudod elore, meddig kell menni

int main() {

    // ============================================================
    // 1. FOR CIKLUS — "csinalld X-szer"
    // ============================================================

    // A for ciklus 3 reszbol all:
    //
    //   for (kezdoertek; feltetel; lepes) { ... }
    //         ^            ^        ^
    //         |            |        +-- minden kor vegen ez tortenik
    //         |            +----------- amig ez IGAZ, fut a ciklus
    //         +------------------------ egyszer, az elejen
    //
    // Pelda: szamoljunk 1-tol 5-ig

    cout << "Szamolas 1-tol 5-ig:" << endl;
    for (int i = 1; i <= 5; i++) {
        // i++ ugyanaz mint i = i + 1 (novel eggyel)
        cout << "  " << i << endl;
    }

    // Mi tortenik lepesrol lepesre:
    //   1. i = 1 (kezdoertek)
    //   2. 1 <= 5? IGAZ → kiir 1, majd i++ → i = 2
    //   3. 2 <= 5? IGAZ → kiir 2, majd i++ → i = 3
    //   4. 3 <= 5? IGAZ → kiir 3, majd i++ → i = 4
    //   5. 4 <= 5? IGAZ → kiir 4, majd i++ → i = 5
    //   6. 5 <= 5? IGAZ → kiir 5, majd i++ → i = 6
    //   7. 6 <= 5? HAMIS → VEGE a ciklusnak!

    // ============================================================
    // 2. FOR CIKLUS — masik pelda
    // ============================================================

    // Szorozzunk! Irjuk ki a 3-as szorzotablat:

    cout << endl << "3-as szorzotabla:" << endl;
    for (int i = 1; i <= 10; i++) {
        cout << "  3 x " << i << " = " << 3 * i << endl;
    }

    // A ciklus tokeletes ismetlodo mintakra!

    // ============================================================
    // 3. FOR CIKLUS — visszafele szamlalas
    // ============================================================

    // Nem csak felfelé szamlalhatunk!
    // i-- az i = i - 1 roviditese (csokkent eggyel)

    cout << endl << "Visszaszamlalas:" << endl;
    for (int i = 5; i >= 1; i--) {
        cout << "  " << i << "..." << endl;
    }
    cout << "  START!" << endl;

    // ============================================================
    // 4. WHILE CIKLUS — "amig igaz, csinalld"
    // ============================================================

    // A `while` ciklus addig ismetel, amig a feltetel IGAZ.
    // Hasznald, ha NEM TUDOD ELORE, hanyszor kell ismetelni.
    //
    // Gondolj ra igy:
    //   "AMIG nem talaltam meg a kulcsomat, keresem tovabb."

    cout << endl << "While ciklus — duplazas:" << endl;
    int value = 1;
    while (value < 100) {
        cout << "  " << value << endl;
        value = value * 2;  // megduplazzuk
    }
    cout << "  Vegso ertek: " << value << endl;

    // Mi tortent:
    //   1 → 2 → 4 → 8 → 16 → 32 → 64 → 128 (STOP, mert 128 >= 100)

    // ============================================================
    // 5. VEGTELEN CIKLUS VESZELYE
    // ============================================================

    // **VIGYAZZ!** Ha a feltetel SOHA nem lesz hamis,
    // a ciklus orokke fut! Ezt vegtelen ciklusnak hivjak.
    //
    // Rossz pelda (NE futtasd, lefagyhat!):
    //   while (true) { cout << "Help!" << endl; }
    //
    // Kerdes: miert vegtelen ez?
    // Mert `true` sosem lesz `false`!
    //
    // Mindig gyozodj meg rola, hogy a ciklusod VALAHOL megall.
    // A for ciklus biztonsagosabb, mert a lepes beepitett.

    // ============================================================
    // 6. BREAK ES CONTINUE
    // ============================================================

    // `break` — azonnal kilep a ciklusbol
    // `continue` — atugorja az aktualis kort es megy a kovetkezore

    cout << endl << "Break pelda — keressuk az elso 3-mal oszthatot:" << endl;
    for (int i = 1; i <= 20; i++) {
        if (i % 3 == 0) {
            cout << "  Megtalaltam: " << i << endl;
            break;  // Kilep a ciklusbol, nem keres tovabb
        }
    }

    cout << endl << "Continue pelda — csak paros szamok:" << endl;
    for (int i = 1; i <= 10; i++) {
        if (i % 2 != 0) {
            continue;  // Atugorja a paratlanokat
        }
        cout << "  " << i << endl;
    }

    // ============================================================
    // 7. EGYMASBA AGYAZOTT CIKLUSOK
    // ============================================================

    // Egy ciklust beletehetsz egy masik ciklusba!
    // Pelda: szorzotabla

    cout << endl << "Szorzotabla (1-5):" << endl;
    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= 5; j++) {
            // A belso ciklus TELJESEN lefut minden kulso lepesre
            cout << i * j << "\t";  // \t = tab (tavolsag)
        }
        cout << endl;  // Uj sor a kulso ciklus vegen
    }

    // ============================================================
    // OSSZEFOGLALAS
    // ============================================================

    // | Ciklus   | Mikor hasznald                        |
    // |----------|---------------------------------------|
    // | for      | Ha tudod, hanyszor kell ismetelni     |
    // | while    | Ha nem tudod elore, meddig kell menni |
    // | break    | Azonnal kilep a ciklusbol             |
    // | continue | Atugorja az aktualis kort             |
    //
    // Fontos:
    // - i++ = novel 1-gyel, i-- = csokkent 1-gyel
    // - Mindig gyozodj meg, hogy a ciklus VEGET ER!
    // - Egymasba agyazott ciklusok: a belso teljesen lefut
    //   minden kulso lepesre
    //
    // A kovetkezo leckeben fuggvenyeket tanulunk!

    return 0;
}

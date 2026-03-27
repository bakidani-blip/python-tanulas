/*
=============================================================
4. LECKE: Ciklusok — ismétlés a programban
Futtasd: a böngészőben a Futtatás gombbal
=============================================================
*/

#include <iostream>
#include <string>
using namespace std;

// ============================================================
// MIÉRT KELLENEK CIKLUSOK?
// ============================================================

// Képzeld el, hogy 10-szer ki akarod írni: "Hello!"
// Írhatnál 10 darab cout sort... de az borzasztó lenne.
//
// A ciklus (loop) megoldja ezt: megmondod MIT csináljon,
// és HÁNYSZOR — a gép megcsinálja helyetted.
//
// Két fő ciklus létezik C++-ban:
//   - `for`   — ha tudod, hányszor kell ismételni
//   - `while` — ha nem tudod előre, meddig kell menni

int main() {

    // ============================================================
    // 1. FOR CIKLUS — "csináld X-szer"
    // ============================================================

    // A for ciklus 3 részből áll:
    //
    //   for (kezdőérték; feltétel; lépés) { ... }
    //         ^            ^        ^
    //         |            |        +-- minden kör végén ez történik
    //         |            +----------- amíg ez IGAZ, fut a ciklus
    //         +------------------------ egyszer, az elején
    //
    // Példa: számoljunk 1-től 5-ig

    cout << "Számolás 1-től 5-ig:" << endl;
    for (int i = 1; i <= 5; i++) {
        // i++ ugyanaz mint i = i + 1 (növel eggyel)
        cout << "  " << i << endl;
    }

    // Mi történik lépésről lépésre:
    //   1. i = 1 (kezdőérték)
    //   2. 1 <= 5? IGAZ → kiír 1, majd i++ → i = 2
    //   3. 2 <= 5? IGAZ → kiír 2, majd i++ → i = 3
    //   4. 3 <= 5? IGAZ → kiír 3, majd i++ → i = 4
    //   5. 4 <= 5? IGAZ → kiír 4, majd i++ → i = 5
    //   6. 5 <= 5? IGAZ → kiír 5, majd i++ → i = 6
    //   7. 6 <= 5? HAMIS → VÉGE a ciklusnak!

    // ============================================================
    // 2. FOR CIKLUS — másik példa
    // ============================================================

    // Szorozzunk! Írjuk ki a 3-as szorzótáblát:

    cout << endl << "3-as szorzótábla:" << endl;
    for (int i = 1; i <= 10; i++) {
        cout << "  3 x " << i << " = " << 3 * i << endl;
    }

    // A ciklus tökéletes ismétlődő mintákra!

    // ============================================================
    // 3. FOR CIKLUS — visszafelé számlálás
    // ============================================================

    // Nem csak felfelé számlálhatunk!
    // i-- az i = i - 1 rövidítése (csökkent eggyel)

    cout << endl << "Visszaszámlálás:" << endl;
    for (int i = 5; i >= 1; i--) {
        cout << "  " << i << "..." << endl;
    }
    cout << "  START!" << endl;

    // ============================================================
    // 4. WHILE CIKLUS — "amíg igaz, csináld"
    // ============================================================

    // A `while` ciklus addig ismétél, amíg a feltétel IGAZ.
    // Használd, ha NEM TUDOD ELŐRE, hányszor kell ismételni.
    //
    // Gondolj rá így:
    //   "AMÍG nem találtam meg a kulcsomat, keresem tovább."

    cout << endl << "While ciklus — duplázás:" << endl;
    int value = 1;
    while (value < 100) {
        cout << "  " << value << endl;
        value = value * 2;  // megduplázzuk
    }
    cout << "  Végső érték: " << value << endl;

    // Mi történt:
    //   1 → 2 → 4 → 8 → 16 → 32 → 64 → 128 (STOP, mert 128 >= 100)

    // ============================================================
    // 5. VÉGTELEN CIKLUS VESZÉLYE
    // ============================================================

    // **VIGYÁZZ!** Ha a feltétel SOHA nem lesz hamis,
    // a ciklus örökké fut! Ezt végtelen ciklusnak hívják.
    //
    // Rossz példa (NE futtasd, lefagyhat!):
    //   while (true) { cout << "Help!" << endl; }
    //
    // Kérdés: miért végtelen ez?
    // Mert `true` sosem lesz `false`!
    //
    // Mindig győződj meg róla, hogy a ciklusod VALAHOL megáll.
    // A for ciklus biztonságosabb, mert a lépés beépített.

    // ============================================================
    // 6. BREAK ÉS CONTINUE
    // ============================================================

    // `break` — azonnal kilép a ciklusból
    // `continue` — átugorja az aktuális kört és megy a következőre

    cout << endl << "Break példa — keressük az első 3-mal oszthatót:" << endl;
    for (int i = 1; i <= 20; i++) {
        if (i % 3 == 0) {
            cout << "  Megtaláltam: " << i << endl;
            break;  // Kilép a ciklusból, nem keres tovább
        }
    }

    cout << endl << "Continue példa — csak páros számok:" << endl;
    for (int i = 1; i <= 10; i++) {
        if (i % 2 != 0) {
            continue;  // Átugorja a páratlanokat
        }
        cout << "  " << i << endl;
    }

    // ============================================================
    // 7. EGYMÁSBA ÁGYAZOTT CIKLUSOK
    // ============================================================

    // Egy ciklust beletehetsz egy másik ciklusba!
    // Példa: szorzótábla

    cout << endl << "Szorzótábla (1-5):" << endl;
    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= 5; j++) {
            // A belső ciklus TELJESEN lefut minden külső lépésre
            cout << i * j << "\t";  // \t = tab (távolság)
        }
        cout << endl;  // Új sor a külső ciklus végén
    }

    // ============================================================
    // ÖSSZEFOGLALÁS
    // ============================================================

    // | Ciklus   | Mikor használd                        |
    // |----------|---------------------------------------|
    // | for      | Ha tudod, hányszor kell ismételni     |
    // | while    | Ha nem tudod előre, meddig kell menni |
    // | break    | Azonnal kilép a ciklusból             |
    // | continue | Átugorja az aktuális kört             |
    //
    // Fontos:
    // - i++ = növel 1-gyel, i-- = csökkent 1-gyel
    // - Mindig győződj meg, hogy a ciklus VÉGET ÉR!
    // - Egymásba ágyazott ciklusok: a belső teljesen lefut
    //   minden külső lépésre
    //
    // A következő leckében függvényeket tanulunk!

    return 0;
}

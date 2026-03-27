/*
=============================================================
1. LECKE: C++ alapok — Hello World es a program felepitese
Futtasd: a bongeszoben a Futtatas gombbal
=============================================================
*/

#include <iostream>
using namespace std;

// ============================================================
// MI AZ A C++?
// ============================================================

// A C++ az egyik legelterjedtebb programozasi nyelv a vilagon.
// Jatekokat, operacios rendszereket, bongeszoket irnak benne.
//
// Miert tanulod?
// - **Gyors**: kozel van a hardverhez, ezert villamposan fut
// - **Mindenhol hasznaljak**: jatek, auto, robot, telefon
// - **Alapozas**: ha ezt megtanulod, barmi mas nyelv konnyu lesz
//
// Ne ijedj meg a szintaxistol! Lepesrol lepesre haladunk.

// ============================================================
// AZ ELSO PROGRAM: HELLO WORLD
// ============================================================

// Minden C++ program a `main()` fuggvennyel kezdodik.
// Ez olyan, mint a belso ajto: a program ITT indul el.
//
// `#include <iostream>` — ez mondja meg a fordítonak:
// "Szuksegem van az input/output eszkozokre" (pl. kiiras kepernyore).
//
// `using namespace std;` — ez lehetove teszi, hogy `cout`-ot
// irjunk `std::cout` helyett. Egyszeru rovidites.
//
// Nezzuk a legegyszerubb programot:

int main() {
    // `cout` = "character output" = kiiras a kepernyore
    // `<<` = "kuldd oda" operator — azt jelenti: "ird ki ezt"
    // `endl` = "end line" = uj sor (mint az Enter billentyű)

    cout << "Hello, Vilag!" << endl;

    // A `return 0;` azt jelenti: "minden rendben, vege a programnak"
    // 0 = siker, barmi mas = hiba tortent
    return 0;
}

// ============================================================
// HOGYAN OLVASSUK A KODOT?
// ============================================================

// Bontsuk darabokra az elso programunkat:
//
// 1. `#include <iostream>` — "importalj" eszkozoket (mint Pythonban az import)
// 2. `using namespace std;` — hasznald az std (standard) nevteret
// 3. `int main()` — a foprogram kezdete
//    - `int` = egesz szamot ad vissza (a 0-t a vegen)
//    - `main` = kotelező nev, innen indul a program
//    - `()` = parameterlista (most ures)
// 4. `{ ... }` — kapcsos zarojelek kozott van a program teste
// 5. `cout << "szoveg" << endl;` — kiiras
// 6. `return 0;` — program vege, sikeres
// 7. Minden utasitas vegen **pontosvesszo** `;` — ez KOTELEZO!
//
// **Gyakori hiba**: elfelejtett pontosvesszo!
// Ha a fordito furcsa hibat ir, eloszor ezt ellenorizd.

// ============================================================
// TOBBSOROS KIIRAS
// ============================================================

// Tobb dolgot is kiirhatunk egymas utan:
//
// cout << "Elso sor" << endl;
// cout << "Masodik sor" << endl;
//
// Vagy akár egyetlen sorban:
//
// cout << "Nev: " << "Kata" << ", Kor: " << 14 << endl;
//
// A `<<` operator "osszefuzi" a darabokat.
// Szamot es szoveget is vegyithetunk!

// ============================================================
// OSSZEFOGLALAS
// ============================================================

// Amit ma megtanultal:
// - Minden C++ program a `main()` fuggvennyel indul
// - `#include <iostream>` kell a kiiras/beolvasashoz
// - `cout << ... << endl;` = kiiras a kepernyore
// - Minden sor vegen `;` pontosvesszo
// - `return 0;` = sikeres program vege
//
// A kovetkezo leckeben valtozokkal es tipusokkal foglalkozunk!

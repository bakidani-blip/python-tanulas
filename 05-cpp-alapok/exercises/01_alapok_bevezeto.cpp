/*
=============================================================
1. LECKE: C++ alapok — Hello World és a program felépítése
Futtasd: a böngészőben a Futtatás gombbal
=============================================================
*/

#include <iostream>
using namespace std;

// ============================================================
// MI AZ A C++?
// ============================================================

// A C++ az egyik legelterjedtebb programozási nyelv a világon.
// Játékokat, operációs rendszereket, böngészőket írnak benne.
//
// Miért tanulod?
// - **Gyors**: közel van a hardverhez, ezért villámgyorsan fut
// - **Mindenhol használják**: játék, autó, robot, telefon
// - **Alapozás**: ha ezt megtanulod, bármi más nyelv könnyű lesz
//
// Ne ijedj meg a szintaxistól! Lépésről lépésre haladunk.

// ============================================================
// AZ ELSŐ PROGRAM: HELLO WORLD
// ============================================================

// Minden C++ program a `main()` függvénnyel kezdődik.
// Ez olyan, mint a belső ajtó: a program ITT indul el.
//
// `#include <iostream>` — ez mondja meg a fordítónak:
// "Szükségem van az input/output eszközökre" (pl. kiírás képernyőre).
//
// `using namespace std;` — ez lehetővé teszi, hogy `cout`-ot
// írjunk `std::cout` helyett. Egyszerű rövidítés.
//
// Nézzük a legegyszerűbb programot:

int main() {
    // `cout` = "character output" = kiírás a képernyőre
    // `<<` = "küldd oda" operátor — azt jelenti: "írd ki ezt"
    // `endl` = "end line" = új sor (mint az Enter billentyű)

    cout << "Hello, Világ!" << endl;

    // A `return 0;` azt jelenti: "minden rendben, vége a programnak"
    // 0 = siker, bármi más = hiba történt
    return 0;
}

// ============================================================
// HOGYAN OLVASSUK A KÓDOT?
// ============================================================

// Bontsuk darabokra az első programunkat:
//
// 1. `#include <iostream>` — "importálj" eszközöket (mint Pythonban az import)
// 2. `using namespace std;` — használd az std (standard) névteret
// 3. `int main()` — a főprogram kezdete
//    - `int` = egész számot ad vissza (a 0-t a végén)
//    - `main` = kötelező név, innen indul a program
//    - `()` = paraméterlista (most üres)
// 4. `{ ... }` — kapcsos zárójelek között van a program teste
// 5. `cout << "szöveg" << endl;` — kiírás
// 6. `return 0;` — program vége, sikeres
// 7. Minden utasítás végén **pontosvessző** `;` — ez KÖTELEZŐ!
//
// **Gyakori hiba**: elfelejtett pontosvessző!
// Ha a fordító furcsa hibát ír, először ezt ellenőrizd.

// ============================================================
// TÖBBSOROS KIÍRÁS
// ============================================================

// Több dolgot is kiírhatunk egymás után:
//
// cout << "Első sor" << endl;
// cout << "Második sor" << endl;
//
// Vagy akár egyetlen sorban:
//
// cout << "Név: " << "Kata" << ", Kor: " << 14 << endl;
//
// A `<<` operátor "összefűzi" a darabokat.
// Számot és szöveget is vegyíthetünk!

// ============================================================
// ÖSSZEFOGLALÁS
// ============================================================

// Amit ma megtanultál:
// - Minden C++ program a `main()` függvénnyel indul
// - `#include <iostream>` kell a kiírás/beolvasáshoz
// - `cout << ... << endl;` = kiírás a képernyőre
// - Minden sor végén `;` pontosvessző
// - `return 0;` = sikeres program vége
//
// A következő leckében változókkal és típusokkal foglalkozunk!

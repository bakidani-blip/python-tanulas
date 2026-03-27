/*
=============================================================
3. LECKE: Feltetelek — dontes a programban
Futtasd: a bongeszoben a Futtatas gombbal
=============================================================
*/

#include <iostream>
#include <string>
using namespace std;

// ============================================================
// MIERT KELLENEK FELTETELEK?
// ============================================================

// Kepzeld el, hogy a programod egy utat jar be.
// Eddig ez az ut egyenes volt — minden sor lefutott, sorban.
//
// De az eletben is donteseket hozunk:
//   "Ha esik az eso, viszek esernyot. Kulonben nem."
//
// A programban PONTOSAN igy mukodik a feltetel:
//   if (feltetel) { csinalj valamit; }
//   else { csinalj mast; }
//
// A feltetel vagy IGAZ (true), vagy HAMIS (false).
// Ez alapjan dont a program, melyik uton menjen tovabb.

int main() {

    // ============================================================
    // 1. EGYSZERÜ IF — "ha igaz, csinalld meg"
    // ============================================================

    // Az `if` a legegyszerubb feltetel.
    // Ha a zarojelben levo dolog IGAZ, vegrehajtja a kapcsos zarojelek kozotti kodot.
    // Ha HAMIS, atugorja.

    int age = 16;

    if (age >= 18) {
        cout << "Felnoett vagy, mehetsz szavazni!" << endl;
    }

    // Ez NEM fog kiirodni, mert 16 < 18, tehat a feltetel HAMIS.
    // Probald meg atirni az age-et 20-ra es futtasd ujra!

    // ============================================================
    // 2. IF-ELSE — "ha igaz, ezt csinalld, kulonben azt"
    // ============================================================

    // Az `else` ag akkor fut le, ha a feltetel HAMIS.
    // Igy mindig tortenik VALAMI — vagy az if, vagy az else.

    int temperature = 35;

    if (temperature > 30) {
        cout << "Nagyon meleg van! (" << temperature << " fok)" << endl;
    } else {
        cout << "Elfogadhato a homerseklet. (" << temperature << " fok)" << endl;
    }

    // Gondolj ra ugy: ez egy elgazas az uton.
    // Vagy balra mesz (if), vagy jobbra (else). De valamelyikre MINDIG.

    // ============================================================
    // 3. OSSZEHASONLITO OPERATOROK
    // ============================================================

    // Ezekkel az operatorokkal hasonlitunk ossze ket erteket:
    //
    //   ==   egyenlo-e?          (VIGYAZZ: ket egyenloseg jel!)
    //   !=   nem egyenlo-e?
    //   >    nagyobb?
    //   <    kisebb?
    //   >=   nagyobb vagy egyenlo?
    //   <=   kisebb vagy egyenlo?
    //
    // **GYAKORI HIBA**: egy `=` az ERTEKADAS, ket `==` az OSSZEHASONLITAS!
    //   age = 18   → "legyen 18"      (ertekadas)
    //   age == 18  → "egyenlo 18-cal?" (kerdes)

    int score = 75;

    cout << endl;
    if (score == 100) {
        cout << "Tokeletes pontszam!" << endl;
    } else if (score >= 80) {
        cout << "Nagyon jo eredmeny!" << endl;
    } else if (score >= 60) {
        cout << "Atment!" << endl;
    } else {
        cout << "Sajnos nem ment at." << endl;
    }

    // Itt a valasz: "Atment!" — mert 75 >= 60 igaz.
    // Fontos: a program FELULROL LEFELE vizsgalja a felteteleket,
    // es az ELSO igaz agat hajtja vegre, a tobbit atugorja!

    // ============================================================
    // 4. ELSE IF — tobb lehetoseg
    // ============================================================

    // Az `else if` segitsegevel tobb agat is letre tudsz hozni.
    // Olyan, mint egy tobbfele elgazas:
    //   Ha A → csinalj X-et
    //   Kulonben ha B → csinalj Y-t
    //   Kulonben ha C → csinalj Z-t
    //   Kulonben → csinalj valami mast

    int hour = 14;

    cout << endl;
    if (hour < 6) {
        cout << "Jo ejszakat!" << endl;
    } else if (hour < 12) {
        cout << "Jo reggelt!" << endl;
    } else if (hour < 18) {
        cout << "Jo napot!" << endl;
    } else {
        cout << "Jo estet!" << endl;
    }

    // 14 ora → "Jo napot!" (mert 14 >= 12 es 14 < 18)

    // ============================================================
    // 5. LOGIKAI OPERATOROK — felteteleket kotni ossze
    // ============================================================

    // Neha tobb feltetelt is vizsgalni akarunk egyszerre:
    //
    //   &&  — ÉS (and): MINDKET feltetelnek igaznak kell lennie
    //   ||  — VAGY (or): LEGALABB az egyiknek igaznak kell lennie
    //   !   — NEM (not): megforditja: igazbol hamis lesz, hamisbol igaz
    //
    // Hasonlat:
    //   && = "Elmegyek setalni, HA szep az ido ÉS van idom"
    //   || = "Boldog vagyok, HA nyaralok VAGY fagylaltot eszem"
    //   !  = "NEM esik az eso" (az ellenkezoje)

    int user_age = 20;
    bool has_ticket = true;

    cout << endl;
    if (user_age >= 18 && has_ticket) {
        cout << "Belephet a koncertre!" << endl;
    } else {
        cout << "Nem lephet be." << endl;
    }

    // Mindketto igaz (20 >= 18 ÉS van jegye), tehat belephet.

    bool is_weekend = true;
    bool is_holiday = false;

    if (is_weekend || is_holiday) {
        cout << "Szabad nap — pihenj!" << endl;
    } else {
        cout << "Munkanap — hajra!" << endl;
    }

    // ============================================================
    // 6. SWITCH — valasztas tobb fix ertek kozul
    // ============================================================

    // Ha egy valtozo erteket KONKRET ertekekhez hasonlitod
    // (pl. 1, 2, 3), a `switch` attekinthetobb, mint sok else if.
    //
    // Gondolj ra, mint egy automatara:
    //   Nyomd meg az 1-est → kapj kavet
    //   Nyomd meg a 2-est → kapj teat
    //   Nyomd meg a 3-ast → kapj vizet
    //   Barmi mas → "ismeretlen gomb"

    int day = 3;

    cout << endl;
    switch (day) {
        case 1:
            cout << "Hetfo" << endl;
            break;  // FONTOS! break nelkul "lecsuszik" a kovetkezore!
        case 2:
            cout << "Kedd" << endl;
            break;
        case 3:
            cout << "Szerda" << endl;
            break;
        case 4:
            cout << "Csutortok" << endl;
            break;
        case 5:
            cout << "Pentek" << endl;
            break;
        default:
            cout << "Hetvege!" << endl;
            break;
    }

    // A `break` KOTELEZO minden `case` vegen!
    // Nelkule a program "atfolyik" a kovetkezo case-be
    // (ez egy C++ sajatossag, es gyakori hibaforrás).

    // ============================================================
    // OSSZEFOGLALAS
    // ============================================================

    // Amit ma megtanultal:
    //
    // | Szerkezet      | Mikor hasznald                      |
    // |----------------|-------------------------------------|
    // | if             | Egyetlen feltetel vizsgalata         |
    // | if-else        | Ket lehetoseg kozul valasztas       |
    // | else if        | Tobb lehetoseg (lancolt feltetelek) |
    // | switch-case    | Fix ertekek kozul valasztas          |
    // | &&, ||, !      | Feltetelek osszekotese              |
    //
    // Fontos:
    // - `==` az osszehasonlitas, `=` az ertekadas — ne keverd!
    // - `switch`-ben mindig irj `break`-et!
    // - A felteteleket felulrol lefele vizsgalja a program.
    //
    // A kovetkezo leckeben ciklusokat tanulunk: for es while!

    return 0;
}

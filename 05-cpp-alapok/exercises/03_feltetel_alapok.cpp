/*
=============================================================
3. LECKE: Feltételek — döntés a programban
Futtasd: a böngészőben a Futtatás gombbal
=============================================================
*/

#include <iostream>
#include <string>
using namespace std;

// ============================================================
// MIÉRT KELLENEK FELTÉTELEK?
// ============================================================

// Képzeld el, hogy a programod egy utat jár be.
// Eddig ez az út egyenes volt — minden sor lefutott, sorban.
//
// De az életben is döntéseket hozunk:
//   "Ha esik az eső, viszek esernyőt. Különben nem."
//
// A programban PONTOSAN így működik a feltétel:
//   if (feltétel) { csinálj valamit; }
//   else { csinálj mást; }
//
// A feltétel vagy IGAZ (true), vagy HAMIS (false).
// Ez alapján dönt a program, melyik úton menjen tovább.

int main() {

    // ============================================================
    // 1. EGYSZERŰ IF — "ha igaz, csináld meg"
    // ============================================================

    // Az `if` a legegyszerűbb feltétel.
    // Ha a zárójelben lévő dolog IGAZ, végrehajtja a kapcsos zárójelek közötti kódot.
    // Ha HAMIS, átugorja.

    int age = 16;

    if (age >= 18) {
        cout << "Felnőtt vagy, mehetsz szavazni!" << endl;
    }

    // Ez NEM fog kiíródni, mert 16 < 18, tehát a feltétel HAMIS.
    // Próbáld meg átírni az age-et 20-ra és futtasd újra!

    // ============================================================
    // 2. IF-ELSE — "ha igaz, ezt csináld, különben azt"
    // ============================================================

    // Az `else` ág akkor fut le, ha a feltétel HAMIS.
    // Így mindig történik VALAMI — vagy az if, vagy az else.

    int temperature = 35;

    if (temperature > 30) {
        cout << "Nagyon meleg van! (" << temperature << " fok)" << endl;
    } else {
        cout << "Elfogadható a hőmérséklet. (" << temperature << " fok)" << endl;
    }

    // Gondolj rá úgy: ez egy elágazás az úton.
    // Vagy balra mész (if), vagy jobbra (else). De valamelyikre MINDIG.

    // ============================================================
    // 3. ÖSSZEHASONLÍTÓ OPERÁTOROK
    // ============================================================

    // Ezekkel az operátorokkal hasonlítunk össze két értéket:
    //
    //   ==   egyenlő-e?          (VIGYÁZZ: két egyenlőség jel!)
    //   !=   nem egyenlő-e?
    //   >    nagyobb?
    //   <    kisebb?
    //   >=   nagyobb vagy egyenlő?
    //   <=   kisebb vagy egyenlő?
    //
    // **GYAKORI HIBA**: egy `=` az ÉRTÉKADÁS, két `==` az ÖSSZEHASONLÍTÁS!
    //   age = 18   → "legyen 18"      (értékadás)
    //   age == 18  → "egyenlő 18-cal?" (kérdés)

    int score = 75;

    cout << endl;
    if (score == 100) {
        cout << "Tökéletes pontszám!" << endl;
    } else if (score >= 80) {
        cout << "Nagyon jó eredmény!" << endl;
    } else if (score >= 60) {
        cout << "Átment!" << endl;
    } else {
        cout << "Sajnos nem ment át." << endl;
    }

    // Itt a válasz: "Átment!" — mert 75 >= 60 igaz.
    // Fontos: a program FELÜLRŐL LEFELÉ vizsgálja a feltételeket,
    // és az ELSŐ igaz ágat hajtja végre, a többit átugorja!

    // ============================================================
    // 4. ELSE IF — több lehetőség
    // ============================================================

    // Az `else if` segítségével több ágat is létre tudsz hozni.
    // Olyan, mint egy többfelé elágazás:
    //   Ha A → csinálj X-et
    //   Különben ha B → csinálj Y-t
    //   Különben ha C → csinálj Z-t
    //   Különben → csinálj valami mást

    int hour = 14;

    cout << endl;
    if (hour < 6) {
        cout << "Jó éjszakát!" << endl;
    } else if (hour < 12) {
        cout << "Jó reggelt!" << endl;
    } else if (hour < 18) {
        cout << "Jó napot!" << endl;
    } else {
        cout << "Jó estét!" << endl;
    }

    // 14 óra → "Jó napot!" (mert 14 >= 12 és 14 < 18)

    // ============================================================
    // 5. LOGIKAI OPERÁTOROK — feltételeket kötni össze
    // ============================================================

    // Néha több feltételt is vizsgálni akarunk egyszerre:
    //
    //   &&  — ÉS (and): MINDKÉT feltételnek igaznak kell lennie
    //   ||  — VAGY (or): LEGALÁBB az egyiknek igaznak kell lennie
    //   !   — NEM (not): megfordítja: igazból hamis lesz, hamisból igaz
    //
    // Hasonlat:
    //   && = "Elmegyek sétálni, HA szép az idő ÉS van időm"
    //   || = "Boldog vagyok, HA nyaralok VAGY fagylaltot eszem"
    //   !  = "NEM esik az eső" (az ellenkezője)

    int user_age = 20;
    bool has_ticket = true;

    cout << endl;
    if (user_age >= 18 && has_ticket) {
        cout << "Beléphet a koncertre!" << endl;
    } else {
        cout << "Nem léphet be." << endl;
    }

    // Mindkettő igaz (20 >= 18 ÉS van jegye), tehát beléphet.

    bool is_weekend = true;
    bool is_holiday = false;

    if (is_weekend || is_holiday) {
        cout << "Szabad nap — pihenj!" << endl;
    } else {
        cout << "Munkanap — hajrá!" << endl;
    }

    // ============================================================
    // 6. SWITCH — választás több fix érték közül
    // ============================================================

    // Ha egy változó értékét KONKRÉT értékekhez hasonlítod
    // (pl. 1, 2, 3), a `switch` áttekinthetőbb, mint sok else if.
    //
    // Gondolj rá, mint egy automatára:
    //   Nyomd meg az 1-est → kapj kávét
    //   Nyomd meg a 2-est → kapj teát
    //   Nyomd meg a 3-ast → kapj vizet
    //   Bármi más → "ismeretlen gomb"

    int day = 3;

    cout << endl;
    switch (day) {
        case 1:
            cout << "Hétfő" << endl;
            break;  // FONTOS! break nélkül "lecsúszik" a következőre!
        case 2:
            cout << "Kedd" << endl;
            break;
        case 3:
            cout << "Szerda" << endl;
            break;
        case 4:
            cout << "Csütörtök" << endl;
            break;
        case 5:
            cout << "Péntek" << endl;
            break;
        default:
            cout << "Hétvége!" << endl;
            break;
    }

    // A `break` KÖTELEZŐ minden `case` végén!
    // Nélküle a program "átfolyik" a következő case-be
    // (ez egy C++ sajátosság, és gyakori hibaforrás).

    // ============================================================
    // ÖSSZEFOGLALÁS
    // ============================================================

    // Amit ma megtanultál:
    //
    // | Szerkezet      | Mikor használd                      |
    // |----------------|-------------------------------------|
    // | if             | Egyetlen feltétel vizsgálata         |
    // | if-else        | Két lehetőség közül választás       |
    // | else if        | Több lehetőség (láncolt feltételek) |
    // | switch-case    | Fix értékek közül választás          |
    // | &&, ||, !      | Feltételek összekötése              |
    //
    // Fontos:
    // - `==` az összehasonlítás, `=` az értékadás — ne keverd!
    // - `switch`-ben mindig írj `break`-et!
    // - A feltételeket felülről lefelé vizsgálja a program.
    //
    // A következő leckében ciklusokat tanulunk: for és while!

    return 0;
}

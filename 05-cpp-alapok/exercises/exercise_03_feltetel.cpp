/*
=============================================================
GYAKORLO FELADATOK — C++ feltetelek (if/else, switch)
=============================================================
*/

// @TASK 1. Paros vagy paratlan?
// @DESC A `number` valtozo erteke **7**. Ird meg az if-else feltetelt:
// ha paros → irasd ki **"Paros"**, ha paratlan → irasd ki **"Paratlan"**.
// @HINT A `%` (modulo) operator megadja az osztas maradekat. Ha `number % 2 == 0`, akkor paros!
// @CODE
#include <iostream>
using namespace std;
int main() {
    int number = 7;

    // MEGOLDAS IDE:

    return 0;
}
// @END

// @TASK 2. Jegyezes
// @DESC A `points` valtozo erteke **73**. Allitsd be a `grade` valtozot:
// 90-100 → "Jeles", 75-89 → "Jo", 60-74 → "Kozepes", 40-59 → "Elegseges", 0-39 → "Elegtelen".
// Vegul irasd ki a `grade`-et!
// @HINT Hasznalj `if / else if / else` lancot, felulrol lefele: `if (points >= 90) { ... } else if ...`
// @CODE
#include <iostream>
#include <string>
using namespace std;
int main() {
    int points = 73;
    string grade = "";

    // MEGOLDAS IDE:

    // ELLENORZES:
    if (grade == "Kozepes") {
        cout << "✓ OK — 73 pont = " << grade << endl;
    } else {
        cout << "✗ 73 pont = Kozepes kene legyen! Kaptam: \"" << grade << "\"" << endl;
    }
    return 0;
}
// @END

// @TASK 3. Beleptetes
// @DESC Ket valtozo: `visitor_age` (22) es `has_id` (true).
// Ha 18 vagy idosebb **ES** van igazolvanya → irasd ki **"Belephet"**, kulonben **"Nem lephet be"**.
// @HINT Hasznald az `&&` (ES) operatort: `if (visitor_age >= 18 && has_id)`
// @CODE
#include <iostream>
using namespace std;
int main() {
    int visitor_age = 22;
    bool has_id = true;

    // MEGOLDAS IDE:

    return 0;
}
// @END

// @TASK 4. Evszak meghatarozasa
// @DESC A `month` valtozo erteke **8** (augusztus). Hasznalj **switch**-et es allitsd be a `season`-t:
// 12,1,2 → "Tel" | 3,4,5 → "Tavasz" | 6,7,8 → "Nyar" | 9,10,11 → "Osz"
// @HINT Tobb case-t is irhatsz egymas ala break nelkul: `case 6: case 7: case 8: season = "Nyar"; break;`
// @CODE
#include <iostream>
#include <string>
using namespace std;
int main() {
    int month = 8;
    string season = "";

    // MEGOLDAS IDE:

    // ELLENORZES:
    if (season == "Nyar") {
        cout << "✓ OK — 8. honap = " << season << endl;
    } else {
        cout << "✗ Augusztus = Nyar! Kaptam: \"" << season << "\"" << endl;
    }
    return 0;
}
// @END

// @TASK 5. Korkategoria
// @DESC A `cat_age` erteke **10**. Allitsd be a `category` valtozot:
// 0-2 → "Csecsemo" | 3-5 → "Ovodas" | 6-14 → "Iskolas" | 15-17 → "Tinedzser" | 18+ → "Felnott"
// @HINT Hasznalj `else if` lancot: `if (cat_age <= 2) { ... } else if (cat_age <= 5) { ... }`
// @CODE
#include <iostream>
#include <string>
using namespace std;
int main() {
    int cat_age = 10;
    string category = "";

    // MEGOLDAS IDE:

    // ELLENORZES:
    if (category == "Iskolas") {
        cout << "✓ OK — 10 eves = " << category << endl;
    } else {
        cout << "✗ 10 eves = Iskolas! Kaptam: \"" << category << "\"" << endl;
    }
    return 0;
}
// @END

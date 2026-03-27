/*
=============================================================
GYAKORLÓ FELADATOK — C++ feltételek (if/else, switch)
=============================================================
*/

// @TASK 1. Páros vagy páratlan?
// @DESC A `number` változó értéke **7**. Írd meg az if-else feltételt:
// ha páros → írasd ki **"Páros"**, ha páratlan → írasd ki **"Páratlan"**.
// @HINT A `%` (modulo) operátor megadja az osztás maradékát. Ha `number % 2 == 0`, akkor páros!
// @CODE
#include <iostream>
using namespace std;
int main() {
    int number = 7;

    // MEGOLDÁS IDE:

    return 0;
}
// @END

// @TASK 2. Jegyezés
// @DESC A `points` változó értéke **73**. Állítsd be a `grade` változót:
// 90-100 → "Jeles", 75-89 → "Jó", 60-74 → "Közepes", 40-59 → "Elégséges", 0-39 → "Elégtelen".
// Végül írasd ki a `grade`-et!
// @HINT Használj `if / else if / else` láncot, felülről lefelé: `if (points >= 90) { ... } else if ...`
// @CODE
#include <iostream>
#include <string>
using namespace std;
int main() {
    int points = 73;
    string grade = "";

    // MEGOLDÁS IDE:

    // ELLENŐRZÉS:
    if (grade == "Közepes") {
        cout << "✓ OK — 73 pont = " << grade << endl;
    } else {
        cout << "✗ 73 pont = Közepes kéne legyen! Kaptam: \"" << grade << "\"" << endl;
    }
    return 0;
}
// @END

// @TASK 3. Beléptetés
// @DESC Két változó: `visitor_age` (22) és `has_id` (true).
// Ha 18 vagy idősebb **ÉS** van igazolványa → írasd ki **"Beléphet"**, különben **"Nem léphet be"**.
// @HINT Használd az `&&` (ÉS) operátort: `if (visitor_age >= 18 && has_id)`
// @CODE
#include <iostream>
using namespace std;
int main() {
    int visitor_age = 22;
    bool has_id = true;

    // MEGOLDÁS IDE:

    return 0;
}
// @END

// @TASK 4. Évszak meghatározása
// @DESC A `month` változó értéke **8** (augusztus). Használj **switch**-et és állítsd be a `season`-t:
// 12,1,2 → "Tél" | 3,4,5 → "Tavasz" | 6,7,8 → "Nyár" | 9,10,11 → "Ősz"
// @HINT Több case-t is írhatsz egymás alá break nélkül: `case 6: case 7: case 8: season = "Nyár"; break;`
// @CODE
#include <iostream>
#include <string>
using namespace std;
int main() {
    int month = 8;
    string season = "";

    // MEGOLDÁS IDE:

    // ELLENŐRZÉS:
    if (season == "Nyár") {
        cout << "✓ OK — 8. hónap = " << season << endl;
    } else {
        cout << "✗ Augusztus = Nyár! Kaptam: \"" << season << "\"" << endl;
    }
    return 0;
}
// @END

// @TASK 5. Korkategória
// @DESC A `cat_age` értéke **10**. Állítsd be a `category` változót:
// 0-2 → "Csecsemő" | 3-5 → "Óvodás" | 6-14 → "Iskolás" | 15-17 → "Tinédzser" | 18+ → "Felnőtt"
// @HINT Használj `else if` láncot: `if (cat_age <= 2) { ... } else if (cat_age <= 5) { ... }`
// @CODE
#include <iostream>
#include <string>
using namespace std;
int main() {
    int cat_age = 10;
    string category = "";

    // MEGOLDÁS IDE:

    // ELLENŐRZÉS:
    if (category == "Iskolás") {
        cout << "✓ OK — 10 éves = " << category << endl;
    } else {
        cout << "✗ 10 éves = Iskolás! Kaptam: \"" << category << "\"" << endl;
    }
    return 0;
}
// @END

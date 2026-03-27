/*
=============================================================
GYAKORLO FELADATOK — C++ ciklusok (for, while)
=============================================================
*/

// @TASK 1. Szamolas 1-tol 10-ig
// @DESC Irj egy **for ciklust**, ami osszeadja a szamokat 1-tol 10-ig a `sum` valtozoba.
// A vart eredmeny: **sum = 55** (1+2+3+...+10)
// @HINT `for (int i = 1; i <= 10; i++) { sum = sum + i; }`
// @CODE
#include <iostream>
using namespace std;
int main() {
    int sum = 0;

    // MEGOLDAS IDE:

    // ELLENORZES:
    if (sum == 55) {
        cout << "✓ OK — sum = " << sum << endl;
    } else {
        cout << "✗ Vart: 55, kaptam: " << sum << endl;
    }
    return 0;
}
// @END

// @TASK 2. Paros szamok osszege
// @DESC Irj egy for ciklust 1-tol 20-ig, de **csak a paros szamokat** add hozza az `even_sum`-hoz.
// Vart eredmeny: **even_sum = 110** (2+4+6+...+20)
// @HINT A cikluson belul hasznalj if-et: `if (i % 2 == 0) { even_sum = even_sum + i; }`
// @CODE
#include <iostream>
using namespace std;
int main() {
    int even_sum = 0;

    // MEGOLDAS IDE:

    // ELLENORZES:
    if (even_sum == 110) {
        cout << "✓ OK — even_sum = " << even_sum << endl;
    } else {
        cout << "✗ Vart: 110, kaptam: " << even_sum << endl;
    }
    return 0;
}
// @END

// @TASK 3. Visszaszamlalas
// @DESC Irj egy for ciklust, ami **10-tol 1-ig** szamol visszafele, es osszeepiti a `countdown` stringet.
// Vart eredmeny: **"10 9 8 7 6 5 4 3 2 1 "**
// @HINT `for (int i = 10; i >= 1; i--) { countdown = countdown + to_string(i) + " "; }`
// A `to_string()` szamma alakit egy szamot szovegge.
// @CODE
#include <iostream>
#include <string>
using namespace std;
int main() {
    string countdown = "";

    // MEGOLDAS IDE:

    // ELLENORZES:
    if (countdown == "10 9 8 7 6 5 4 3 2 1 ") {
        cout << "✓ OK — " << countdown << endl;
    } else {
        cout << "✗ Vart: \"10 9 8 7 6 5 4 3 2 1 \"" << endl;
        cout << "  Kaptam: \"" << countdown << "\"" << endl;
    }
    return 0;
}
// @END

// @TASK 4. Duplazas while ciklussal
// @DESC A `power` valtozo erteke **1**. Irj egy **while ciklust**, ami addig duplazza
// (szorozza 2-vel), amig el nem eri az **1000**-et. Szamold a lepeseket a `steps`-be!
// Vart: **power = 1024**, **steps = 10**
// @HINT `while (power < 1000) { power = power * 2; steps++; }` — a `steps++` novel eggyel.
// @CODE
#include <iostream>
using namespace std;
int main() {
    int power = 1;
    int steps = 0;

    // MEGOLDAS IDE:

    // ELLENORZES:
    if (power == 1024 && steps == 10) {
        cout << "✓ OK — 2^" << steps << " = " << power << endl;
    } else {
        cout << "✗ Vart: power=1024, steps=10" << endl;
        cout << "  Kaptam: power=" << power << ", steps=" << steps << endl;
    }
    return 0;
}
// @END

// @TASK 5. Csillag piramis
// @DESC Irj **ket egymasba agyazott for ciklust**, ami felépiti a `pyramid` stringet:
// `*`, `**`, `***`, `****`, `*****` (minden sor vegen ujsor).
// A kulso ciklus a sorok (1-5), a belso annyi `*`-ot ir, ahany a sorszam.
// @HINT A kulso: `for (int row = 1; row <= 5; row++)`,
// belso: `for (int col = 1; col <= row; col++) { pyramid = pyramid + "*"; }`
// Minden sor utan: `pyramid = pyramid + "\n";`
// @CODE
#include <iostream>
#include <string>
using namespace std;
int main() {
    string pyramid = "";

    // MEGOLDAS IDE:

    // ELLENORZES:
    string expected = "*\n**\n***\n****\n*****\n";
    if (pyramid == expected) {
        cout << "✓ OK" << endl;
        cout << pyramid;
    } else {
        cout << "✗ Nem stimmel a piramis!" << endl;
        cout << "Kaptam:" << endl << pyramid;
    }
    return 0;
}
// @END

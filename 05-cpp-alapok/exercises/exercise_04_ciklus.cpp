/*
=============================================================
GYAKORLÓ FELADATOK — C++ ciklusok (for, while)
=============================================================
*/

// @TASK 1. Számolás 1-től 10-ig
// @DESC Írj egy **for ciklust**, ami összeadja a számokat 1-től 10-ig a `sum` változóba.
// A várt eredmény: **sum = 55** (1+2+3+...+10)
// @HINT `for (int i = 1; i <= 10; i++) { sum = sum + i; }`
// @CODE
#include <iostream>
using namespace std;
int main() {
    int sum = 0;

    // MEGOLDÁS IDE:

    // ELLENŐRZÉS:
    if (sum == 55) {
        cout << "✓ OK — sum = " << sum << endl;
    } else {
        cout << "✗ Várt: 55, kaptam: " << sum << endl;
    }
    return 0;
}
// @END

// @TASK 2. Páros számok összege
// @DESC Írj egy for ciklust 1-től 20-ig, de **csak a páros számokat** add hozzá az `even_sum`-hoz.
// Várt eredmény: **even_sum = 110** (2+4+6+...+20)
// @HINT A cikluson belül használj if-et: `if (i % 2 == 0) { even_sum = even_sum + i; }`
// @CODE
#include <iostream>
using namespace std;
int main() {
    int even_sum = 0;

    // MEGOLDÁS IDE:

    // ELLENŐRZÉS:
    if (even_sum == 110) {
        cout << "✓ OK — even_sum = " << even_sum << endl;
    } else {
        cout << "✗ Várt: 110, kaptam: " << even_sum << endl;
    }
    return 0;
}
// @END

// @TASK 3. Visszaszámlálás
// @DESC Írj egy for ciklust, ami **10-től 1-ig** számol visszafelé, és összeépíti a `countdown` stringet.
// Várt eredmény: **"10 9 8 7 6 5 4 3 2 1 "**
// @HINT `for (int i = 10; i >= 1; i--) { countdown = countdown + to_string(i) + " "; }`
// A `to_string()` számot alakít szöveggé.
// @CODE
#include <iostream>
#include <string>
using namespace std;
int main() {
    string countdown = "";

    // MEGOLDÁS IDE:

    // ELLENŐRZÉS:
    if (countdown == "10 9 8 7 6 5 4 3 2 1 ") {
        cout << "✓ OK — " << countdown << endl;
    } else {
        cout << "✗ Várt: \"10 9 8 7 6 5 4 3 2 1 \"" << endl;
        cout << "  Kaptam: \"" << countdown << "\"" << endl;
    }
    return 0;
}
// @END

// @TASK 4. Duplázás while ciklussal
// @DESC A `power` változó értéke **1**. Írj egy **while ciklust**, ami addig duplázza
// (szorozza 2-vel), amíg el nem éri az **1000**-et. Számold a lépéseket a `steps`-be!
// Várt: **power = 1024**, **steps = 10**
// @HINT `while (power < 1000) { power = power * 2; steps++; }` — a `steps++` növel eggyel.
// @CODE
#include <iostream>
using namespace std;
int main() {
    int power = 1;
    int steps = 0;

    // MEGOLDÁS IDE:

    // ELLENŐRZÉS:
    if (power == 1024 && steps == 10) {
        cout << "✓ OK — 2^" << steps << " = " << power << endl;
    } else {
        cout << "✗ Várt: power=1024, steps=10" << endl;
        cout << "  Kaptam: power=" << power << ", steps=" << steps << endl;
    }
    return 0;
}
// @END

// @TASK 5. Csillag piramis
// @DESC Írj **két egymásba ágyazott for ciklust**, ami felépíti a `pyramid` stringet:
// `*`, `**`, `***`, `****`, `*****` (minden sor végén újsor).
// A külső ciklus a sorok (1-5), a belső annyi `*`-ot ír, ahány a sorszám.
// @HINT A külső: `for (int row = 1; row <= 5; row++)`,
// belső: `for (int col = 1; col <= row; col++) { pyramid = pyramid + "*"; }`
// Minden sor után: `pyramid = pyramid + "\n";`
// @CODE
#include <iostream>
#include <string>
using namespace std;
int main() {
    string pyramid = "";

    // MEGOLDÁS IDE:

    // ELLENŐRZÉS:
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

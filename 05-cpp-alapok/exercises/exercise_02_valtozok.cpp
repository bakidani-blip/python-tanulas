/*
=============================================================
GYAKORLO FELADATOK — C++ valtozok es tipusok
=============================================================
*/

// @TASK 1. Egesz szam valtozo
// @DESC Hozz letre egy `my_age` nevu **int** valtozot a koroddal, es irasd ki!
// @HINT `int my_age = 25;` majd `cout << my_age << endl;`
// @CODE
#include <iostream>
using namespace std;
int main() {
    // MEGOLDAS IDE:

    // ELLENORZES:
    if (my_age > 0 && my_age < 120) {
        cout << "✓ OK — my_age = " << my_age << endl;
    } else {
        cout << "✗ Adj meg valos kort!" << endl;
    }
    return 0;
}
// @END

// @TASK 2. Tort szam
// @DESC Hozz letre egy `my_height` nevu **double** valtozot a magassagoddal meterben (pl. `1.72`), es irasd ki!
// @HINT `double my_height = 1.72;`
// @CODE
#include <iostream>
using namespace std;
int main() {
    // MEGOLDAS IDE:

    // ELLENORZES:
    if (my_height > 0.5 && my_height < 2.5) {
        cout << "✓ OK — my_height = " << my_height << " m" << endl;
    } else {
        cout << "✗ Adj meg valos magassagot meterben!" << endl;
    }
    return 0;
}
// @END

// @TASK 3. Szoveg valtozo
// @DESC Hozz letre egy `my_name` nevu **string** valtozot a neveddel, es irasd ki!
// Ne felejtsd el: `#include <string>` is kell a programba!
// @HINT `string my_name = "Kata";`
// @CODE
#include <iostream>
#include <string>
using namespace std;
int main() {
    // MEGOLDAS IDE:

    // ELLENORZES:
    if (my_name.length() > 0) {
        cout << "✓ OK — my_name = \"" << my_name << "\"" << endl;
    } else {
        cout << "✗ Ne hagyd uresen a neved!" << endl;
    }
    return 0;
}
// @END

// @TASK 4. Bemutatkozas valtozokkal
// @DESC Hozz letre egy `name` (string) es egy `age` (int) valtozot.
// Irasd ki egy sorban: **"Szia! Nevem [nev], [kor] eves vagyok."**
// A valtozokat a `<<` operatorral fuzd bele!
// @HINT `cout << "Szia! Nevem " << name << ", " << age << " eves vagyok." << endl;`
// @CODE
#include <iostream>
#include <string>
using namespace std;
int main() {
    // MEGOLDAS IDE:

    return 0;
}
// @END

// @TASK 5. Szamolas
// @DESC Hozz letre ket int valtozot: `a` erteke **15**, `b` erteke **4**.
// Irasd ki harom kulon sorba az **osszeget**, **kulonbseget** es **szorzatot**!
// Pelda kimenet: "Osszeg: 19"
// @HINT Az osszeg: `a + b`, kulonbseg: `a - b`, szorzat: `a * b`
// @CODE
#include <iostream>
using namespace std;
int main() {
    // MEGOLDAS IDE:

    // ELLENORZES:
    if (a == 15 && b == 4) {
        cout << "✓ OK — a=" << a << ", b=" << b << endl;
    } else {
        cout << "✗ a legyen 15, b legyen 4!" << endl;
    }
    return 0;
}
// @END

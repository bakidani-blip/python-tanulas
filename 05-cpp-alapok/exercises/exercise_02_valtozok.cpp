/*
=============================================================
GYAKORLÓ FELADATOK — C++ változók és típusok
=============================================================
*/

// @TASK 1. Egész szám változó
// @DESC Hozz létre egy `my_age` nevű **int** változót a koroddal, és írasd ki!
// @HINT `int my_age = 25;` majd `cout << my_age << endl;`
// @CODE
#include <iostream>
using namespace std;
int main() {
    // MEGOLDÁS IDE:

    // ELLENŐRZÉS:
    if (my_age > 0 && my_age < 120) {
        cout << "✓ OK — my_age = " << my_age << endl;
    } else {
        cout << "✗ Adj meg valós kort!" << endl;
    }
    return 0;
}
// @END

// @TASK 2. Tört szám
// @DESC Hozz létre egy `my_height` nevű **double** változót a magasságoddal méterben (pl. `1.72`), és írasd ki!
// @HINT `double my_height = 1.72;`
// @CODE
#include <iostream>
using namespace std;
int main() {
    // MEGOLDÁS IDE:

    // ELLENŐRZÉS:
    if (my_height > 0.5 && my_height < 2.5) {
        cout << "✓ OK — my_height = " << my_height << " m" << endl;
    } else {
        cout << "✗ Adj meg valós magasságot méterben!" << endl;
    }
    return 0;
}
// @END

// @TASK 3. Szöveg változó
// @DESC Hozz létre egy `my_name` nevű **string** változót a neveddel, és írasd ki!
// Ne felejtsd el: `#include <string>` is kell a programba!
// @HINT `string my_name = "Kata";`
// @CODE
#include <iostream>
#include <string>
using namespace std;
int main() {
    // MEGOLDÁS IDE:

    // ELLENŐRZÉS:
    if (my_name.length() > 0) {
        cout << "✓ OK — my_name = \"" << my_name << "\"" << endl;
    } else {
        cout << "✗ Ne hagyd üresen a neved!" << endl;
    }
    return 0;
}
// @END

// @TASK 4. Bemutatkozás változókkal
// @DESC Hozz létre egy `name` (string) és egy `age` (int) változót.
// Írasd ki egy sorban: **"Szia! Nevem [név], [kor] éves vagyok."**
// A változókat a `<<` operátorral fűzd bele!
// @HINT `cout << "Szia! Nevem " << name << ", " << age << " éves vagyok." << endl;`
// @CODE
#include <iostream>
#include <string>
using namespace std;
int main() {
    // MEGOLDÁS IDE:

    return 0;
}
// @END

// @TASK 5. Számolás
// @DESC Hozz létre két int változót: `a` értéke **15**, `b` értéke **4**.
// Írasd ki három külön sorba az **összeget**, **különbséget** és **szorzatot**!
// Példa kimenet: "Összeg: 19"
// @HINT Az összeg: `a + b`, különbség: `a - b`, szorzat: `a * b`
// @CODE
#include <iostream>
using namespace std;
int main() {
    // MEGOLDÁS IDE:

    // ELLENŐRZÉS:
    if (a == 15 && b == 4) {
        cout << "✓ OK — a=" << a << ", b=" << b << endl;
    } else {
        cout << "✗ a legyen 15, b legyen 4!" << endl;
    }
    return 0;
}
// @END

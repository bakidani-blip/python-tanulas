/*
=============================================================
GYAKORLO FELADATOK — C++ fuggvenyek
=============================================================
*/

// @TASK 1. Teglalap terulete
// @DESC Irj egy `rectangle_area` nevu fuggvenyt, ami kap ket **int** parametert
// (`width` es `height`) es **visszaadja** a teruletüket (szelesseg * magassag).
// @HINT `int rectangle_area(int width, int height) { return width * height; }`
// @CODE
#include <iostream>
using namespace std;

// MEGOLDAS IDE (a fuggvenyt a main ELE ird!):


int main() {
    // ELLENORZES:
    if (rectangle_area(5, 3) == 15 && rectangle_area(10, 10) == 100) {
        cout << "✓ OK — rectangle_area(5,3) = " << rectangle_area(5,3) << endl;
    } else {
        cout << "✗ rectangle_area(5,3) = 15 kene legyen!" << endl;
    }
    return 0;
}
// @END

// @TASK 2. Nagyobb szam
// @DESC Irj egy `bigger` nevu fuggvenyt, ami kap ket **int**-et (`a` es `b`)
// es **visszaadja a nagyobbat** a ketto kozul.
// @HINT Hasznalj if-else-t: `if (a >= b) { return a; } else { return b; }`
// @CODE
#include <iostream>
using namespace std;

// MEGOLDAS IDE:


int main() {
    // ELLENORZES:
    if (bigger(10, 7) == 10 && bigger(3, 9) == 9 && bigger(5, 5) == 5) {
        cout << "✓ OK — bigger(10,7) = " << bigger(10,7) << endl;
    } else {
        cout << "✗ bigger(10,7) = 10, bigger(3,9) = 9 kene legyen!" << endl;
    }
    return 0;
}
// @END

// @TASK 3. Udvozlo uzenet
// @DESC Irj egy `create_greeting` nevu fuggvenyt, ami kap egy **string** parametert (`name`)
// es **visszaad egy stringet**: `"Udvozollek, [name]!"`
// @HINT `string create_greeting(string name) { return "Udvozollek, " + name + "!"; }`
// @CODE
#include <iostream>
#include <string>
using namespace std;

// MEGOLDAS IDE:


int main() {
    // ELLENORZES:
    if (create_greeting("Kata") == "Udvozollek, Kata!") {
        cout << "✓ OK — " << create_greeting("Kata") << endl;
    } else {
        cout << "✗ create_greeting(\"Kata\") = \"Udvozollek, Kata!\" kene legyen!" << endl;
    }
    return 0;
}
// @END

// @TASK 4. Oszthato-e?
// @DESC Irj egy `is_divisible` nevu fuggvenyt, ami kap ket **int**-et (`number` es `divisor`)
// es visszaad **true**-t ha `number` oszthato `divisor`-ral, kulonben **false**-t.
// @HINT `bool is_divisible(int number, int divisor) { return number % divisor == 0; }`
// @CODE
#include <iostream>
using namespace std;

// MEGOLDAS IDE:


int main() {
    // ELLENORZES:
    if (is_divisible(10, 5) == true && is_divisible(10, 3) == false) {
        cout << "✓ OK — is_divisible(10,5)=true, is_divisible(10,3)=false" << endl;
    } else {
        cout << "✗ Hasznald: return number % divisor == 0;" << endl;
    }
    return 0;
}
// @END

// @TASK 5. Faktorialis
// @DESC Irj egy `factorial` nevu fuggvenyt, ami kap egy **int** `n`-et
// es visszaadja **n!** erteket (1 * 2 * 3 * ... * n).
// Pelda: `factorial(5)` → **120**
// @HINT Hasznalj for ciklust: `int result = 1; for (int i = 1; i <= n; i++) { result = result * i; } return result;`
// @CODE
#include <iostream>
using namespace std;

// MEGOLDAS IDE:


int main() {
    // ELLENORZES:
    if (factorial(5) == 120 && factorial(1) == 1 && factorial(3) == 6) {
        cout << "✓ OK — factorial(5) = " << factorial(5) << endl;
    } else {
        cout << "✗ factorial(5) = 120, factorial(3) = 6 kene legyen!" << endl;
    }
    return 0;
}
// @END

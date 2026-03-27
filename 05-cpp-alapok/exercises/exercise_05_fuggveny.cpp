/*
=============================================================
GYAKORLÓ FELADATOK — C++ függvények
=============================================================
*/

// @TASK 1. Téglalap területe
// @DESC Írj egy `rectangle_area` nevű függvényt, ami kap két **int** paramétert
// (`width` és `height`) és **visszaadja** a területüket (szélesség * magasság).
// @HINT `int rectangle_area(int width, int height) { return width * height; }`
// @CODE
#include <iostream>
using namespace std;

// MEGOLDÁS IDE (a függvényt a main ELÉ írd!):


int main() {
    // ELLENŐRZÉS:
    if (rectangle_area(5, 3) == 15 && rectangle_area(10, 10) == 100) {
        cout << "✓ OK — rectangle_area(5,3) = " << rectangle_area(5,3) << endl;
    } else {
        cout << "✗ rectangle_area(5,3) = 15 kéne legyen!" << endl;
    }
    return 0;
}
// @END

// @TASK 2. Nagyobb szám
// @DESC Írj egy `bigger` nevű függvényt, ami kap két **int**-et (`a` és `b`)
// és **visszaadja a nagyobbat** a kettő közül.
// @HINT Használj if-else-t: `if (a >= b) { return a; } else { return b; }`
// @CODE
#include <iostream>
using namespace std;

// MEGOLDÁS IDE:


int main() {
    // ELLENŐRZÉS:
    if (bigger(10, 7) == 10 && bigger(3, 9) == 9 && bigger(5, 5) == 5) {
        cout << "✓ OK — bigger(10,7) = " << bigger(10,7) << endl;
    } else {
        cout << "✗ bigger(10,7) = 10, bigger(3,9) = 9 kéne legyen!" << endl;
    }
    return 0;
}
// @END

// @TASK 3. Üdvözlő üzenet
// @DESC Írj egy `create_greeting` nevű függvényt, ami kap egy **string** paramétert (`name`)
// és **visszaad egy stringet**: `"Üdvözöllek, [name]!"`
// @HINT `string create_greeting(string name) { return "Üdvözöllek, " + name + "!"; }`
// @CODE
#include <iostream>
#include <string>
using namespace std;

// MEGOLDÁS IDE:


int main() {
    // ELLENŐRZÉS:
    if (create_greeting("Kata") == "Üdvözöllek, Kata!") {
        cout << "✓ OK — " << create_greeting("Kata") << endl;
    } else {
        cout << "✗ create_greeting(\"Kata\") = \"Üdvözöllek, Kata!\" kéne legyen!" << endl;
    }
    return 0;
}
// @END

// @TASK 4. Osztható-e?
// @DESC Írj egy `is_divisible` nevű függvényt, ami kap két **int**-et (`number` és `divisor`)
// és visszaad **true**-t ha `number` osztható `divisor`-ral, különben **false**-t.
// @HINT `bool is_divisible(int number, int divisor) { return number % divisor == 0; }`
// @CODE
#include <iostream>
using namespace std;

// MEGOLDÁS IDE:


int main() {
    // ELLENŐRZÉS:
    if (is_divisible(10, 5) == true && is_divisible(10, 3) == false) {
        cout << "✓ OK — is_divisible(10,5)=true, is_divisible(10,3)=false" << endl;
    } else {
        cout << "✗ Használd: return number % divisor == 0;" << endl;
    }
    return 0;
}
// @END

// @TASK 5. Faktoriális
// @DESC Írj egy `factorial` nevű függvényt, ami kap egy **int** `n`-et
// és visszaadja **n!** értékét (1 * 2 * 3 * ... * n).
// Példa: `factorial(5)` → **120**
// @HINT Használj for ciklust: `int result = 1; for (int i = 1; i <= n; i++) { result = result * i; } return result;`
// @CODE
#include <iostream>
using namespace std;

// MEGOLDÁS IDE:


int main() {
    // ELLENŐRZÉS:
    if (factorial(5) == 120 && factorial(1) == 1 && factorial(3) == 6) {
        cout << "✓ OK — factorial(5) = " << factorial(5) << endl;
    } else {
        cout << "✗ factorial(5) = 120, factorial(3) = 6 kéne legyen!" << endl;
    }
    return 0;
}
// @END

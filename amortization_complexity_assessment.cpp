// The function calculates the length of the longest consecutive group of identical characters.

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

size_t max_consecutive_elements(const string &str) {
    size_t result = 0;
    size_t cur_letter_idx = 0;

    while (cur_letter_idx < str.size()) {
        size_t next_letter_idx = cur_letter_idx;
        while (next_letter_idx < str.size()
                && str[next_letter_idx] == str[cur_letter_idx]) {
            ++next_letter_idx;
        }
        result = max(result, next_letter_idx - cur_letter_idx);
        cur_letter_idx = next_letter_idx;
    }
    return result;
}

int main() {
    string str;
    cin >> str;

    cout << max_consecutive_elements(str) << endl;

    return 0;
}
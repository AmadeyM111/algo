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
    string test = "aaaabbbcc";
    cout << "Max consecutive:" << max_consecutive_elements(test) << endl;
    return 0;
}
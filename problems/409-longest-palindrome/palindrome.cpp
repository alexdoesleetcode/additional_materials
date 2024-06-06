#include <map>
#include <string>

using std::string;

class Solution {
public:
    int longestPalindrome(string s) {
        // Count how many times each character appears
        std::map<char, int> freq;
        for (char ch : s) {
            freq[ch]++;
        }
        // Count many pairs of characters are there
        int count = 0;
        for (auto it = freq.begin(); it != freq.end(); ++it) {
            int c = it->second;
            if (c % 2 == 0) {
                count += c;
            } else {
                count += c-1;
            }
        }
        // If there are letters leftover, use one for the middle
        if (count < s.length()) {
            count += 1;
        }
        return count;
    }
};

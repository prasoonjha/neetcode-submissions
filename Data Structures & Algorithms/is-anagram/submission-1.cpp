class Solution {
public:
    bool isAnagram(string s, string t) {
        int vector_s[26] {0};
        int vector_t[26] {0};
        for(char& c: s){
            int idx {static_cast<int>(c)-97};
            vector_s[idx] +=1;
        }
        for(char& c: t){
            int idx {static_cast<int>(c)-97};
            vector_t[idx] +=1;
        }
        for(int i=0; i<26; i++){
            if (vector_t[i] != vector_s[i]){
                return false;
            }
        }
        return true;
    }
};

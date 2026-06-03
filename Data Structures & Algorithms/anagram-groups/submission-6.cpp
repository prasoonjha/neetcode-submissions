class Solution {
public:
    string _toString(vector<int>& _input) {
        string res = "";
        for(auto i : _input){
            res+=to_string(i)+"#";
        }
        return res;
    }
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> _map;
        for(string& word : strs){
            vector<int> _count(26,0);
            for(char& c: word){
                _count[c-'a'] +=1;
            }
            string s = _toString(_count);
            _map[s].push_back(word);
        }
        vector<vector<string>> res;
        for (auto& pair : _map) {
            cout<<pair.first<<endl;
            res.push_back(pair.second);
        }
        return res;
    }
};

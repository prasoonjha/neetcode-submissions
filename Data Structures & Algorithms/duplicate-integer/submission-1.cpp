class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> _set;
        for(int i=0; i<nums.size(); i++){
            if(_set.contains(nums[i])){
                return true;
            }
            _set.insert(nums[i]);
        }
        return false;
    }
};
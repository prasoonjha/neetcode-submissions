class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int, bool> _map;
        for(int i=0; i<nums.size(); i++){
            if(_map.contains(nums[i])){
                return true;
            }
            _map[nums[i]] = true;
        }
        return false;
    }
};
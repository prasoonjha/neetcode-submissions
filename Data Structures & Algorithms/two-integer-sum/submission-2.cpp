class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        int x;
        int y;
        for(int i=0; i<nums.size(); i++){
            int diff = target-nums[i];
            if (seen.count(diff)){
                x = i;
                y = seen[diff];
            }
            seen[nums[i]] = i;
        }
        if (x<=y){
            return {x, y};
        }
        return {y, x};
    }
};

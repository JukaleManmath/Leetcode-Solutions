class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int,int> mp;
        for(int i : nums){
            mp[i]++;
        }
        int res;
        for(auto i: mp){
            if(i.second > (nums.size()/2)){
                res = i.first;
            }
        }
        return res;
    }
};
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0 , len = INT_MIN , n = s.length();
        unordered_map<char , int> mp;
        for(int r = 0 ; r < n ; r++){
            if(mp.count(s[r]) == 0 || mp[s[r]] < l){
                mp[s[r]] = r;
                len = max(len,r-l+1);
            }else{
               l = mp[s[r]] + 1;
               mp[s[r]] = r;
            }
        }
        return len == INT_MIN ? 0 : len;
    }
};
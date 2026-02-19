class Solution {
public:
    int countBinarySubstrings(string s) {
        int ans = 0;
        int one = 0, zero = 0;
        int n = s.size();
        int r = 0;
        while (r < n){
            while(r < n && s[r] == '0'){
                zero++;
                r++;
            }
            if (zero && one){
                ans += min(zero, one);
            }
            one = 0;
            while(r < n && s[r] == '1'){
                one++;
                r++;
            }
            if (zero && one){
                ans += min(zero, one);
            }

            zero = 0;

        }
        return ans;
    }
};
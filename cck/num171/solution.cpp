class Solution {
public:
    int titleToNumber(string s) {
        int res = 0;
        int len = s.size(); //string::size()同string::length()
        for(int i=0; i<len; i++) //从第一个字符到最后一个字符
        {
            int mult = 1; //26进制，在对应位置上要乘以mult
            for(int j=0; j<len - i -1; j++) //计算mult
            {
                mult *= 26;
            }
            res += (s[i] - 'A' +1) * mult; 
        }
        return res;
    }
};

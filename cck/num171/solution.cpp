class Solution {
public:
    int titleToNumber_1(string s) { //时间复杂度o(n^2)
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
    
    int titleToNumber_2(string s){
        int res = 0;
        for(int i=0; i<s.size(); i++)
        {
            res = res * 26 + (s[i] - 'A' +1);
        }
        return res;
    }
};

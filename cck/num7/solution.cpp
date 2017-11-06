class Solution {
public:
    int reverse(int x) {//15ms
        string num = to_string(abs(x));  //整数部分拆分为字符串
        long res = 0; //结果用长整形表示
        for(int i=0; i<num.size();i++){  
            res = res *10 + num[num.size()-i-1]-'0';
            if(res>0x7fffffff)  //如果超过int的最大值
                return 0;
        }
        if(x<0)
            res = -res;
        return (int)res;
    }
   
    int reverse_2(int x){
        long res = 0; //结果用长整形表示
        while(x){  
            res = res *10 + x % 10;
            x /= 10;
            if(res>(int)0x7fffffff||res<(int)0x80000000)  
            //如果超过int的最大值或小于int的最小值
                return 0;
        }
        return (int)res;
    }
};

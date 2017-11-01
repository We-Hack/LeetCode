class Solution {
public:
    int hammingDistance_1(int x, int y) {//3ms
	int temp = x ^ y;  //异或
        int count = 0;
        for(int i=0;i<32;i++)  
        {
            if(temp%2==1)  //除二计数
            {
            count++;
            }
            temp=temp/2;
        }  
        return count;  
    }

    int hammingDistance_2(int x, int y){ //3ms
        int temp = x ^ y;
        int count = 0;
        for(int i=0;i<32;i++)  //左移计数
        {
            if(temp&(1<<i))
            {
            count++;
            }
        }
        return count;   //beats 0.2858 submissions
    }
    
    int hammingDistance_3(int x, int y){ //6ms
        bitset<32> bs(x^y);
        return bs.count(); // beats 0.28
        }
};

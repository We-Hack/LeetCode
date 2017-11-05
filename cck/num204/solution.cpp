class Solution {
public:
    int countPrimesi_1(int n) { //29ms 
        if(n==0) return 0;
        bool isprime[n+1];//从0到n，下表也从0到n
        isprime[0] = false; //0不是质数
        isprime[1] = false;//1不是质数
        for(int i=2; i < n+1; i++){
            isprime[i] = true;  //假设2之后都是质数
        }
        int count = n-1; //n+1个数，目前有n-1个质数
        for(int i=2; i< n+1; i++){ 
            if(isprime[i]){  //只要i是质数
                for(int j=2*i; j<=n; j+=i){ //则2i, 3i ...不是质数
                    isprime[j] = false;
                    count--;
                }
            }
        }
    return count;
    }

    int countPrimes_2(int n) {
        if(n==0 || n==1) return 0;
        int count = 0;
        vector<bool> isprime(n,true);//从0到n-1，下表也从0到n-1
        isprime[0] = false; //0不是质数
        isprime[1] = false;//1不是质数
        for(int i=2; i< n; i++){ 
            if(isprime[i]){  //只要i是质数
                count++;
                if(i>sqrt(n)) continue;//防止i*i越界
                for(int j=i*i; j<n; j+=i){ //则i*i ,(i+1)*i...不是质数
                    isprime[j] = false;
                }
            }
        }
        return count;
    }
};

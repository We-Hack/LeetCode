class Solution {
public:
    vector<string> fizzBuzz(int n) {         
        vector<string> res(n,"");//等价于vector<string> res(n);
         for(int i=0; i<n; i++)
         {   
             if((i+1)%3==0)
                 res[i].append("Fizz");//等价于res[i]+="Fizz"
             if((i+1)%5==0)
                 res[i].append("Buzz");
             if(res[i]=="")//等价于if(!res[i].size())
                res[i]=to_string(i+1);
        }
        return res;
    }
};

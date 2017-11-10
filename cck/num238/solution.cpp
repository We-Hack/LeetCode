class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {//结果中的每个数都是之前的数与之后的数的积
        vector<int> forward(nums.size()),backward(nums.size());
        
        forward[0]=1;
        for(int i=1;i<nums.size();i++){
            forward[i] = forward[i-1] * nums[i-1];
        }
        backward[nums.size()-1]=1;
        for(int i=nums.size()-2;i>=0;i--){
            backward[i] = backward[i+1] * nums[i+1];
        }
        
        for(int i=0;i<nums.size();i++){
            forward[i] = forward[i]*backward[i];
        }
        return forward;
    }
   
};

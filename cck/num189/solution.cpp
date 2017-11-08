class Solution {
public:
    void rotate(vector<int>& nums, int k) {//19ms 时间o(n) 空间o(k)
        vector<int> cpy(nums); //a copy of nums
        k = k%nums.size();
        for(int i=0;i<k;i++){//把最后k个元素放到最前面
            nums[i] = cpy[nums.size() - k +i];
        }
        for(int i=k;i<nums.size();i++){
            nums[i] = cpy[i-k];
        }
    }
    void rotate_2(vector<int>& nums, int k) {//非常慢 480ms
        k = k%nums.size();
        for(int i=0; i<k; i++){ //每一轮让每个元素右移一个，移动K轮
            int temp = nums[nums.size()-1];
            for(int j=nums.size()-1;j>0;j--){
                nums[j] = nums[j-1];
            }
            nums[0] = temp;
        }
    }

    void rotate(vector<int>& nums, int k) {//19ms 时间o(n) 空间o(1)
        k = k % nums.size();
        reverse(nums.begin(),nums.end()-k);
        reverse(nums.end()-k,nums.end());
        reverse(nums.begin(),nums.end());
    }
};

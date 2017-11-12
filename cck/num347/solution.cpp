class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> freq;  //freq字典，key为数组里的元素，val为出现的次数
        for(int i=0;i<nums.size();i++){
            if(freq.count(nums[i])==0)
                freq[nums[i]] = 0;
            else
                freq[nums[i]] ++;
        }
        
        vector<int> res;
        priority_queue<pair<int,int>> pq; 
        for(auto it = freq.begin(); it != freq.end(); it++){
            pq.push(make_pair(it->second, it->first));
            if(pq.size() > (int)freq.size() - k){
                res.push_back(pq.top().second);
                pq.pop();
            }
        }
        return res;
    }
};

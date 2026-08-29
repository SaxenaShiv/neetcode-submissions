class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> count = new HashMap<>();
        for(int num:nums){
            count.put(num,count.getOrDefault(num,0)+1);
        }
        List<int[]>ans = new ArrayList<>();

        for(Map.Entry<Integer,Integer> entry:count.entrySet()){
            ans.add(new int[]{entry.getValue(),entry.getKey()});
        }
        ans.sort((a,b)->b[0]-a[0]);

        int []res = new int[k];
        for(int i=0;i<k;i++){
            res[i]=ans.get(i)[1];
        }
        return res;
    }
}

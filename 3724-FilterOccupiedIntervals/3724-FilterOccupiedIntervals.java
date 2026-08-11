// Last updated: 8/11/2026, 4:02:40 PM
import java.util.*;
class Solution {
    public List<List<Integer>> filterOccupiedIntervals(int[][] occupiedIntervals, int freeStart, int freeEnd) {
        Arrays.sort(occupiedIntervals,(a,b)->Integer.compare(a[0],b[0]));
        List<int[]>merged=new ArrayList<>();
        for(int[]interval:occupiedIntervals){
            if(merged.isEmpty()||interval[0]>merged.get(merged.size() -1)[1]+1){
                merged.add(new int[]{interval[0],interval[1]});
            }else{
                merged.get(merged.size()-1)[1]= Math.max(merged.get(merged.size()-1)[1],interval[1]);
            }     
        }
        List<List<Integer>> ans= new ArrayList<>();
        for(int [] in : merged){
            int L = in[0],r=in[1];
            if(r<freeStart||L>freeEnd){
                ans.add(Arrays.asList(L,r));
            }else{
                if(L<freeStart){
                ans.add(Arrays.asList(L,freeStart-1));
            }
            if(r>freeEnd){
                ans.add(Arrays.asList(freeEnd+1,r));
            }
        }
    }
    return ans;
  }
}
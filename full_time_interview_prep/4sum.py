from collections import defaultdict
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        pair_map = defaultdict(list)
        visited = set()
        unique_quad = set()
        result = []
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                pair_sum = nums[i] + nums[j]
                pair_map[pair_sum].append((i,j))
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                pair_sum = target - ( nums[i] + nums[j] )
                for x,y in pair_map[pair_sum]:
                    indices = tuple(sorted([x,y,i,j]))
                    quads = tuple(sorted([nums[x],nums[y],nums[i],nums[j]]))
                    if len(set([x,y,i,j])) == 4 and indices not in visited and \
                      quads not in unique_quad:
                        result.append(list(quads))
                        visited.add(indices)
                        unique_quad.add(quads)
                       
        return result
                        
                        
                    
                
                
        
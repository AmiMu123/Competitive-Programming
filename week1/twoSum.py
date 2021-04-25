# // var twoSum = function(nums, target) {
# //     var map = new Map();  // O(1)
# //     for(var i = 0;i<nums.length;i++){  //O(n)
# //       currNum = nums[i];
# //       var value = target - currNum;
# //         if(map.has(value)){
# //             var array = [i];
# //             console.log(map.get(value))
# //             // array.push(map.get(value))
# //             return array;
# //         }
# //         else{
# //             map.set(currNum,i)

# //         }

# // }

# // };
# // console.log(twoSum([1,2,3,4,5],9));
# [1, 2, 3, 4, 5]
# i = 0   1   2   3    4
# = 9-1, 9-2, 9-3, 9-4, 9-5 =
# val 8,   7,   6,   5,   4
# // dic = arr[i]: val
# 1: 8, 2: 7, 3: 6, 4: 5, 5: 4

# 12


def twoSum(arr, t):
    dic = dict()
    for i in range(len(arr)):
        val = t - arr[i]
        # print(val)
        if val not in dic:
            dic[arr[i]] = i
        else:
            return dic[val], i
    return [-1, -1]


print(twoSum([1, 2, 3, 4, 5], 0))

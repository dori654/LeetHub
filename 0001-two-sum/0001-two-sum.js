/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const hashMap = {};

    for(let i=0;i<nums.length; i++){
        const completed = target - nums[i];

        if(hashMap[completed] !== undefined){
            return [hashMap[completed],i];
        }

        // Store the current number and its index in the hash table
        hashMap[nums[i]] = i;
    }
    return [];
};
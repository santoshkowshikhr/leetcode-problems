func twoSum(nums []int, target int) []int {

    nums_dict := make(map[int]int)

    for i, num := range nums{
        comp := target - nums[i]

        if j, exists := nums_dict[comp]; exists{
            return []int{j, i}
        }

        nums_dict[num] = i
    }

    return nil
    
}
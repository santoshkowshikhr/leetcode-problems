func moveZeroes(nums []int)  {
    zeroIdx := 0

    for i := 0; i < len(nums); i ++ {
        if nums[i] != 0 {
            nums[zeroIdx], nums[i] = nums[i], nums[zeroIdx]
            zeroIdx += 1
        }
    }
    
}
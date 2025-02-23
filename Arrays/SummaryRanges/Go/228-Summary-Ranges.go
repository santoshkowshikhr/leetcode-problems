func summaryRanges(nums []int) []string {
    result := []string{}

    i := 0

    for j := 1; j< len(nums) + 1; j++ {
        if j == len(nums) || nums[j] != nums[j-1] + 1 {
            if i == j -1 {
                srange := fmt.Sprintf(\%d\, nums[i])
                result = append(result, srange)
            } else {
                srange := fmt.Sprintf(\%d->%d\, nums[i], nums[j-1])
                result = append(result, srange)
            }

            i = j
        }
    }
    return result
}
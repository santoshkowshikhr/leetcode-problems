func missingNumber(nums []int) int {
    n := len(nums)
    expSum := n * (n+1) / 2
    curSum := 0

    for _, n := range nums {
        curSum += n
    }

    return expSum - curSum
    
}
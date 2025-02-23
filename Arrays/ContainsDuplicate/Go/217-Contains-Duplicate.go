func containsDuplicate(nums []int) bool {
    count_map := make(map[int]bool)


    for _, num := range nums {
        if _, exists := count_map[num]; exists {
            return true
        } 
        count_map[num] = true
    }
    return false
}
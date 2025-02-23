func containsNearbyDuplicate(nums []int, k int) bool {
    compMap := make(map[int]int)

    for i, num := range nums {
        if lastIdx, exists := compMap[num]; exists {
            distance := i - lastIdx
            if distance <= k {
                return true
            }
        }
        compMap[num] = i
    }

    return false    
    
}
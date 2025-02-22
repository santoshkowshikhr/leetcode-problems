func majorityElement(nums []int) int {
    count_map := make(map[int]int)

    for _, num := range nums {
        count_map[num] ++
    }

    maj_ele := len(nums) / 2

    for k, v := range count_map {
        if v > maj_ele {
            return k
        }
    }
    return -1
}
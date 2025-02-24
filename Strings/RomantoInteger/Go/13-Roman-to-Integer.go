func romanToInt(s string) int {
    romMap := map[byte]int {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000,
    }

    result := 0
    n := len(s)

    for i := 0; i < n; i++ {
        if i < n-1 && romMap[s[i]] < romMap[s[i+1]] {
            result -= romMap[s[i]]
        } else {
            result += romMap[s[i]]
        }
    }
    
    return result
}
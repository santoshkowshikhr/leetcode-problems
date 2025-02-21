func generate(numRows int) [][]int {
        if numRows == 0 {
        return [][]int{}
    }

    res := [][]int{{1}}

    for i := 1; i < numRows; i++ {
        lastRow := res[len(res)-1]
        preRow := append([]int{0}, lastRow...)
        preRow = append(preRow, 0)

        row := []int{}
        for j := 0; j < len(lastRow)+1; j++ {
            row = append(row, preRow[j]+preRow[j+1])
        }
        res = append(res, row)
    }
    return res    
}
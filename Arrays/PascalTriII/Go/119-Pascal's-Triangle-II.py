class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex<0:
            return []
    
        res = [[1]]

        for i in range(rowIndex):
            preRow = res[-1]
            temp = [0] + preRow + [0]

            row = [temp[j]+temp[j+1] for j in range(len(preRow)+1)]
            res.append(row)
        
        return res[rowIndex]
                
        
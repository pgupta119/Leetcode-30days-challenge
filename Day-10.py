#  Given an integer numRows, return the first numRows of Pascal's triangle.


#MY Solution  using sum method

class Solution:
    def generate(self, numRows) :
        res = [[1]]
        for i in range(numRows -1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1])+1):
                row.append(temp[j] + temp[j+1])
            res.append(row)
        return res

# using row and column method

class Solution:
    def generate(self,numRows):
        triangle = []

        for row_num  in range(numRows):

            row = [None for _ in range(row_num +1)]
            row[0],row[-1] = 1,1

            for j in range(1, len(row) -1):
                row[j] = triangle[row_num -1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle

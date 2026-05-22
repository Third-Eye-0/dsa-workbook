class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r,c=len(matrix),len(matrix[0])
        self.m=[[0]*(c+1) for i in range(r+1)]

        for i in range(r):
            p=0
            for j in range(c):
                p+=matrix[i][j]
                a=self.m[i][j+1]
                self.m[i+1][j+1]=p+a

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1=row1+1
        r2=row2+1
        c1=col1+1
        c2=col2+1
        br=self.m[r2][c2]
        a=self.m[r1-1][c2]
        l=self.m[r2][c1-1]
        tl=self.m[r1-1][c1-1]
        return br-a-l+tl


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
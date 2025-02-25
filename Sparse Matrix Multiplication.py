# Approach:
# - Since the matrices are **sparse**, many elements are zeros.
# - Instead of computing the full matrix multiplication, we **only compute nonzero elements**.
# - We first store the nonzero elements of `mat1` in a dictionary to speed up multiplication.
# - We then iterate through `mat2` column-wise to calculate the product efficiently.

# Time Complexity: O(m * k * n) in the worst case, but optimized for sparse matrices.
# Space Complexity: O(m * n) for the result matrix.

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])  # Get matrix dimensions
        result = [[0] * n for _ in range(m)]  # Initialize result matrix

        # Store nonzero values of mat1 in a dictionary for fast access
        mat1_nonzero = {}
        for i in range(m):
            for j in range(k):
                if mat1[i][j] != 0:  
                    mat1_nonzero.setdefault(i, []).append((j, mat1[i][j]))  # Store (column index, value)

        # Multiply nonzero values with mat2
        for i in mat1_nonzero:  # Iterate over nonzero rows in mat1
            for j, val in mat1_nonzero[i]:  # Get column index and value from mat1
                for col in range(n):  # Iterate over columns in mat2
                    if mat2[j][col] != 0:  # Multiply only if nonzero
                        result[i][col] += val * mat2[j][col]

        return result  # Return the computed matrix

# Example cases
solution = Solution()
print(solution.multiply([[1,0,0],[-1,0,3]], [[7,0,0],[0,0,0],[0,0,1]]))  # Output: [[7,0,0],[-7,0,3]]
print(solution.multiply([[0]], [[0]]))  # Output: [[0]]

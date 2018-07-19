class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        max_layer = len(matrix) // 2
        layer = 0

        offset = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while layer < max_layer:
            row, col = len(matrix) - layer - 1, layer
            locations = []
            for cycle in range(4):
                offset_row, offset_col = offset[cycle]
                for _ in range(len(matrix) - 2 * layer):
                    locations.append(matrix[row][col])

                    row += offset_row
                    col += offset_col

                row -= offset_row
                col -= offset_col

            row, col, index = layer, layer, 0
            for cycle in range(1, 5):
                offset_row, offset_col = offset[cycle % 4]
                for _ in range(len(matrix) - 2 * layer):
                    matrix[row][col] = locations[index]
                    index += 1
                    row += offset_row
                    col += offset_col

                row -= offset_row
                col -= offset_col

            layer += 1

        return matrix


x = Solution()
print (x.rotate([
    [1, 2],
    [3, 4]
]) == [
    [3, 1],
    [4, 2]
])
print (x.rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
]) == [
  [7,4,1],
  [8,5,2],
  [9,6,3]
])

print (x.rotate([
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]) == [
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
])
        
# https://leetcode.com/problems/subrectangle-queries/description/


class SubRectangleQueries(object):
    def __init__(self, rectangle):
        """
        :type rectangle: List[List[int]]
        """
        self.rectangle = rectangle
        self.row_l = len(self.rectangle)
        self.col_l = len(self.rectangle[0])

    def update_subrectangle(self, row1, col1, row2, col2, newValue):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :type newValue: int
        :return type: None
        """
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.rectangle[i][j] = newValue

    def get_value(self, row, col):
        """
        :type row: int
        :type col: int
        :return type: int
        """
        return self.rectangle[row][col]

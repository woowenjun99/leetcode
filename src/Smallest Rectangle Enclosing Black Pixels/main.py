from typing import List

class Solution:
    def __col_has_black_square(self, image: List[List[str]], row: int) -> bool:
        for col in range(len(image[0])):
            if image[row][col] != "1": continue
            return True
        return False
    
    def __row_has_black_square(self, image: List[List[str]], col: int) -> bool:
        for row in range(len(image)):
            if image[row][col] != "1": continue
            return True
        return False
    
    def minArea(self, image: List[List[str]], row: int, col: int) -> int:
        right = left_boundary = right_boundary = col
        left = 0
        while left <= right:
            mid = left + (right - left) // 2
            if self.__row_has_black_square(image, mid):
                left_boundary = mid
                right = mid - 1
            else: left = mid + 1

        left = col
        right = len(image[0]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.__row_has_black_square(image, mid):
                right_boundary = mid
                left = mid + 1
            else: right = mid - 1

        left = 0
        right = row
        upper_boundary = lower_boundary = row
        while left <= right:
            mid = left + (right - left) // 2
            if self.__col_has_black_square(image, mid):
                upper_boundary = mid
                right = mid - 1
            else: left = mid + 1
        left = row
        right = len(image) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.__col_has_black_square(image, mid):
                lower_boundary = mid
                left = mid + 1
            else: right = mid - 1
        return (right_boundary - left_boundary + 1) * (lower_boundary - upper_boundary + 1)
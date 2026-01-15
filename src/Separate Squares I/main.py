from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        low = answer = 0
        POW = 10 ** 6
        high = max([square[1] + square[2] for square in squares])
        while low <= high:
            mid = low + (high - low) / 2

            top_area = bottom_area = 0
            for _, y, length in squares:
                if y >= mid:
                    top_area += length ** 2
                    continue
                elif y + length <= mid:
                    bottom_area += length ** 2
                    continue
                bottom_area += (mid - y) * length
                top_area += length * length - (mid - y) * length

            top_area *= POW
            bottom_area *= POW
            if top_area - bottom_area <= 10:
                answer = mid
                high = mid - pow(10, -6)
            elif bottom_area > top_area:
                high = mid - pow(10, -6)
            else:
                low = mid + pow(10, -6)

        return answer
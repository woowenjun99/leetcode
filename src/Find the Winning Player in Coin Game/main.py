class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        winner = "Bob"
        while True:
            if x <= 0 or y <= 3:
                return winner
            x -= 1
            y -= 4
            winner = "Alice" if winner == "Bob" else "Bob"
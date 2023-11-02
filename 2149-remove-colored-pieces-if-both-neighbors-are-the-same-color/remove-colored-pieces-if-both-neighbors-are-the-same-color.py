class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        scores = {
            "A": 0,
            "B": 0,
        }
        current_color = colors[0]
        current_count = 1
        for color in colors[1:] + "_":
            if color == current_color:
                current_count += 1
            else:
                if current_count > 2:
                    scores[current_color] += current_count - 2
                current_color = color
                current_count = 1
        return scores["A"] > scores["B"]

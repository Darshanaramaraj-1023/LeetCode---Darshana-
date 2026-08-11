# Last updated: 8/11/2026, 4:05:12 PM
class Solution:
    def checkStraightLine(self, coordinates):
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        dx = x2 - x1
        dy = y2 - y1

        for x, y in coordinates[2:]:
            if (y - y1) * dx != dy * (x - x1):
                return False

        return True
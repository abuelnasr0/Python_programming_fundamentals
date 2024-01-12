import random
import math

class Point:
    def __init__(self, x=None, y=None):
        if x is not None:
            self.x = x
        else:
            self.x = random.uniform(0.0,10.0)
        
        if y is not None:
            self.y = y
        else:
            self.y = random.uniform(0.0,10.0)

    def distance(self, point):
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"


class Space:
    def __init__(self, size=50):
        self.points = []
        for i in range(size):
            self.points.append(Point())

    def search(self, source_point, top_k = 1):
        distances = []
        for i, point in enumerate(self.points):
            distances.append((i, source_point.distance(point)))

        distances.sort(key = lambda x : x[1])

        output = []

        for distance in distances[:min(top_k, len(distances))]:
            output.append({
                "distance": distance[1],
                "point": self.points[distance[0]]
            })

        return output

if __name__ == "__main__":
    space = Space()
    print(space.search(Point(1.2, 3.5)))

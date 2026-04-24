class Point:
    """A simple class to hold point data like ID, X, Y and a label."""
    def __init__(self, point_id, x, y, label):
        # Converting inputs to correct types
        self.id = int(point_id)
        self.x = float(x)
        self.y = float(y)
        self.label = str(label).strip()

    def __str__(self):
        return f"Point {self.id}: {self.label} at ({self.x}, {self.y})"


class Line:
    """A class for lines that are made of multiple coordinate pairs."""
    def __init__(self, line_id, name):
        self.id = int(line_id)
        self.name = name
        self.coordinates = []  # This list will store our (x, y) tuples

    def add_coordinate(self, x, y):
        """Method to add a new vertex to the line's path."""
        self.coordinates.append((float(x), float(y)))

    def __str__(self):
        # Shows how many points the line has
        return f"Line {self.id} ({self.name}) with {len(self.coordinates)} points"
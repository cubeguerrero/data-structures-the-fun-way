import math

class Grid:
    def __init__(self, x_start, x_end, y_start, y_end, num_x_bins, num_y_bins):
        self.x_start = x_start
        self.x_end = x_end
        self.y_start = y_start
        self.y_end = y_end
        self.num_x_bins = num_x_bins
        self.num_y_bins = num_y_bins
        self.x_bin_width = (x_end - x_start) / num_x_bins
        self.y_bin_width = (y_end - y_start) / num_y_bins
        # Create bins
        self.bins = [0] * self.num_x_bins
        for i in range(len(self.bins)):
            self.bins[i] = [None] * self.num_y_bins

    def insert(self, x, y):
        xbin = math.floor((x - self.x_start) / self.x_bin_width)
        ybin = math.floor((y - self.y_start) / self.y_bin_width)

        if xbin < 0 or xbin >= self.num_x_bins:
            return False

        if ybin < 0 or ybin >= self.num_y_bins:
            return False

        next_point = self.bins[xbin][ybin]
        self.bins[xbin][ybin] = GridPoint(x, y)
        self.bins[xbin][ybin].next = next_point

    def delete(self, x, y):
        xbin = math.floor((x - self.x_start) / self.x_bin_width)
        ybin = math.floor((y - self.y_start) / self.y_bin_width)
        if xbin < 0 or xbin >= self.num_x_bins:
            return False

        if ybin < 0 or ybin >= self.num_y_bins:
            return False

        current = self.bins[xbin][ybin]
        previous = None
        while current:
            if current.is_approx_equal(x, y):
                if previous:
                    previous.next = current.next
                else:
                    self.bins[xbin][ybin] = current.next
            previous = current
            current = current.next

        return False

    def linear_scan(self, x, y):
        best_dist = math.inf
        best_candidate = None

        xbin = 0
        while xbin < self.num_x_bins:
            ybin = 0
            while ybin < self.num_y_bins:
                if self._min_dist_to_bin(xbin, ybin, x, y) < best_dist:
                    current = self.bins[xbin][ybin]
                    print(current)
                    while current:
                        dist = Grid._euclidean_dist(x, y, current.x, current.y)
                        if dist < best_dist:
                            best_dist = dist
                            best_candidate = current
                        current = current.next
                ybin += 1
            xbin += 1

        return best_candidate


    def _min_dist_to_bin(self, xbin, ybin, x, y):
        if xbin < 0 or xbin >= self.num_x_bins:
            return math.inf

        if ybin < 0 or ybin >= self.num_y_bins:
            return math.inf

        x_min = self.x_start + xbin * self.x_bin_width
        x_max = self.x_start + (xbin + 1) * self.x_bin_width
        x_dist = 0
        if x < x_min:
            x_dist = x_min - x
        if x > x_max:
            x_dist = x - x_max

        y_min = self.y_start + ybin * self.y_bin_width
        y_max = self.y_start + (ybin + 1) * self.y_bin_width
        y_dist = 0
        if y < y_min:
            y_dist = y_min - y
        if y > y_max:
            y_dist = y - y_max

        return math.sqrt(x_dist**2 + y_dist**2)            

    def _euclidean_dist(x1, y1, x2, y2):
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)

    def __str__(self):
        return str(self.bins)


class GridPoint:
    THRESHOLD = 0.00001

    def __init__(self, x, y, next = None):
        self.x = x
        self.y = y
        self.next = next

    def is_approx_equal(self, x, y):
        if abs(x - self.x) > GridPoint.THRESHOLD:
            return False

        if abs(y - self.y) > GridPoint.THRESHOLD:
            return False

        return True
            

    def __str__(self):
        return f"({self.x}, {self.y})"


if __name__ == '__main__':
    g = Grid(1, 10, 1, 10, 10, 10)
    g.insert(1, 1)
    g.insert(1.5, 1.5)
    print(g)
    print(g.linear_scan(1.1, 1.1))

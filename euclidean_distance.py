def calc_nearest_euc_dist(list1: list) -> list:
    res = []
    distances = lambda point: (point[0] ** 2 + point[1] ** 2) ** (1 / 2)
    dist = map(distances, list1)
    res = [(x, y) for (x, y) in zip(list1, dist)]
    return sorted(res)


class Solution(object):
    '''
    def calc_nearest_euc_dist(self, points: list) -> list:
        res = []

        dist = lambda point: (point[0] ** 2 + point[1] ** 2) ** (1 / 2)
        distances = list(map(dist, points))
         points = [(x, y) for (x, y) in zip(points, distances)]
        return sorted(points)
    '''


if __name__ == "__main__":
    sol = Solution()
    print(calc_nearest_euc_dist([(1, 3), (-2, -2), (10, 10)]))

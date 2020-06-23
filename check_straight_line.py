def slope1(args):
    pass


def check_str_line(list1 : list)->bool:
    flag = True
    res = []
    slope = 1

    slope = lambda p : (p[1]/p[0])
    calc = map(slope, list1)
    res = [(x,y) for (x,y) in zip(list1, calc)]
    print (res)

    return flag


class Solution(object):
    pass




if __name__ == "__main__":
    sol = Solution()
    print(check_str_line([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]))
class Solution(object):
    pass

    def find_product(self, lis1: list) -> list:
        res = []
        _product = 1

        for index, item in enumerate(lis1):
            if item == 0:
                pass
            else:
                _product *= item
        '''
        for i in range(lis1):
            _product *= i
        '''
        for i in range(len(lis1)):
            if lis1[i] == 0 :
                res.append(int(_product / 1))
            else:
                res.append(int(_product/lis1[i]))

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.find_product([1, 2, 3, 0, 4]))

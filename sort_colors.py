class Solution(object):
    def find_anagrams(self, b, p):

        def str_to_dict(string: str) -> dict:
            dict1 = {char: sum(i == char for i in string) for char in string}
            return dict1

        size = len(p)
        p_dict = str_to_dict(p)

        res = []
        for i, _ in enumerate(b):
            candidate_anagram = b[i:i + size]
            if p_dict == str_to_dict(candidate_anagram):
                res.append(i)

        return res


if __name__ == "__main__":
    sol = Solution()
    output = sol.find_anagrams("cbacbbabc", "abc")
    print(output)

class Solution(object):
    pass

    def check_anagrams(self, str1: str, str2: str) -> list:
        size = len(str2)

        def str_to_dict(string: str) -> dict:
            dict1 = {char: sum(i == char for i in string) for char in string}
            return dict1

        str2_dict = str_to_dict(str2)
        result = []

        for i, _ in enumerate(str1):
            anagram_str = str1[i:i + size]
            if str2_dict == str_to_dict(anagram_str):
                result.append(i)

        return result


if __name__ == "__main__":
    sol = Solution()
    output = sol.check_anagrams("cabcbbbbca", "abc")
    print(output)

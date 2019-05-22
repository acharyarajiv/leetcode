from collections import Counter


class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        # build char.tolower() count map
        char_count_map = Counter()
        # normalize char to lower
        for c in licensePlate.lower():
            # check if char is alphabet
            if c.isalpha():
                # increment count
                char_count_map[c] += 1
        min_word = None

        for word in words:
            # one liner of code from line 12 to 18
            word_char_count = Counter(word.lower())
            isSame = False
            # check if all letters appear in word_char_count
            for key in char_count_map:
                isSame = key in word_char_count and char_count_map[key] <= word_char_count[key]
                if not isSame:
                    break
            # check if length of previous matched word is greater than current matched
            if isSame and (min_word is None or len(word) < len(min_word)):
                min_word = word
        return min_word


if __name__ == '__main__':
    inp_arr = [['1s3 456', ["looks", "pest", "stew", "show"]], 
               ['1s3 PSt', ["step", "steps", "stripe", "stepple"]],
               ['Ah71752', ["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"]],
               ['GrC8950', ["measure","other","every","base","according","level","meeting","none","marriage","rest"]]]
    out_arr = ['pest', 'steps', "husband", "according"]

    s = Solution()
    for index, value in enumerate(inp_arr):
        licensePlate = value[0]
        words = value[1]
        res = s.shortestCompletingWord(licensePlate, words)
        print('input moves %s' % (value))
        print('output expected %s actual %s\n' % (out_arr[index], res))

#!/usr/bin/env python3
# coding: utf-8
# FileName: num030.py
# Author: lxw
# Date: 11/5/17 5:00 PM

"""
Num 030: Substring with Concatenation of All Words
Source: https://leetcode.com/problems/substring-with-concatenation-of-all-words/#/description

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter). 
"""

import copy

class Solution:
    def findSubstring(self, s, words):
        """
        Bad: Time Limit Exceeded.
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        length = len(s)
        if length < 1 or len(words) < 1:
            return []
        elif len(words[0]) < 1:
            return []

        # 1. Create words_count.
        words_count = {}
        for word in words:
            if word in words_count:
                words_count[word] += 1
            else:
                words_count[word] = 1

        # 2. Interate on "s".
        result = []
        WORD_LEN = len(words[0])
        for start_index in range(length):
            words_count_copy = copy.deepcopy(words_count)
            index = start_index
            while index < length:
                cur_word = s[index:index+WORD_LEN]
                if cur_word in words_count_copy:
                    if words_count_copy[cur_word] == 1:
                        del words_count_copy[cur_word]
                        if len(words_count_copy) == 0:
                            result.append(start_index)
                            break
                    else:
                        words_count_copy[cur_word] -= 1
                    index += WORD_LEN
                else:    # cur_word not in words_count_copy
                    break
        return result


def main():
    sol = Solution()
    """
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    """
    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "good"]
    result = sol.findSubstring(s, words)
    print("result:{}".format(result))


if __name__ == "__main__":
    main()

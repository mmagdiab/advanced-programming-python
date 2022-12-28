""""
In Chapter 12, the way we checked to see if a word w was a real word was:
if w in words:
where words was the list of words generated from a wordlist. This is unfortunately slow, but
there is a faster way, called a binary search. To implement a binary search in a function, start
by comparing w with the middle entry in words. If they are equal, then you are done and
the function should return True. On the other hand, if w comes before the middle entry, then
search the first half of the list. If it comes after the middle entry, then search the second half of
the list. Then repeat the process on the appropriate half of the list and continue until the word
is found or there is nothing left to search, in which case the function short return False. The
< and > operators can be used to alphabetically compare two strings.
"""


words = ['apple', 'book', 'pie', 'jar', 'car', 'man', 'woman', 'nurse', 'something']


def binary_search(word_to_search: str):
    # FIRST sort words list
    words.sort()
    min_index = 0
    max_index = len(words) - 1
    while min_index <= max_index:
        mid = (max_index + min_index) // 2
        if words[mid] == word_to_search:
            return True
        elif words[mid] > word_to_search:
            max_index = mid - 1
        else:
            min_index = mid + 1
    else:
        return False

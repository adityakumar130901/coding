def find_longest_substring(word):
    
    #we may use array, store index at ascii value ie arr = [], arr['a'%26] = index
    char_hash_map = {}

    global_word = word[0]
    local_word = word[0]

    start = 0

    for index, char in enumerate(word):
        if char in char_hash_map:
            index_of_first_occurance = char_hash_map[char]
            if len(global_word) < (index-start):
                global_word = word[start:index]
            start = index_of_first_occurance + 1

        char_hash_map[char] = index

    if len(global_word) < (index-start):
        global_word = word[start:index]
        
    return global_word

word_list = ["abcabcbb", "bbbbbb", "pwwkew"]
for word in word_list:
    print "Input: %s"%word
    _substring = find_longest_substring(word)
    print "Output: %s"%_substring


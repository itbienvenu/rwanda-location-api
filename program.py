def shortest(data, keys):
    from collections import Counter, defaultdict

    required = Counter(keys)
    char_count = defaultdict(int)
    print(required)
    left = 0
    min_length = float('inf')
    min_substring = None
    formed = 0
    required_unique = len(required)

    for right, char in enumerate(data):
        char_count[char] += 1
        if char in required and char_count[char] == required[char]:
            formed += 1


        while formed == required_unique:
            current_length = right - left + 1
            print(current_length)
            if current_length < min_length:
                min_length = current_length
                min_substring = data[left:right + 1]


            left_char = data[left]
            char_count[left_char] -= 1
            if left_char in required and char_count[left_char] < required[left_char]:
                formed -= 1
            left += 1

    return min_substring


print(shortest("abccXa1AbYc2baZaac","abca"))
def create_table(pattern, patter_length):
    prefix_table = [0] * patter_length
    prefix_length = 0
    i = 1
    while i < patter_length:
        if pattern[i] == pattern[prefix_length]:
            prefix_length += 1
            prefix_table[i] = prefix_length
            i += 1
        else:
            if prefix_length != 0:
                prefix_length = prefix_table[prefix_length - 1]
            else:
                prefix_table[i] = 0
                i += 1
    return prefix_table


def kmp_search(text, pattern):
    patter_length = len(pattern)
    text_length = len(text)
    indexes = []

    prefix_table = create_table(pattern, patter_length)

    i = 0
    j = 0
    while i < text_length:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == patter_length:
            indexes.append(i - j)
            j = prefix_table[j - 1]

        elif i < text_length and pattern[j] != text[i]:
            if j != 0:
                j = prefix_table[j - 1]
            else:
                i += 1

    return indexes

def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for alpha in list(string):
        if alpha.isalpha():
            alphabet_occurrence_array[ord(alpha) - ord("a")] += 1

    find = alphabet_occurrence_array.index(max(alphabet_occurrence_array))
    result = chr(find + ord('a'))

    return result


results = find_alphabet_occurrence_array("best of best sparta")

print(results)

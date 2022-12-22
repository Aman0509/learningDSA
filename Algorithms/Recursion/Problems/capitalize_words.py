# Write a recursive function which accepts an array of words and return a new array containing each word capitalized.


def capitalize_words(arr):
    assert type(arr) == list, "This function only accepts list"
    if len(arr) == 0:
        return []
    return [arr[0].upper()] + capitalize_words(arr[1:])

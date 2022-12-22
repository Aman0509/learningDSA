# Write a recursive function which return the sum of all even numbers in an object which may contain nested objects.

"""
obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

nestedEvenSum(obj1) # 6

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}

nestedEvenSum(obj2) # 10

"""


def nested_even_sum(obj, sum=0):
    assert type(obj) == dict, "This function only accepts dictionary"
    if obj == {}:
        return sum
    num = obj.popitem()[1]
    if isinstance(num, dict):
        return nested_even_sum(obj, sum + nested_even_sum(num, 0))
    elif isinstance(num, int) and not num % 2:
        return nested_even_sum(obj, sum + num)
    else:
        return nested_even_sum(obj, sum)

# Write a function which accepts an object and returns an array of all the values in the object that have a type of
# string.

"""
obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}

collectStrings(obj) # ['foo', 'bar', 'baz']
"""


def collect_strings(obj):
    assert type(obj) == dict, "This function only accepts dictionary"
    if obj == {}:
        return []
    ele = obj.popitem()
    str_obj = collect_strings(obj)
    if isinstance(ele[1], dict):
        str_obj.extend(collect_strings(ele[1]))
        # str_obj = str_obj + collect_strings(ele[1])
    elif isinstance(ele[1], str):
        str_obj.append(ele[1])
    else:
        obj.update({ele[0]: ele[1]})
    return str_obj

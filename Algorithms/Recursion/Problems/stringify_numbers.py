# Write a function called which takes in an object and finds all of the values which are numbers and converts them to
# strings.

"""
obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}

stringify_numbers(obj)

{'num': '1', 
 'test': [], 
 'data': {'val': '4', 
          'info': {'isRight': True, 'random': '66'}
          }
}
"""


def stringify_numbers(obj):
    assert type(obj) == dict, "This function only accepts dictionary"
    if obj == {}:
        return {}
    ele = obj.popitem()
    str_obj = stringify_numbers(obj)
    if isinstance(ele[1], dict):
        str_obj.update({ele[0]: stringify_numbers(ele[1])})
    elif type(ele[1]) is int:
        str_obj.update({ele[0]: str(ele[1])})
    else:
        str_obj.update({ele[0]: ele[1]})
    return str_obj

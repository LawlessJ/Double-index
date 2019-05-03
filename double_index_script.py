def double_index(lst, index):
  if index >=0 and index < len(lst):
    lst[index] *= 2
    return lst
  else:
    return lst


print(double_index([3, 8, -10, 12], 2))
# returns [3, 8, -20, 12] to the console
print(double_index([3, 8, -10, 12], -1))
# returns [3, 8, -10, 24] to the console

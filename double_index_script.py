def double_index(lst, index):
  if index >=0 and index < len(lst):
    lst[index] *= 2
    return lst
  else:
    return lst


#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))
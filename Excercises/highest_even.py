def highest_even(li):
  max_even = None

  for i in li:
    if i % 2 == 0 and not max_even:
      max_even = i
    elif i % 2 == 0 and max_even:
      if i > max_even:
        max_even = i

  return max_even


print(highest_even([2,10,4,5,1]))
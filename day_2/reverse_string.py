def reverse_and_remove_duplicates(lst):
 seen =set()
 result =[]
 for item in reversed(lst):
   if item not in seen:
     seen.add(item)
     result.append(item)

 return result

print(reverse_and_remove_duplicates([1,2,3,4,5,6,6,5,4,2,1])
      )

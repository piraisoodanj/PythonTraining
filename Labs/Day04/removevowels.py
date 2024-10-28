# write a function that return the string after removing vowels

def removevowels(name):
  result = [c for c in name if c not in 'aeiou']
  return result

print(removevowels("pirai"))
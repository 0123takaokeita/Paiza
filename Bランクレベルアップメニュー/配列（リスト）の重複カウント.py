import collections


array = ["HND", "NRT", "KIX", "NGO", "NGO", "NGO", "NGO", "NGO"]
dict = dict(collections.Counter(array))
for i in dict:
  if dict[i] != 1:
    print(dict[i])

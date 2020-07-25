import operator
from operator import itemgetter
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(0))
print('Dictionary in ascending order by key: ',sorted_d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(0),reverse=True))
print('Dictionary in descending order by key : ',sorted_d)


x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(sorted(x.values()))
print('Dictionary in ascending order by value: ',sorted(d.items(), key=itemgetter(1)))
print('Dictionary in ascending order by value: ',sorted(x.items(), key=lambda kv: kv[1]))






# import collections
#
# sorted_dict = collections.OrderedDict(sorted_x)
#
#
#
# sorted(d.items(), key=lambda x: x[1])
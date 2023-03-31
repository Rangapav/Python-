# SEARCH:TO SEARCH THE SPECIFIED STRING IN INPUT OR NOT


import re

# p="OOPS is said to be object oriented programming system"
#
# x=re.search('object',p)
# print(x)

# findall:to find duplicates for specific pattern

s='''The 37th meeting started on 12th November 2020.
It was a virtual meeting that was presided by Viet Nam Prime Minister against the backdrop of COVID-19 pandemic.
Theme – Cohesive and Responsive ASEAN
Read more about ASEAN in the linked article.'''

print(re.findall('meeting',s))
print(re.findall('\r''aeiou',s))


# You are given a set  and  other sets.
# Your job is to find whether set  is a strict superset of each of the  sets.

# Print True, if  is a strict superset of each of the  sets. Otherwise, print False.

# A strict superset has at least one element that does not exist in its subset.



a = set(raw_input().split())
counter , n = 0, int(input())
for i in range (n):
        b = set(raw_input().split())
        if a.issuperset(b) :
                counter += 1
print(counter == n)

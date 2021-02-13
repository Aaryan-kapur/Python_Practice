

# You are given two sets, 1 and 2 .
# Your job is to find whether set 1 is a subset of set 2.



def check(aPoora,bPoora):
  flag = 0
  if(all(x in bPoora for x in aPoora)): 
    flag = 1
  if flag:
    return(True)
  else:
    return(False)
n = int(input(""))
aaaaa = []
for i in range(n):
  a = int(input(""))
  aPoora = list(map(int, raw_input().split()))
  b = int(input(""))
  bPoora = list(map(int, raw_input().split()))
  aaaaa.append(check(aPoora,bPoora))

for i in aaaaa:
  print(i)

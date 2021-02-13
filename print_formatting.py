# The included code stub will read an integer, n , from STDIN.

# Without using any string methods, try to print the following:

# 12345.......n


# Note that "12345.......n" represents the consecutive values in between.

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(1,n+1):
      print(i,end="")

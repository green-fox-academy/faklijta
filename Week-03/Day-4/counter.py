# Write a recursive function that takes one parameter: n and counts down from n.
def counter(n):
    if n == 0:
        return 0
    else:
        return counter(n-1)

print(counter(4))
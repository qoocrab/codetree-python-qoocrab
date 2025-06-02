# Time Complexity: O(1)
# Space Complexity: O(1)
a, b, c = map(int, input().split())
s = a + b + c
avg = s // 3
print(s, avg, s - avg, sep="\n")

n = int(input())
arr = []
for i in range(n):
    arr.append(input())
arr.sort(key=int)
for _ in arr:
    print(_)

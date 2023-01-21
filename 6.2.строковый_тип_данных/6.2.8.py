s1, s2, s3 = input(), input(), input()
sm = max(len(s1), len(s2), len(s3))
smin = min(len(s1), len(s2), len(s3))
if smin == len(s1):
    print(s1)
elif smin == len(s2):
    print(s2)
else:
    print(s3)
if sm == len(s1):
    print(s1)
elif sm == len(s2):
    print(s2)
else:
    print(s3)
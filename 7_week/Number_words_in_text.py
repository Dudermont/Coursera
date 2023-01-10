import sys
lines = sys.stdin.read()
line = set(map(str, lines.split()))
print(len(set(line)))

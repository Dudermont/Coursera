n = list(map(int, input().split()))
weekends = set(range(6, n[0] + 1, 7)) | set(range(7, n[0] + 1, 7))
all_strikes = set()
for i in range(n[1]):
    party_strikes = list(map(int, input().split()))
    all_strikes |= set(range(party_strikes[0], n[0] + 1, party_strikes[1]))
print(len(all_strikes - weekends))

S = input()
K = input()

found = False

for i in range(len(S) - len(K) + 1):
    if S[i:i + len(K)] == K:
        print((i, i + len(K) - 1))
        found = True

if not found:
    print((-1, -1))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
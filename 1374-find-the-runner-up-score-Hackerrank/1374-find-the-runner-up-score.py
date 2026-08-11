n = int(input())
arr = list(map(int, input().split()))

unique_scores = list(set(arr))
unique_scores.sort()

print(unique_scores[-2])


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
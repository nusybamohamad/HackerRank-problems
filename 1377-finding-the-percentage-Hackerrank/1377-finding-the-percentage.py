n = int(input())

students = {}

for _ in range(n):
    data = input().split()
    name = data[0]
    marks = list(map(float, data[1:]))
    students[name] = marks

query_name = input()

average = sum(students[query_name]) / len(students[query_name])

print(f"{average:.2f}")


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
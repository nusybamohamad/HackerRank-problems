import re

regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"

P = input()

print(bool(re.match(regex_integer_in_range, P)) and
      len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
regex_alternating_repetitive_digit_pair = r"_________"	# Do not delete 'r'.



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
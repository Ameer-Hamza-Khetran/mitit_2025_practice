import sys


def is_good_contest_name(s):
    n = len(s)
    for b_len in range(1, n):  # Possible lengths of B
        if n >= 2 * b_len + 1:  # Ensure we have enough characters for ABB
            # Get the two parts of B
            part1 = s[n - 2 * b_len:n - b_len]
            part2 = s[n - b_len:]
            # Check if they are equal
            if part1 == part2:
                return "YES"
    return "NO"


# Read input directly from the command line (manual paste)
print("Paste your input (press Ctrl+D when done):")
input_lines = sys.stdin.read().strip().split("\n")
q = int(input_lines[0])  # First line contains the number of strings
results = []

for i in range(1, q + 1):
    contest_name = input_lines[i].strip()
    results.append(is_good_contest_name(contest_name))

# Output the results
print("\n".join(results))

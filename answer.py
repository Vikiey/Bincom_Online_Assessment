import random
import math
from collections import Counter

# Extract the Data
data = {
"MONDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
"TUESDAY": "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE",
"WEDNESDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE",
"THURSDAY": "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
"FRIDAY": "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE"
}

# Data Cleaning
all_colours = []
for colours in data.values():
  # Split by comma, strip whitespace, and fix the "BLEW" typo
  cleaned_colours = [c.strip().replace('BLEW', 'BLUE').replace('ARSH', 'ASH') for c in colours.split(',')]
  all_colours.extend(cleaned_colours)

# Frequency Count
# This creates a dictionary: {'BLUE': 31, 'WHITE': 16, ...}
colour_count = Counter(all_colours)
total_colours = len(all_colours)
frequencies = list(colour_count.values())

# 1. Mean Frequency
mean_freq = sum(frequencies) / len(frequencies)
mean_colour = min(colour_count, key=lambda x: abs(colour_count[x] - mean_freq))

# 2. Most Worn (Mode)
mostly_worn = colour_count.most_common(1)[0][0]

# 3. Median
sorted_freqs = sorted(colour_count.items(), key=lambda x: x[1])
n = len(sorted_freqs)
if n % 2 == 0:
median_colour = (sorted_freqs[n//2 - 1][0], sorted_freqs[n//2][0])
else:
median_colour = sorted_freqs[n//2][0]

# 4. Variance
variance = sum((f - mean_freq) ** 2 for f in frequencies) / len(frequencies)

# 5. Probability of Red
prob_red = colour_count['RED'] / total_colours

# Output Results
print(f"1. Mean Colour: {mean_colour}")
print(f"2. Mostly Worn Colour: {mostly_worn}")
print(f"3. Median Colour(s): {median_colour}")
print(f"4. Variance: {variance:.2f}")
print(f"5. Probability of Red: {prob_red:.4f}")

# 6. Save to PostgreSQL
import psycopg2

def save_to_postgres(color_count):
  try:
    conn = psycopg2.connect(
      dbname="colours_db", user="postgres", 
      password="your_password", host="localhost", port="5432"
    )
    
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS colour_frequency (colour VARCHAR(20), frequency INT);")
    
    for colour, count in colour_count.items():
      cur.execute("INSERT INTO colour_frequency (colour, frequency) VALUES (%s, %s)", (colour, count))

    conn.commit()
    cur.close()
    conn.close()

    print("Data saved successfully.")
    
  except Exception as e:
    print(f"Error: {e}")

#Example data
counts = {'BLUE': 31, 'WHITE': 16, 'GREEN': 10, 'ORANGE': 9, 'RED': 9}
save_to_postgres(counts)

# 7. Recursive Search
# Generate a random 4-digit binary number as a string
binary_num = "".join(str(random.randint(0, 1)) for i in range(4))

#Convert to base 10
decimal_num = int(binary_num, 2)
print(f"Generated Binary: {binary_num}")
print(f"Base 10 (Decimal): {decimal_num}")

# 8. Random 4-digit Binary to Decimal
def recursive_search(arr, target, index=0):
# Base Case 1: The index has reached the end of the list (not found)
if index >= len(arr):
    return -1

# Base Case 2: The current element matches the target
if arr[index] == target:
    return index

# Recursive Step: Search the next index
return recursive_search(arr, target, index + 1)

# Use case
num_arr = [5, 10, 15, 20, 25, 30]
target_num = int(input("Enter a number to search: "))
result = recursive_search(num_arr, target_num)
print(f"Index of number: {result}" if result != -1 else "Not found")

# 9. Sum of First 50 Fibonacci Sequence
def fibonacci_sum(n):
if n <= 0:
    return 0
elif n == 1:
    return 0

# Initialize the first two terms
a, b = 0, 1
total_sum = a + b

# Calculate terms from 3 to n
for i in range(2, n):
    a, b = b, a + b
    total_sum += b

return total_sum

# Calculate the sum for the first 50 terms
n_terms = 50
result = fibonacci_sum(n_terms)
print(f"The sum of the first {n_terms} Fibonacci numbers is: {result}")

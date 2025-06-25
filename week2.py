
# 1. Skip numbers divisible by 5, stop if number > 50
print("\n--- Task 1: Skip numbers divisible by 5 and stop if number > 50 ---")
numbers = [10, 12, 25, 30, 41, 55, 60, 70]

for num in numbers:
    if num > 50:
        break
    if num % 5 == 0:
        continue
    print(num)

# 2. Password strength checker
print("\n--- Task 2: Password Strength Checker ---")
import string

password = input("Enter your password: ")

has_letter = any(c.isalpha() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(c in "@#$%&" for c in password)

if len(password) < 6 or (has_letter and not has_digit and not has_special):
    print("Weak")
elif len(password) >= 6 and has_letter and has_digit and not has_special:
    print("Moderate")
elif len(password) >= 8 and has_letter and has_digit and has_special:
    print("Strong")
else:
    print("Moderate")

# 3. Alternate word reversal in string
print("\n--- Task 3: Alternate Word Reversal ---")
text = input("Enter a sentence: ")
words = text.split()

for i in range(len(words)):
    if i % 2 == 1:
        words[i] = words[i][::-1]

new_text = " ".join(words)
print("Output:", new_text)

# 4. Find repeated words with frequency
print("\n--- Task 4: Count Repeated Words ---")
words = ["apple", "banana", "apple", "orange", "banana", "banana"]
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

duplicates = {}

for word, count in word_count.items():
    if count > 1:
        duplicates[word] = count

print(duplicates)

# 5. Book availability checker
print("\n--- Task 5: Book Store Inventory Check ---")
books = {
    'Book1': 5,
    'Book2': 6,
    'Book3': 10,
    'Book4': 2,
}

book_name = input("Enter the name of the book you want: ")

while True:
    quantity_input = input("Enter the number of copies you want to buy: ")
    if quantity_input.isdigit():
        quantity = int(quantity_input)
        break
    else:
        print("Please enter a valid number.")

if book_name in books:
    available = books[book_name]
    if available >= quantity:
        print("Available")
    elif available > 0:
        print("Partially Available")
    else:
        print("Unavailable")
else:
    print("Unavailable")

# 6. Frequency of all words in a list
print("\n--- Task 6: Word Frequency Counter ---")
word_list = ["This", "is", "good", "is"]
word_freq = {}

for word in word_list:
    word_lower = word.lower()
    if word_lower in word_freq:
        word_freq[word_lower] += 1
    else:
        word_freq[word_lower] = 1

print(word_freq)

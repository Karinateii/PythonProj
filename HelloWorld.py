#Palindrome Checker
print("Enter a word");
word = input()

#convert string word to char array
original = list(word)
reversed = list(word)

#reverse the char array
reversed.reverse()

if original == reversed:
    print("The word is a palindrome")
else: 
    print("The word is not a palindrome")

#Write a function that takes a sentence and reverses the order of words, not the characters.
print("Enter a sentence")
sentence = input()
words = sentence.split()
reversed_words = words[::-1]
reversed_sentence = ' '.join(reversed_words)
print(reversed_sentence)

#Write a program that counts how many times each word appears in a sentence.
# For example, "Hello world hello" should return "Hello: 1, world: 1, hello: 1".
print("Enter a sentence")
sentence = input()
words = sentence.split()
word_count = {}
for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
for word, count in word_count.items():
    print(f"{word}: {count}")

#//Write a function that takes a string and returns the first non-repeating character in it.
#//If all characters repeat, return "None" or ' '.
print("Enter a string")
string = input()
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1  
for char in string:
    if char_count[char] == 1:
        print(f"The first non-repeating character is: {char}")
        break
else:
    print("None")

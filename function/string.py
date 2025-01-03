#1. reverse a string
a=input("Enter a string:")
print(a)
a=a[::-1]
print()



# 2.count vowels in a string
# def count_vowels(input_string):
#     vowels = 'aeiouAEIOU'
#     count = 0
#     for char in input_string:
#         if char in vowels:
#             count += 1
#     return count
# string_to_check = "krushi koradiya"
# vowel_count = count_vowels(string_to_check)
# print(f"Number of vowels in the string: {vowel_count}")


# #3. check palindrome
# def is_palindrome(input_string):
    
#     processed_string = input_string.replace(" ", "").lower()
   
#     return processed_string == processed_string[::-1]
# string_to_check = "121"
# if is_palindrome(string_to_check):
#     print(f'"{string_to_check}" is a palindrome.')
# else:
#     print(f'"{string_to_check}" is not a palindrome.')


# #4. count the word in python
# def count_words(input_string):
#     return len(input_string.split())
# a = "nice to meet you?"
# b = count_words(a)
# print(f"Number of words in the string: {b}")



#5. remove duplicate in a string
def remove_duplicates(input_string):
    seen = set()
    result = []
    for char in input_string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)
original_string = "krushi koradiya"
print(remove_duplicates(original_string))


#6. count consonen in python
def count_consonants(input_string):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for char in input_string:
        if char in consonants:
            count += 1
    return count
original_string = "hello world"
print(count_consonants(original_string))  # Output: 7


#7. Check for anagram





# 8.check substring 



# 9.check subsequence





# 

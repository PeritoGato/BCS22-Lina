import string

def is_palindrome(sentence):
    cleaned_sentence = remove_spaces_lowercase(sentence)
    cleaned_sentence = remove_punctuation(cleaned_sentence)
    return is_palindrome_check(cleaned_sentence)

def remove_spaces_lowercase(sentence):
    return ''.join(char.lower() for char in sentence if char != ' ')

def remove_punctuation(sentence):
    return ''.join(char for char in sentence if char not in string.punctuation)

def is_palindrome_check(sentence):
    cleaned_sentence = remove_spaces_lowercase(sentence)
    length = len(cleaned_sentence)
    for i in range(length // 2):
        if cleaned_sentence[i] != cleaned_sentence[length - 1 - i]:
            return False
    return True

# Example usage:
sentence = "A man, a plan, a canal, Panama"
result = is_palindrome(sentence)
print(f"The sentence '{sentence}' is a palindrome: {result}")



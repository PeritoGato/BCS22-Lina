class Stack:
    def __init__(self):
        """
        Stack class to implement a stack data structure.
        """
        self.items = []  # Use a list to store stack elements

    def push(self, data):
        """
        Pushes an element onto the stack.

        Args:
        - data: Element to be pushed onto the stack.
        """
        self.items.append(data)  # Append the data to the list

    def pop(self):
        """
        Pops an element from the stack.

        Returns:
        - toReturn: Element popped from the stack.
        """
        if not self.is_empty():
            return self.items.pop()  # Pop and return the last element from the list
        else:
            print("> Stack Underflow.")
            return None

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
        - bool: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

# Function to check if string is a palindrome
def is_palindrome(input_string):
    alphanumeric_chars = [char.lower() for char in input_string if char.isalnum()]
    string_stack = Stack()

    for char in alphanumeric_chars:
        string_stack.push(char)  # Push alphanumeric characters onto the stack

    reversed_string = ''.join(string_stack.pop() for _ in range(len(alphanumeric_chars)))

    return input_string.lower() == reversed_string  # Compare input with its reversed version

# Main program
while True:
    user_string_input = input("\nPalindrome check!\nInput a word or sentence to check whether it's a palindrome.\n>> ").strip()

    is_input_palindrome = is_palindrome(user_string_input)

    print(f"\nInput: {user_string_input}")
    if is_input_palindrome:
        print("It's a palindrome!")
    else:
        print("It's NOT a palindrome!")

    if input("\nTry again? (y/n)\n>> ")[0] != "y":
        break  # Break the loop if user does not want to try again



"""
Palindrome class realization.
"""

from linkedstack import LinkedStack


class Palindrome:
    """A class that represents a palindrome."""

    @staticmethod
    def read_file(filename: str) -> list:
        """Return a list of words from the file."""
        words = []

        file = open(filename, encoding="utf-8", mode="r")
        for line in file.readlines():
            words.append(line.strip().split()[0])
        file.close()

        return words

    @staticmethod
    def write_to_file(palindromes: list, filename: str) -> None:
        """Write the palindromes into a file."""
        file = open(filename, encoding="utf-8", mode="w")
        for palindrome in palindromes:
            file.write(palindrome + "\n")
        file.close()

    @classmethod
    def find_palindromes(cls, read_filename: str, write_filename: str) -> list:
        """
        Return the list of palindromes from the read_filename file and
        write them to the write_filename file.
        """
        palindromes = []

        words = cls.read_file(read_filename)
        for word in words:
            if cls.is_palindrome(word):
                palindromes.append(word)

        cls.write_to_file(palindromes, write_filename)
        return palindromes

    @staticmethod
    def is_palindrome(word: str) -> bool:
        """Check whether the word is a palindrome."""
        stack = LinkedStack()

        for index, char in enumerate(word, 1):
            if char.isalpha() and index <= len(word) / 2:
                stack.push(char)

            elif char.isalpha() and (index > len(word) / 2) \
                    and (index != (len(word) / 2) + 0.5):
                if stack.isEmpty():
                    return False

                char_from_stack = stack.pop()
                if char != char_from_stack:
                    return False

        return stack.isEmpty()

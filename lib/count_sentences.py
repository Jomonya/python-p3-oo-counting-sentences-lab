#!/usr/bin/env python3

class MyString:
  pass
class MyString:
    def __init__(self, value=''):
        if isinstance(value, str):
            self.value = value
        else:
            print ("The value must be a string.")
            self.value = ''

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Replace all punctuation marks with periods to simplify splitting
        modified_string = self.value.replace('?', '.').replace('!', '.')
        # Split the string by periods
        sentences = modified_string.split('.')
        # Filter out empty strings from the list
        sentences = [sentence for sentence in sentences if sentence.strip()]
        # Return the count of remaining sentences
        return len(sentences)

# Example usage:
string = MyString()
string.value = "This is a string! It has three sentences. Right?"
print(string.count_sentences())  # Output: 3

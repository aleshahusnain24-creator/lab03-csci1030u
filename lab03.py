# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Replace each `pass` with your code, and use `return` to send the answer
# back (not `print`).


def pig_latin(word):
    # TODO (Part 1): return the Pig Latin form of a single lowercase word.
    #   If it starts with a vowel (a, e, i, o, u): add "way" to the end.
    #   Otherwise: move the first letter to the end and add "ay".
    if word[0] in "aeiou":
        return word + "way"
    else:
        return word[1:] + word[0] + "ay"





def word_lengths(sentence):
    # TODO (Part 2): return a list with the length of each word in `sentence`
    #   (words are separated by spaces).
    ##words = sentence.split() # seperates words in a sentence into a list

    lengths = [] # creates a list of the lengths of each word
    for word in sentence.split(): # iterates through each word in the sentence
        lengths.append(len(word)) # appends the length of each word to the list
    return lengths




def reverse_words(sentence):
    # TODO (Part 3): return `sentence` with the order of its words reversed.
    #   e.g. "hello world" -> "world hello"
    words = sentence.split() # splits the sentence into a list of words
    reverse_words = words[::-1] # reverses the list of words
    result = " "
    for word in reverse_words: # iterates through the reversed list of words
        result += word + " " # adds each word to the result string with a space
        return result.strip() # returns the result string with leading and trailing spaces removed
    #return " ".join(reverse_words) # joins the reversed list of words into a string and returns it





def letter_counts(text):
    # TODO (Part 4 - STRETCH, optional): return a dictionary mapping each letter
    #   to how many times it appears in `text`. Ignore case, and ignore anything
    #   that isn't a letter.
    counts = {} # creates an empty dictionary to store the letter counts
    for letter in text.lower(): # iterates through each letter in the text, converting it to lowercase
        if letter.isalpha(): # checks if the letter is an alphabetic character
            if letter in counts: # checks if the letter is already in the dictionary
                counts[letter] += 1 # increments the count for that letter
            else:
                counts[letter] = 1 # adds the letter to the dictionary with a count of 1
    return counts


def main():
    # Optional scratch space - use this to try your functions with sample values.
    # print(pig_latin("banana"))                    # ananabay
    # print(word_lengths("the quick brown fox"))    # [3, 5, 5, 3]
    # print(reverse_words("the quick brown fox"))   # fox brown quick the
    # print(letter_counts("hello"))                 # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    pass


if __name__ == "__main__":
    main()

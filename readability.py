import sys

def main():
    # Get text input from user.
    text = input("Text: ")

    # Instantiate counts for number of letters, words, and sentences.
    letters = 0
    words = 0
    sentences = 0

    # Loop through indexes in input in order to track each character. 
    for i in range(len(text)):
        # Check if character is alpha and increment letters count if it is.
        if text[i].isalpha():
            letters += 1
        # Check if character is space
        elif text[i] == " ":
            # Check that the preceeding character is alpha or is not end of sentence punctuation and incremenet words count.
            # Checking for end of sentence punctuation prevents double counting words and takes into account other punctuation like commas or quotes.
            if text[i-1].isalpha() or text[i-1] not in [".", "!", "?"]:
                words += 1
        # Check if character is period, exclamation mark, or question mark and increment sentences count.
        elif text[i] in [".", "!", "?"]:
            sentences += 1
            words += 1

    # Calculate Coleman-Liau index with coleman_liau() to get a readability score.
    index = coleman_liau(letters, words, sentences)
    # If index is less than 1, print Before Grade 1.
    if index < 1:
        print("Before Grade 1")
        return
    # If index is 16 or greater, print Grade 16+.
    if index >= 16:
        print("Grade 16+")
        return
    # Else print Grade + index.
    print(f"Grade {index}")
    return

# Define coleman_liau() function that takes the count of letters, words, and sentences in passage. 
def coleman_liau(letters, words, sentences):
    # Find the average number of letters per 100 words.
    avg_L = letters / words * 100
    # Find the average number of sentences per 100 words.
    avg_S = sentences / words * 100
    # Calculate index with Coleman Liau formula.
    index = round(0.0588 * avg_L - 0.296 * avg_S - 15.8)
    return index


if __name__ == "__main__":
    main()
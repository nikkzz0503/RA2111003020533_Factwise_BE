def number_to_words(n):
    # Define dictionaries for mapping numbers to words
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand"]
    
    if n == 0:
        return "zero"
    
    words = []
    
    # Handle thousands
    if n >= 1000:
        words.append(ones[n // 1000])
        words.append(thousands[1])
        n %= 1000
    
    # Handle hundreds
    if n >= 100:
        words.append(ones[n // 100])
        words.append("hundred")
        n %= 100
        if n > 0:
            words.append("and")
    
    # Handle tens and ones
    if n >= 20:
        words.append(tens[n // 10])
        n %= 10
    elif 10 <= n < 20:
        words.append(teens[n - 10])
        n = 0
    
    if n > 0:
        words.append(ones[n])
    
    return "".join(words)

def count_letters(word):
    # Count letters and exclude spaces and hyphens
    return len(word.replace(" ", "").replace("-", ""))

def count_letters_up_to(n):
    total_letters = 0
    for i in range(1, n + 1):
        word_representation = number_to_words(i)
        total_letters += count_letters(word_representation)
    return total_letters

# Calculate the total number of letters from 1 to 1000
total_letters = count_letters_up_to(1000)
print("Total letters used from 1 to 1000:", total_letters)

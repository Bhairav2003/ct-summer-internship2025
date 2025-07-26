def solve(s):
    words = s.split()
    capitalized_words = []
    for word in words:
        if word and word[0].isalpha():
            capitalized_words.append(word[0].upper() + word[1:])
        else:
            capitalized_words.append(word)
    return ' '.join(capitalized_words)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

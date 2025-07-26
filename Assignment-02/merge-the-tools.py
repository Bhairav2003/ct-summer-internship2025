def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        t = string[i:i+k]
        u = ''
        seen = set()
        for char in t:
            if char not in seen:
                seen.add(char)
                u += char
        print(u)
    # your code goes here

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
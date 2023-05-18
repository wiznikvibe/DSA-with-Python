def reverse(text, idx, n):
    if idx == n:
        return
    temp = text[idx]
    reverse(text,idx+1,n)
    print(temp, end='')

string = "abcd"
n = len(string)
reverse(string, 0, n)
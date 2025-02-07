def permutations(string, answer=""):
    if len(string) == 0:
        print(answer)
        return
    



    for i in range(len(string)):
        letter1 = string[i]
        remaining = string[:i] + string[i + 1:]
        permutations(remaining, answer + letter1)

string = str(input())
permutations(string)

def convert_string(s):
    result = ''
    for c in s:
        if c == 'S':
            result += 'E'
        elif c == 'E':
            result += 'S'
        else:
            print("ERRROR")

    return result


T = int(input())

for i in range(T):
    N = input()
    s = input()

    print("Case #" + str(i + 1) + ": " + convert_string(s))
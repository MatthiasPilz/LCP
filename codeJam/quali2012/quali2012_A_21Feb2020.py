dic = {
    "a": "y",
    "b": "h",
    "c": "e",
    "d": "s",
    "e": "o",
    "f": "c",
    "g": "v",
    "h": "x",
    "i": "d",
    "j": "u",
    "k": "i",
    "l": "g",
    "m": "l",
    "n": "b",
    "o": "k",
    "p": "r",
    "q": "z",
    "r": "t",
    "s": "n",
    "t": "w",
    "u": "j",
    "v": "p",
    "w": "f",
    "x": "m",
    "y": "a",
    "z": "q",
    " ": " "
}


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().strip())

    for i in range(n):
        s = "Case #" + str(i+1) + ": "
        for j in range(len(arr[i])):
            s += dic[arr[i][j]]

        print(s)


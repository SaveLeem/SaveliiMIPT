vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"

f = open('input.txt', 'r')
data = f.read()
f.close()

res = ""
i = 0
while i < len(data):
    res += data[i]
    if data[i] in vowels:
        prev_vowel = (i > 0 and data[i-1] in vowels)
        next_vowel = (i + 1 < len(data) and data[i+1] in vowels)
        if not prev_vowel and not next_vowel:
            res += "с" + data[i]
        elif not prev_vowel and next_vowel:
            if i > 0 and data[i-1].isalpha() and data[i-1] not in vowels:
                res += "с" + data[i]
    i += 1

print(res)
 #Mr.Deepseek все красиво оформил
data = input("Введите строку")
mirror_letetrs_nch = "AHIMOTUVWXY18"
mirror_letetrs_ch = "EJSZ3L25"
#проверка на полиндром
def polindrom(data):
    cnt = 0
    for i in range(len(data)//2):
        if (data[i] == data[len(data)-1-i]):
            cnt = cnt + 1
        else:
            break
    if (cnt == len(data)//2):
        return True
    else:
        return False
#проверка наличия букв, имеющих отображение
def check_letetrs(data):
    cnt = 0
    for i in range(len(data)):
        if (mirror_letetrs_ch.find(data[i]) != -1 or
            mirror_letetrs_nch.find(data[i]) != -1 ):
            cnt = cnt + 1
        else:
            break
    if (cnt == len(data)):
        return True
    else:
        return False
#проверка того, что строка является зеркальной
def change_letters(data):
    mirrorred_reversed_data = [None] * len(data)
    for i in range(len(data)):
        if (mirror_letetrs_nch.find(data[i]) != -1):
            mirrorred_reversed_data[len(data)-1-i] = data[i]
        elif(mirror_letetrs_ch.find(data[i]) != -1):
            found = mirror_letetrs_ch.find(data[i])
            if (found > 3):
                represent = found - 4
            else:
                represent = found + 4
            mirrorred_reversed_data[len(data)-1-i] = mirror_letetrs_ch[represent]
    if mirrorred_reversed_data == list(data):
        return True
    else:
        return False
is_palindrome = polindrom(data)
has_mirror = check_letetrs(data)
is_mirrored = has_mirror and change_letters(data)

if not has_mirror:
    print(f'"{data}" is not a palindrome.')
elif is_palindrome and is_mirrored:
    print(f'"{data}" is a mirrored palindrome.')
elif is_mirrored:
    print(f'"{data}" is a mirrored string.')
elif is_palindrome:
    print(f'"{data}" is a regular palindrome.')
else:
    print(f'"{data}" is not a palindrome.')

#дипсик сильно помог, сказал, что я все правильно написал
#PS: комментарии сам писал по коду

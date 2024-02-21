def atbash(s):
    abc = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz"
    return s.translate(str.maketrans(
        abc + abc.upper(), abc[::-1] + abc.upper()[::-1]))

print(atbash("Привет Мир!"))

def atbash(s):
    abc = "abcdefghijklmnopqrstuvwxyz"
    return s.translate(str.maketrans(
        abc + abc.upper(), abc[::-1] + abc.upper()[::-1]))

print(atbash("Privet!"))



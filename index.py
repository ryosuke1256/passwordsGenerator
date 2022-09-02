import random, string

def generatePassword(passwordLength: int) -> str:
    passwords = string.ascii_letters + '#$&@'
    generatingPassword = ''
    for k in range(passwordLength):
        generatingPassword += random.choice(passwords)
    return generatingPassword

passwordLength: int = int(input('生成したいパスワードの文字数を入力してください: '))
print(generatePassword(passwordLength))

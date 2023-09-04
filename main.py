def palindrome(s):
    s = s.replace(" ","").lower()
    reversed_s = s[::-1]
    return s == reversed_s

print(palindrome(input('Введите слово или слова для проверки на палиндром')))
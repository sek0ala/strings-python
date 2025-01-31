def fizz_buzz():
    n = 1
    while n <= 100:
        if n%3 == 0 and n%5 == 0:
            print("FizzBuzz")
        elif n%3 == 0:
            print("Fizz")
        elif n%5 == 0:
            print("Buzz")
        else: print(n)
        n += 1

def reverse():
    s = input("Enter a string you would like to reverse\n")
    reverse = ''
    length = len(s)
    index = -(length + 1)
    letters = []
    for i in range(-1, index, -1):
        reversed += s[i]
    return reverse

def count_vowels(s):
    s = input("Enter a string\n")
    vowels = ['a', 'e', 'i', 'o', 'u']
    length = len(s)
    count = 0
    a = 0
    e = 0
    i = 0
    o = 0 
    u = 0
    for x in range(length):
        letter = s[x].lower()
        if letter in vowels:
            count += 1
            if letter == 'a':
                a += 1
            elif letter == 'e':
                e += 1
            elif letter == 'i':
                i += 1
            elif letter == 'o':
                o += 1
            elif letter == 'u':
                u += 1
    print(count)
    print(f'{a} A(s), {e} E(s), {i} I(s), {o} O(s), and {u} U(s)')

def check_palindrome():
    pass

def main():
    pass

if __name__ == '__main__': main()
d = {1: 'A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т', 2: 'D, G, Д, К, Л, М, П, У',
     3: 'B, C, M, P, Б, Г, Ё, Ь, Я', 4: 'F, H, V, W, Y, Й, Ы', 5: 'K, Ж, З, Х, Ц, Ч', 8: 'J, X, Ш, Э, Ю',
     10: 'Q, Z, Ф, Щ, Ъ'}

word = input()
word = word.upper()
points = 0

for i in word:
    if i in d[1]:
        points += 1
    elif i in d[2]:
        points += 2
    elif i in d[3]:
        points += 3
    elif i in d[4]:
        points += 4
    elif i in d[5]:
        points += 5
    elif i in d[8]:
        points += 8
    elif i in d[10]:
        points += 10

print(points)

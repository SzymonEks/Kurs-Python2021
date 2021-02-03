# a. Słowo występujące w pliku największą ilość razy.
# b. Słowo występujące w pliku najmniejszą ilość razy.
# c. Najdłuższe słowo
# d. Najkrótsze słowo
# e. Ilość samogłosek w całym pliku
# f. Ilość spółgłosek w całym pliku
# g. Ilość cyfr w całym pliku
# h. Ilość znaków specjalnych (bez spacji)

import collections
with open('words.txt', 'r') as z:
# a. Słowo występujące w pliku największą ilość razy.
    a = collections.Counter(z).most_common(1)
    print(a)
# b. Słowo występujące w pliku najmniejszą ilość razy.
    b = collections.Counter(z).most_common('-1')
    print(b)
# # c. Najdłuższe słowo
#     c= collections.Counter(z).most_common(1)[-1][0]
#     print(c)

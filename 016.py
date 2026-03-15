"""
Permutasi adalah susunan objek yang terurut. Misalnya, 3124 adalah salah satu kemungkinan permutasi dari angka 1, 2, 3, dan 4. Jika semua permutasi dicantumkan secara numerik atau alfabetis, kita menyebutnya urutan leksikografis. Permutasi leksikografis dari 0, 1, dan 2 adalah:

012 021 102 120 201 210

Berapakah permutasi leksikografis ke sejuta dari angka 0, 1, 2, 3, 4, 5, 6, 7, 8 dan 9?
"""

import itertools

counter = 0
for i in itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
    counter += 1
    if counter == 1000000:
        print("".join(map(str, i)))
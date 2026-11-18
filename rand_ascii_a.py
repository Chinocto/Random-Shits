from random import choice

size = 100
pcnt_A = 37
pcnt_letters = 67

ASCII_PRINTABLE_START = 32
ASCII_PRINTABLE_END = 126

ORD_A = ord("A")
ORD_Z = ord("Z")
ORD_a = ord("a")
ORD_z = ord("z")

NON_LETTER_ORDS = []
for r in [(ASCII_PRINTABLE_START, ORD_A - 1), (ORD_Z + 1, ORD_a - 1), (ORD_z + 1, ASCII_PRINTABLE_END)]:
    for n in range(r[0], r[1] + 1):
        NON_LETTER_ORDS.append(n)

LETTERS_ORDS = []
for r in [(ORD_A, ORD_Z), (ORD_a, ORD_z)]:
    for n in range(r[0], r[1] + 1):
        LETTERS_ORDS.append(n)

def rand_char_in_ords(ords):
    return chr(choice(ords))

def rand_printable_non_letter_ascii():
    return rand_char_in_ords(NON_LETTER_ORDS)

def rand_letter():
    return rand_char_in_ords(LETTERS_ORDS)

final_l = [rand_printable_non_letter_ascii() for i in range(size)]

def replace_random_percentage(arr, percentage, generator, indices=None):
    n = len(arr)
    k = int(n * (percentage / 100))
    
    replaced_indices = []
    left_indices = list(range(n)) if indices is None else indices
    
    for _ in range(k):
        i = choice(left_indices)
        
        left_indices.remove(i)
        replaced_indices.append(i)
        
        arr[i] = generator()
    return replaced_indices

def print_join(pl):
    print("".join(pl))

li = replace_random_percentage(final_l, pcnt_letters, rand_letter)
replace_random_percentage(final_l, pcnt_A, lambda _=None: "A", li)
print_join(final_l)

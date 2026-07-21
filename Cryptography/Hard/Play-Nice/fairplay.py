def build_matrix(alphabet):
    return [list(alphabet[i:i+6]) for i in range(0, 36, 6)]

def find_position(matrix, char):
    for r in range(6):
        for c in range(6):
            if matrix[r][c] == char:
                return r, c
    return None

def decrypt_playfair(ciphertext, alphabet):
    matrix = build_matrix(alphabet)
    plaintext = []
    
    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i+1]
        
        r1, c1 = find_position(matrix, char1)
        r2, c2 = find_position(matrix, char2)
        
        if r1 == r2:
            plaintext.append(matrix[r1][(c1 - 1) % 6])
            plaintext.append(matrix[r2][(c2 - 1) % 6])
        elif c1 == c2:
            plaintext.append(matrix[(r1 - 1) % 6][c1])
            plaintext.append(matrix[(r2 - 1) % 6][c2])
        else:
            plaintext.append(matrix[r1][c2])
            plaintext.append(matrix[r2][c1])
            
    return "".join(plaintext)

alphabet = "nk7lvy8wq96tzfodsjh41ib5xrae3cmpu02g"
ciphertext = "nx9kokre3ks4hkvxfjlsfquc73jvq6"

plaintext = decrypt_playfair(ciphertext, alphabet)

print("=== HASIL DEKRIPSI ===")
print(f"Plaintext mentah: {plaintext}")
print(f"Flag format perkiraan: {plaintext}")
import math
import sys

# funkcija za unos simbola i njihovih verovatnoca
# simboli i kodovi se cuvaju kao recnici u formatu { 'simbol': verovatnoca }


def get_probability_distribution():
    distribution = {}
    n = int(input("Unesite broj simbola: "))
    for i in range(1, n + 1):
        symbol = input(f"Unesite simbol {i}: ")
        probability = float(input(f"Unesite verovatnocu simbola {symbol}: "))
        distribution[symbol] = probability

    total_probability = sum(distribution.values())
    if total_probability != 1.0:
        print("Verovatnoce nisu jednake 1")
        sys.exit()
    return distribution



def huffman(p):
    # Base case of only two symbols, assign 0 or 1 arbitrarily
    if len(p) == 2:
        return dict(zip(p.keys(), ['0', '1']))

    # Create a new distribution by merging lowest prob. pair
    p_prime = p.copy()
    a1, a2 = lowest_prob_pair(p)
    p1, p2 = p_prime.pop(a1), p_prime.pop(a2)
    p_prime[a1 + a2] = p1 + p2

    # Recurse and construct code on new distribution
    c = huffman(p_prime)
    ca1a2 = c.pop(a1 + a2)
    c[a1], c[a2] = ca1a2 + '0', ca1a2 + '1'

    return c

def lowest_prob_pair(p):
    '''Return pair of symbols from distribution p with lowest probabilities.'''
    assert len(p) >= 2  # Ensure there are at least 2 symbols in the dist.

    sorted_p = sorted(p.items(), key=lambda x: x[1])
    return sorted_p[0][0], sorted_p[1][0]

# Get user input for probability distribution
user_input = get_probability_distribution()

# Funkcija za odredjivanje da li su kodovi prefiksi jedni drugih
def is_prefix(code1, code2):
    return code1.startswith(code2) or code2.startswith(code1)


# Racunanje entropije
def calculate_entropy(prob_distribution):
    '''Calculate entropy of a probability distribution.'''
    entropy = 0.0

    for probability in prob_distribution.values():
        entropy -= probability * (math.log(probability,2) if probability > 0 else 0)

    return entropy


# Hafmenov kod 
huffman_code = huffman(user_input)
print("Huffman Code:", huffman_code)

# Entropija
entropy = calculate_entropy(user_input)
print("Entropy:", entropy)


# Provera da li je kod trenutan prolazenjem kroz izlazni recnik
# Provera se vrsi tako sto se ispituje da li su neki od kodova u prefiksnoj vezi

symbols = list(huffman_code.keys())
for i in range(len(symbols)):
    for j in range(i + 1, len(symbols)):
        symbol_i, symbol_j = symbols[i], symbols[j]
        if is_prefix(huffman_code[symbol_i], huffman_code[symbol_j]) or is_prefix(huffman_code[symbol_j], huffman_code[symbol_i]):
            print(f"Generisani Hafmenov kodovi {huffman_code[symbol_i]} i {huffman_code[symbol_j]} su prefiksi jedni drugih.")
        
print("Kod je trenutan")


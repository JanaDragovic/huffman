import heapq
from collections import defaultdict
import math

# definisanje klase Node koja predstavlja cvor u stablu
class Node:
    def __init__(self, simbol, verovatnoca):

        #uneti simbol
        self.simbol = simbol
        self.verovatnoca = verovatnoca
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.verovatnoca < other.verovatnoca
    

# funkcija koja simbolima dodeljuje unesene verovatnoce
def huffman_coding(verovatnoce):
    heap = [Node(simbol, verovatnoca) for simbol, verovatnoca in verovatnoce.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.verovatnoca + right.verovatnoca)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    root = heap[0]
    codes = {}
    generisanje_Hafmenovih_kodova(root, "", codes)

    return codes

# funkcija koja rekurzivno prolazi kroz stablo i simbolima dodeljuje kodove
def generisanje_Hafmenovih_kodova(node, code, codes):
    if node.simbol:
        codes[node.simbol] = code
    if node.left:
        generisanje_Hafmenovih_kodova(node.left, code + "0", codes)
    if node.right:
        generisanje_Hafmenovih_kodova(node.right, code + "1", codes)

# entropija
def racunanje_entropije(verovatnoce):
    entropy = -sum(verovatnoca * (1 if verovatnoca > 0 else 0) * (math.log(verovatnoca, 2) if verovatnoca > 0 else 0) for verovatnoca in verovatnoce.values())
    return entropy


# provera uslova i izvrsavanje koda
if __name__ == '__main__':
    verovatnoce = {}
    sum_of_verovatnoce = 0

    while True:
        simbol = input("Unesite simbol ili 'kraj' kako biste zavrsili unos): ")
        if simbol == 'kraj':
            break
        verovatnoca = float(input("Unesite verovatnocu simbola: "))
        verovatnoce[simbol] = verovatnoca
        sum_of_verovatnoce += verovatnoca

    if sum_of_verovatnoce != 1:
        print("Greska! Zbir unesenih verovatnoca nije jednak 1.")
    else:
        huffman_codes = huffman_coding(verovatnoce)
        print("Hafmenov kod:")
        for simbol, code in huffman_codes.items():
            print(f"{simbol}: {code}")

        check_valid = all(code not in code for code in huffman_codes.values())
        print(f"Kod je trenutan: {check_valid}")

        entropy = racunanje_entropije(verovatnoce)
        print(f"Entropija: {entropy}")

def calculate_efficiency(huffman_codes, verovatnoce):
    average_code_length = sum(len(code) * verovatnoce[simbol] for simbol, code in huffman_codes.items())
    efficiency = entropy / average_code_length
    return efficiency

# Add this to your main block to use the function
efficiency = calculate_efficiency(huffman_codes, verovatnoce)
print(f"Efikasnost kompresije: {efficiency}")


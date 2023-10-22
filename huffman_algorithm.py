import heapq
from collections import defaultdict
import math

class Node:
    def __init__(self, symbol, probability):
        self.symbol = symbol
        self.probability = probability
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.probability < other.probability

def huffman_coding(probabilities):
    heap = [Node(symbol, probability) for symbol, probability in probabilities.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.probability + right.probability)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    root = heap[0]
    codes = {}
    generate_huffman_codes(root, "", codes)

    return codes

def generate_huffman_codes(node, code, codes):
    if node.symbol:
        codes[node.symbol] = code
    if node.left:
        generate_huffman_codes(node.left, code + "0", codes)
    if node.right:
        generate_huffman_codes(node.right, code + "1", codes)

def calculate_entropy(probabilities):
    entropy = -sum(probability * (1 if probability > 0 else 0) * (math.log(probability, 2) if probability > 0 else 0) for probability in probabilities.values())
    return entropy

if __name__ == '__main__':
    probabilities = {}
    sum_of_probabilities = 0

    while True:
        symbol = input("Enter a symbol (or 'done' to finish): ")
        if symbol == 'done':
            break
        probability = float(input("Enter the probability of the symbol: "))
        probabilities[symbol] = probability
        sum_of_probabilities += probability

    if sum_of_probabilities != 1:
        print("Sum of probabilities is not equal to 1. Exiting.")
    else:
        huffman_codes = huffman_coding(probabilities)
        print("Huffman Codes:")
        for symbol, code in huffman_codes.items():
            print(f"{symbol}: {code}")

        check_valid = all(code not in code for code in huffman_codes.values())
        print(f"Codes are current: {check_valid}")

        entropy = calculate_entropy(probabilities)
        print(f"Entropy: {entropy}")

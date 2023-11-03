
def compress_string(s: str) -> str:
    char_map: dict = {}

    for char in s:
        char_map[char] = char_map.get(char, 0) + 1
    
    compressed_string: str = ''.join([f"{key}{value}" for key, value in char_map.items()])

    return compressed_string if len(compressed_string) < len(s) else s

input1: str = "aaabcccccaaa"
output1: str = compress_string(input1)
print("Compressed String 1: ", output1)

input2: str = "xxxxyyzyzzzxyzz" 
output2: str = compress_string(input2)
print("Compressed String 2: ", output2)

input3: str = "aabb"
output3: str = compress_string(input3)
print("Compressed String 3: ", output3)

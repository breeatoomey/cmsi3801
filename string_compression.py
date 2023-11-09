def compress_string(s: str) -> str:
    compressed_list = []
    char_count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            char_count += 1
        else:
            compressed_list.append(s[i - 1] + str(char_count))
            char_count = 1

    compressed_list.append(s[-1] + str(char_count))
    compressed_string = "".join(compressed_list)

    return compressed_string if len(compressed_string) < len(s) else s


# Tests:
input1: str = "aabcccccaaa"  # a2b1c5a3
output1: str = compress_string(input1)
print("Compressed String 1: ", output1)

input2: str = "xxxxyyzyzzzzz"  # x4y2z1y1z5
output2: str = compress_string(input2)
print("Compressed String 2: ", output2)

input3: str = "aabb"  # aabb
output3: str = compress_string(input3)
print("Compressed String 3: ", output3)

input4: str = "xxyyyzxyzzyyxxzyzxyz"  # xxyyyzxyzzyyxxzyzxyz
output4: str = compress_string(input4)
print("Compressed String 4: ", output4)

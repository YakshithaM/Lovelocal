def length_of_last_word(s):
    words = s.split()
    if not words:
        return 0
    return len(words[-1])
input1 = "Hello World"
output1 = length_of_last_word(input1)
print(f"Input: {input1}\nOutput: {output1}\n")

input2 = "   fly me   to   the moon  "
output2 = length_of_last_word(input2)
print(f"Input: {input2}\nOutput: {output2}\n")

input3 = "luffy is still joyboy"
output3 = length_of_last_word(input3)
print(f"Input: {input3}\nOutput: {output3}")
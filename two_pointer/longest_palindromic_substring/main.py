s ="cbbd"
# s ="bb"
# if len(s)==0:
#     return ""
even = 1 if len(s) %2 == 0 else 0

left_pointer= 0
right_pointer= 0
longest_palandrom = ""

for base_pointer in range(len(s)):
    left_pointer = base_pointer
    right_pointer = base_pointer + even
    current_word = s[left_pointer :right_pointer+1 + even]
    for i in range(base_pointer, len(s)):
        left_pointer -= 1
        right_pointer += 1
        if left_pointer < 0 or right_pointer > len(s)- 1:
            break
        elif s[left_pointer] == s[right_pointer]:
            current_word = s[left_pointer:right_pointer+1]
        else:
            break
    longest_palandrom = current_word if len(current_word) > len(longest_palandrom) else longest_palandrom

print( longest_palandrom)
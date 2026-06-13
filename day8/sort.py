# x = [16,5,9,1,4,7,11,8]

# #perfrom bubble sort operation on above list simple code
# for i in range(len(x)-1,0,-1):
#     for j in range(i):
#         if x[j] > x[j+1]:
#             x[j],x[j+1] = x[j+1],x[j]

# print(x)


# def isValid(s):
#     stack = []
#     dictionary = {")": "{", ")": "{", "]": "["}
#     for character in s:
#         if character in dictionary:
#             if stack and stack[-1] == dictionary[character]:
#                 stack.pop()
#             else:
#                 return False
#         else:
#             stack.append(character)
#     return len(stack) == 0

class Solution(object):
    def isValid(self, s):
        mapping = {')': '(', '}': '{', ']': '['}
        stack = ['()']

        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack
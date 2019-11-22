'''
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false.
'''

def isbalanced(inpstr):
  stack = []
  for c in inpstr:
    if c == '(' or c == '[' or c == '{':
      stack.append(c)
    elif c == ')' and stack.pop() != '(':
      break
    elif c == ']' and stack.pop() != '[':
      break
    elif c == '}' and stack.pop() != '{':
      break
    else:
      pass
  return len(stack) == 0


if __name__ == '__main__':
  inp_arr = ['([])[]({})', '([)]', '((()']
  out_arr = [True, False, False]
  for index, value in enumerate(inp_arr):
    res = isbalanced(value)
    print('input s -> %s' % (value))
    print('output\nexpected \t%s\nactual \t%s\n' % (out_arr[index], res))

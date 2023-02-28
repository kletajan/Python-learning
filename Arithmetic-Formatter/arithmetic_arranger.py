import re

def arithmetic_arranger(problems, solve=False):

  if(len(problems) > 5): return "Error: Too many problems."
    
  first_line = ""
  second_line = ""
  total = ""
  text = ""
  lines = ""
  for problem in problems:
    if (re.search("[^\s0-9.+-]", problem)):
      if (re.search("[/]", problem) or re.search("[*]", problem)):
        return "Error: Operator must be '+' or '-'."      
      return "Error: Numbers must only contain digits."

    firstNB = problem.split(" ")[0]
    sign = problem.split(" ")[1]
    secondNB = problem.split(" ")[2]

    if(len(firstNB) >= 5 or len(secondNB) >= 5):
      return "Error: Numbers cannot be more than four digits."

    sum = ""
    if(sign == "+"):
      sum = str(int(firstNB) + int(secondNB))
    elif(sign == "-"):
      sum = str(int(firstNB) - int(secondNB))

    length = max(len(firstNB), len(secondNB)) + 2
    top_line = str(firstNB).rjust(length)
    bottom_line = sign + str(secondNB).rjust(length - 1)
    line = ""
    rest_space = str(sum).rjust(length)
    for s in range(length):
      line += "-"

    if problem != problems[-1]:
      first_line += top_line + '    '
      second_line += bottom_line + '    '
      lines += line + '    '
      total += rest_space + '    '
    else:
      first_line += top_line
      second_line += bottom_line
      lines += line
      total += rest_space

  if solve:
    text = first_line + "\n" + second_line + "\n" + lines + "\n" + total
  else:  
    text = first_line + "\n" + second_line + "\n" + lines
  return text
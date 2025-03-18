def addmultiplenumbers (numbers):

  total = 0
  for num in numbers:
    total += num

    return total
  
def multiplymultiplenumbers (numbers):

  total = 1
  for num in numbers:
    total *= num

    return total
  

def isiteven(num):
  if num % 2 == 0:
    return True
  else:
    return False



def main():
  print("Hello learners!")

      

if __name__=="__main__":
  main()
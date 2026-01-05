import time

i= 1
def code():
  global i
  print(i)
  i+=1

def looper():
  while True:
    print("\nProgram Awoke\n")
    code()
    print("\nProgram Sleeping\n")
    time.sleep(10)

if __name__ == "__main__":
    looper()
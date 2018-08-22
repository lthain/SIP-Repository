# --- Define your functions below! ---
def intro():
    print("You've come to a mysterious place and hear whispering.")

def response(userResponse):
    
# --- Put your main program below! ---
def main():
  while True:
    answer = input("(What will you say?) ")
    response(answer)
    break

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  intro()
  main()

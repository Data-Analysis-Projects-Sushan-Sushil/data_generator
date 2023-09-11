import random
start = int(input("Enter the range: "))

random_integers = [random.randint(1, start) for _ in range(start)]

print("list: ", random_integers)

cmd1 = input("Would you like to save the list of integers as a file (Y/N): ")



if cmd1 == "Y":
    
    header = input("Enter the name for column: ")
    # Open a file in write mode
    with open('random_integers.txt', 'w') as f:
        #writing_header
        f.write(header + '\n')
        
        for num in random_integers:
            f.write(str(num) + '\n')
    
    print("The list of random integers has been saved to 'random_integers.txt'.")
else:
    print("Thank you :) ")

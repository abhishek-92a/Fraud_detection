# model.py is a file in branch model to experiment on different models without breaking the master branch

# Print an inverted pramid of height height

height = int(input("Enter the height of the pyramid "))

for i in range(height,0,-1):
    for j in range(0, i):
        print(i , end =" ")
        i-=1
    print(" ")

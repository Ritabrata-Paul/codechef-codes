# We have populated the solutions for the 10 easiest problems for your support.
# Click on the SUBMIT button to make a submission to this problem.

#Note that it's python3 Code. Here, we are using input() instead of raw_input().
#You can check on your local machine the version of python by typing "python --version" in the terminal.


#Solution provided by Sloth Coders 
n = int(input())
for _ in range(n):
    num = input()
    sum = 0
    for i in num:
        sum += int(i)
    print(sum)

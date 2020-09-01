import random

fact_mem = []
mult_mem = []
range_mem = 0

def calc_factors(num):
    prime_nos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if num == 1:
        print("This number do not have any factors")
    elif num in prime_nos:
        print("This is a prime number")
    else:
        fact_li = []
        i=2
        while i<num:
            if num%i == 0 and not(i in fact_mem):
                fact_li.append(i)
            i += 1
        random.shuffle(fact_li)
        fact_mem.append(fact_li[0])
        print("One factor of that number is (Hint: excluding itself): ", fact_li[0])

def calc_multiples(num):
    multiple = num*random.randint(2,10)
    while multiple in mult_mem:
        multiple = num*random.randint(2,10)
    print("One multiple to that number is (Hint: between [2x] to [10x]): ",multiple)
    mult_mem.append(multiple)

def calc_range(num):
    num1 = 0
    num2 = 0
    if num>20-4*range_mem and num<80+4*range_mem:
        while not((num >= num1 and num <= num2) or (num >= num2 and num <= num1)):
            num1 = random.randint(num-10+2*range_mem,num+10-2*range_mem)
            num2 = random.randint(num-10+2*range_mem,num+10-2*range_mem)
            if (num >= num1 and num <= num2):
                print("The number lies between (inclusive): ", num1, ", ", num2)
            elif (num >= num2 and num <= num1):
                print("The number lies between: (inclusive)", num2, ", ", num1)
    elif num<=20-4*range_mem:
        while not((num >= num1 and num <= num2) or (num >= num2 and num <= num1)):
            num1 = random.randint(0,20-4*range_mem)
            num2 = random.randint(0,20-4*range_mem)
            if (num >= num1 and num <= num2):
                print("The number lies between (inclusive): ", num1, ", ", num2)
            elif (num >= num2 and num <= num1):
                print("The number lies between: (inclusive)", num2, ", ", num1)
    elif num>=80+4*range_mem:
        while not((num >= num1 and num <= num2) or (num >= num2 and num <= num1)):
            num1 = random.randint(80+4*range_mem,100)
            num2 = random.randint(80+4*range_mem,100)
            if (num >= num1 and num <= num2):
                print("The number lies between (inclusive): ", num1, ", ", num2)
            elif (num >= num2 and num <= num1):
                print("The number lies between: (inclusive)", num2, ", ", num1)



case = list(range(0,3))
random.shuffle(case)

def clue(num,itr): #operation/clue selector
    if case[0] == itr%3:
        calc_range(num)
    elif case[1] == itr%3:
        calc_multiples(num)
    elif case[2] == itr%3:
        calc_factors(num)



#Execution starts from here
print ("""Welcome player, please read the instructions:
1. You have 100 points initially.
2. Each wrong guess will cost you 10 points.
3. Guess the number correctly using the given clues.
4. If your points goes less than 0, you loose, else you win.\n""")

num = random.randint(1,100)
points = 100
deduction = 10
user_input = 0
itr = 0;

#menu
while points>0:
    clue(num,itr)
    itr += 1
    user_input = int(input("Guess the number: "))
    if user_input == num:
        print("\nNow you got it right!\n")
        break
    else:
        print("\nYou were very wrong this time!\n")
        points -= deduction

print("Number is: ", num)

if (points <= 0):
    print("\nSorry, You failed.\n")
else:
    print("\nYour score: ",points,"\n")
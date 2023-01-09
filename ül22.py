import random
choice = ['kivi', 'paber', 'käärid']

while true: 
    
print('0) ei soovi rohkem mängida')
print('1)kivi')
print('2)paber')
print('3)käärid')
user_choice = int(input('Tee valik '))
computer_choice = random.randint(1, 3)

if user_choice != 0:
    break

print('sinu valik oli' , choices[user_choice-1])
print('arvuti valik oli' , choices[computer_choice-1])


if user_choice == computer_choice:
    print('viik!')
elif user_choice == 1 and computer_choice == 3 or user_choice == 2 and computer_choice == 1 or user_choice == 3 and computer_choice == 2:
    print('sinu võit!')
else:
    print('arvuti võit')

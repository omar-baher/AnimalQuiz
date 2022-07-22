import datetime
from colorama import Fore

score = 0
life = 3

day = datetime.datetime.now()

print(f"{Fore.GREEN}")
print(f'-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*{Fore.LIGHTRED_EX}')
print(f'---------------------> Welcome to the Animal Quiz <------------------------{Fore.LIGHTCYAN_EX}')
print(f'---------------------> Developed by Omar Elkobia <------------------------{Fore.GREEN}')
print(f'-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')


questions = {
    'What is the largest animal? ': 'whale',
    'What is the smallest animal? ': 'ant',
    'What is the fastest animal? ': 'cheetah',
    'What is the slowest animal? ': 'turtle',
    'What is the common pet? ': 'cat'
}

for question, answer in questions.items():
    if life <= 0:
        print(f'You have {life} life left, you lost 😠')
        break

    print(Fore.GREEN)
    q_answer = input(question)

    if answer == q_answer.lower().rstrip().lstrip():
        print(f"{Fore.LIGHTCYAN_EX}You are correct 😀")
        score = score + 1
    else:
        print(f"{Fore.LIGHTCYAN_EX}You are incorrect 😠")
        life = life - 1

print('')
print(f'{Fore.LIGHTCYAN_EX}You answered {score} out of {len(questions)} correct')

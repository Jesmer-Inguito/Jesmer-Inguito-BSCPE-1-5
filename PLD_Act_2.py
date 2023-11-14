import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

name = 'Jesmer H. Inguito'
age = '18 yrs old'
address = 'Blk 10 Lot 42 Legian 1 Subd. Carsadang Bago 2, Imus Cavite'

print(Fore.MAGENTA + Style.BRIGHT + 'Name: ' + Fore.GREEN + Style.BRIGHT + name)
print(Fore.MAGENTA + Style.BRIGHT + 'Age: ' + Fore.GREEN + Style.BRIGHT + age)
print(Fore.MAGENTA + Style.BRIGHT + 'Address: ' + Fore.GREEN + Style.BRIGHT + address)
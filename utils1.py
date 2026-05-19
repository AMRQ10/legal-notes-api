from colorama import Fore, Style, init

init(autoreset=True)



def print_header(title):
    print(Fore.CYAN + "=" * 30)
    print(Style.BRIGHT + title)
    print(Fore.CYAN + "=" * 30)

    print(Fore.GREEN + "Note added successfully.")
    print(Fore.RED + "ERROR: Emplpoyee name cannot be empty.")
    print(Fore.CYAN + "=" * 30)
    print(Style.BRIGHT + "Employee Notes System")

def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty")
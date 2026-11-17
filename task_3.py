import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)  # колір скидається після кожного print


def show_tree(path, indent=""):
    """Рекурсивно виводить вміст папки: папки синім, файли зеленим."""
    for item in sorted(path.iterdir()):
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}📂 {item.name}")
            show_tree(item, indent + "    ")
        else:
            print(f"{indent}{Fore.GREEN}📜 {item.name}")


def main():
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Вкажіть шлях до папки: python3 task_3.py /шлях/до/папки")
        return

    path = Path(sys.argv[1])

    if not path.exists():
        print(f"{Fore.RED}Шлях не існує: {path}")
        return
    if not path.is_dir():
        print(f"{Fore.RED}Це не папка: {path}")
        return

    print(f"{Fore.YELLOW}📦 {path.resolve().name}")
    show_tree(path, "    ")


if __name__ == "__main__":
    main()
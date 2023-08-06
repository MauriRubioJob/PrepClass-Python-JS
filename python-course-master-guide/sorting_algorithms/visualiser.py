import time
import os

t_width, t_height = os.get_terminal_size()


def create_displayer(*, delay=00, user=False):
    os.system("cls")

    def display(values, highlight=None, colour=None, offset=0):
        output = f"\033[{offset+3};0H"
        char = "▅"
        for i, n in enumerate(values):
            output += f"{n:>2} "
            for j in range(t_width - 4):
                if j > n:
                    output += " "
                elif colour and i in colour:
                    output += f"\033[92m{char}\033[0m"
                elif highlight and i in highlight:
                    output += f"\033[93m{char}\033[0m"
                else:
                    output += char
            output += "\n"
        print(output)
        if delay:
            time.sleep(delay)
        elif user:
            input()
    return display

import webbrowser
import pyperclip
import argparse
from random import choice

parser = argparse.ArgumentParser(description="Select random elements from your clipboard")
parser.add_argument("--amount", metavar="A", default=10, type=int, help="Amount of items to select, defaults to 10")
parser.add_argument("--open", action=argparse.BooleanOptionalAction, help="Open the links in the web browser", default=True)
args = parser.parse_args()

all_elements = pyperclip.paste().split('\n')
selected_elements = []
for _ in range(args.amount):
    selected_elements.append(choice(all_elements))

for id, element in enumerate(selected_elements):
    print(f"{id+1}: {element}")
    if args.open == True:
        webbrowser.open_new_tab(element)
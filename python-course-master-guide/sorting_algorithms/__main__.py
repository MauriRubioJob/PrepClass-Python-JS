import random


from bubble_sort import bubble
from merge_sort import merge_pure, merge_inplace
from visualiser import create_displayer

display = create_displayer(delay=0.01)
data = random.sample(range(50), k=32)


bubbled = data.copy()
bubble(bubbled, printer=display)
input()
merged = data.copy()
merge_inplace(merged, printer=display)


# print(f"{'Original:':<10}{data}")
# print(f"{'Bubble:':<10}{bubbled}")
# print(f"{'Merge:':<10}{merged}")

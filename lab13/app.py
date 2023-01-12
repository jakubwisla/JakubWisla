from typing import List
def bubblesort(input_array: List) -> List:
    if not isinstance(input_array, List): # sprawdzenie czy argument funkcji jest listą
        return None
    n = len(input_array)
    copy_list = input_array
    while n > 1: # pętla, w której następuje sortowanie
        changes = 0 # zmienna wprowadzona, aby pętla zatrzymała się, gdy lista jest posortowana
        for i in range(1, n):
            if copy_list[i - 1] > copy_list[i]:
                copy_list[i - 1], copy_list[i] = copy_list[i], copy_list[i - 1]
                changes += 1
        if changes == 0:
            break # przerwanie pętli w momencie posortowania listy
        n -= 1
    return copy_list
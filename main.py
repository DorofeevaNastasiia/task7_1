import random


def check_input(arr):
    if len(arr) == 2:
        if type(arr[0]) == int and type(arr[1]) == int:
            if arr[0] < arr[1]:
                return True
    return False


def get_ladder(arr):
    index = random.randint(arr[0], arr[1])
    b_n = ['*' * x for x in range(arr[1], index-1, -1)]
    a_n = ['*' * x for x in range(arr[0], index+1, 1)]
    return b_n + a_n


def main(arr):
    for i in arr:
        if check_input(i):
            fnl = get_ladder(i)
            #print(fnl)
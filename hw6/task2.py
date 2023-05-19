
def find_num(array,n):
    for s, d in enumerate(array):
        if s == n-1:
            print(f'num_in_seq({n}) = {d}')

array = [8, 15, 22, 29, 36]
n=int(input('What number would you like to see: '))

find_num(array,n)
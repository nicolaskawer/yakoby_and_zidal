# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def check_row(row):
    for r in range(size):
        sum = 0
        for r1 in range(size):
            if r == r1:
                continue
            else:
                sum += row[r1]
        if sum < row[r]:
            mat_dict[r] = row
            return

def dominant_diagonal():
    for n in range(size):
        check_row(matrixA[i])
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    matrixA = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
    vectorB = [[2], [6], [5]]
    size = 3
    mat_dict = {}
    for i in range(size):
        mat_dict[i] = []

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

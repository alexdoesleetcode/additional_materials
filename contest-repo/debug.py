def printgrid(grid, width=3, x_axis=None, y_axis=None):
    n = len(grid)
    if n == 0:
        print("--no rows--")
        return
    m = len(grid[0])
    if m == 0:
        print("--no cols--")
        return
    if y_axis:
        y_axis_width = max([len(str(label)) for label in y_axis])
    if x_axis:
        if y_axis:
            print(" " * (y_axis_width + 2), end="")
        for j in range(m):
            print(str(x_axis[j]).rjust(width), end="")
        print()
        if y_axis:
            print(" " * (y_axis_width + 2), end="")
        print("-" * (width*m))
    for i in range(n):
        if y_axis:
            print(str(y_axis[i]).rjust(y_axis_width), end=" |")
        for j in range(m):
            print(str(grid[i][j]).rjust(width), end="")
        print()
#PF-Prac-42
def maxvalue_in_column(pixel_grid):
    #start writing your code here
    l1 = []
    for i in zip(*pixel_grid):
        l1.append(max(i))


    result_list = l1
    return result_list

pixel_grid = [[4, 2, 3],
            [16, 5, 0],
            [3, 200, 6],
            [0, 10, 12]]
pixel_grid1 = [[4],
             [16],
             [3],
             [0]]
pixel_grid2 = [[4, 2, 3]]
pixel_grid3 = [[6]]

print("Pixel grid is:")
for i in pixel_grid:
    print(i)
output = maxvalue_in_column(pixel_grid2)
print("The maximum values of each column are:", output)

'''
Failed but educational

def frequency_sort(items):

    def second_value(x):
        return x[1]

    result_list = list((i, items.count(i)) for i in items)
    result_list.sort(key=second_value, reverse=True)
    print(result_list)
    result = [x[0] for x in result_list]
    print(result)
    return result
'''

"""
TODO IN FUTURE

def find_sequence(matrix: List[List[int]]) -> bool:

    def get_neighbours(current_elem, elem_row, elem_col, match_counter: int) -> bool:
        for r in range(-1, 1):
            for c in range(-1, 1):
                if r == 0 and c == 0:
                    continue
                try:
                    #print("checking " + matrix[elem_row+r][elem_col+c] + " and " + str(current_elem))
                    if int(matrix[elem_row+r][elem_col+c]) == current_elem:
                        print(match_counter + " for " + str(matrix[elem_row+r][elem_col+c]) +
                              " in " + str(elem_row+r) + " " + str(elem_row+r))
                        match_counter += 1
                        if match_counter == 4:
                            return True
                        return get_neighbours(current_elem, [elem_row+r], [elem_col+c], match_counter)
                except:
                    continue
        return False

    for row_ind, row in enumerate(matrix, start=0):
        for elem_ind, elem in enumerate(row, start=0):
            print("start " + str(row_ind) + " " + str(elem_ind) + " -> " + str(elem))
            if get_neighbours(elem, row_ind, elem_ind, 0):
                return True

    return False
"""


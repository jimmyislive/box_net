# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
Box Towers

In the not so distant future, Box has commissioned you to design the new Box Worldwide Headquarters - The Box Towers. The design principal is a series of boxes (what else?),  one on top of each other. Each department in Box will be located in a different box.

Now each department has decided they have different needs in terms of the height, width and length (depth) of their box. For structural integrity reasons, you must also not place a box that has a larger footprint on top of a box with a smaller footprint i.e a box can be kept on the top of another box only if the Length of the upper box is not more than the Length of box below and the same for Width. You may rotate the boxes as necessary to make any of the face as base i.e 3D rotation is allowed.

Given the set of boxes, come up with the tallest building possible while satisfying the above constraints. It may not be possible to use all the boxes.

Input Format:

1st line contains the number of boxes , N.

Then follow N lines describing the configuration of each of the N boxes. Each of these lines contain three integers (length, width and height of the box)

Output Format:

Output a single line which is the height of the tallest possible building that can be formed with some of the boxes given and satisfying the constraints.

Sample Input

 

3
5 2 4
1 4 2
4 4 2

 

Sample Output

13

Explanation

Place box 2 on top below which is box 1 and the bottom-most box is box 3. Box 2 is placed with base ( 1 2 ) and height 4 , box 1 is placed with base ( 2 4 ) and height 5, and box 3 is placed with base ( 2 4 ) and height 4. So total height of this tower is 13.

Constraints:

N, the number of boxes is not more than 20

For any box , 1 <= Length,Width,Height <= 100
'''

import copy

def _is_valid(stack, new_item):
    if not stack:
        return True

    length, width = stack[len(stack) - 1]
    if (new_item[0] > length or new_item[1] > width):
        if (new_item[0] > width or new_item[1] > length):
            return False
        else:
            return True
    else:
        return True

def _get_area_dimensions(element, height_dimension):
    length_width_dimensions = []
    dim_considered = False
    for i in range(len(element)):
        if element[i] == height_dimension and not dim_considered:
            dim_considered = True
        else:
            length_width_dimensions.append(element[i])

    return length_width_dimensions

def get_max_height(boxes, n_at_a_time, max_level=0, max_current_level_iteration=0, arrays_stack=[], already_seen=[],level=0):

    if level + 1 > n_at_a_time:
        return max(max_level, max_current_level_iteration)


    for element in boxes:

        if element in already_seen:
            continue

        new_already_seen = copy.deepcopy(already_seen)
        new_already_seen.append(element)

        for dimension in element:

            if arrays_stack:
                if not _is_valid(arrays_stack, _get_area_dimensions(element, dimension)):
                    continue

            new_stack = arrays_stack + [_get_area_dimensions(element, dimension)]
            max_level = get_max_height(boxes, n_at_a_time, max_level, max_current_level_iteration + dimension, new_stack , new_already_seen, level + 1)

    return max_level



def main():

    num_of_inputs = int(raw_input())

    boxes = []
    for i in range(num_of_inputs):
        data = raw_input().split()
        data.sort()
        dim1, dim2, dim3 = data
        boxes.append((int(dim1), int(dim2), int(dim3)))

    max_so_far = 0
    max_current_level = 0

    for n_at_a_time in range(1, num_of_inputs + 1):
        max_so_far = max(max_so_far, get_max_height(boxes, n_at_a_time))

    print max_so_far

if __name__ == '__main__':
    main()

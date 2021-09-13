"""
You are assigned to put some amount of boxes onto one truck. You are given a 2D array
boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be
put on the truck. You can choose any boxes to put on the truck as long as the number of
boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.

Example 1:
Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

Example 2:
Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91
"""


def maximum_units(box_types, truck_size):
    box_types.sort(key=lambda x: -x[1])
    max_units = 0

    for num_boxes, unit in box_types:
        if truck_size <= num_boxes:
            max_units += truck_size * unit
            break
        max_units += num_boxes * unit
        truck_size -= num_boxes
    return max_units


# -------------------- Another Solution -------------------------

def maximum_units_2(box_types, truck_size):
    box_types_sorted = sorted(box_types, key=lambda x: x[1], reverse=True)
    num_units = 0
    for box_type in box_types_sorted:
        num_boxes = min(box_type[0], truck_size)
        num_units += num_boxes * box_type[1]
        truck_size -= num_boxes
        if truck_size == 0:
            break
    return num_units


if __name__ == "__main__":
    maximum_units([[5, 10], [2, 5], [4, 7], [3, 9]], 10)

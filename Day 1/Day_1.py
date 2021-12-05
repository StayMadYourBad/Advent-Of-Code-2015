"""
--- Day 1: Not Quite Lisp ---
Santa was hoping for a white Christmas, but his weather machine's "snow" function is powered by stars, and he's fresh out! To save Christmas, he needs you to collect fifty stars by December 25th.

Collect stars by helping Santa solve puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Here's an easy puzzle to warm you up.

Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

For example:

(()) and ()() both result in floor 0.
((( and (()(()( both result in floor 3.
))((((( also results in floor 3.
()) and ))( both result in floor -1 (the first basement level).
))) and )())()) both result in floor -3.
To what floor do the instructions take Santa?

"""

def directions_to_floor(stairs_data: str) -> int:
    """
    Takes in the stairs directions and converts it to the floor level.

    Args:
        stairs_data (str): The stairs_instructions given to us by Santa


    Returns:
        int: The floor Santa needs to go to

    """
    return stairs_data.count("(") - stairs_data.count(")")


if __name__ == "__main__":

    with open("day_1_data.txt", 'r') as file:
        stairs_data = [data.strip() for data in file][0]
    
    floor_level = directions_to_floor(stairs_data)
    print(f"The directions would lead Santa to the {floor_level} floor")
    
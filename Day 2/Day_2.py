"""
--- Day 2: I Was Told There Would Be No Math ---
The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

For example:

A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

To begin, get your puzzle input.
    """

def wrapping_paper_calculator(length: int, width: int, height: int) -> int:
    surface_area = (2 * length * width ) + (2 * width * height) + (2 * height * length)
    area_smallest_side = min(length * width, length * height, width * height)
    return surface_area + area_smallest_side
    

if __name__ == "__main__":
    with open(r"C:\Users\safee\Desktop\Grinch's Revenge\Advent of Code 2015\Day 2\day_2_data.txt", 'r') as file:
        data = [dimensions.strip() for dimensions in file]

    total_square_feet = 0
    for dimensions in data:
        length, width, height = dimensions.split("x")
        total_square_feet += wrapping_paper_calculator(int(length), int(width), int(height))
    
    print(f"The elves would need {total_square_feet} square feet of wrapping paper")


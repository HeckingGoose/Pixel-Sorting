# Pixel-Sorting
**Built for Python 3.10+**

A Python-based program that takes an input image and returns an output image where the pixels have been sorted based on a few parameters.

The program can sort across both the x and y axis, with either a descending or ascending sort. The program uses the r, g or b values of each pixel to determine the order of which they are sorted.

Here's an example:

Unsorted | Sorted
:-------------------------:|:-------------------------:
![Unsorted](https://github.com/HeckingGoose/Pixel-Sorting/blob/00cdba28e9859adf7f88cbc3abe2750ed69e9433/TestImage.png) | ![Sorted](https://github.com/HeckingGoose/Pixel-Sorting/blob/00cdba28e9859adf7f88cbc3abe2750ed69e9433/Sorted/TestImage_sorted(g%2C%20ascend%2C%20ascend).png)

Not the prettiest result, but it is ***literal*** pixel sorting, so i'd recommend using it for the backgrounds of images or something.

#
### To do:
- [x] Replace bubble sort with an algorithm that scales better,
- [x] Limit how large the Pygame window can be so that large images do not cover a user's entire screen space,
- [ ] Implement a system for allowing the window to be resized during runtime, while maintaining its aspect ratio,
- [ ] Implement support for more sort values,
- [ ] Try and implement a mode where the sorting is a little prettier.

🦆

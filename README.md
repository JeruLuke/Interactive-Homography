# Selective-Homography
Sometimes theremight be a need to engrave one image into another. Homography can help you achieve that. This easy-to-understand repo has an implementation using OpenCV to choose where you want to engrave an image at a location of your choice.

To know more about Homography visit the [blog post by Satya Mallick](https://www.learnopencv.com/homography-examples-using-opencv-python-c/). It is written in a way easy to understand along with code examples in Python and C++. Towards the end of the post he mentions the steps to make a virtual billboard. This is what I am about to demonstrate here. 

I have an image of a street in New York (the image in the blog) and would like to place an image having the cast of Spartacus (TV series) on one of their billboards.

Here are the images used:

1. The street of New York city:

![alt text](https://github.com/JeruLuke/Interactive-Homography/blob/master/images/billboard.jpg)

2. The cast of the TV series Spartacus:

![alt text](https://github.com/JeruLuke/Interactive-Homography/blob/master/images/Spartacus.jpg)

## Software and Installation

Any version of Python with OpenCV version 3.0.0 (at the least).

## Project Structure

```
Main Folder
  |--> homography_mouseclick.py
  |--> homography_mouseclick_argument.py
  |--> images
     |--> billboard.jpg (base image)
     |--> Spartacus.jpg (inner image)
  |--> results
     |--> mask.jpg
     |--> Spartacus_billboard.jpg
     |--> warped.jpg
     |--> Final.jpg
```

## How to run it?

Open the terminal, navigate to the location of the repository and execute the following:

`python homography_mouseclick_argument.py -b images/billboard.jpg -s images/Spartacus.jpg`

Notice the two arguments:

1. `-b` takes in the base image (the image where the other image is to be placed). Here it is `billboard.jpg`.
2. `-s` takes in the inner image to be placed (otherwise called homographed image). Here it is `Sapartacus.jpg`.

Upon execution both the input images would show up. Choose **four** points on the base image where you want the other image to be placed. Selection of points must be in anti-clockwise direction starting from top-left, in other words: top-left -> top-right -> bottom-right -> bottom_left. Have a look at the following:

![alt text](https://github.com/JeruLuke/Interactive-Homography/blob/master/point_ordering.JPG)

After choosing the four points correctly, the program displays 4 windows:
1. An image with the chosen points (`Marked_image.jpg`)
2. A window with the homographed image warped in with dimensions of the base image. (`warped.jpg`)
3. Another window containing the mask which needs to be added with the previous image. (`mask.jpg`)
4. The expected result. (`Final.jpg`)

## Result

The following are the results:

**Point-marked image:**

![alt text](https://github.com/JeruLuke/Interactive-Homography/blob/master/results/Marked_image.jpg)

**Warped Image:**

![alt text](https://github.com/JeruLuke/Interactive-Homography/blob/master/results/warped.jpg)

**Mask Image:**

![alt text](https://github.com/JeruLuke/Interactive-Homography/blob/master/results/mask.jpg)

The following is the intended result. Notice the billboard on the left with the cast of Spartacus:

![alt text](https://github.com/JeruLuke/Interactive-Homography/blob/master/Spartacus_billboard.jpg)

**Some other results:**

1. Notice the billboard on the right:

![alt text](https://github.com/JeruLuke/Interactive-Homography/blob/master/Spartacus_billboard_2.jpg)

2. Notice the cast on the building to the left:

![alt text](https://github.com/JeruLuke/Interactive-Homography/blob/master/Spartacus_billboard_3.jpg)

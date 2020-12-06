import numpy as np
import cv2 as cv2
from matplotlib import pyplot as plt
from math import atan, pi, sqrt


def main():

    img_path = 'images/test360image.png'
    img = read_image(img_path)
    greyscale_img = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
    #show_image(img)
    cropped_img = crop_image(img)
    show_image(cropped_img)
    write_image(cropped_img, 'testC.png')
    show_image(semicircle_to_pyramid(cropped_img))
    write_image(semicircle_to_pyramid(cropped_img), 'test1C.png')
    # try_out_find_angle()


def read_image(img_path):
    """
    :param img_path: Path of the image you want to read
    :return:
    """
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    return img


def show_image(img, display_time=0):
    """
    :param img: The image you want to display
    :param display_time: The amount of time you want to display the image for in ms.
    Note: A value of 0 will display intently until a KEY is pressed.
    """
    cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('image', img)
    cv2.waitKey(display_time)
    cv2.destroyAllWindows()


def write_image(img, img_saving_path):
    """
    :param img: A list or numpy array of image
    :param img_saving_path: The path you want to save image to
    """
    if isinstance(img, list):
        img = np.asarray(img, dtype=np.uint8)
    elif not isinstance(img, np.ndarray):
        print(type(img))
        raise TypeError("img is neither a list nor a ndarray.")

    cv2.imwrite(img_saving_path, img)


def find_angle_of_pixel(locate_pixel, center_pixel):
    """
    :param locate_pixel: A tuple or list of len 2 with an x and y value representing the position of the pixel in an image
    This is the pixel who's angle relative to the center you'd like to find
    :param center_pixel: A tuple or list of len 2 with an x and y value representing the position of the pixel in an image
    This is the pixel at the center of the image
    :return: The angle of locate_pixel relative to the center_pixel in radians. In the image above the center of the
    circle is north: radian 0, to the right is east: radian pi/2, to the south: radian pi, to the west: radian 3pi/2
    """

    x = float(locate_pixel[0] - center_pixel[0])
    y = float(locate_pixel[1] - center_pixel[1])

    if x == 0 and y < 0:
        return 0 # N
    elif x > 0 and y == 0:
        return pi/2.0 # E
    elif x == 0 and y > 0:
        return pi # S
    elif x < 0 and y == 0:
        return (3*pi)/2.0 # W
    elif x == 0 and y == 0:
        return -1 # center

    angle = atan(x / y)

    if x > 0 and y < 0:
        return -1 * angle # NE Q1
    elif x > 0 and y > 0:
        return (pi/2.0) + angle  # SE Q2
    elif x < 0 and y > 0:
        return pi + (-1 * angle) # SW Q3
    elif x < 0 and y < 0:
        return (2*pi) - angle # NW Q4

    return '???'


def slice_circle(circle_matrix):
    return np.vsplit(circle_matrix, 2)

def flatten_semi_circle(semi_circle_matrix):
    return semi_circle_matrix.max(axis=1)

def try_out_find_angle():
    print('N:', find_angle_of_pixel((2, 0), (2, 2)))
    print('Q1:', find_angle_of_pixel((3, 1), (2, 2)))
    print('E:', find_angle_of_pixel((4, 2), (2, 2)))
    print('Q2:', find_angle_of_pixel((3, 4), (2, 2)))
    print('S:', find_angle_of_pixel((2, 4), (2, 2)))
    print('Q3:', find_angle_of_pixel((1, 5), (2, 2)))
    print('W:', find_angle_of_pixel((0, 2), (2, 2)))
    print('Q4:', find_angle_of_pixel((1, 1), (2, 2)))

def crop_image(img: np.ndarray) -> np.ndarray:
    '''
    Crops out deadspace from input image. Function does not save image and has no other side effects.
        Parameters:
            img (np.ndarray): Image to crop
        Returns:
            cropped_img (np.ndarray): Cropped image
    '''
    return img[10:-20,90:-140].copy()

def semicircle_to_pyramid(img: np.ndarray) -> np.ndarray:
    '''
    Function to turn a semi circle into a pyramid for Tensorflow object detection. This app is for testing the methodology, 
    not for production purposes.
        Parameters:
            img (np.ndarray): Input image.
        Returns:
            pyramid_img (np.ndarray): Pyramid representation of the lower half of the img.

    '''
    def shift_amount(x:int)->int:
        '''
        Calculates amount of pixels to shift based on the x coordinate on the diameter of the semicircle.
            Parameters:
                x(int): x coordinate on the diameter.
            Returns:
                shift(int): Amount of pixels needed to shift array.
        '''
        delta_x = int(abs(285-x))
        return 285 - int(sqrt(285**2 - delta_x**2))
    
    bottom_semicircle: np.ndarray= img[285:-1,0:-1].T.copy()

    if len(bottom_semicircle) == 3:
        for c in range(len(bottom_semicircle)):
            for i in range(len(bottom_semicircle[0])):
                shift = shift_amount(i)
                bottom_semicircle[c][i] = np.roll(bottom_semicircle[c][i], shift, axis=0)
    else:
        for i,row in enumerate(bottom_semicircle):
            shift = shift_amount(i)
            bottom_semicircle[i] = np.roll(bottom_semicircle[i],shift,axis=0)
    return bottom_semicircle.T

if __name__ == '__main__':
    a = np.array([[1, 1, 1],
                  [2, 2, 2],
                  [3, 3, 3],
                  [4, 4, 4],
                  [5, 5, 5],
                  [6, 6, 6]])
    # roll_test = np.roll(np.arange(9,dtype='int8').reshape(3,3),1,axis=0)
    # print(roll_test)
    main()

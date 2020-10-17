import numpy as np
import cv2 as cv2
from matplotlib import pyplot as plt


def main():
    img = read_image('news.jpg')
    show_image(img)


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
    else:
        raise TypeError("img is neither a list nor a ndarray.")

    cv2.imwrite(img_saving_path, img)


if __name__ == '__main__':
    main()

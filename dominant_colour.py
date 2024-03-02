import cv2
import numpy as np
from sklearn.cluster import KMeans
import webcolors

def find_dominant_colours(image_path, k=5):
    image = cv2.imread(image_path)
    
    pixels = image.reshape(-1, 3)
    pixels = pixels.astype(float)
    
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(pixels)
    
    centers = kmeans.cluster_centers_
    
    nparray = centers.astype(int)

    output_list = []

    for rgb_value in nparray:
        output_list.append(tuple(rgb_value.tolist()))

    return rgb_to_colour_name(output_list)

def rgb_to_colour_name(rgb_list):
    output_list = []

    for rgb_tuple in rgb_list:
        try:
            closest_colour = webcolors.rgb_to_name(rgb_tuple)
        except ValueError:
            closest_colour = find_closest_colour_name(rgb_tuple)
    
        output_list.append(closest_colour) 
    
    return output_list


def find_closest_colour_name(rgb_tuple):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - rgb_tuple[0]) ** 2
        gd = (g_c - rgb_tuple[1]) ** 2
        bd = (b_c - rgb_tuple[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


if __name__ == "__main__":
    image_path = input("Enter the path to the image: ")
    k = int(input("Enter the number of dominant colours to find: "))
    
    dominant_colours = find_dominant_colours(image_path, k)
    
    print(dominant_colours)
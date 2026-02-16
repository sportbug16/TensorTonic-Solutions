def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    intensity = [0 for i in range(256)]
    for row in image:
        for pixel in row:
            intensity[pixel] += 1
    return intensity
    # Write code here
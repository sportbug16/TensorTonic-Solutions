def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here
    ans = []
    for row in image:
        ans_row = []
        for pixel in row:
            ans_pixel = 0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2]
            ans_row.append(ans_pixel)
        ans.append(ans_row)
    return ans
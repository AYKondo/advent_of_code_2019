def decode_image(wide, tall, image):
    '''Create a transparency array, then for each pixel in image compare if the pixel in that position
    in final image is transparency, if its not then put the pixel in final image.'''
    # Multiply tall x wide to get array size
    image_size = wide * tall
    # Create an "tranparency" array with image size
    final_layer = [2] * image_size
    pre_layer = 0 # Controler to use like an index
    for char in image:
        char = int(char)
        if pre_layer == image_size: # If controller equals image_size, reset index to 0
            pre_layer = 0
        
        # If final layer index is tranparency and the pixel is not transparency, put the pixel in final layer
        if final_layer[pre_layer] == 2 and char < 2:
            final_layer[pre_layer] = char

        pre_layer += 1

    return final_layer

if __name__ == "__main__":
    image_wide = 25
    image_tall = 6
    
    with open('./input.txt') as f:
        image = f.readline()
        layer = decode_image(image_wide, image_tall, image)

    print(layer)

def decode_image(wide, tall, image):
    image_size = wide * tall
    layer = {}
    number_count = {
        0: 0,
        1: 0,
        2: 0
    }
    layer_count = 0
    for char in image:
        char = int(char)
        if layer_count < image_size:
            layer_count += 1
            if char in number_count:
                number_count[char] += 1
        else:
            if not layer:
                layer = number_count
            elif number_count[0] < layer[0]:
                layer = number_count
            layer_count = 0
            number_count = {0: 0, 1: 0, 2: 0}

    return layer

if __name__ == "__main__":
    image_wide = 25
    image_tall = 6
    
    with open('./input.txt') as f:
        image = f.readline()
        layer = decode_image(image_wide, image_tall, image)

    print(layer[1] * layer[2])


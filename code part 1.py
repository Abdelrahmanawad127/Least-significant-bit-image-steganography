image = input("input your image path or type yes to use any image: ").strip('"')
message = input("enter a message or enter a txt file: ").strip('"')
if image == "":
    print("you cant leave it empty")
    exit()
if message == "":
    print("you must enter a message to encode")
    exit()
if image.lower() == "yes":
    default_image = "C:/Users/it/Downloads/OIP.bmp"
    output_path = "C:/Users/it/Downloads/OIP_hidden.bmp"
else:
    default_image = image
    output_path = image.replace(".bmp", "_hidden.bmp")
if not default_image.lower().endswith(".bmp"):
    print("Only .bmp images are allowed")
    exit()
if message.lower().endswith(".txt"):
    try:
        with open(message, 'r', encoding='latin-1') as f:
            message = f.read()
    except FileNotFoundError:
        print("please input an existing file")
        exit()
    except:
        print("can't open file for unknown reason")
        exit()
full_message = message + "this_is_the_end"
message_in_binary = ""
for character in full_message:
    message_in_binary += format(ord(character), "08b")
try:
    with open(default_image, "rb") as f:
        data = f.read()
except FileNotFoundError:
    print("please input an existing file")
    exit()
except PermissionError:
    print("this file cannot be opened")
    exit()
except:
    print("An unknown error has occurred when opening your image")
    exit()
if len(data) == 0:
    print("file is empty")
    exit()
pixel_offset = data[10] + (data[11] << 8) + (data[12] << 16) + (data[13] << 24)
pixels = []
for i in range(pixel_offset, len(data) - 2, 3):
    blue = data[i]
    green = data[i + 1]
    red = data[i + 2]
    pixels.append((red, green, blue))
flattening = []
for (red, green, blue) in pixels:
    flattening += [red, green, blue]
needed_bits = len(message_in_binary)
available_bits = len(flattening)
if needed_bits > available_bits:
    print(f"Error: Message is too large for this image")
    print(f"Message requires {needed_bits} bits, but image only has {available_bits} bits available")
    print(f"Maximum message length: {available_bits // 8} characters")
    exit()
for i in range(len(message_in_binary)):
    message_bit = int(message_in_binary[i])
    component_lsb = flattening[i] & 1
    if message_bit != component_lsb:
        flattening[i] = flattening[i] ^ 1
new_pixels = []
for i in range(0, len(flattening), 3):
    red = flattening[i]
    green = flattening[i + 1]
    blue = flattening[i + 2]
    new_pixels.append((red, green, blue))
    



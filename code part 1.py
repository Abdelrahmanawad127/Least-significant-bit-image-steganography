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
from PIL import Image
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Function to convert a message into a binary string
def text_to_bin(message):
    return ''.join([format(ord(i), '08b') for i in message])

# Function to convert binary to text
def bin_to_text(binary):
    binary_chunks = [binary[i:i+8] for i in range(0, len(binary), 8)]
    message = ''.join([chr(int(chunk, 2)) for chunk in binary_chunks])
    return message

# Function to encode the message into the image
def encode_image(image_path, message, output_path):
    img = Image.open(image_path)
    binary_message = text_to_bin(message) + '1111111111111110'  # End delimiter

    pixels = list(img.getdata())
    binary_pixels = [format(pixel, '08b') for pixel in pixels]

    encoded_pixels = []
    binary_message_idx = 0
    for pixel in binary_pixels:
        if binary_message_idx < len(binary_message):
            encoded_pixel = pixel[:-1] + binary_message[binary_message_idx]
            binary_message_idx += 1
        else:
            encoded_pixel = pixel
        encoded_pixels.append(int(encoded_pixel, 2))

    img.putdata(encoded_pixels)
    img.save(output_path)
    print(f"{Fore.GREEN}Message successfully encoded into {output_path}!")

# Function to decode the message from the image
def decode_image(image_path):
    img = Image.open(image_path)
    binary_pixels = [format(pixel, '08b') for pixel in list(img.getdata())]
    binary_message = ''

    for pixel in binary_pixels:
        binary_message += pixel[-1]
        if binary_message[-16:] == '1111111111111110':  # Check for end delimiter
            break

    return bin_to_text(binary_message[:-16])  # Remove delimiter

def main():
    print(f"{Fore.CYAN}{Style.BRIGHT}🖼️🔒 Welcome to PicCipher 🔒🖼️")
    print(f"{Fore.YELLOW}{Style.BRIGHT}Your ultimate tool for hiding secret messages in images!\n")

    choice = input(f"{Fore.MAGENTA}Do you want to (e)ncode or (d)ecode? {Fore.RESET}")

    if choice.lower() == 'e':
        print(f"\n{Fore.BLUE}--- Encoding Mode ---")
        image_path = input(f"{Fore.CYAN}Enter the path to the image: {Fore.RESET}")
        message = input(f"{Fore.CYAN}Enter the message to hide: {Fore.RESET}")
        output_path = input(f"{Fore.CYAN}Enter the output image path: {Fore.RESET}")
        encode_image(image_path, message, output_path)

    elif choice.lower() == 'd':
        print(f"\n{Fore.BLUE}--- Decoding Mode ---")
        image_path = input(f"{Fore.CYAN}Enter the path to the encoded image: {Fore.RESET}")
        hidden_message = decode_image(image_path)
        print(f"{Fore.GREEN}{Style.BRIGHT}Hidden message: {hidden_message}")

    else:
        print(f"{Fore.RED}Invalid choice. Please select (e) to encode or (d) to decode.")

if __name__ == "__main__":
    main()
import cv2
import pytesseract

from PIL import Image, ImageDraw, ImageFont


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def split_into_characters(ocr_result):
    """
    Split OCR results into individual characters, with each character having
    the confidence level of the original text element it belongs to.

    Parameters:
    - ocr_result (dict): The OCR result from pytesseract.image_to_data.

    Returns:
    - List[dict]: A list of dictionaries, each representing a character.
    """
    characters = []
    for i, text in enumerate(ocr_result['text']):
        if text.strip():  # Ensure there is text
            num_chars = len(text)
            width_per_char = ocr_result['width'][i] // max(num_chars, 1)
            
            for j, char in enumerate(text):
                char_data = {
                    "letter": char,
                    "x": ocr_result['left'][i] + j * width_per_char,
                    "y": ocr_result['top'][i],
                    "width": width_per_char,
                    "height": ocr_result['height'][i],
                    "conf": ocr_result['conf'][i]  # Confidence of the whole text element
                }
                characters.append(char_data)

    return characters


def extract_text_and_boxes(image_path):
    """
    Extract text and their bounding boxes from an image using OCR.

    :param image_path: The path to the image file.
    :return: A list of dictionaries, each containing a single letter and its bounding box details.
    """
    # Read the image
    img = cv2.imread(image_path)
    
    # Convert the image to grayscale (optional but often helps in OCR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Use pytesseract to get OCR data including bounding boxes
    ocr_result = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)

    # Extract letters and their bounding boxes
    characters_data = split_into_characters(ocr_result)

    return characters_data


def create_collage(letter_images):
    """
    Create a collage of images grouped by letters.

    :param letter_images: A dictionary with letters as keys and lists of PIL image objects as values.
    """
    collage_width, collage_height = 1000, 1000  # Define the dimensions of the collage
    collage = Image.new(
        "RGB", (collage_width, collage_height), "white"
    )  # Create a new white image for the collage

    x, y = 0, 0  # Starting coordinates
    x_offset = 50  # Horizontal space between images

    # Iterate over each letter and its corresponding images
    for _, images in letter_images.items():
        for img in images:
            collage.paste(img, (x, y))  # Paste each image into the collage
            x += img.width + x_offset  # Move to the next position
            # If the next image exceeds the collage width, move to the next row
            if x > collage_width - img.width:
                x = 0
                y += img.height + x_offset

    collage.save("collage.png")  # Save the collage as a PNG file


def create_mock_image(letter, author):
    """
    Generate a mock image representation for demonstration purposes.

    :param letter: The letter to be represented.
    :param author: The author associated with the letter.
    :return: A dictionary representing a mock image.
    """
    return {
        "letter": letter,
        "author": author,
        "image": f"Image of {letter} from {author}",
    }


def generate_letter_images(ocr_data, author):
    """
    Generate mock images for each letter found in OCR data.

    :param ocr_data: OCR data containing letters and their details.
    :param author: The author associated with the OCR data.
    :return: A dictionary grouping letters to their generated mock images.
    """
    letter_images = {}
    for item in ocr_data:
        letter = item["letter"]
        letter_images.setdefault(letter, []).append(create_mock_image(letter, author))
    return letter_images


def create_mock_collage(author1_images, author2_images):
    """
    Combine images from two authors into a single collage structure.

    :param author1_images: Mock images generated for Author 1.
    :param author2_images: Mock images generated for Author 2.
    :return: A dictionary representing the combined collage.
    """
    collage = {}
    for letter in "abcdefghijklmnopqrstuvwxyz":
        collage[letter] = author1_images.get(letter, []) + author2_images.get(
            letter, []
        )
    return collage


def create_juxtaposed_collage(ocr_data1, ocr_data2, author1_path, author2_path):
    """
    Create a collage juxtaposing the handwriting of two authors with original handwriting from images,
    including equal margins and a middle column with a computer-generated version of each letter.
    
    :param ocr_data1: OCR data for author 1.
    :param ocr_data2: OCR data for author 2.
    :param author1_path: File path for author 1's image.
    :param author2_path: File path for author 2's image.
    """
    # Load the original images
    img1 = cv2.imread(author1_path)
    img2 = cv2.imread(author2_path)

    # Convert to PIL.Image format for easier manipulation
    img1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    img2 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))

    # Dimensions for the collage
    middle_column_width = 100
    margin = 50

    # Calculate the max height from both sets of OCR data
    max_height = max([item['height'] for item in ocr_data1 + ocr_data2]) * 26

    collage_width = img1.width + middle_column_width + margin * 2 + 4000
    collage_height = max_height - 1800
    collage = Image.new("RGB", (collage_width, collage_height), "white")

    # Prepare font for the middle column letters
    font = ImageFont.truetype("arial.ttf", 24 * 8)
    draw = ImageDraw.Draw(collage)

    # Function to extract and crop letter images from OCR data
    def crop_letter_images(ocr_data, img):
        letters = {}
        for item in ocr_data:
            letter = item['letter'].lower()
            if letter.isalpha():  # Filter only alphabet letters
                x, y, width, height = item['x'], item['y'], item['width'], item['height']
                cropped = img.crop((x, y, x + width + 10, y + height + 10))
                letters.setdefault(letter, []).append(cropped)
        return letters

    letters1 = crop_letter_images(ocr_data1, img1)
    letters2 = crop_letter_images(ocr_data2, img2)

    y_offset = 0
    fixed_height = 300  # Fixed height for all letter images
    padding = 30  # Padding between images
    for letter in "abcdefghijklmnopqrstuvwxyz":
        # Assuming each letter's block height is max_height // 26
        block_height = max_height // 26
        
        # Center text in the middle of each block's height
        letter_img_x = collage_width / 2  # Adjust X as needed
        letter_img_y = y_offset  # Adjust Y for approximate vertical centering
        
        x_offset_author2 = collage_width - margin

        draw.text((letter_img_x, letter_img_y), letter.upper(), fill="black", font=font)

        # Retrieve all images for this letter from both authors
        author1_imgs = letters1.get(letter, [Image.new("RGB", (10, fixed_height), "grey")])  # Assuming minimal width if no image
        author2_imgs = letters2.get(letter, [Image.new("RGB", (10, fixed_height), "grey")])

        # Starting x position for Author 1's letters
        x_offset_author1 = margin

        # Paste all of Author 1's images for this letter side by side
        for img in author1_imgs:
            # Resize image to have a consistent height, maintaining aspect ratio
            aspect_ratio = img.width / img.height
            resized_width = int(fixed_height * aspect_ratio)
            resized_img = img.resize((resized_width, fixed_height), Image.Resampling.LANCZOS)
            
            collage.paste(resized_img, (x_offset_author1, y_offset))
            x_offset_author1 += resized_width + padding  # Add padding for the next image

        # Paste all of Author 2's images for this letter, right-justified
        for img in reversed(author2_imgs):  # Reverse to start placing from right to left
            # Resize image to have a consistent height, maintaining aspect ratio
            aspect_ratio = img.width / img.height
            resized_width = int(fixed_height * aspect_ratio)
            resized_img = img.resize((resized_width, fixed_height), Image.Resampling.LANCZOS)
            
            x_offset_author2 -= (resized_width + padding)  # Move left for the next image, include padding
            collage.paste(resized_img, (x_offset_author2, y_offset))

        # Increment the y_offset for the next row/letter
        y_offset += fixed_height + padding

    collage.save("juxtaposed_letter_collage_final.png")

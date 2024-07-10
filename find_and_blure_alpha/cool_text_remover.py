import cv2
import numpy as np
import easyocr


class ImageTextRemover:

    def __init__(self):
        # Initialize the EasyOCR reader
        self.reader = easyocr.Reader(['en'], gpu=False)

    def remove_text(self, image_path, output_path):
        # Read the image
        image = cv2.imread(image_path)

        # Use EasyOCR to detect text
        results = self.reader.readtext(image)

        # Mask for inpainting
        mask = np.zeros(image.shape[:2], dtype=np.uint8)

        for (bbox, text, prob) in results:
            # Unpack the bounding box coordinates
            (top_left, top_right, bottom_right, bottom_left) = bbox
            top_left = (int(top_left[0]), int(top_left[1]))
            bottom_right = (int(bottom_right[0]), int(bottom_right[1]))

            # Draw the text bounding box on the mask
            cv2.rectangle(mask, top_left, bottom_right, 255, -1)

        # Inpaint the text regions
        inpainted_image = cv2.inpaint(image, mask, 7, cv2.INPAINT_TELEA)

        # Save the output image
        cv2.imwrite(output_path, inpainted_image)


if __name__ == "__main__":
    # Initialize the text remover
    remover = ImageTextRemover()

    # Remove text from the image and save the result
    remover.remove_text(
        '/home/smiroshnychenko/GeneralPython/find_and_blure_alpha/car-3.jpeg',
        '/home/smiroshnychenko/GeneralPython/find_and_blure_alpha/output-car-3.jpeg')

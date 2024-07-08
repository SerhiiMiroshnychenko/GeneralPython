import cv2


class ImageTextRemover:

    @staticmethod
    def remove_text(image_path, output_path):
        # Read the image
        image = cv2.imread(image_path)

        # Convert image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Thresholding
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        # Morphological operations
        close_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 3))
        close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, close_kernel, iterations=1)

        dilate_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3))
        dilate = cv2.dilate(close, dilate_kernel, iterations=1)

        # Find contours
        cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]

        # Blur text regions based on area
        for c in cnts:
            area = cv2.contourArea(c)
            if 800 < area < 15000:
                x, y, w, h = cv2.boundingRect(c)
                sub_img = image[y:y + h, x:x + w]
                sub_img = cv2.GaussianBlur(sub_img, (25, 25), 30)
                image[y:y + h, x:x + w] = sub_img

        # Save the output image
        cv2.imwrite(output_path, image)


if __name__ == "__main__":
    # Initialize the text remover with the Tesseract command path if needed
    remover = ImageTextRemover()

    # Remove text from the image and save the result
    remover.remove_text(
        '/home/smiroshnychenko/GeneralPython/find_and_blure_alpha/car-1.jpeg',
        '/home/smiroshnychenko/GeneralPython/find_and_blure_alpha/output-car-1.jpeg')

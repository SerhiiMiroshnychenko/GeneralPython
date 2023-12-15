import base64
import csv

input_file_path = "/home/smiroshnychenko/GeneralPython/contacts/images/1-80-companies.csv"
output_file_path = "/home/smiroshnychenko/GeneralPython/contacts/images/FilteredImages.csv"


def is_base64(encoded_data):
    try:
        # спробуємо декодувати дані в форматі base64
        base64.b64decode(encoded_data)
        return True
    except Exception as e:
        return False


def filter_images(input_file_path, output_file_path):
    with open(input_file_path, 'r', newline='') as input_file, open(output_file_path, 'w', newline='') as output_file:
        reader = csv.DictReader(input_file)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            external_id = row['External ID']
            image_data = row['Image']

            if not is_base64(image_data):
                print(f"External ID {external_id}: Invalid base64 data. Row skipped.")
            else:
                writer.writerow(row)


if __name__ == "__main__":
    filter_images(input_file_path, output_file_path)

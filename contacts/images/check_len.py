import csv

input_file_path = "/home/smiroshnychenko/GeneralPython/contacts/images/1-80-companies.csv"


def print_image_lengths(input_file_path):
    with open(input_file_path, 'r', newline='') as input_file:
        reader = csv.DictReader(input_file)

        for row in reader:
            external_id = row['External ID']
            image_data = row['Image']
            image_length = len(image_data)

            print(f"External ID {external_id}: Image length = {image_length}")


if __name__ == "__main__":
    print_image_lengths(input_file_path)

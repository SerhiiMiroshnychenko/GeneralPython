import csv

input_file_path = "/home/smiroshnychenko/GeneralPython/contacts/images/Contact_Images.csv"
output_file_path = "/home/smiroshnychenko/GeneralPython/contacts/images/preparedImages2.csv"


def filter_images_by_length_and_presence(input_file_path, output_file_path, max_length=20000):
    with open(input_file_path, 'r', newline='') as input_file, open(output_file_path, 'w', newline='') as output_file:
        reader = csv.DictReader(input_file)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()

        counter = 0

        try:
            for row in reader:
                counter += 1
                name = row['Name']
                print(f"Row {counter}, {name} ")
                external_id = row['External ID']
                image_data = row['Image']

                if image_data and len(image_data) <= max_length:
                    writer.writerow(row)
                else:
                    print(f"External ID {external_id}: Image data missing or exceeds 20000. Row skipped.")
        except Exception as e:
            print(f'{counter = }',e.__class__, e)


if __name__ == "__main__":
    filter_images_by_length_and_presence(input_file_path, output_file_path)

import csv
import base64

# Шлях до вихідного CSV-файлу та шлях до файлу для зберігання результатів
input_csv_path = 'Images.csv'
output_csv_path = 'Images_base64.csv'


def encode_image_data(input_data):
    # Перетворення вхідних даних у base64
    try:
        encoded_data = base64.b64encode(input_data.encode()).decode('utf-8')
        return encoded_data
    except Exception as e:
        print(f"Error encoding image data: {str(e)}")
        return None


# Відкриваємо вхідний та вихідний CSV-файли
with open(input_csv_path, 'r') as input_csv, open(output_csv_path, 'w', newline='') as output_csv:
    # Створюємо об'єкти для читання та запису CSV
    csv_reader = csv.DictReader(input_csv)
    fieldnames = csv_reader.fieldnames + ['Encoded Image']  # Додаємо новий стовпець для закодованих даних
    csv_writer = csv.DictWriter(output_csv, fieldnames=fieldnames)

    # Записуємо заголовок у вихідний файл
    csv_writer.writeheader()

    # Обробляємо кожен рядок у вхідному CSV-файлі
    for row in csv_reader:
        external_id = row.get('External ID', '')
        image_data = row.get('Image', '')

        # Перетворюємо дані у полі "Image" у base64
        encoded_image_data = encode_image_data(image_data)

        # Записуємо рядок у вихідний файл
        csv_writer.writerow({**row, 'Encoded Image': encoded_image_data})

print(f"Conversion complete. Encoded data saved to {output_csv_path}")


import pandas as pd

# Шляхи до файлів
bom_file_path = "bom.csv"
mrp_bom_file_path = "mrp.bom.csv"

# Зчитуємо DataFrames з файлів
bom_df = pd.read_csv(bom_file_path)
mrp_bom_df = pd.read_csv(mrp_bom_file_path)

# Об'єднуємо DataFrames за полем "id" та "bom_ids/id"
res_bom_df = pd.merge(mrp_bom_df, bom_df, left_on="id", right_on="bom_ids/id", how="inner")

# Вибираємо потрібні поля
selected_columns = ["id_x", "name_x", "type", "product_efficiency", "product_tmpl_id/id", "product_qty",
                    "product_uom/id", "sequence", "message_follower_ids/id", "bom_line_ids/id", "id_y", "name_y",
                    "default_code", "bom_ids/id"]

# Перейменовуємо поля для зручності
res_bom_df.columns = selected_columns

# Записуємо результат у файл "res_bom.csv"
res_bom_df.to_csv("res_bom.csv", index=False)

print("Results have been written to 'res_bom.csv'.")

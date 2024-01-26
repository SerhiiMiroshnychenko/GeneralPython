import pandas as pd

# Зчитуємо дані з файлу sum2.csv
sum2_df = pd.read_csv('sum2.csv')


# Функція для заміни значень поля відповідно до умов
def replace_values(value):
    if value == "__export__.product_pricelist_18":
        return "__export__.product_pricelist_4_5193ba80"
    elif value == "__export__.product_pricelist_21":
        return "__export__.product_pricelist_2_a39c9a52"
    elif value == "account.account_payment_term_net":
        return "account.account_payment_term_30days_early_discount"
    elif value == "__export__.account_payment_term_8":
        return "account.account_payment_term_30_days_end_month_the_10"
    elif value == "__export__.account_payment_term_9":
        return "account.account_payment_term_advance_60days"
    elif value == "__export__.account_payment_term_4":
        return "account.account_payment_term_30days"
    elif value == "__export__.account_payment_term_5":
        return "account.account_payment_term_45days"
    elif value == "__export__.account_payment_term_6":
        return "account.account_payment_term_45days"
    elif value == "__export__.account_payment_term_7":
        return "__export__.account_payment_term_13_d46e44c0"
    else:
        return value


# Замінюємо значення за допомогою функції
sum3_df = sum2_df.applymap(replace_values)

# Зберігаємо результат у файл sum3.csv
sum3_df.to_csv('sum3.csv', index=False)

from datetime import datetime
from statistics import mode


class SimpleReport():
    def generate(dict):
        date_fab = [items["data_de_fabricacao"] for items in dict]
        date_now = str(datetime.now().today())
        date_val = [items["data_de_validade"] for items in dict
                    if items["data_de_validade"] > date_now]
        big_company = [items["nome_da_empresa"] for items in dict]

        return (
            f"Data de fabricação mais antiga: {min(date_fab)}\n"
            f"Data de validade mais próxima: {min(date_val)}\n"
            "Empresa com maior quantidade de produtos estocados: "
            f"{mode(big_company)}"
        )

# referencies:
# https://www.geeksforgeeks.org/python-statistics-mode-function/
# https://pythonacademy.com.br/blog/list-comprehensions-no-python

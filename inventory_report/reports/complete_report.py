from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport():
    def generate(dict):
        simple_report = SimpleReport.generate(dict)
        companies = [items["nome_da_empresa"] for items in dict]

        list_companies = ""

        for company in Counter(companies).items():
            list_companies += f"- {company[0]}: {company[1]}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa: \n" +
            list_companies
        )
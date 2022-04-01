from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:

    def import_data(cls, path, type):
        if(path.endswith('.csv')):
            list_products = cls.csv_read_file(path)
        elif(path.endswith('.json')):
            list_products = cls.json_read_file(path)
        elif(path.endswith('.xml')):
            list_products = cls.xml_read_file(path)
        return cls.generate_report(list_products, type)
# https://www.w3schools.com/python/ref_string_endswith.asp

    @classmethod
    def generate_report(dict, type):
        if type == "simples":
            return SimpleReport.generate(dict)
        else:
            return CompleteReport.generate(dict)

    @classmethod
    def csv_read_file(path):
        list_products = []
        with open(path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                list_products.append(row)
        return list_products

    @classmethod
    def json_read_file(path):
        with open(path, 'r') as jsonfile:
            list_products = json.load(jsonfile)
        return list_products

    @classmethod
    def xml_read_file(path):
        with open(path, 'r') as xmlfile:
            list_products = xmltodict.parse(xmlfile.read())
        return list_products
# https://omz-software.com/pythonista/docs/ios/xmltodict.html
# https://linuxhint.com/python_xml_to_dictionary/

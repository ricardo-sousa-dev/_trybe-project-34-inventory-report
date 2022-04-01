from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
from xml.etree import ElementTree


class Inventory():

    def import_data(path, type):
        if(path.endswith('.csv')):
            list_products = Inventory.csv_read_file(path)
        elif(path.endswith('.json')):
            list_products = Inventory.json_read_file(path)
        elif(path.endswith('.xml')):
            list_products = Inventory.xml_read_file(path)
        return Inventory.generate_report(list_products, type)
# https://www.w3schools.com/python/ref_string_endswith.asp

    def generate_report(dict, type):
        if type == "simples":
            return SimpleReport.generate(dict)
        else:
            return CompleteReport.generate(dict)

    def csv_read_file(path):
        list_products = []
        with open(path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                list_products.append(row)
        return list_products

    def json_read_file(path):
        with open(path, 'r') as jsonfile:
            list_products = json.load(jsonfile)
        return list_products

    def xml_read_file(path):
        tree = ElementTree.parse(path)
        root = tree.getroot()
        list_products = []
        for inventory in root:
            list_child = {}
            for tag_child in inventory:
                list_child[tag_child.tag] = tag_child.text
            list_products.append(list_child)
        return list_products

# https://omz-software.com/pythonista/docs/ios/xmltodict.html
# https://linuxhint.com/python_xml_to_dictionary/

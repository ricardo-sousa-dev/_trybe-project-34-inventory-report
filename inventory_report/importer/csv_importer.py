from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class CsvImporter(Importer):
    @staticmethod
    def import_data(filename):
        if filename.endswith('csv'):
            return Inventory.csv_read_file(filename)
        else:
            raise ValueError('Arquivo inválido')

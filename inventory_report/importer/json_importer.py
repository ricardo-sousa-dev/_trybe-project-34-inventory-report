from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class JsonImporter(Importer):
    @staticmethod
    def import_data(filename):
        if filename.endswith('json'):
            return Inventory.json_read_file(filename)
        else:
            raise ValueError('Arquivo inválido')

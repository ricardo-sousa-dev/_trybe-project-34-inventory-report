from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class XmlImporter(Importer):
    @staticmethod
    def import_data(filename):
        if filename.endswith('xml'):
            return Inventory.xml_read_file(filename)
        else:
            raise ValueError('Arquivo inválido')

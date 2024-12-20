from PyQt5.QtCore import QObject, QSortFilterProxyModel

from model.Material import Material


class MaterialsFilteredModel(QSortFilterProxyModel):
    def __init__(self, parent: QObject | None = ...):
        super().__init__(parent)
        self.material_type = -1
        self.filter = ""

    def set_material_type(self, material_type_id):
        self.material_type = material_type_id
        self.invalidateFilter()

    def set_filter(self, filter_str: str):
        self.filter = filter_str.lower()
        self.invalidateFilter()

    def filterAcceptsRow(self, source_row, source_parent):
        material: Material = self.sourceModel().get_row_fields(source_row)
        if self.material_type > 0 and material.type_id != self.material_type:
            return False
        if self.filter != "":
            search_fields = f"{material.name} {material.type}".lower()
            if search_fields.find(self.filter) < 0:
                return False
        return super().filterAcceptsRow(source_row, source_parent)

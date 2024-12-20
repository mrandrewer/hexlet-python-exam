from PyQt5.QtCore import (
    QModelIndex,
    QObject,
    QSize,
    QEvent,
    QMargins
)
from PyQt5.QtGui import QPainter, QFontMetrics
from PyQt5.QtWidgets import (
    QStyledItemDelegate,
    QStyleOptionViewItem,
)
from controls.MaterialsDialog import MaterialsDialog
from controls.MaterialsWidget import MaterialsWidget
from model.Material import Material
from model.MaterialsModel import MaterialsModel


class MaterialsItemDelegate(QStyledItemDelegate):

    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__(parent)
        self.widget = MaterialsWidget()

    def sizeHint(self, option, index):
        fm = QFontMetrics(option.font)
        return QSize(150, fm.height() * 7 + fm.leading())

    def paint(
            self,
            painter: QPainter | None,
            option: QStyleOptionViewItem,
            index: QModelIndex) -> None:
        material: Material = index.model() \
            .sourceModel() \
            .get_row_fields(index.model().mapToSource(index).row())
        self.widget.setMaterial(material)
        self.widget.resize(option.rect.size())
        self.widget.render(
            painter,
            self.parent().geometry().topLeft() + option.rect.topLeft())

    def editorEvent(self, event, model, option, index):
        if event.type() == QEvent.MouseButtonRelease:
            material: Material = model.sourceModel() \
                .get_row_fields(model.mapToSource(index).row())
            source_model: MaterialsModel = model.sourceModel()
            types = source_model.get_types()
            units = source_model.get_units()
            dlg = MaterialsDialog("Редактирование материала", types, units, True, self.parent())
            dlg.set_material(material)
            exec_result = dlg.exec()
            print(exec_result)
            if exec_result == 1:
                new_material = dlg.get_material()
                new_material.id = material.id
                source_model.update(new_material)
        return False

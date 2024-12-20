from PyQt5.QtWidgets import (
    QWidget,
    QDialog,
    QLabel,
    QComboBox,
    QLineEdit,
    QSpinBox,
    QDoubleSpinBox,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)
from PyQt5.QtCore import pyqtSlot
from model.Material import Material


class MaterialsDialog(QDialog):

    def __init__(
            self,
            header: str,
            material_types: dict,
            unit_types: dict,
            show_delete: bool,
            parent: QWidget | None = ...) -> None:
        super().__init__(parent)
        self.setWindowTitle(header)

        name_lbl = QLabel("&Наименование", parent=self)
        self.__name_edit = QLineEdit(parent=self)
        name_lbl.setBuddy(self.__name_edit)

        type_lbl = QLabel("&Тип материала", parent=self)
        self.__type_edit = QComboBox(parent=self)
        type_lbl.setBuddy(self.__type_edit)
        self.__type_edit.addItem("", -1)
        for id, name in material_types.items():
            self.__type_edit.addItem(name, id)

        inventory_lbl = QLabel("&Остаток", parent=self)
        self.__inventory_edit = QSpinBox(parent=self)
        self.__inventory_edit.setMaximum(100000)
        inventory_lbl.setBuddy(self.__inventory_edit)

        unit_lbl = QLabel("&Единица измерения", parent=self)
        self.__unit_edit = QComboBox(parent=self)
        unit_lbl.setBuddy(self.__unit_edit)
        self.__unit_edit.addItem("", -1)
        for id, name in unit_types.items():
            self.__unit_edit.addItem(name, id)

        package_amount_lbl = QLabel("&Количество в упаковке", parent=self)
        self.__package_amount_edit = QSpinBox(parent=self)
        self.__package_amount_edit.setMaximum(100000)
        package_amount_lbl.setBuddy(self.__package_amount_edit)

        min_amount_lbl = QLabel("&Минимальный остаток", parent=self)
        self.__min_amount_edit = QSpinBox(parent=self)
        self.__min_amount_edit.setMinimum(0)
        self.__min_amount_edit.setMaximum(100000)
        min_amount_lbl.setBuddy(self.__min_amount_edit)

        price_lbl = QLabel("&Стоимость", parent=self)
        self.__price_edit = QDoubleSpinBox(parent=self)
        self.__price_edit.setMinimum(0)
        self.__price_edit.setMaximum(1000000)
        self.__price_edit.setDecimals(2)
        price_lbl.setBuddy(self.__price_edit)

        ok_btn = QPushButton("ОК", parent=self)
        ok_btn.setObjectName("ok_btn")
        cancel_btn = QPushButton("Отмена", parent=self)
        cancel_btn.setObjectName("cancel_btn")

        layout = QVBoxLayout()
        layout.addWidget(name_lbl)
        layout.addWidget(self.__name_edit)
        layout.addWidget(type_lbl)
        layout.addWidget(self.__type_edit)
        layout.addWidget(inventory_lbl)
        layout.addWidget(self.__inventory_edit)
        layout.addWidget(unit_lbl)
        layout.addWidget(self.__unit_edit)        
        layout.addWidget(package_amount_lbl)
        layout.addWidget(self.__package_amount_edit)
        layout.addWidget(min_amount_lbl)
        layout.addWidget(self.__min_amount_edit)
        layout.addWidget(price_lbl)
        layout.addWidget(self.__price_edit)

        btn_layout = QHBoxLayout()
        if show_delete:
            del_btn = QPushButton("Удалить", parent=self)
            del_btn.setObjectName("del_btn")
            del_btn.clicked.connect(self.delete)
            btn_layout.addWidget(del_btn)
        btn_layout.addStretch()
        btn_layout.addWidget(ok_btn)
        btn_layout.addWidget(cancel_btn)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

        ok_btn.clicked.connect(self.finish)
        cancel_btn.clicked.connect(self.reject)

        self.setStyleSheet("""
            QDialog {
                background-color:white;
            }
            QPushButton#ok_btn, QPushButton#del_btn {
                background-color: #D32B39;
            }
        """)

    @pyqtSlot()
    def finish(self):
        model = self.get_material()
        if model.name == "" or model.type_id == -1:
            return
        self.accept()

    @pyqtSlot()
    def delete(self):
        self.done(2)

    def set_material(self, model: Material):
        self.__name_edit.setText(model.name)
        self.__type_edit.setCurrentIndex(model.type_id)
        self.__inventory_edit.setValue(model.inventory)
        self.__min_amount_edit.setValue(model.min_amount)
        self.__price_edit.setValue(model.price)
        self.__package_amount_edit.setValue(model.package_amount)
        self.__unit_edit.setCurrentIndex(model.unit_id)
        return model

    def get_material(self):
        model = Material()
        model.name = self.__name_edit.text()
        model.type_id = self.__type_edit.currentData()
        model.inventory = self.__inventory_edit.value()
        model.min_amount = self.__min_amount_edit.value()
        model.price = self.__price_edit.value()
        model.package_amount = self.__package_amount_edit.value()
        model.unit_id = self.__unit_edit.currentData()
        return model

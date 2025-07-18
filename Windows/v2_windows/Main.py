from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setMaximumSize(QtCore.QSize(800, 500))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(169, 70, 461, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_sell = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sell.sizePolicy().hasHeightForWidth())
        self.btn_sell.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_sell.setFont(font)
        self.btn_sell.setObjectName("btn_sell")
        self.horizontalLayout.addWidget(self.btn_sell)
        self.btn_service = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_service.sizePolicy().hasHeightForWidth())
        self.btn_service.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_service.setFont(font)
        self.btn_service.setObjectName("btn_service")
        self.horizontalLayout.addWidget(self.btn_service)
        self.btn_del = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_del.sizePolicy().hasHeightForWidth())
        self.btn_del.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_del.setFont(font)
        self.btn_del.setObjectName("btn_del")
        self.horizontalLayout.addWidget(self.btn_del)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(130, 130, 531, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.search_box = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_box.sizePolicy().hasHeightForWidth())
        self.search_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.search_box.setFont(font)
        self.search_box.setObjectName("search_box")
        self.verticalLayout.addWidget(self.search_box)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 200, 760, 250))#(left,top,width,hight)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.products_table = QtWidgets.QTableWidget(parent=self.verticalLayoutWidget_2)
        self.products_table.setObjectName("products_table")
        self.products_table.setColumnCount(3)
        self.products_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(2, item)
        self.verticalLayout_2.addWidget(self.products_table)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 20, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:brown;")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")

        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")

        self.menu_2 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_2.setObjectName("menu_2")

        self.menu_3 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_3.setObjectName("menu_3")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.tab_employee = QtGui.QAction(parent=MainWindow)
        self.tab_employee.setObjectName("tab_employee")

        self.tab_customer = QtGui.QAction(parent=MainWindow)
        self.tab_customer.setObjectName("tab_customer")
        self.tab_supplier = QtGui.QAction(parent=MainWindow)
        self.tab_supplier.setObjectName("tab_supplier")
        self.tab_product = QtGui.QAction(parent=MainWindow)
        self.tab_product.setObjectName("tab_product")

        self.tab_sales_history = QtGui.QAction(parent=MainWindow)
        self.tab_sales_history.setObjectName("tab_sales_history")

        self.tab_services_table = QtGui.QAction(parent=MainWindow)
        self.tab_services_table.setObjectName("tab_services_table")

        self.tab_deposit_to_supplier = QtGui.QAction(parent=MainWindow)
        self.tab_deposit_to_supplier.setObjectName("tab_deposit_to_supplier")

        self.tab_employee_withdraw = QtGui.QAction(parent=MainWindow)
        self.tab_employee_withdraw.setObjectName("tab_employee_withdraw")

        self.tab_products_table = QtGui.QAction(parent=MainWindow)
        self.tab_products_table.setObjectName("tab_products_table")

        self.tab_suppliers_table = QtGui.QAction(parent=MainWindow)
        self.tab_suppliers_table.setObjectName("tab_suppliers_table")

        self.tab_customers_table = QtGui.QAction(parent=MainWindow)
        self.tab_customers_table.setObjectName("tab_customers_table")

        self.tab_employees_table = QtGui.QAction(parent=MainWindow)
        self.tab_employees_table.setObjectName("tab_employees_table")

        self.tab_transactions_table = QtGui.QAction(parent=MainWindow)
        self.tab_transactions_table.setObjectName("tab_transactions_table")

        self.tab_total_income = QtGui.QAction(parent=MainWindow)
        self.tab_total_income.setObjectName("tab_total_income")


        self.menu.addAction(self.tab_employee)
        self.menu.addAction(self.tab_customer)
        self.menu.addAction(self.tab_supplier)
        self.menu.addAction(self.tab_product)
   
        self.menu_2.addAction(self.tab_sales_history)
        self.menu_2.addAction(self.tab_products_table)
        self.menu_2.addAction(self.tab_services_table)
        self.menu_2.addAction(self.tab_suppliers_table)
        self.menu_2.addAction(self.tab_customers_table)
        self.menu_2.addAction(self.tab_employees_table)
        self.menu_2.addAction(self.tab_transactions_table)
        self.menu_2.addAction(self.tab_total_income)

        self.menu_3.addAction(self.tab_deposit_to_supplier)
        self.menu_3.addAction(self.tab_employee_withdraw)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_sell.setText(_translate("MainWindow", "بيع"))
        self.btn_service.setText(_translate("MainWindow", "خدمة"))
        self.btn_del.setText(_translate("MainWindow", "حذف"))
        
        self.search_box.setPlaceholderText(_translate("MainWindow", "أكتب إسم السلعة هنا للبحث"))
        item = self.products_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "المرجع"))
        item = self.products_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "إسم السلعة"))
        item = self.products_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "السعر"))
        self.label.setText(_translate("MainWindow", "بنوأمية لإدارة المحلات الصـغيرة - الإصدار الثالث"))
        self.menu.setTitle(_translate("MainWindow", "إضافة"))
        self.menu_2.setTitle(_translate("MainWindow", "سجل"))
        self.menu_3.setTitle(_translate("MainWindow","إدارة"))
        self.tab_employee.setText(_translate("MainWindow", "موظف"))
        self.tab_customer.setText(_translate("MainWindow", "عميل"))
        self.tab_supplier.setText(_translate("MainWindow", "مورد"))
        self.tab_product.setText(_translate("MainWindow", "سلعة"))
   

        self.tab_sales_history.setText(_translate("MainWindow", "المبيعات"))
        self.tab_services_table.setText(_translate("MainWindow","الخدمات"))
        self.tab_products_table.setText(_translate("MainWindow","السلع"))
        self.tab_suppliers_table.setText(_translate("MainWindow","الموردين"))
        self.tab_customers_table.setText(_translate("MainWindow","العملاء"))
        self.tab_employees_table.setText(_translate("MainWindow","الموظفين"))
        self.tab_transactions_table.setText(_translate("MainWindow","المعاملات المالية"))
        self.tab_total_income.setText(_translate("MainWindow","مدخول الشهر"))
        

        self.tab_deposit_to_supplier.setText(_translate("MainWindow","إيداع المال"))
        self.tab_employee_withdraw.setText(_translate("MainWindow","سحب المال"))

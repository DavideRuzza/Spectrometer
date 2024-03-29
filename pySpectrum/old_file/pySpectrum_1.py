# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_win.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1622, 700)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Davide/.designer/Spectruino.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.main_widget = QtWidgets.QWidget(MainWindow)
        self.main_widget.setObjectName("main_widget")
        self.main_layout = QtWidgets.QGridLayout(self.main_widget)
        self.main_layout.setObjectName("main_layout")
        self.plot_frame = QtWidgets.QFrame(self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_frame.sizePolicy().hasHeightForWidth())
        self.plot_frame.setSizePolicy(sizePolicy)
        self.plot_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.plot_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.plot_frame.setObjectName("plot_frame")
        self.plot_frame_layout = QtWidgets.QGridLayout(self.plot_frame)
        self.plot_frame_layout.setObjectName("plot_frame_layout")
        self.plot_wid = PlotWidget(self.plot_frame)
        self.plot_wid.setObjectName("plot_wid")
        self.plot_frame_layout.addWidget(self.plot_wid, 0, 0, 1, 1)
        self.main_layout.addWidget(self.plot_frame, 1, 0, 1, 1)
        self.top_control_layout = QtWidgets.QHBoxLayout()
        self.top_control_layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.top_control_layout.setObjectName("top_control_layout")
        self.com_group = QtWidgets.QGroupBox(self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.com_group.sizePolicy().hasHeightForWidth())
        self.com_group.setSizePolicy(sizePolicy)
        self.com_group.setMinimumSize(QtCore.QSize(300, 0))
        self.com_group.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.com_group.setFont(font)
        self.com_group.setObjectName("com_group")
        self.gridLayout = QtWidgets.QGridLayout(self.com_group)
        self.gridLayout.setObjectName("gridLayout")
        self.port_grid_layout = QtWidgets.QGridLayout()
        self.port_grid_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.port_grid_layout.setObjectName("port_grid_layout")
        self.port_label = QtWidgets.QLabel(self.com_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.port_label.sizePolicy().hasHeightForWidth())
        self.port_label.setSizePolicy(sizePolicy)
        self.port_label.setSizeIncrement(QtCore.QSize(0, 0))
        self.port_label.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.port_label.setFont(font)
        self.port_label.setTextFormat(QtCore.Qt.AutoText)
        self.port_label.setAlignment(QtCore.Qt.AlignCenter)
        self.port_label.setWordWrap(True)
        self.port_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.port_label.setObjectName("port_label")
        self.port_grid_layout.addWidget(self.port_label, 0, 0, 1, 1)
        self.port_combo = QtWidgets.QComboBox(self.com_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.port_combo.sizePolicy().hasHeightForWidth())
        self.port_combo.setSizePolicy(sizePolicy)
        self.port_combo.setMinimumSize(QtCore.QSize(120, 25))
        self.port_combo.setMaximumSize(QtCore.QSize(150, 16777215))
        self.port_combo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.port_combo.setAutoFillBackground(False)
        self.port_combo.setCurrentText("...")
        self.port_combo.setObjectName("port_combo")
        self.port_combo.addItem("")
        self.port_grid_layout.addWidget(self.port_combo, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.port_grid_layout, 0, 0, 1, 1)
        self.refresh_btn = QtWidgets.QPushButton(self.com_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refresh_btn.sizePolicy().hasHeightForWidth())
        self.refresh_btn.setSizePolicy(sizePolicy)
        self.refresh_btn.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.refresh_btn.setFont(font)
        self.refresh_btn.setObjectName("refresh_btn")
        self.gridLayout.addWidget(self.refresh_btn, 0, 1, 1, 1)
        self.open_btn = QtWidgets.QPushButton(self.com_group)
        self.open_btn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_btn.sizePolicy().hasHeightForWidth())
        self.open_btn.setSizePolicy(sizePolicy)
        self.open_btn.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.open_btn.setFont(font)
        self.open_btn.setObjectName("open_btn")
        self.gridLayout.addWidget(self.open_btn, 0, 2, 1, 1)
        self.top_control_layout.addWidget(self.com_group)
        self.measure_group = QtWidgets.QGroupBox(self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measure_group.sizePolicy().hasHeightForWidth())
        self.measure_group.setSizePolicy(sizePolicy)
        self.measure_group.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.measure_group.setFont(font)
        self.measure_group.setObjectName("measure_group")
        self.measure_grup_layout = QtWidgets.QGridLayout(self.measure_group)
        self.measure_grup_layout.setObjectName("measure_grup_layout")
        self.Radio_layout = QtWidgets.QVBoxLayout()
        self.Radio_layout.setObjectName("Radio_layout")
        self.single_radio = QtWidgets.QRadioButton(self.measure_group)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.single_radio.setFont(font)
        self.single_radio.setChecked(True)
        self.single_radio.setObjectName("single_radio")
        self.radio_group = QtWidgets.QButtonGroup(MainWindow)
        self.radio_group.setObjectName("radio_group")
        self.radio_group.addButton(self.single_radio)
        self.Radio_layout.addWidget(self.single_radio)
        self.continued_radio = QtWidgets.QRadioButton(self.measure_group)
        self.continued_radio.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.continued_radio.setFont(font)
        self.continued_radio.setChecked(False)
        self.continued_radio.setObjectName("continued_radio")
        self.radio_group.addButton(self.continued_radio)
        self.Radio_layout.addWidget(self.continued_radio)
        self.measure_grup_layout.addLayout(self.Radio_layout, 0, 2, 1, 1)
        self.stop_btn = QtWidgets.QPushButton(self.measure_group)
        self.stop_btn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop_btn.sizePolicy().hasHeightForWidth())
        self.stop_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.stop_btn.setFont(font)
        self.stop_btn.setFlat(False)
        self.stop_btn.setObjectName("stop_btn")
        self.measure_grup_layout.addWidget(self.stop_btn, 0, 4, 1, 1)
        self.count_frame = QtWidgets.QFrame(self.measure_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.count_frame.sizePolicy().hasHeightForWidth())
        self.count_frame.setSizePolicy(sizePolicy)
        self.count_frame.setMinimumSize(QtCore.QSize(70, 0))
        self.count_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.count_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.count_frame.setObjectName("count_frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.count_frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.count_value = QtWidgets.QLabel(self.count_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.count_value.setFont(font)
        self.count_value.setAlignment(QtCore.Qt.AlignCenter)
        self.count_value.setObjectName("count_value")
        self.gridLayout_4.addWidget(self.count_value, 2, 0, 1, 1)
        self.count_label = QtWidgets.QLabel(self.count_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.count_label.sizePolicy().hasHeightForWidth())
        self.count_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.count_label.setFont(font)
        self.count_label.setAlignment(QtCore.Qt.AlignCenter)
        self.count_label.setObjectName("count_label")
        self.gridLayout_4.addWidget(self.count_label, 1, 0, 1, 1)
        self.measure_grup_layout.addWidget(self.count_frame, 0, 5, 1, 1)
        self.start_btn = QtWidgets.QPushButton(self.measure_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_btn.sizePolicy().hasHeightForWidth())
        self.start_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.start_btn.setFont(font)
        self.start_btn.setFlat(False)
        self.start_btn.setObjectName("start_btn")
        self.measure_grup_layout.addWidget(self.start_btn, 0, 3, 1, 1)
        self.measure_grid_layout = QtWidgets.QGridLayout()
        self.measure_grid_layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.measure_grid_layout.setObjectName("measure_grid_layout")
        self.measure_label = QtWidgets.QLabel(self.measure_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measure_label.sizePolicy().hasHeightForWidth())
        self.measure_label.setSizePolicy(sizePolicy)
        self.measure_label.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.measure_label.setFont(font)
        self.measure_label.setObjectName("measure_label")
        self.measure_grid_layout.addWidget(self.measure_label, 0, 0, 1, 1)
        self.measure_spin_box = QtWidgets.QSpinBox(self.measure_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measure_spin_box.sizePolicy().hasHeightForWidth())
        self.measure_spin_box.setSizePolicy(sizePolicy)
        self.measure_spin_box.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.measure_spin_box.setFont(font)
        self.measure_spin_box.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.measure_spin_box.setSuffix("")
        self.measure_spin_box.setPrefix("")
        self.measure_spin_box.setMaximum(99999)
        self.measure_spin_box.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.measure_spin_box.setProperty("value", 1)
        self.measure_spin_box.setObjectName("measure_spin_box")
        self.measure_grid_layout.addWidget(self.measure_spin_box, 0, 1, 1, 1)
        self.integration_label = QtWidgets.QLabel(self.measure_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.integration_label.sizePolicy().hasHeightForWidth())
        self.integration_label.setSizePolicy(sizePolicy)
        self.integration_label.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.integration_label.setFont(font)
        self.integration_label.setObjectName("integration_label")
        self.measure_grid_layout.addWidget(self.integration_label, 1, 0, 1, 1)
        self.integration_spin_box = QtWidgets.QSpinBox(self.measure_group)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.integration_spin_box.setFont(font)
        self.integration_spin_box.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.integration_spin_box.setReadOnly(False)
        self.integration_spin_box.setMaximum(99999)
        self.integration_spin_box.setProperty("value", 100)
        self.integration_spin_box.setObjectName("integration_spin_box")
        self.measure_grid_layout.addWidget(self.integration_spin_box, 1, 1, 1, 1)
        self.measure_grid_layout.setColumnMinimumWidth(0, 120)
        self.measure_grid_layout.setColumnMinimumWidth(1, 100)
        self.measure_grup_layout.addLayout(self.measure_grid_layout, 0, 0, 1, 1)
        self.v_sep1 = QtWidgets.QFrame(self.measure_group)
        self.v_sep1.setMinimumSize(QtCore.QSize(10, 0))
        self.v_sep1.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_sep1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.v_sep1.setObjectName("v_sep1")
        self.measure_grup_layout.addWidget(self.v_sep1, 0, 1, 1, 1)
        self.top_control_layout.addWidget(self.measure_group)
        self.background_group = QtWidgets.QGroupBox(self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background_group.sizePolicy().hasHeightForWidth())
        self.background_group.setSizePolicy(sizePolicy)
        self.background_group.setMinimumSize(QtCore.QSize(0, 100))
        self.background_group.setObjectName("background_group")
        self.background_group_layout = QtWidgets.QHBoxLayout(self.background_group)
        self.background_group_layout.setObjectName("background_group_layout")
        self.background_btn = QtWidgets.QPushButton(self.background_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background_btn.sizePolicy().hasHeightForWidth())
        self.background_btn.setSizePolicy(sizePolicy)
        self.background_btn.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.background_btn.setFont(font)
        self.background_btn.setObjectName("background_btn")
        self.background_group_layout.addWidget(self.background_btn)
        self.subtract_check_box = QtWidgets.QCheckBox(self.background_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subtract_check_box.sizePolicy().hasHeightForWidth())
        self.subtract_check_box.setSizePolicy(sizePolicy)
        self.subtract_check_box.setMinimumSize(QtCore.QSize(40, 0))
        self.subtract_check_box.setObjectName("subtract_check_box")
        self.background_group_layout.addWidget(self.subtract_check_box)
        self.top_control_layout.addWidget(self.background_group)


        self.graph_setting_group = QtWidgets.QGroupBox(self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_setting_group.sizePolicy().hasHeightForWidth())
        self.graph_setting_group.setSizePolicy(sizePolicy)
        self.graph_setting_group.setMinimumSize(QtCore.QSize(400, 100))
        self.graph_setting_group.setObjectName("graph_setting_group")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.graph_setting_group)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.low_ref_label = QtWidgets.QLabel(self.graph_setting_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.low_ref_label.sizePolicy().hasHeightForWidth())
        self.low_ref_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.low_ref_label.setFont(font)
        self.low_ref_label.setObjectName("low_ref_label")
        self.verticalLayout.addWidget(self.low_ref_label)
        self.high_ref_label = QtWidgets.QLabel(self.graph_setting_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.high_ref_label.sizePolicy().hasHeightForWidth())
        self.high_ref_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.high_ref_label.setFont(font)
        self.high_ref_label.setObjectName("high_ref_label")
        self.verticalLayout.addWidget(self.high_ref_label)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.high_val = QtWidgets.QLineEdit(self.graph_setting_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.high_val.sizePolicy().hasHeightForWidth())
        self.high_val.setSizePolicy(sizePolicy)
        self.high_val.setMinimumSize(QtCore.QSize(50, 0))
        self.high_val.setObjectName("high_val")
        self.verticalLayout_3.addWidget(self.high_val)
        self.low_val = QtWidgets.QLineEdit(self.graph_setting_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.low_val.sizePolicy().hasHeightForWidth())
        self.low_val.setSizePolicy(sizePolicy)
        self.low_val.setMinimumSize(QtCore.QSize(50, 0))
        self.low_val.setObjectName("low_val")
        self.verticalLayout_3.addWidget(self.low_val)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.high_get_btn = QtWidgets.QPushButton(self.graph_setting_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.high_get_btn.sizePolicy().hasHeightForWidth())
        self.high_get_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.high_get_btn.setFont(font)
        self.high_get_btn.setObjectName("high_get_btn")
        self.horizontalLayout.addWidget(self.high_get_btn)
        self.set_btn = QtWidgets.QPushButton(self.graph_setting_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.set_btn.sizePolicy().hasHeightForWidth())
        self.set_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.set_btn.setFont(font)
        self.set_btn.setObjectName("set_btn")
        self.horizontalLayout.addWidget(self.set_btn)
        self.grid_toggle_check_box = QtWidgets.QCheckBox(self.graph_setting_group)
        self.grid_toggle_check_box.setObjectName("grid_toggle_check_box")
        self.horizontalLayout.addWidget(self.grid_toggle_check_box)
        self.top_control_layout.addWidget(self.graph_setting_group)


        self.main_layout.addLayout(self.top_control_layout, 0, 0, 1, 2)
        self.control_frame = QtWidgets.QFrame(self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.control_frame.sizePolicy().hasHeightForWidth())
        self.control_frame.setSizePolicy(sizePolicy)
        self.control_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.control_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.control_frame.setObjectName("control_frame")
        self.control_frame_layout = QtWidgets.QVBoxLayout(self.control_frame)
        self.control_frame_layout.setObjectName("control_frame_layout")
        self.rename_layout = QtWidgets.QHBoxLayout()
        self.rename_layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.rename_layout.setObjectName("rename_layout")
        self.rename_label = QtWidgets.QLabel(self.control_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rename_label.sizePolicy().hasHeightForWidth())
        self.rename_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.rename_label.setFont(font)
        self.rename_label.setObjectName("rename_label")
        self.rename_layout.addWidget(self.rename_label)
        self.rename_val = QtWidgets.QLineEdit(self.control_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rename_val.sizePolicy().hasHeightForWidth())
        self.rename_val.setSizePolicy(sizePolicy)
        self.rename_val.setMaximumSize(QtCore.QSize(90, 16777215))
        self.rename_val.setObjectName("rename_val")
        self.rename_layout.addWidget(self.rename_val)
        self.rename_btn = QtWidgets.QPushButton(self.control_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rename_btn.sizePolicy().hasHeightForWidth())
        self.rename_btn.setSizePolicy(sizePolicy)
        self.rename_btn.setObjectName("rename_btn")
        self.rename_layout.addWidget(self.rename_btn)
        self.empy_btn_1 = QtWidgets.QPushButton(self.control_frame)
        self.empy_btn_1.setEnabled(False)
        self.empy_btn_1.setText("")
        self.empy_btn_1.setFlat(True)
        self.empy_btn_1.setObjectName("empy_btn_1")
        self.rename_layout.addWidget(self.empy_btn_1)
        self.control_frame_layout.addLayout(self.rename_layout)
        self.h_sep1 = QtWidgets.QFrame(self.control_frame)
        self.h_sep1.setFrameShape(QtWidgets.QFrame.HLine)
        self.h_sep1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.h_sep1.setObjectName("h_sep1")
        self.control_frame_layout.addWidget(self.h_sep1)
        self.ctrl_btns_layout = QtWidgets.QHBoxLayout()
        self.ctrl_btns_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.ctrl_btns_layout.setObjectName("ctrl_btns_layout")
        self.remove_btn = QtWidgets.QPushButton(self.control_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_btn.sizePolicy().hasHeightForWidth())
        self.remove_btn.setSizePolicy(sizePolicy)
        self.remove_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.remove_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.remove_btn.setToolTipDuration(-1)
        self.remove_btn.setText("")
        self.remove_btn.setIcon(icon)
        self.remove_btn.setIconSize(QtCore.QSize(20, 20))
        self.remove_btn.setObjectName("remove_btn")
        self.ctrl_btns_layout.addWidget(self.remove_btn)
        self.probe_btn = QtWidgets.QPushButton(self.control_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probe_btn.sizePolicy().hasHeightForWidth())
        self.probe_btn.setSizePolicy(sizePolicy)
        self.probe_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.probe_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.probe_btn.setText("")
        self.probe_btn.setIcon(icon)
        self.probe_btn.setIconSize(QtCore.QSize(20, 20))
        self.probe_btn.setObjectName("probe_btn")
        self.ctrl_btns_layout.addWidget(self.probe_btn)
        self.empty_btn = QtWidgets.QPushButton(self.control_frame)
        self.empty_btn.setEnabled(False)
        self.empty_btn.setAutoFillBackground(False)
        self.empty_btn.setText("")
        self.empty_btn.setFlat(True)
        self.empty_btn.setObjectName("empty_btn")
        self.ctrl_btns_layout.addWidget(self.empty_btn)
        self.control_frame_layout.addLayout(self.ctrl_btns_layout)
        self.graph_view = QtWidgets.QTreeWidget(self.control_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_view.sizePolicy().hasHeightForWidth())
        self.graph_view.setSizePolicy(sizePolicy)
        self.graph_view.setMinimumSize(QtCore.QSize(220, 0))
        self.graph_view.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.graph_view.setFrameShape(QtWidgets.QFrame.Panel)
        self.graph_view.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.graph_view.setLineWidth(1)
        self.graph_view.setObjectName("graph_view")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.graph_view.headerItem().setFont(0, font)
        self.graph_view.headerItem().setBackground(0, QtGui.QColor(255, 255, 169))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.graph_view.headerItem().setForeground(0, brush)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.graph_view.headerItem().setFont(1, font)
        self.graph_view.headerItem().setBackground(1, QtGui.QColor(255, 255, 169))
        item_0 = QtWidgets.QTreeWidgetItem(self.graph_view)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item_0.setFont(0, font)
        brush = QtGui.QBrush(QtGui.QColor(220, 241, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item_0.setBackground(0, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_0.setForeground(0, brush)
        font = QtGui.QFont()
        font.setPointSize(9)
        item_0.setFont(1, font)
        brush = QtGui.QBrush(QtGui.QColor(220, 241, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item_0.setBackground(1, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_0.setForeground(1, brush)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setItalic(True)
        item_1.setFont(0, font)
        item_1.setFlags(QtCore.Qt.NoItemFlags)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setItalic(True)
        item_1.setFont(0, font)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setItalic(True)
        item_1.setFont(0, font)
        self.graph_view.header().setVisible(True)
        self.graph_view.header().setDefaultSectionSize(130)
        self.control_frame_layout.addWidget(self.graph_view)
        self.h_sep2 = QtWidgets.QFrame(self.control_frame)
        self.h_sep2.setFrameShape(QtWidgets.QFrame.HLine)
        self.h_sep2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.h_sep2.setObjectName("h_sep2")
        self.control_frame_layout.addWidget(self.h_sep2)
        self.gamma__layout = QtWidgets.QHBoxLayout()
        self.gamma__layout.setObjectName("gamma__layout")
        self.gamma_label = QtWidgets.QLabel(self.control_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gamma_label.sizePolicy().hasHeightForWidth())
        self.gamma_label.setSizePolicy(sizePolicy)
        self.gamma_label.setMinimumSize(QtCore.QSize(30, 30))
        self.gamma_label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.gamma_label.setAlignment(QtCore.Qt.AlignCenter)
        self.gamma_label.setObjectName("gamma_label")
        self.gamma__layout.addWidget(self.gamma_label)
        self.horizontalSlider = QtWidgets.QSlider(self.control_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(120, 30))
        self.horizontalSlider.setMaximumSize(QtCore.QSize(16777215, 30))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider.setTickInterval(8)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gamma__layout.addWidget(self.horizontalSlider)
        self.control_frame_layout.addLayout(self.gamma__layout)
        self.main_layout.addWidget(self.control_frame, 1, 1, 2, 1)
        MainWindow.setCentralWidget(self.main_widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1622, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action_Save = QtWidgets.QAction(MainWindow)
        self.action_Save.setObjectName("action_Save")
        self.actionExport_data = QtWidgets.QAction(MainWindow)
        self.actionExport_data.setObjectName("actionExport_data")
        self.menuFile.addAction(self.action_Save)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "pySpectrum"))
        self.com_group.setTitle(_translate("MainWindow", "Comunication"))
        self.port_label.setText(_translate("MainWindow", "Port:"))
        self.port_combo.setItemText(0, _translate("MainWindow", "..."))
        self.refresh_btn.setText(_translate("MainWindow", "Refresh"))
        self.open_btn.setText(_translate("MainWindow", "Open"))
        self.measure_group.setTitle(_translate("MainWindow", "Measure"))
        self.single_radio.setText(_translate("MainWindow", "Single"))
        self.continued_radio.setText(_translate("MainWindow", "Continued"))
        self.stop_btn.setText(_translate("MainWindow", "Stop\n"
" Measure"))
        self.count_value.setText(_translate("MainWindow", "0"))
        self.count_label.setText(_translate("MainWindow", "Count:"))
        self.start_btn.setText(_translate("MainWindow", "Start\n"
" Measure"))
        self.measure_label.setText(_translate("MainWindow", "N° measure"))
        self.integration_label.setText(_translate("MainWindow", "Integration (ms)"))
        self.background_group.setTitle(_translate("MainWindow", "Background"))
        self.background_btn.setText(_translate("MainWindow", "Set measure as \n"
" BackGround"))
        self.subtract_check_box.setText(_translate("MainWindow", "Subtract"))
        self.graph_setting_group.setTitle(_translate("MainWindow", "Graph Setting"))
        self.low_ref_label.setText(_translate("MainWindow", "Low ref"))
        self.high_ref_label.setText(_translate("MainWindow", "High ref"))
        self.high_get_btn.setText(_translate("MainWindow", "Get"))
        self.set_btn.setText(_translate("MainWindow", "Set"))
        self.grid_toggle_check_box.setText(_translate("MainWindow", "Grid on/off"))
        self.rename_label.setText(_translate("MainWindow", "Rename:"))
        self.rename_btn.setText(_translate("MainWindow", "Rename"))
        self.remove_btn.setToolTip(_translate("MainWindow", "Remove Selected Measure"))
        self.probe_btn.setToolTip(_translate("MainWindow", "Probe The Graph"))
        self.graph_view.headerItem().setText(0, _translate("MainWindow", "Name"))
        self.graph_view.headerItem().setText(1, _translate("MainWindow", "Value"))
        __sortingEnabled = self.graph_view.isSortingEnabled()
        self.graph_view.setSortingEnabled(False)
        self.graph_view.topLevelItem(0).setText(0, _translate("MainWindow", "Grafico 1"))
        self.graph_view.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Integration"))
        self.graph_view.topLevelItem(0).child(0).setText(1, _translate("MainWindow", "2000"))
        self.graph_view.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "Count"))
        self.graph_view.topLevelItem(0).child(1).setText(1, _translate("MainWindow", "500"))
        self.graph_view.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "Gamma"))
        self.graph_view.topLevelItem(0).child(2).setText(1, _translate("MainWindow", "0.2"))
        self.graph_view.setSortingEnabled(__sortingEnabled)
        self.gamma_label.setText(_translate("MainWindow", "Gamma"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.action_Save.setText(_translate("MainWindow", "Save Graph"))
        self.action_Save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExport_data.setText(_translate("MainWindow", "Export data"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'survey.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1229, 1347)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 1586))
        self.centralwidget.setObjectName("centralwidget")
        self.description = QtWidgets.QLabel(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(0, 0, 1241, 151))
        self.description.setObjectName("description")
        self.teacher_name = QtWidgets.QLabel(self.centralwidget)
        self.teacher_name.setGeometry(QtCore.QRect(700, 130, 441, 151))
        self.teacher_name.setObjectName("teacher_name")
        self.male_btn_12 = QtWidgets.QRadioButton(self.centralwidget)
        self.male_btn_12.setGeometry(QtCore.QRect(-50, 2520, 151, 41))
        self.male_btn_12.setObjectName("male_btn_12")
        self.female_btn_31 = QtWidgets.QRadioButton(self.centralwidget)
        self.female_btn_31.setGeometry(QtCore.QRect(170, 2520, 151, 41))
        self.female_btn_31.setObjectName("female_btn_31")
        self.verticalLayoutWidget_13 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_13.setGeometry(QtCore.QRect(80, 290, 1031, 951))
        self.verticalLayoutWidget_13.setObjectName("verticalLayoutWidget_13")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_13)
        self.verticalLayout_13.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.male_btn = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.male_btn.setObjectName("male_btn")
        self.horizontalLayout.addWidget(self.male_btn)
        self.female_btn_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.female_btn_2.setObjectName("female_btn_2")
        self.horizontalLayout.addWidget(self.female_btn_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_13.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnyas_18_24 = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnyas_18_24.setObjectName("btnyas_18_24")
        self.horizontalLayout_2.addWidget(self.btnyas_18_24)
        self.btnyas25_30 = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnyas25_30.setObjectName("btnyas25_30")
        self.horizontalLayout_2.addWidget(self.btnyas25_30)
        self.btnyas31_40 = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnyas31_40.setObjectName("btnyas31_40")
        self.horizontalLayout_2.addWidget(self.btnyas31_40)
        self.btnyas40_50 = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnyas40_50.setObjectName("btnyas40_50")
        self.horizontalLayout_2.addWidget(self.btnyas40_50)
        self.btnyas_50_plus = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnyas_50_plus.setObjectName("btnyas_50_plus")
        self.horizontalLayout_2.addWidget(self.btnyas_50_plus)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_13.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_boy_160_alt = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btn_boy_160_alt.setObjectName("btn_boy_160_alt")
        self.horizontalLayout_3.addWidget(self.btn_boy_160_alt)
        self.btnboy_160_169 = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnboy_160_169.setObjectName("btnboy_160_169")
        self.horizontalLayout_3.addWidget(self.btnboy_160_169)
        self.btnboy_170_179 = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnboy_170_179.setObjectName("btnboy_170_179")
        self.horizontalLayout_3.addWidget(self.btnboy_170_179)
        self.btnboy_180_189 = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnboy_180_189.setObjectName("btnboy_180_189")
        self.horizontalLayout_3.addWidget(self.btnboy_180_189)
        self.btnboy_190_plus = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnboy_190_plus.setObjectName("btnboy_190_plus")
        self.horizontalLayout_3.addWidget(self.btnboy_190_plus)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_13.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnkilo_61_70 = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnkilo_61_70.setObjectName("btnkilo_61_70")
        self.horizontalLayout_4.addWidget(self.btnkilo_61_70)
        self.btnkilo_50_60 = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnkilo_50_60.setObjectName("btnkilo_50_60")
        self.horizontalLayout_4.addWidget(self.btnkilo_50_60)
        self.btnkilo_71_80 = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnkilo_71_80.setObjectName("btnkilo_71_80")
        self.horizontalLayout_4.addWidget(self.btnkilo_71_80)
        self.btnkilo_81_90 = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnkilo_81_90.setObjectName("btnkilo_81_90")
        self.horizontalLayout_4.addWidget(self.btnkilo_81_90)
        self.btnkilo_91_100 = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnkilo_91_100.setObjectName("btnkilo_91_100")
        self.horizontalLayout_4.addWidget(self.btnkilo_91_100)
        self.btnkilo_100plus = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnkilo_100plus.setObjectName("btnkilo_100plus")
        self.horizontalLayout_4.addWidget(self.btnkilo_100plus)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btnegitimdurumu_ilkokul = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnegitimdurumu_ilkokul.setObjectName("btnegitimdurumu_ilkokul")
        self.horizontalLayout_5.addWidget(self.btnegitimdurumu_ilkokul)
        self.btnegitimdurumu_ortaokul = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnegitimdurumu_ortaokul.setObjectName("btnegitimdurumu_ortaokul")
        self.horizontalLayout_5.addWidget(self.btnegitimdurumu_ortaokul)
        self.btnegitimdurumu_lise = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnegitimdurumu_lise.setObjectName("btnegitimdurumu_lise")
        self.horizontalLayout_5.addWidget(self.btnegitimdurumu_lise)
        self.btnegitimdurumu_on_lisans = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnegitimdurumu_on_lisans.setObjectName("btnegitimdurumu_on_lisans")
        self.horizontalLayout_5.addWidget(self.btnegitimdurumu_on_lisans)
        self.btnegitimdurumu_lisans = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnegitimdurumu_lisans.setObjectName("btnegitimdurumu_lisans")
        self.horizontalLayout_5.addWidget(self.btnegitimdurumu_lisans)
        self.btnegitimdurumu_lisansustu = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnegitimdurumu_lisansustu.setObjectName("btnegitimdurumu_lisansustu")
        self.horizontalLayout_5.addWidget(self.btnegitimdurumu_lisansustu)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_13.addLayout(self.verticalLayout_4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.isyerikidem_usta = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.isyerikidem_usta.setObjectName("isyerikidem_usta")
        self.horizontalLayout_6.addWidget(self.isyerikidem_usta)
        self.isyerikidem_usta_basi = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.isyerikidem_usta_basi.setObjectName("isyerikidem_usta_basi")
        self.horizontalLayout_6.addWidget(self.isyerikidem_usta_basi)
        self.isyerikidem_operator = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.isyerikidem_operator.setObjectName("isyerikidem_operator")
        self.horizontalLayout_6.addWidget(self.isyerikidem_operator)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.verticalLayout_13.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btnelaletikullanmadeneyimok = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnelaletikullanmadeneyimok.setObjectName("btnelaletikullanmadeneyimok")
        self.horizontalLayout_7.addWidget(self.btnelaletikullanmadeneyimok)
        self.btnelaletikullanmadeneyimnok = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnelaletikullanmadeneyimnok.setObjectName("btnelaletikullanmadeneyimnok")
        self.horizontalLayout_7.addWidget(self.btnelaletikullanmadeneyimnok)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.verticalLayout_13.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_8.addWidget(self.label_10)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.profelaletiok = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.profelaletiok.setObjectName("profelaletiok")
        self.horizontalLayout_8.addWidget(self.profelaletiok)
        self.profelaletinok = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.profelaletinok.setObjectName("profelaletinok")
        self.horizontalLayout_8.addWidget(self.profelaletinok)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.verticalLayout_13.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_9.addWidget(self.label_11)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.prof_kullanim_zamani_1_5 = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.prof_kullanim_zamani_1_5.setObjectName("prof_kullanim_zamani_1_5")
        self.horizontalLayout_9.addWidget(self.prof_kullanim_zamani_1_5)
        self.prof_kullanim_zamani_6_10 = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.prof_kullanim_zamani_6_10.setObjectName("prof_kullanim_zamani_6_10")
        self.horizontalLayout_9.addWidget(self.prof_kullanim_zamani_6_10)
        self.prof_kullanim_zamani_11_15 = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.prof_kullanim_zamani_11_15.setObjectName("prof_kullanim_zamani_11_15")
        self.horizontalLayout_9.addWidget(self.prof_kullanim_zamani_11_15)
        self.prof_kullanim_zamani_16_20 = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.prof_kullanim_zamani_16_20.setObjectName("prof_kullanim_zamani_16_20")
        self.horizontalLayout_9.addWidget(self.prof_kullanim_zamani_16_20)
        self.prof_kullanim_zamani_20plus = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.prof_kullanim_zamani_20plus.setObjectName("prof_kullanim_zamani_20plus")
        self.horizontalLayout_9.addWidget(self.prof_kullanim_zamani_20plus)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.verticalLayout_13.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_10.addWidget(self.label_12)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.btnengelok = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnengelok.setObjectName("btnengelok")
        self.horizontalLayout_10.addWidget(self.btnengelok)
        self.btnengelnok = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnengelnok.setObjectName("btnengelnok")
        self.horizontalLayout_10.addWidget(self.btnengelnok)
        self.verticalLayout_10.addLayout(self.horizontalLayout_10)
        self.verticalLayout_13.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_11.addWidget(self.label_13)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.btnmemnum1 = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnmemnum1.setObjectName("btnmemnum1")
        self.horizontalLayout_11.addWidget(self.btnmemnum1)
        self.btnmemnum2 = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnmemnum2.setObjectName("btnmemnum2")
        self.horizontalLayout_11.addWidget(self.btnmemnum2)
        self.btnmemnum3 = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnmemnum3.setObjectName("btnmemnum3")
        self.horizontalLayout_11.addWidget(self.btnmemnum3)
        self.btnmemnum4 = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnmemnum4.setObjectName("btnmemnum4")
        self.horizontalLayout_11.addWidget(self.btnmemnum4)
        self.btnmemnum5 = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnmemnum5.setObjectName("btnmemnum5")
        self.horizontalLayout_11.addWidget(self.btnmemnum5)
        self.verticalLayout_11.addLayout(self.horizontalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_12.addWidget(self.label_14)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.btnonayok = QtWidgets.QRadioButton(self.verticalLayoutWidget_13)
        self.btnonayok.setObjectName("btnonayok")
        self.horizontalLayout_12.addWidget(self.btnonayok)
        self.verticalLayout_12.addLayout(self.horizontalLayout_12)
        self.verticalLayout_11.addLayout(self.verticalLayout_12)
        self.verticalLayout_13.addLayout(self.verticalLayout_11)
        self.save_button = QtWidgets.QPushButton(self.verticalLayoutWidget_13)
        self.save_button.setStyleSheet("background-color: rgb(119, 118, 123);")
        self.save_button.setObjectName("save_button")
        self.verticalLayout_13.addWidget(self.save_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1229, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.description.setText(_translate("MainWindow", "    Sayın Katılımcı, \n"
"    Bu anket formu “Üretim Hattında Kullanılan Elektrikli El Aletlerini Kullanan Kişilerin Davranış Analizinin Tahmin Edilmesine Yönelik Bir Yöntem Geliştirilmesi” başlıklı \n"
"    doktora tez çalışmasında kullanılması amaçlanmaktadır. Araştırmanın bilimsel özelliği açısından, soruları içtenlikle yanıtlamanız son derece önemlidir. \n"
"    Ankete katılanların verdikleri bilgiler kesinlikle gizli tutulacak ve herhangi bir ticari amaçla kullanılmayacaktır. \n"
"     Katılımınız için şimdiden teşekkür ederim.\n"
""))
        self.teacher_name.setText(_translate("MainWindow", "İstanbul Okan Üniversitesi Lisansüstü Eğitim Enstitüsü (2023)\n"
"\n"
"Doktora Öğrencisi: Kader NİKBAY OYLUM\n"
"\n"
"Danışman Öğretim Üyesi: Prof. Dr. Turgay Tugay BİLGİN"))
        self.male_btn_12.setText(_translate("MainWindow", "Evet"))
        self.female_btn_31.setText(_translate("MainWindow", "Hayır"))
        self.label_3.setText(_translate("MainWindow", "1. Cinsiyetiniz:"))
        self.male_btn.setText(_translate("MainWindow", "Erkek"))
        self.female_btn_2.setText(_translate("MainWindow", "Kadın"))
        self.label_4.setText(_translate("MainWindow", "2. Yaşınız :"))
        self.btnyas_18_24.setText(_translate("MainWindow", "18-24"))
        self.btnyas25_30.setText(_translate("MainWindow", "25-30"))
        self.btnyas31_40.setText(_translate("MainWindow", "31-40"))
        self.btnyas40_50.setText(_translate("MainWindow", "40- 50  "))
        self.btnyas_50_plus.setText(_translate("MainWindow", "50 -"))
        self.label_5.setText(_translate("MainWindow", "3. Boy :"))
        self.btn_boy_160_alt.setText(_translate("MainWindow", "160 altı  "))
        self.btnboy_160_169.setText(_translate("MainWindow", "160 – 169  "))
        self.btnboy_170_179.setText(_translate("MainWindow", "170 – 179  "))
        self.btnboy_180_189.setText(_translate("MainWindow", "180 – 189         "))
        self.btnboy_190_plus.setText(_translate("MainWindow", "190 üstü"))
        self.label_6.setText(_translate("MainWindow", "4. Kilo:"))
        self.btnkilo_61_70.setText(_translate("MainWindow", "61 – 70"))
        self.btnkilo_50_60.setText(_translate("MainWindow", "50 – 60"))
        self.btnkilo_71_80.setText(_translate("MainWindow", "71 – 80 "))
        self.btnkilo_81_90.setText(_translate("MainWindow", "81 – 90 "))
        self.btnkilo_91_100.setText(_translate("MainWindow", "91-100"))
        self.btnkilo_100plus.setText(_translate("MainWindow", "100 üstü"))
        self.label_7.setText(_translate("MainWindow", "5.  Eğitim Durumunuz:  "))
        self.btnegitimdurumu_ilkokul.setText(_translate("MainWindow", "İlkokul "))
        self.btnegitimdurumu_ortaokul.setText(_translate("MainWindow", "Ortaokul"))
        self.btnegitimdurumu_lise.setText(_translate("MainWindow", " Lise    "))
        self.btnegitimdurumu_on_lisans.setText(_translate("MainWindow", "Ön Lisans"))
        self.btnegitimdurumu_lisans.setText(_translate("MainWindow", "Lisans    "))
        self.btnegitimdurumu_lisansustu.setText(_translate("MainWindow", "Lisansüstü"))
        self.label_8.setText(_translate("MainWindow", "6.  İş yerindeki kıdeminiz:  "))
        self.isyerikidem_usta.setText(_translate("MainWindow", "Usta"))
        self.isyerikidem_usta_basi.setText(_translate("MainWindow", "Usta Başı "))
        self.isyerikidem_operator.setText(_translate("MainWindow", "Operatör"))
        self.label_9.setText(_translate("MainWindow", "7.  Üretim ortamındaki el aletlerini kullanma deneyiminiz var mı? "))
        self.btnelaletikullanmadeneyimok.setText(_translate("MainWindow", "Evet, var"))
        self.btnelaletikullanmadeneyimnok.setText(_translate("MainWindow", "Hayır, yok    "))
        self.label_10.setText(_translate("MainWindow", "8.  7. Soruya ‘Evet’ yanıtını veren kullanıcılar için cevaplanacak sorudur.\n"
"Yapmış olduğunuz iş profesyonel olarak el aletlerinin kullanımını gerektirmiyor mu? "))
        self.profelaletiok.setText(_translate("MainWindow", "Evet"))
        self.profelaletinok.setText(_translate("MainWindow", "Hayır"))
        self.label_11.setText(_translate("MainWindow", "9.  8. Soruya ‘Evet’ yanıtını veren kullanıcılar için cevaplanacak sorudur.\n"
"Profesyonel olarak bu işi ne kadar süredir yapıyorsunuz?"))
        self.prof_kullanim_zamani_1_5.setText(_translate("MainWindow", "1-5 yıl"))
        self.prof_kullanim_zamani_6_10.setText(_translate("MainWindow", " 6 - 10 yıl"))
        self.prof_kullanim_zamani_11_15.setText(_translate("MainWindow", "11 - 15 yıl "))
        self.prof_kullanim_zamani_16_20.setText(_translate("MainWindow", "16-20 yıl"))
        self.prof_kullanim_zamani_20plus.setText(_translate("MainWindow", "20 yıl üzeri"))
        self.label_12.setText(_translate("MainWindow", "10. Üretimde kullanılan elektrikli el aletlerini kullanmaya yönelik fiziksel bir engeliniz bulunuyor mu? "))
        self.btnengelok.setText(_translate("MainWindow", "Evet"))
        self.btnengelnok.setText(_translate("MainWindow", "Hayır"))
        self.label_13.setText(_translate("MainWindow", "11. Yaptığınız işten memnun musunuz?"))
        self.btnmemnum1.setText(_translate("MainWindow", "Hiç Memnun Değilim"))
        self.btnmemnum2.setText(_translate("MainWindow", "Memnun Değilim"))
        self.btnmemnum3.setText(_translate("MainWindow", "Kararsızım"))
        self.btnmemnum4.setText(_translate("MainWindow", "Çok Memnunum"))
        self.btnmemnum5.setText(_translate("MainWindow", "Memnunum"))
        self.label_14.setText(_translate("MainWindow", "Bu çalışma ile el aletini kullanma davranışınıza yönelik veri toplanacaktır ve bu verilerin doktora tezi kapsamında işlenmesine onay veriyorum. "))
        self.btnonayok.setText(_translate("MainWindow", "Evet"))
        self.save_button.setText(_translate("MainWindow", "Kaydet"))
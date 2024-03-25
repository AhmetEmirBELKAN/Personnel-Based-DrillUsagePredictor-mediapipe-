import csv
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QButtonGroup,QPushButton
from PyQt5.QtCore import pyqtSignal
from design.survey2 import Ui_Dialog 
from PyQt5 import QtCore, QtGui, QtWidgets      
from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QPushButton

class SurveyForm(QDialog,Ui_Dialog):
    survey_saved = pyqtSignal()
    def __init__(self):
        super(SurveyForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.save_button.clicked.connect(self.save_data)
        self.cinsiyet_group = QButtonGroup()
        self.cinsiyet_group.addButton(self.ui.male_btn)
        self.cinsiyet_group.addButton(self.ui.female_btn_2)

        
        self.yas_group = QButtonGroup()
        self.yas_group.addButton(self.ui.btnyas_18_24)
        self.yas_group.addButton(self.ui.btnyas25_30)
        self.yas_group.addButton(self.ui.btnyas31_40)
        self.yas_group.addButton(self.ui.btnyas40_50)
        self.yas_group.addButton(self.ui.btnyas_50_plus)




        self.boy_group = QButtonGroup()
        self.boy_group.addButton(self.ui.btn_boy_160_alt)
        self.boy_group.addButton(self.ui.btnboy_160_169)
        self.boy_group.addButton(self.ui.btnboy_170_179)
        self.boy_group.addButton(self.ui.btnboy_180_189)
        self.boy_group.addButton(self.ui.btnboy_190_plus)



        self.kilo_group = QButtonGroup()
        self.kilo_group.addButton(self.ui.btnkilo_50_60)
        self.kilo_group.addButton(self.ui.btnkilo_61_70)
        self.kilo_group.addButton(self.ui.btnkilo_71_80)
        self.kilo_group.addButton(self.ui.btnkilo_81_90)
        self.kilo_group.addButton(self.ui.btnkilo_91_100)
        self.kilo_group.addButton(self.ui.btnkilo_100plus)
        

        self.egitim_durumu_group = QButtonGroup()
        self.egitim_durumu_group.addButton(self.ui.btnegitimdurumu_ilkokul)
        self.egitim_durumu_group.addButton(self.ui.btnegitimdurumu_ortaokul)
        self.egitim_durumu_group.addButton(self.ui.btnegitimdurumu_lise)
        self.egitim_durumu_group.addButton(self.ui.btnegitimdurumu_on_lisans)
        self.egitim_durumu_group.addButton(self.ui.btnegitimdurumu_lisans)
        self.egitim_durumu_group.addButton(self.ui.btnegitimdurumu_lisansustu)



        self.isyerindeki_kidem_durumu_group = QButtonGroup()
        self.isyerindeki_kidem_durumu_group.addButton(self.ui.isyerikidem_usta)
        self.isyerindeki_kidem_durumu_group.addButton(self.ui.isyerikidem_operator)
        self.isyerindeki_kidem_durumu_group.addButton(self.ui.isyerikidem_usta_basi)


        self.elaleti_kullanma_deneyimi_group = QButtonGroup()
        self.elaleti_kullanma_deneyimi_group.addButton(self.ui.btnelaletikullanmadeneyimok)
        self.elaleti_kullanma_deneyimi_group.addButton(self.ui.btnelaletikullanmadeneyimnok)


        self.elaleti_kullanma_gerekliligi_group = QButtonGroup()
        self.elaleti_kullanma_gerekliligi_group.addButton(self.ui.profelaletiok)
        self.elaleti_kullanma_gerekliligi_group.addButton(self.ui.profelaletinok)




        self.prof_kullanim_zamani_group = QButtonGroup()
        self.prof_kullanim_zamani_group.addButton(self.ui.prof_kullanim_zamani_1_5)
        self.prof_kullanim_zamani_group.addButton(self.ui.prof_kullanim_zamani_6_10)
        self.prof_kullanim_zamani_group.addButton(self.ui.prof_kullanim_zamani_11_15)
        self.prof_kullanim_zamani_group.addButton(self.ui.prof_kullanim_zamani_16_20)
        self.prof_kullanim_zamani_group.addButton(self.ui.prof_kullanim_zamani_20plus)


        self.elaleti_kullanma_fiziksel_engel_group = QButtonGroup()
        self.elaleti_kullanma_fiziksel_engel_group.addButton(self.ui.btnengelok)
        self.elaleti_kullanma_fiziksel_engel_group.addButton(self.ui.btnengelnok)





        self.yaptiginiz_isten_memnun_musunuz_group = QButtonGroup()
        self.yaptiginiz_isten_memnun_musunuz_group.addButton(self.ui.btnmemnum1)
        self.yaptiginiz_isten_memnun_musunuz_group.addButton(self.ui.btnmemnum2)
        self.yaptiginiz_isten_memnun_musunuz_group.addButton(self.ui.btnmemnum3)
        self.yaptiginiz_isten_memnun_musunuz_group.addButton(self.ui.btnmemnum4)
        self.yaptiginiz_isten_memnun_musunuz_group.addButton(self.ui.btnmemnum5)

        self.verilerin_kullanilmasi_group = QButtonGroup()
        self.verilerin_kullanilmasi_group.addButton(self.ui.btnonayok)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  
        
        

    def save_data(self):
     
       
        csv_file = "anket_verileri.csv"

        
        if os.path.exists(csv_file):
            print("dosya zaten varrr")
            mode = 'a'  
        else:
            print("yeni dosyaaaaaaaaaaaaa")
            mode = 'w'  
            
            with open(csv_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Cinsiyet", "Yaş", "Boy", "Kilo", "Eğitim Durumu", "İş Yerindeki Kıdem Durumu", "El_Aleti_Kullanma_Deneyimi", "El_Aleti_Kullanma_Gerekliliği", "Profolarak_çalışma_zamani", "Elaleti_Kullanma_Fiziksel_Engel", "Yaptiginiz_İsten_Memnun_Musunuz", "Verilerin_Kullanilmasi"])  

        
        with open(csv_file, mode="a", newline='') as file:
            writer = csv.writer(file)
           
            selected_cinsiyet_button = self.cinsiyet_group.checkedButton()
            cinsiyet = selected_cinsiyet_button.text() if selected_cinsiyet_button else "Seçilmedi"

            
            selected_yas_button = self.yas_group.checkedButton()
            yas = selected_yas_button.text() if selected_yas_button else "Seçilmedi"

            selected_boy_button = self.boy_group.checkedButton()
            boy = selected_boy_button.text() if selected_boy_button else "Seçilmedi"

            selected_kilo_button = self.kilo_group.checkedButton()
            kilo = selected_kilo_button.text() if selected_kilo_button else "Seçilmedi"

            selected_egitim_durumu_button = self.egitim_durumu_group.checkedButton()
            egitim_durumu = selected_egitim_durumu_button.text() if selected_egitim_durumu_button else "Seçilmedi"

            isyerindeki_kidem_durumu_button = self.isyerindeki_kidem_durumu_group.checkedButton()
            isyerindeki_kidem_durumu = isyerindeki_kidem_durumu_button.text() if isyerindeki_kidem_durumu_button else "Seçilmedi"

            elaleti_kullanma_deneyimi_button = self.elaleti_kullanma_deneyimi_group.checkedButton()
            elaleti_kullanma_deneyimi = elaleti_kullanma_deneyimi_button.text() if elaleti_kullanma_deneyimi_button else "Seçilmedi"
            
            elaleti_kullanma_gerekliligi_button = self.elaleti_kullanma_gerekliligi_group.checkedButton()
            elaleti_kullanma_gerekliligi = elaleti_kullanma_gerekliligi_button.text() if elaleti_kullanma_gerekliligi_button else "Seçilmedi"

            prof_kullanim_zamani_button = self.prof_kullanim_zamani_group.checkedButton()
            prof_kullanim_zamani = prof_kullanim_zamani_button.text() if prof_kullanim_zamani_button else "Seçilmedi"

            elaleti_kullanma_fiziksel_engel_button = self.elaleti_kullanma_fiziksel_engel_group.checkedButton()
            elaleti_kullanma_fiziksel_engel = elaleti_kullanma_fiziksel_engel_button.text() if elaleti_kullanma_fiziksel_engel_button else "Seçilmedi"

            yaptiginiz_isten_memnun_musunuz_button = self.yaptiginiz_isten_memnun_musunuz_group.checkedButton()
            yaptiginiz_isten_memnun_musunuz = yaptiginiz_isten_memnun_musunuz_button.text() if yaptiginiz_isten_memnun_musunuz_button else "Seçilmedi"
            
            verilerin_kullanilmasi_button = self.verilerin_kullanilmasi_group.checkedButton()
            verilerin_kullanilmasi = verilerin_kullanilmasi_button.text() if verilerin_kullanilmasi_button else "Seçilmedi"
            
            
            writer.writerow([cinsiyet, yas, boy, kilo, egitim_durumu, isyerindeki_kidem_durumu, elaleti_kullanma_deneyimi, elaleti_kullanma_gerekliligi, prof_kullanim_zamani, elaleti_kullanma_fiziksel_engel, yaptiginiz_isten_memnun_musunuz, verilerin_kullanilmasi])

        print("Veriler CSV dosyasına kaydedildi:", csv_file)
        print("Emitting survey_saved signal with path:", csv_file)
        self.survey_saved.emit(csv_file)
        self.accept()
        
        
        
   
def main():
    app = QApplication([])
    window = SurveyForm()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()


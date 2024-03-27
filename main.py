import csv
import re
from datetime import datetime
import sys
import traceback
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from design.output import Ui_MainWindow
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFontMetrics
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets      
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtWidgets import QApplication, QMainWindow,QButtonGroup,QPushButton
import mediapipe as mp
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QThread, pyqtSignal
import time
import serial.tools.list_ports
import glob
import os
from pathlib import Path
import PyQt5
import pandas as pd
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = os.fspath(
    Path(PyQt5.__file__).resolve().parent / "Qt5" / "plugins"
)
class DataReaderThread(QThread):
    data_received = pyqtSignal(str)
    Thread_Connection_Status=pyqtSignal(bool)
    def __init__(self, serial_connection):
        super().__init__()
        self.serial_connection = serial_connection
        self.running = True
        
   
    def run(self):
        while self.running:
            try:
                
                data = self.serial_connection.readline().decode('utf-8')
                if data:
                    self.Thread_Connection_Status.emit(True)
                    self.data_received.emit(data)
                else:
                    print("degilseee")
                    time.sleep(0.1)  
            except serial.SerialException as se:
                self.Thread_Connection_Status.emit(False)
                print("SerialException:", se)
                break
            except Exception as e:
                self.Thread_Connection_Status.emit(False)
                print("Error reading data:", e)
                break

    def stop(self):
        self.running = False

class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.show_survey_form()
        self.serialportConnectionStatus=False
        self.data_dict = {
            'VOLT': [],
            'MOTOR_AKIM': [],
            'X_AC': [],
            'Y_AC': [],
            'Z_AC': [],
            'X_GY': [],
            'Y_GY': [],
            'Z_GY': [],
            'NN':[]
        }
        self.datapairs=None
        self.writedatacsv=False
        self.serial_connection = None
        self.Camera_Connection=None
        self.ui.actionConnect.triggered.connect(self.Start_Communication)
        self.ui.btn_serial_connect.clicked.connect(self.ConnectSerial)
        self.ui.btn_serial_connect.clicked.connect(self.FindSerialPort)
        self.ui.resfreshbtn.clicked.connect(self.FindSerialPort)
        self.ui.btn_capture_connect.clicked.connect(self.CaptureValueSet)        

        self.cap = None
        self.groupbutton_list=[]
        self.current_tab_index=None
        self.baud_rates = [9600, 19200, 115200]
        self.ui.comboBaud.addItems([str(baud) for baud in self.baud_rates])
        self.data_bits = [serial.FIVEBITS, serial.SIXBITS, serial.SEVENBITS, serial.EIGHTBITS]
        self.parities = [serial.PARITY_NONE, serial.PARITY_EVEN, serial.PARITY_ODD]
        self.stop_bits = serial.STOPBITS_ONE
        self.ui.comboData.addItems([str(bits) for bits in self.data_bits])
        self.ui.comboParity.addItems([str(parity) for parity in self.parities])
        
        
        self.results = []
        self.timer = QTimer(self)
        self.survey_data=None
     

        
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_draw = mp.solutions.drawing_utils

        
        self.ui.resulttableWidget.setColumnCount(3)
        self.ui.resulttableWidget.setHorizontalHeaderLabels(['Anatomik Yer', 'X', 'Y'])

        
        self.keypoints_map = {
            0: "El Tabanı (Wrist)",
            1: "Baş Parmak: İkinci Ekleme (Thumb: CMC)",
            2: "Baş Parmak: İkinci Ekleme-Burun (Thumb: MCP)",
            3: "Baş Parmak: İkinci Ekleme-Ucu (Thumb: IP)",
            4: "Baş Parmak: İkinci Ekleme-Ucu (Thumb: Tip)",
            5: "İşaret Parmak: İkinci Ekleme (Index finger: MCP)",
            6: "İşaret Parmak: İkinci Ekleme-Burun (Index finger: PIP)",
            7: "İşaret Parmak: İkinci Ekleme-Ucu (Index finger: DIP)",
            8: "İşaret Parmak: İkinci Ekleme-Ucu (Index finger: Tip)",
            9: "Orta Parmak: İkinci Ekleme (Middle finger: MCP)",
            10: "Orta Parmak: İkinci Ekleme-Burun (Middle finger: PIP)",
            11: "Orta Parmak: İkinci Ekleme-Ucu (Middle finger: DIP)",
            12: "Orta Parmak: İkinci Ekleme-Ucu (Middle finger: Tip)",
            13: "Yüzük Parmak: İkinci Ekleme (Ring finger: MCP)",
            14: "Yüzük Parmak: İkinci Ekleme-Burun (Ring finger: PIP)",
            15: "Yüzük Parmak: İkinci Ekleme-Ucu (Ring finger: DIP)",
            16: "Yüzük Parmak: İkinci Ekleme-Ucu (Ring finger: Tip)",
            17: "Serçe Parmak: İkinci Ekleme (Little finger: MCP)",
            18: "Serçe Parmak: İkinci Ekleme-Burun (Little finger: PIP)",
            19: "Serçe Parmak: İkinci Ekleme-Ucu (Little finger: DIP)",
            20: "Serçe Parmak: İkinci Ekleme-Ucu (Little finger: Tip)"
        }
        self.ui.save_button_3.clicked.connect(self.save_data)
        self.ui.btn_reset_survey.clicked.connect(self.Survey_Screen_Reload)
        self.cinsiyet_group = QButtonGroup()
        self.cinsiyet_group.addButton(self.ui.male_btn,1)
        self.cinsiyet_group.addButton(self.ui.female_btn,2)
        self.groupbutton_list.append(self.cinsiyet_group)

        self.yas_group = QButtonGroup()
        self.yas_group.addButton(self.ui.btnyas_18_24,1)
        self.yas_group.addButton(self.ui.btnyas25_30,2)
        self.yas_group.addButton(self.ui.btnyas31_40,3)
        self.yas_group.addButton(self.ui.btnyas40_50,4)
        self.yas_group.addButton(self.ui.btnyas_50_plus,5)
        self.groupbutton_list.append(self.yas_group)   

        self.boy_group = QButtonGroup()
        self.boy_group.addButton(self.ui.btn_boy_160_alt,1)
        self.boy_group.addButton(self.ui.btnboy_160_169,2)
        self.boy_group.addButton(self.ui.btnboy_170_179,3)
        self.boy_group.addButton(self.ui.btnboy_180_189,4)
        self.boy_group.addButton(self.ui.btnboy_190_plus,5)
        self.groupbutton_list.append(self.boy_group)   

        self.kilo_group = QButtonGroup()
        self.kilo_group.addButton(self.ui.btnkilo_50_60,1)
        self.kilo_group.addButton(self.ui.btnkilo_61_70,2)
        self.kilo_group.addButton(self.ui.btnkilo_71_80,3)
        self.kilo_group.addButton(self.ui.btnkilo_81_90,4)
        self.kilo_group.addButton(self.ui.btnkilo_91_100,5)
        self.kilo_group.addButton(self.ui.btnkilo_100plus,6)
        self.groupbutton_list.append(self.kilo_group)   

        self.egitim_durumu_group = QButtonGroup()
        self.egitim_durumu_group.addButton(self.ui.btnegitimdurumu_ilkokul,1)
        self.egitim_durumu_group.addButton(self.ui.btnegitimdurumu_ortaokul,2)
        self.egitim_durumu_group.addButton(self.ui.btnegitimdurumu_lise,3)
        self.egitim_durumu_group.addButton(self.ui.btnegitimdurumu_on_lisans,4)
        self.egitim_durumu_group.addButton(self.ui.btnegitimdurumu_lisans,5)
        self.egitim_durumu_group.addButton(self.ui.btnegitimdurumu_lisansustu,6)
        self.groupbutton_list.append(self.egitim_durumu_group)   

        self.isyerindeki_kidem_durumu_group = QButtonGroup()
        self.isyerindeki_kidem_durumu_group.addButton(self.ui.isyerikidem_usta,1)
        self.isyerindeki_kidem_durumu_group.addButton(self.ui.isyerikidem_operator,2)
        self.isyerindeki_kidem_durumu_group.addButton(self.ui.isyerikidem_usta_basi,3)
        self.groupbutton_list.append(self.isyerindeki_kidem_durumu_group)   

        self.elaleti_kullanma_deneyimi_group = QButtonGroup()
        self.elaleti_kullanma_deneyimi_group.addButton(self.ui.btnelaletikullanmadeneyimok,1)
        self.elaleti_kullanma_deneyimi_group.addButton(self.ui.btnelaletikullanmadeneyimnok,2)
        self.groupbutton_list.append(self.elaleti_kullanma_deneyimi_group)   

        self.elaleti_kullanma_gerekliligi_group = QButtonGroup()
        self.elaleti_kullanma_gerekliligi_group.addButton(self.ui.profelaletiok,1)
        self.elaleti_kullanma_gerekliligi_group.addButton(self.ui.profelaletinok,2)
        self.groupbutton_list.append(self.elaleti_kullanma_gerekliligi_group)   

        self.prof_kullanim_zamani_group = QButtonGroup()
        self.prof_kullanim_zamani_group.addButton(self.ui.prof_kullanim_zamani_1_5,1)
        self.prof_kullanim_zamani_group.addButton(self.ui.prof_kullanim_zamani_6_10,2)
        self.prof_kullanim_zamani_group.addButton(self.ui.prof_kullanim_zamani_11_15,3)
        self.prof_kullanim_zamani_group.addButton(self.ui.prof_kullanim_zamani_16_20,3)
        self.prof_kullanim_zamani_group.addButton(self.ui.prof_kullanim_zamani_20plus,4)
        self.groupbutton_list.append(self.prof_kullanim_zamani_group)   

        self.elaleti_kullanma_fiziksel_engel_group = QButtonGroup()
        self.elaleti_kullanma_fiziksel_engel_group.addButton(self.ui.btnengelok,1)
        self.elaleti_kullanma_fiziksel_engel_group.addButton(self.ui.btnengelnok,2)
        self.groupbutton_list.append(self.elaleti_kullanma_fiziksel_engel_group)   

        self.yaptiginiz_isten_memnun_musunuz_group = QButtonGroup()
        self.yaptiginiz_isten_memnun_musunuz_group.addButton(self.ui.btnmemnum1,1)
        self.yaptiginiz_isten_memnun_musunuz_group.addButton(self.ui.btnmemnum2,2)
        self.yaptiginiz_isten_memnun_musunuz_group.addButton(self.ui.btnmemnum3,3)
        self.yaptiginiz_isten_memnun_musunuz_group.addButton(self.ui.btnmemnum4,4)
        self.yaptiginiz_isten_memnun_musunuz_group.addButton(self.ui.btnmemnum5,5)
        self.groupbutton_list.append(self.yaptiginiz_isten_memnun_musunuz_group)   

        self.verilerin_kullanilmasi_group = QButtonGroup()
        self.verilerin_kullanilmasi_group.addButton(self.ui.btnonayok,1)
        self.groupbutton_list.append(self.verilerin_kullanilmasi_group)   

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  
        
    def CheckButtonGroupId(self,checked_button,group):
        resultid=None
        if checked_button is not None:  # Eğer bir buton seçili ise
            checked_id = group.id(checked_button)
            print(f"Seçili olan butonun ID'si: {checked_id}")
            resultid=checked_id
        else:
            print("Hiçbir buton seçili değil.")
            resultid=0
        return resultid
    
    def Survey_Screen_Reload(self):
        for buttonGroup in self.groupbutton_list:
            buttonGroup.setExclusive(False)  # Bunu grup içindeki herhangi bir butonun seçimini kaldırmak için kullanıyoruz.
            for button in buttonGroup.buttons():
                if button.isChecked():
                    button.setChecked(False)
                    print(f"Unchecked button: {button}")
            buttonGroup.setExclusive(True)  # Grubun tekrar yalnızca bir seçime izin vermesini sağlamak için kullanıyoruz.

    
    def Survey_Nullable_Check(self):
        counter=0
        for buttonGroup in self.groupbutton_list:
            buttonList = buttonGroup.buttons()  
            buttonList_len = len(buttonList)  
            
            for button in buttonList:
                    
                if button.isChecked():
                    counter+=1
                    print(f"len(self.groupbutton_list) : {len(self.groupbutton_list)}")
                    print(f"counter : {counter}")

        if(len(self.groupbutton_list)!=counter):
            QtWidgets.QMessageBox.critical(self.ui.groupBox, "Survey Error", "Anketi tamamlayınız !!!")
            return False
        elif(len(self.groupbutton_list)==counter):
            return True
                    
    def column_name_Add_survey_csv(self,csv_file):

        if os.path.exists(csv_file):
            mode = 'a'  
        else:
            mode = 'w'  
            with open(csv_file, mode='w', newline='') as file:
                writer = csv.writer(file)
      
                writer.writerow(["Cinsiyet", "Yaş", "Boy", "Kilo", "Eğitim Durumu", "İş Yerindeki Kıdem Durumu", "El_Aleti_Kullanma_Deneyimi", "El_Aleti_Kullanma_Gerekliliği", "Profolarak_çalışma_zamani", "Elaleti_Kullanma_Fiziksel_Engel", "Yaptiginiz_İsten_Memnun_Musunuz", "Verilerin_Kullanilmasi"]) 

    def CaptureReadTimer(self,time=1):
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(time)  

    def CaptureValueSet(self):   
        try:
            capture_index=int(self.ui.Capture_Combo.currentText())
            self.cap=cv2.VideoCapture(capture_index)  
            if(self.cap.isOpened()):
                self.CaptureReadTimer()
                self.Camera_Connection=True
            
            else:
                self.Camera_Connection=False
            
                QtWidgets.QMessageBox.critical(self.ui.groupBox, "Capture Connection Error", "can't open camera by index  tekrardan bağlantı deneyin !!!")

        except Exception as ex:
            error_message = f"CaptureValueSet hata oluştu hata: {traceback.format_exc()} "
            self.Camera_Connection=False
            print(error_message)
        finally:    
            self.CaptureConenctionStatusChange()

    def save_data(self):
        survey_Result=self.Survey_Nullable_Check()
        if(survey_Result):
            self.survey_data=None

            csv_file = "anket_verileri.csv"

            self.column_name_Add_survey_csv(csv_file)
            
            with open( csv_file , mode="a", newline='') as file:
                writer = csv.writer(file)
            
                selected_cinsiyet_button = self.cinsiyet_group.checkedButton()
                cinsiyet=self.CheckButtonGroupId(selected_cinsiyet_button,self.cinsiyet_group)

                selected_yas_button = self.yas_group.checkedButton()
                yas=self.CheckButtonGroupId(selected_yas_button,self.yas_group)
    
                selected_boy_button = self.boy_group.checkedButton()
                boy=self.CheckButtonGroupId(selected_boy_button,self.boy_group)

                selected_kilo_button = self.kilo_group.checkedButton()
                kilo=self.CheckButtonGroupId(selected_kilo_button,self.kilo_group)

                selected_egitim_durumu_button = self.egitim_durumu_group.checkedButton()
                egitim_durumu=self.CheckButtonGroupId(selected_egitim_durumu_button,self.egitim_durumu_group)

                isyerindeki_kidem_durumu_button = self.isyerindeki_kidem_durumu_group.checkedButton()
                isyerindeki_kidem_durumu=self.CheckButtonGroupId(isyerindeki_kidem_durumu_button,self.isyerindeki_kidem_durumu_group)

                elaleti_kullanma_deneyimi_button = self.elaleti_kullanma_deneyimi_group.checkedButton()
                elaleti_kullanma_deneyimi=self.CheckButtonGroupId(elaleti_kullanma_deneyimi_button,self.elaleti_kullanma_deneyimi_group)
                

                elaleti_kullanma_gerekliligi_button = self.elaleti_kullanma_gerekliligi_group.checkedButton()
                elaleti_kullanma_gerekliligi=self.CheckButtonGroupId(elaleti_kullanma_gerekliligi_button,self.elaleti_kullanma_gerekliligi_group)


                prof_kullanim_zamani_button = self.prof_kullanim_zamani_group.checkedButton()
                prof_kullanim_zamani=self.CheckButtonGroupId(prof_kullanim_zamani_button,self.prof_kullanim_zamani_group)


                elaleti_kullanma_fiziksel_engel_button = self.elaleti_kullanma_fiziksel_engel_group.checkedButton()
                elaleti_kullanma_fiziksel_engel=self.CheckButtonGroupId(elaleti_kullanma_fiziksel_engel_button,self.elaleti_kullanma_fiziksel_engel_group)

                yaptiginiz_isten_memnun_musunuz_button = self.yaptiginiz_isten_memnun_musunuz_group.checkedButton()
                yaptiginiz_isten_memnun_musunuz=self.CheckButtonGroupId(yaptiginiz_isten_memnun_musunuz_button,self.yaptiginiz_isten_memnun_musunuz_group)


                verilerin_kullanilmasi_button = self.verilerin_kullanilmasi_group.checkedButton()
                verilerin_kullanilmasi=self.CheckButtonGroupId(verilerin_kullanilmasi_button,self.verilerin_kullanilmasi_group)
                
                
                writer.writerow([cinsiyet, yas, boy, kilo, egitim_durumu, isyerindeki_kidem_durumu, elaleti_kullanma_deneyimi, elaleti_kullanma_gerekliligi, prof_kullanim_zamani, elaleti_kullanma_fiziksel_engel, yaptiginiz_isten_memnun_musunuz, verilerin_kullanilmasi])
                print(f"writer : {writer}")


            print(f"csv_file : {csv_file}")
            self.survey_data=pd.read_csv(csv_file)
            print(f"self.survey_data : {self.survey_data}")
            self.Survey_Screen_Reload()
            QtWidgets.QMessageBox.information(self.ui.groupBox, "Survey", "Anket tamamlandı teşekkür ederiz :)")


    def start_reading_thread(self):
        if self.serial_connection and self.serial_connection.is_open:
            self.data_reader_thread = DataReaderThread(self.serial_connection)
            self.data_reader_thread.data_received.connect(self.on_data_received)
            self.data_reader_thread.Thread_Connection_Status.connect(self.SerialPortConenctionStatusChange)
            print("Thread Baslatildi..")
            self.data_reader_thread.start()

    def list_to_dict(self,data_list):
        data_dict = {item[0]: item[1] for item in data_list}
        return data_dict
            
    def WriteCsv(self,dataPairs):
        data_dict=self.list_to_dict(dataPairs)
        self.csv_file=f"{self.ui.namelineedit.text()}.csv"
        self.ui.namelineedit.setReadOnly(True)  
        with open(f"{self.directory}{self.csv_file}", 'a', newline='') as csvfile:
            fieldnames = list(data_dict.keys())
            
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
            if csvfile.tell() == 0:
                writer.writeheader()
           
            if "NN" in data_dict:
                nn_value = data_dict["NN"]
                if nn_value == "NOK":
                    data_dict["NN"] = 0
                elif nn_value == "OK":
                    data_dict["NN"] = 1

            writer.writerow(data_dict)


    def on_data_received(self, data):
        self.datapairs=data
      
        if(data==None or data==""):
            print("Bağlantı sağlandı ama data gelmiyor ")
        # print(f"data_Received  : {data}")
        self.ui.serialportresulttxt.append(data)
    
    def SerialPortConenctionStatusChange(self,data):
        # print(f"SerialPortConenctionStatusChange : {data}")
        self.serialportConnectionStatus=data
        if(data):
            self.ui.serialport_dial.setStyleSheet("background-color: rgb(0,255,0);")
        else:
            QtWidgets.QMessageBox.critical(self.ui.groupBox, "SerialPortConnection Error", "Portları tekrardan listeleyip bağlantı deneyin !!!")
            self.ui.serialport_dial.setStyleSheet("background-color: rgb(0,0,255);")

    def CaptureConenctionStatusChange(self):
        # print(f"SerialPortConenctionStatusChange : {data}")
        if(self.Camera_Connection):
            self.ui.camera_dial.setStyleSheet("background-color: rgb(0,255,0);")
        else:
            self.ui.camera_dial.setStyleSheet("background-color: rgb(0,0,255);")


    def parse_data(self, data):
        try:
       
            data_pairs = re.findall(r'(\w+):([-0-9.]+|\w+)', data)

            for key, value in data_pairs:
                

                if key in self.data_dict:
                    if key=='NN':
                        if value=='NOK':
                            # # # # print("nok geldi")
                            self.data_dict[key].append(float(0))
                        else:
                            # # # # print("ok geldi") 
                            self.data_dict[key].append(float(1))
                    
            return data_pairs
        except Exception as e:
            # # # # print("Parse Error:", str(e))
            return None

    def Start_Communication(self):
        # self.serial_connection=None
        # self.Camera_Connection = None
        # print(f"self.current_tab_index  : {self.current_tab_index }")
        # self.CaptureValueSet()
        if(self.serial_connection==False or self.serial_connection==None):
            self.ConnectSerial()
        else:
            print("seriport bağlı pass  gec")
        if(self.Camera_Connection==False or self.Camera_Connection==None):
            self.CaptureValueSet()
        else:
            print("camera  bağlı pass  gec")

        

    def FindSerialPort(self): 
        print("FindSerialPort başladı")
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            ports = glob.glob('/dev/ttyUSB*')  # Yalnızca /dev/ttyUSB* portlarını alır
            # print(f"linux ports: {ports}")
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
            # print(f"darwin ports: {ports}")
        else:
            raise EnvironmentError('Unsupported platform')

        self.ui.comboPort.clear()
        for port in ports:
            try:
                
                self.ports = []
                self.ports.append(port)
                # print(port)
                self.ui.comboPort.addItems(self.ports)

            except (OSError, serial.SerialException):
                pass
            
    def ConnectSerial(self):
        print(f"self.serialportConnectionStatus : {self.serialportConnectionStatus}")
        if(self.serialportConnectionStatus!=True):
            port = self.ui.comboPort.currentText()
            print(f"serial Port : {port}")
            baud_rate = int(self.ui.comboBaud.currentText())
            print(f"baud_rate : {baud_rate}")
            data_bits = self.data_bits[self.ui.comboData.currentIndex()]
            print(f"data_bits :  {data_bits} ")
            parity = self.parities[self.ui.comboParity.currentIndex()]
            print(f"parity : {parity}")
            stop_bits = self.stop_bits
            print(f"stop_bits : {stop_bits}")
            if(port==None or port==""):
                QtWidgets.QMessageBox.critical(self.ui.groupBox, "SerialPort Error", "Hedef Portu seçiniz !!!")
                return
            if self.serial_connection and self.serial_connection.is_open:
                self.serial_connection.close()

            try:
                self.serial_connection = serial.Serial(
                    port=port,
                    baudrate=baud_rate,
                    bytesize=data_bits,
                    parity=parity,
                    stopbits=stop_bits
                )
                self.ui.statusBar.showMessage("Connected to " + port)
                self.serialportConnectionStatus=True
                self.start_reading_thread()

            except Exception as e:
                self.ui.statusBar.showMessage("Connection failed: " + str(e))   
                self.serialportConnectionStatus=False
                print(str(e))     
        else:
            print("passs gecccc")

    def save_keypoints_to_csv(self, hand_landmarks, keypoints_map, file_path):
        # print(f"self.serialportConnectionStatus : {self.serialportConnectionStatus}")
        headers = []
        if(self.serialportConnectionStatus and self.Camera_Connection and (self.survey_data.empty is not True)):
            print(f"veirleri csv e kayadediliyor")
            data_pairs = {}
            for pair in self.datapairs.split(','):
                key, value = pair.split(':')
                data_pairs[key.strip()] = value.strip()

            data_pairs = {}
            for pair in self.datapairs.split(','):
                key, value = pair.split(':')
                data_pairs[key.strip()] = value.strip()
            if not os.path.exists(file_path):
                with open(file_path, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    for keypoint_name in keypoints_map.values():
                        headers.extend([f"{keypoint_name}_x", f"{keypoint_name}_y"])
                    for key, value in data_pairs.items():
                        headers.extend([key])
                    writer.writerow(headers)

            with open(file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                row_data = []
                for landmark_idx in range(21): 
                    row_data = []
                    for landmark in hand_landmarks.landmark:
                        if landmark:  
                            x = round(landmark.x * self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                            y = round(landmark.y * self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                        else:  
                            x = -1
                            y = -1
                        row_data.extend([x, y])

                
                    for value in data_pairs.values():
                        row_data.append(value)

                    writer.writerow(row_data)
            
                         
                

            # data_dicts = self.survey_data.to_dict(orient='records')
            # with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            #     fieldnames = data_dicts[0].keys() 
            #     writer = csv.DictWriter(file, fieldnames=fieldnames)

            #     writer.writeheader()  

                
            #     for data_dict in data_dicts:
            #         writer.writerow(data_dict)
              
        else:
            pass

            
    def update_table(self, hand_landmarks):  
        self.ui.resulttableWidget.setRowCount(0)
        for idx, landmark in enumerate(hand_landmarks.landmark):
            x = round(landmark.x * self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            y = round(landmark.y * self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            self.add_row_to_table(idx, x, y)
            

    def add_row_to_table(self, idx, x, y):
        row_position = self.ui.resulttableWidget.rowCount()
        self.ui.resulttableWidget.insertRow(row_position)
        item = QTableWidgetItem(self.keypoints_map.get(idx, f'Keypoint {idx}'))
        item.setTextAlignment(Qt.AlignCenter)  
        self.ui.resulttableWidget.setItem(row_position, 0, item)
        self.ui.resulttableWidget.setItem(row_position, 1, QTableWidgetItem(str(int(x))))
        self.ui.resulttableWidget.setItem(row_position, 2, QTableWidgetItem(str(int(y))))
        font_metrics = QFontMetrics(self.ui.resulttableWidget.font())
        width = font_metrics.width(item.text()) + 20  
        self.ui.resulttableWidget.setColumnWidth(0, width)  

    def update_frame(self):
        try:

            ret, frame = self.cap.read()  
            
            if ret:
                self.Camera_Connection=True
                img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img_rgb.flags.writeable = False  
                results = self.hands.process(img_rgb)  
                
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                        self.update_table(hand_landmarks)

                
                    hand_landmarks_to_save = results.multi_hand_landmarks[0]  
                    self.save_keypoints_to_csv(hand_landmarks_to_save, self.keypoints_map, 'hand_keypoints.csv')

                img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = img_rgb.shape
                bytes_per_line = ch * w
                q_img = QImage(img_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
                
                pixmap = QPixmap.fromImage(q_img)
                self.ui.videocapturelabel.setPixmap(pixmap)
            else:
                self.Camera_Connection=False

        except Exception as e:
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            error_message = f"{current_datetime} - update_frame hata oluştu hata: {traceback.format_exc()} "
            print(error_message)
            self.Camera_Connection=False
        finally:
            self.CaptureConenctionStatusChange()

if __name__ == "__main__":
    # main()
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec_())

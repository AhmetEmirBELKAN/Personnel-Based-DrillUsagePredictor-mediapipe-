import csv
import re
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from design.output import Ui_MainWindow
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFontMetrics
import cv2
import mediapipe as mp
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QThread, pyqtSignal
import time
import serial.tools.list_ports
import glob
import os
from pathlib import Path

import PyQt5

os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = os.fspath(
    Path(PyQt5.__file__).resolve().parent / "Qt5" / "plugins"
)
class DataReaderThread(QThread):
    data_received = pyqtSignal(str)

    def __init__(self, serial_connection):
        super().__init__()
        self.serial_connection = serial_connection
        self.running = True
        
        

   
    def run(self):
        while self.running:
            try:
                
                data = self.serial_connection.readline().decode('utf-8')
                if data:
                    self.data_received.emit(data)
                else:
                    time.sleep(0.1)  
            except serial.SerialException as se:
                print("SerialException:", se)
            except Exception as e:
                print("Error reading data:", e)

    def stop(self):
        self.running = False

class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
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
        self.ui.actionConnect.triggered.connect(self.Start_Communication)
        self.ui.resfreshbtn.clicked.connect(self.FindSerialPort)
        self.cap = cv2.VideoCapture(2)  
          
        self.current_tab_index=None
        self.baud_rates = [9600, 19200, 115200]
        self.ui.comboBaud.addItems([str(baud) for baud in self.baud_rates])
        self.data_bits = [serial.FIVEBITS, serial.SIXBITS, serial.SEVENBITS, serial.EIGHTBITS]
        self.parities = [serial.PARITY_NONE, serial.PARITY_EVEN, serial.PARITY_ODD]
        self.stop_bits = [serial.STOPBITS_ONE, serial.STOPBITS_ONE_POINT_FIVE, serial.STOPBITS_TWO]
        self.ui.comboData.addItems([str(bits) for bits in self.data_bits])
        self.ui.comboParity.addItems([str(parity) for parity in self.parities])
        self.ui.comboStop.addItems([str(stop_bits) for stop_bits in self.stop_bits])
        
        self.results = []

        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(5)  

        
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

    def start_reading_thread(self):
        if self.serial_connection and self.serial_connection.is_open:
            self.data_reader_thread = DataReaderThread(self.serial_connection)
            self.data_reader_thread.data_received.connect(self.on_data_received)
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
        
        self.ui.serialportresulttxt.append(data)
    
    def parse_data(self, data):
        try:
       
            data_pairs = re.findall(r'(\w+):([-0-9.]+|\w+)', data)

            for key, value in data_pairs:
                

                if key in self.data_dict:
                    if key=='NN':
                        if value=='NOK':
                            # # # print("nok geldi")
                            self.data_dict[key].append(float(0))
                        else:
                            # # # print("ok geldi") 
                            self.data_dict[key].append(float(1))
                    
            return data_pairs
        except Exception as e:
            # # # print("Parse Error:", str(e))
            return None

    def Start_Communication(self):
        
        self.serial_connection=None
        self.TCP_connection = None
        self.current_tab_index = self.ui.tabWidget_2.currentIndex()
        # # # print(self.current_tab_index )
       
        self.ConnectSerial()

    def FindSerialPort(self):
        print("FindSerialPort başladı")
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            ports = glob.glob('/dev/ttyUSB*')  # Yalnızca /dev/ttyUSB* portlarını alır
            print(f"linux ports: {ports}")
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
            print(f"darwin ports: {ports}")
        else:
            raise EnvironmentError('Unsupported platform')

        self.ui.comboPort.clear()
        for port in ports:
            try:
                
                self.ports = []
                self.ports.append(port)
                print(port)
                self.ui.comboPort.addItems(self.ports)

            except (OSError, serial.SerialException):
                pass
            
    def ConnectSerial(self):
        port = self.ui.comboPort.currentText()
        baud_rate = int(self.ui.comboBaud.currentText())
        data_bits = self.data_bits[self.ui.comboData.currentIndex()]
        parity = self.parities[self.ui.comboParity.currentIndex()]
        stop_bits = self.stop_bits[self.ui.comboStop.currentIndex()]

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

            self.start_reading_thread()

        except Exception as e:
            self.ui.statusBar.showMessage("Connection failed: " + str(e))   
            print(str(e))     

    def save_keypoints_to_csv(self, hand_landmarks, keypoints_map, file_path):
        headers = []

        print(f"self.datapairs : {self.datapairs}")
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
        ret, frame = self.cap.read()  
        
        if ret:
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec_())

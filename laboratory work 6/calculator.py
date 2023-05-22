import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        
        self.vbox = QVBoxLayout(self)        
        self.hbox_input = QHBoxLayout()        
        self.hbox_first = QHBoxLayout()        
        self.hbox_second = QHBoxLayout()
        self.hbox_third = QHBoxLayout() 
        self.hbox_fourth = QHBoxLayout()  
        self.hbox_fifth = QHBoxLayout()    
               
        self.vbox.addLayout(self.hbox_input)        
        self.vbox.addLayout(self.hbox_first)     
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_third) 
        self.vbox.addLayout(self.hbox_fourth) 
        self.vbox.addLayout(self.hbox_fifth)     
        
        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)  
              
        self.b_ac = QPushButton("AC", self)
        self.hbox_first.addWidget(self.b_ac)
        self.b_mop = QPushButton("±", self)        
        self.hbox_first.addWidget(self.b_mop)        
        self.b_precent = QPushButton("%", self)        
        self.hbox_first.addWidget(self.b_precent)        
        self.b_div = QPushButton("÷", self)        
        self.hbox_first.addWidget(self.b_div)
        
        self.b_7 = QPushButton("7", self)
        self.hbox_second.addWidget(self.b_7)
        self.b_8 = QPushButton("8", self)        
        self.hbox_second.addWidget(self.b_8)        
        self.b_9 = QPushButton("9", self)        
        self.hbox_second.addWidget(self.b_9)        
        self.b_mult = QPushButton("×", self)        
        self.hbox_second.addWidget(self.b_mult)
        
        self.b_4 = QPushButton("4", self)
        self.hbox_third.addWidget(self.b_4)   
        self.b_5 = QPushButton("5", self)
        self.hbox_third.addWidget(self.b_5) 
        self.b_6 = QPushButton("6", self)
        self.hbox_third.addWidget(self.b_6) 
        self.b_minus = QPushButton("-", self)
        self.hbox_third.addWidget(self.b_minus) 
        
        self.b_1 = QPushButton("1", self)
        self.hbox_fourth.addWidget(self.b_1)   
        self.b_2 = QPushButton("2", self)
        self.hbox_fourth.addWidget(self.b_2) 
        self.b_3 = QPushButton("3", self)
        self.hbox_fourth.addWidget(self.b_3) 
        self.b_plus = QPushButton("+", self)
        self.hbox_fourth.addWidget(self.b_plus)
        
        self.b_0 = QPushButton("0", self)
        self.hbox_fifth.addWidget(self.b_0)   
        self.b_comma = QPushButton(",", self)
        self.hbox_fifth.addWidget(self.b_comma)
        self.b_del = QPushButton("del", self)
        self.hbox_fifth.addWidget(self.b_del)
        self.b_result = QPushButton("=", self)        
        self.hbox_fifth.addWidget(self.b_result)
        
        self.b_ac.clicked.connect(lambda: self._operation("AC"))
        self.b_mop.clicked.connect(lambda: self._operation("±"))
        self.b_precent.clicked.connect(lambda: self._operation("%"))
        self.b_div.clicked.connect(lambda: self._operation("÷"))
        self.b_mult.clicked.connect(lambda: self._operation("×"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_plus.clicked.connect(lambda: self._operation("+")) 
        self.b_comma.clicked.connect(lambda: self._operation(","))
        self.b_del.clicked.connect(self.del_last_digit)   
        self.b_result.clicked.connect(self._result)     
        
        self.b_0.clicked.connect(lambda: self._button("0"))   
        self.b_1.clicked.connect(lambda: self._button("1"))        
        self.b_2.clicked.connect(lambda: self._button("2"))        
        self.b_3.clicked.connect(lambda: self._button("3"))  
        self.b_4.clicked.connect(lambda: self._button("4"))    
        self.b_5.clicked.connect(lambda: self._button("5"))  
        self.b_6.clicked.connect(lambda: self._button("6"))  
        self.b_7.clicked.connect(lambda: self._button("7"))    
        self.b_8.clicked.connect(lambda: self._button("8"))  
        self.b_9.clicked.connect(lambda: self._button("9"))  
            
    def _button(self, param):        
            line = self.input.text()        
            self.input.setText(line + param)
            
    def _operation(self, op):
        self.num_1 = self.input.text()
        
        try:
            self.num_1 = int(self.num_1)
        except:
            self.num_1 = float(self.num_1)
        
        self.op = op
        self.input.setText("")
                
        if self.op == ",":
            self.input.setText(str(self.num_1 * 1.0))
            
        if self.op == "±":
            self.input.setText(str(self.num_1 * -1))
        
        if self.op == "%":
            self.input.setText(str(self.num_1 / 100))
        
    def _result(self):
        self.num_2 = self.input.text()
        
        try:
            self.num_2 = int(self.num_2)
        except:
            self.num_2 = float(self.num_2)
                     
        if self.op == "AC":
            self.input.setText(str(""))  
                
        if self.op == "÷":
            if self.num_2 == 0:
                    self.input.setText(str("error"))
            elif (self.num_1 % self.num_2) == 0:
                    self.input.setText(str(self.num_1 // self.num_2))
            else:
                self.input.setText(str(self.num_1 / self.num_2))
                
        if self.op == "×":           
            self.input.setText(str(self.num_1 * self.num_2))
        
        if self.op == "-":            
            self.input.setText(str(self.num_1 - self.num_2))   
                
        if self.op == "+":            
            self.input.setText(str(self.num_1 + self.num_2))
            
    def del_last_digit(self):
        text = self.input.text()
        if len(text) > 0:
            text = text[:-1]
            self.input.setText(text)
            
app = QApplication(sys.argv)
win = Calculator()
win.setWindowTitle('Calculator')
win.show()
sys.exit(app.exec_())

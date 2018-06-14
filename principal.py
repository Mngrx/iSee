import os
from time import gmtime, strftime, sleep

LED1 = 17 # Led que indica foto esta sendo tirada
LED2 = 27 # Led que indica que o teste foi iniciado
LED3 = 22 # Led que indica que o teste foi finalizado
LED4 = 4 # Led que indica que está ligado
BNT1 = 5 # Botão para tirar foto
BNT2 = 6 # Botão para aceitar a foto e passar para o processamento
BNT3 = 13 # Botão para cancelar/resetar o processo

class digitalPort:
  
  def __init__(self, port, mode):
    os.system("echo " + str(port) + " > /sys/class/gpio/export")
    os.system("echo " + str(mode) + " > /sys/class/gpio/gpio" + str(port) +"/direction")
    self.port = port
    self.mode = mode
    self.path = "/sys/class/gpio/gpio" + str(port) +"/value"

  def readValue(self):
    if self.mode == "in":
        file = open(self.path)
        return int(file.readline())
    else:
        return "Invalid"

  def setValue(self, value):
    if self.mode == "out":
        os.system("echo " + str(value) + " > " + self.path)            
    else:
      return "Invalid"


gpio_led1 = digitalPort(LED1, "out")
gpio_led2 = digitalPort(LED2, "out")
gpio_led3 = digitalPort(LED3, "out")
gpio_led4 = digitalPort(LED4, "out")
gpio_bnt1 = digitalPort(BNT1, "in")
gpio_bnt2 = digitalPort(BNT2, "in")
gpio_bnt3 = digitalPort(BNT3, "in")

while True:
  
  fase = 1
  foto = 0
  gpio_led1.setValue(0)
  gpio_led2.setValue(0)
  gpio_led3.setValue(0)
  gpio_led4.setValue(1)
  
  while True:
    
    if (gpio_bnt1.readValue() == 1):
      gpio_led1.setValue(1)
      gpio_led2.setValue(0)
      gpio_led3.setValue(0)
      j = strftime("%Y-%m-%d %H:%M:%S", gmtime())
      #chama função para tirar foto
      #envia foto para firebase
      sleep(1)
      gpio_led1.setValue(0)
      gpio_led2.setValue(0)
      gpio_led3.setValue(0)
      foto = 1
    
    if (foto == 1 and gpio_bnt2.readValue() == 1):
      fase = 2
      gpio_led1.setValue(0)
      gpio_led2.setValue(1)
      gpio_led3.setValue(0)
      #Iniciar o processamento da imagem
      sleep(0.5)
      gpio_led1.setValue(0)
      gpio_led2.setValue(0)
      gpio_led3.setValue(1)
      #Envia dados para o firebase
      sleep(2)
      fase = 2
    
    if (gpio_bnt3.readValue() == 1 or fase == 2):
      gpio_led1.setValue(1)
      gpio_led2.setValue(1)
      gpio_led3.setValue(1)
      gpio_led4.setValue(1)
      sleep(0.3)
      gpio_led1.setValue(0)
      gpio_led2.setValue(0)
      gpio_led3.setValue(0)
      gpio_led4.setValue(0)
      sleep(0.3)
      gpio_led1.setValue(1)
      gpio_led2.setValue(1)
      gpio_led3.setValue(1)
      gpio_led4.setValue(1)
      sleep(0.3)
      gpio_led1.setValue(0)
      gpio_led2.setValue(0)
      gpio_led3.setValue(0)
      gpio_led4.setValue(0)
      sleep(0.8)
      break


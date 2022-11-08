import conexion
import pandas as pd
import logging
import tkinter
from tkinter import messagebox
import threading
import time

def timer():
    count = 0
    messagebox.showinfo("Aviso", "Se va a empezar a ejecutar el programa ")
    while True:
        count +=1
        print(count)
        ejecucion()
        time.sleep(3000)
t = threading.Thread(target=timer)
t.start()

def ejecucion():
    try:
        root = tkinter.Tk()
        root.withdraw()
        # Message Box
        # messagebox.showinfo("Aviso", "Por favor no dar click mas de dos veces al programa")
        logging.info('Inicio!')  # will print a message to the console
        data = conexion.conLect()
        print(data)
        logging.info('Datos completos')  # will not print anything
        df = pd.DataFrame(data)
        logging.info('Guardado de archivo!')  # will print a message to the console
        # This code is to hide the main tkinter window

        # Message Box
        #messagebox.showinfo("Extracción", "Se finalizo correctamente")
        df.to_csv('example.csv', sep='|')

        logging.info('Finalizado guardado')  # will not print anything

    except Exception as e:
        print(e)

#pip install cx_Oracle
#pip install pyinstaller
#pyinstaller -F -w 'nombreArchivo.py' -> realiza el .exe para crear el

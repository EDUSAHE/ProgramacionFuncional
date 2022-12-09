import webview
from tkinter import *

# wroot = tkinter.Tk()
# width= wroot.winfo_screenwidth()  
# height= wroot.winfo_screenheight() 
# # wroot.geometry(f"{width}x{height}")
# wroot.geometry("800x600")
# wroot.state('zoomed')
# wroot.title("Navegador Web")
# wroot.iconbitmap("horoscopo.ico") #Cambiar el icono

# # Crear caja de texto.
# entry = ttk.Entry()
# # Posicionarla en la ventana.
# entry.place(x=50, y=50)

webview.create_window("Navegador Wev", url='www.google.com', html='', js_api=None, width=800, height=600, \
                      x=None, y=None, resizable=True, fullscreen=False, \
                      min_size=(200, 100), hidden=False, frameless=False, \
                      minimized=False, on_top=False, confirm_close=False, \
                      background_color='#FFF', text_select=False)
webview.start()
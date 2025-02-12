import customtkinter
import datetime
from PIL import Image

class function:
    def files():
        print("file button pressed")
        pass

    def task():
        print("task button pressed")
        pass

    def Complete():
        print("complete button pressed")
        pass
    
    def Incomplete():
        print("incomplete button pressed")
        pass
    
    def submit():
        print('submit button pressed')
        pass
    

class Options(customtkinter.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)

        self.fileButton=customtkinter.CTkButton(self,text='File',fg_color='#2C2C50',bg_color='#2C2C50',border_width=0,command=function.files)
        self.fileButton.grid(
            row=0,
            column=0,
            sticky='ew',
        )

        self.taskButton=customtkinter.CTkButton(self,text='Tasks',fg_color='#2C2C50',bg_color='#2C2C50',border_width=0,command=function.task)
        self.taskButton.grid(
            row=1,
            column=0,
            sticky='ew',
        )

        self.completeButton=customtkinter.CTkButton(self,text='Complete',fg_color='#2C2C50',bg_color='#2C2C50',border_width=0,command=function.Complete)
        self.completeButton.grid(
            row=2,
            column=0,
            sticky='ew',
        )

        self.incompleteButton=customtkinter.CTkButton(self,text='Incomplete',fg_color='#2C2C50',bg_color='#2C2C50',border_width=0,command=function.Incomplete)
        self.incompleteButton.grid(
            row=3,
            column=0,
            sticky='ew',

        )

class TopTittle(customtkinter.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        
        self.grid_columnconfigure(0,weight=0)
        self.grid_columnconfigure(1,weight=6)

        # self.imagelable=customtkinter.CTkLabel(self,image=master.applogoimage,text='')
        # self.imagelable.grid(
        #     row=0,
        #     column=0,
        #     sticky='news',
        # )

        self.titlelable=customtkinter.CTkLabel(self,text=master.appName,font=master.appNameFont,)
        self.titlelable.grid(
            row=0,
            column=1,
            sticky='news',
            padx=10,
            pady=(0,10),
            columnspan=2,
        )

class MainWindow(customtkinter.CTkScrollableFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)

class ControlWindow(customtkinter.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)

        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=6)
        self.grid_columnconfigure(1,weight=0)

        self.entryBox=customtkinter.CTkEntry(self,placeholder_text='New Tasks here',placeholder_text_color='#aeb6bf',text_color='white')
        self.entryBox.grid(
            row=0,
            column=0,
            sticky='ew',
            pady=20,
            padx=20,
        )

        self.submitButton=customtkinter.CTkButton(self,text='^',command=function.submit,corner_radius=20,fg_color='#2F3152',text_color='white',height=30)
        self.submitButton.grid(
            row=0,
            column=1,
            pady=20,
            padx=20,
        )


class app(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # APP DEFAULTS
        self.applogoimage=customtkinter.CTkImage(light_image=Image.open("d-Photoroom.png"),dark_image=Image.open("d-Photoroom.png"),size=(50,50))
        self.appName='TODO'
        self.appNameFont=customtkinter.CTkFont(family='Monoton',size=36)

        # ROW CONFIGURATIONS
        self.grid_rowconfigure(0,weight=0)
        self.grid_rowconfigure(2,weight=0)
        self.grid_rowconfigure(1,weight=6)

        # COLUMN CONFIGURATIONS
        self.grid_columnconfigure(0,weight=0)
        self.grid_columnconfigure(1,weight=6)

        self.logo=customtkinter.CTkLabel(self,image=self.applogoimage,text='',fg_color="#2C2C50",bg_color='#2C2C50')
        self.logo.grid(
            row=0,
            column=0,
            sticky='news',
        )

        self.options=Options(master=self,fg_color='#2C2C50',)
        self.options.grid(
            row=1,
            column=0,
            sticky='news',
            rowspan=2,
            )

        self.toptittle=TopTittle(master=self,)
        self.toptittle.grid(
            row=0,
            column=1,
            sticky='news',
        )
        
        self.mainwindow=MainWindow(master=self,)
        self.mainwindow.grid(
            row=1,
            column=1,
            sticky='news',
        )

        self.controlwindow=ControlWindow(master=self,)
        self.controlwindow.grid(
            row=2,
            column=1,
            sticky='news',
        )


todo=app()
todo.mainloop()
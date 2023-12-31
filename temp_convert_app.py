from temp import TempConvert
import customtkinter as ctk
import tkinter as tk



class TempConvertApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self._set_appearance_mode('dark')
        self.title('Temperature Converter App')
        self._geo(500, 300)

        self.varCel = tk.IntVar(value=0)
        self.varCel.trace('w', self.update)
        self.varFahr = tk.IntVar(value=32)
        # self.varFahr.trace('w', self.update)
        self.varKel = tk.IntVar(value=273.15)
        # self.varKel.trace('w', self.update)

        m = Main(self, self.varCel, self.varFahr, self.varKel)
        m.pack(fill='both', expand=True)

        self.bind('<Shift-Escape>', quit)
        self.mainloop()
    
    def _geo(self, w, h):
        pWidth = w
        pHeight = h
        sWidth = self.winfo_screenwidth()
        sHeight = self.winfo_screenheight()
        mWidth = sWidth//2 - pWidth//2
        mHeight = sHeight//2 - pHeight//2

        self.minsize(pWidth, pHeight)

        self.geometry(f'{pWidth}x{pHeight}+{mWidth}+{mHeight}')
    
    def update(self, *args):
        cel = self.varCel.get()

        self.varFahr.set(round(TempConvert.CelToFahr(cel),2))
        self.varKel.set(round(TempConvert.CelToKelvin(cel),2))


class Main(tk.Frame):

    FONT_SIZE = 60
    ENTRY_SIZE = 30
    FONT_TYPE = 'Comic Sans MS'
    BG_COLOR = '#00CC77'

    def __init__(self, parent, cel, fahr, kel):
        super().__init__(parent, background=self.BG_COLOR)

        lblFahr = ctk.CTkLabel(self, font=(self.FONT_TYPE,self.FONT_SIZE, 'bold'), textvariable=fahr)
        lblFahr.pack(fill='both', expand=True)

        slideFrame = ctk.CTkFrame(self, fg_color=self.BG_COLOR)
        slideFrame.rowconfigure(0, weight=1, uniform='a')
        slideFrame.columnconfigure((0,1), weight=1)
        sliderCel = ctk.CTkSlider(slideFrame, to=0, from_=100, variable=cel, width=330, progress_color='yellow', button_hover_color='red')
        sliderCel.grid(row=0, column=0, sticky='news')
        entryCel = ctk.CTkEntry(slideFrame, textvariable=cel, font=(self.FONT_TYPE, self.ENTRY_SIZE), width=70, justify='right')
        entryCel.grid(row=0, column=1, sticky='news', padx=40)
        slideFrame.pack()


        lblKelvin = ctk.CTkLabel(self, font=(self.FONT_TYPE,self.FONT_SIZE, 'bold'), textvariable=kel)
        lblKelvin.pack(fill='both', expand=True)

        lblC = ctk.CTkLabel(self, text='C', font=(self.FONT_TYPE, 30))
        lblC.place(relx=.9, rely=.44)

        lblF = ctk.CTkLabel(self, text='F', font=(self.FONT_TYPE, 50, 'bold'))
        lblF.place(relx=.7, rely=.10)

        lblK = ctk.CTkLabel(self, text='K', font=(self.FONT_TYPE, 50, 'bold'))
        lblK.place(relx=.75, rely=.65)

if __name__ == '__main__':
    t = TempConvertApp()
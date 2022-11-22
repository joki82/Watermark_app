from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageGrab


class ImageWaterMark(Tk):
    def __init__(self):
        super().__init__()
        self.title("test canvas")
        self.minsize(700, 500)
        self.config(bg="lightgray")

        self.photo_frame = Frame(width=550, height=500, bg="lightgray")
        self.photo_frame.grid(row=0, column=0)
        self.canvas = Canvas(width=500, height=400, bg="white")
        self.canvas.grid(row=0, column=0, sticky="e")

        self.widgets_frame = Frame(width=150, height=500, bg="green")
        self.widgets_frame.grid(row=0, column=1, padx=20)

        self.widgets_frame.columnconfigure(0, weight=1)
        self.widgets_frame.rowconfigure(0, weight=1)
        self.widgets_frame.rowconfigure(1, weight=1)
        self.widgets_frame.rowconfigure(2, weight=1)

        self.widgets()
        self.mainloop()

    def widgets(self):
        self.browse_button = Button(self.widgets_frame, text="Browse", command=self.display_image,
                                    highlightbackground="lightgray")
        self.browse_button.grid(row=0, column=0, sticky="wens")
        # self.text_label = Label(self.widgets_frame, text="Enter text for your watermark:", bg="lightgray", fg="black")
        # self.text_label.grid(row=1, column=0, sticky="wens")
        self.text_entry = Entry(self.widgets_frame, background="white", highlightbackground="lightgray", fg="black",
                                justify=CENTER)
        self.text_entry.insert(END, "Enter your text here")
        self.text_entry.grid(row=1, column=0)
        self.add_watermark_button = Button(self.widgets_frame, command=self.add_watermark, text="Add Watermark",
                                           highlightbackground="lightgray")
        self.add_watermark_button.grid(row=2, column=0, sticky="wens")
        self.save_button = Button(self.widgets_frame, text="Save", highlightbackground="lightgray")
        self.save_button.grid(row=3, column=0, sticky="wens")


    def browse(self):
        file = filedialog.askopenfilename()
        print(type(file))
        print(file)
        return file
        # self.display_image(file)

    def display_image(self):
        file = self.browse()
        print(file)
        image = Image.open(file)
        resize_img = image.resize((500, 300))
        photo = ImageTk.PhotoImage(resize_img)
        print(f"photo: {type(photo)}")
        self.canvas.grid_forget()
        self.canvas = Canvas(width=500, height=400, bg="white")
        self.canvas.grid(row=0, column=0)
        self.canvas.create_image(250, 200, image=photo)
        self.mainloop()

    def add_watermark(self):
        wm_text = self.text_entry.get()
        print(wm_text)
        self.canvas.create_text(100, 100, text=wm_text, fill="black")
        self.mainloop()



ImageWaterMark()


# window = Tk()
# window.title("test canvas")
# window.minsize(500, 500)
#
# path = ""
#
#
# def browse():
#     global path
#     path = filedialog.askopenfilename()
#     get_path()
#
#
# def get_path():
#     print(type(path))
#
#
# browse_button = Button(text="Browse", command=browse)
# browse_button.pack()
#
# print(path)
#
# canvas = Canvas(width=400, height=400, bg="white")
# canvas.pack()
#
# image = Image.open()
# photo = ImageTk.PhotoImage(image)
# canvas.create_image(200, 200, image=photo)
#
# window.mainloop()

# photo = Image.open("/Users/Josip/Desktop/Programiranje/Python/Project/56. Personal web page/static/PNGPIX_Tool.png")
# print(photo.format, photo.size, photo.mode)
#
#
#
#
#
# for infile in sys.argv[1:]:
#     f, e = os.path.splitext(infile)
#     outfile = f + ".jpg"
#     if infile != outfile:
#         try:
#             with Image.open(infile) as im:
#                 im.save(outfile)
#         except OSError:
#             print("cannot convert", infile)

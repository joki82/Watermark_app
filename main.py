from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageGrab


class ImageWaterMark(Tk):
    """Creating main window, creating two frames - photo and buttons. Placing canvas over photo frame,
    call widgets method to create and place buttons in buttons frame"""
    def __init__(self):
        super().__init__()
        self.title("test canvas")
        self.minsize(700, 500)
        self.config(bg="lightgray")

        self.photo_frame = Frame(width=550, height=500, bg="lightgray")
        self.photo_frame.grid(row=0, column=0)
        self.canvas = Canvas(width=500, height=400, bg="white")
        self.canvas.grid(row=0, column=0)

        self.widgets_frame = Frame(width=150, height=500, bg="green")
        self.widgets_frame.grid(row=0, column=1, padx=20)

        self.widgets_frame.columnconfigure(0, weight=1)
        self.widgets_frame.rowconfigure(0, weight=1)
        self.widgets_frame.rowconfigure(1, weight=1)
        self.widgets_frame.rowconfigure(2, weight=1)

        self.widgets()
        self.mainloop()

    def widgets(self):
        """Creating buttons and text entry"""
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
        self.save_button = Button(self.widgets_frame, text="Save", command=self.save_image,
                                  highlightbackground="lightgray")
        self.save_button.grid(row=3, column=0, sticky="wens")


    def browse(self):
        """Browse button _ opens file dialog to select image. Method called from display_image and returning
        selected file to display image"""
        file = filedialog.askopenfilename()
        print(type(file))
        print(file)
        return file
        # self.display_image(file)

    def display_image(self):
        """Open object received from browse method and place it on canvas"""
        file = self.browse()
        print(file)
        image = Image.open(file)
        resize_img = image.resize((500, 300))
        photo = ImageTk.PhotoImage(resize_img)
        print(f"photo: {type(photo)}")
        self.canvas.grid_forget()
        # TODO write code to get imported image width&height and determine resize ratio to make canvas same size,
        #  that image fills canvas. Important for image crop to not have part of background crop
        self.canvas = Canvas(width=500, height=400, bg="white")
        self.canvas.grid(row=0, column=0)
        self.canvas.create_image(250, 200, image=photo)
        self.mainloop()

    def add_watermark(self):
        # TODO create text coordinates entry and proceed to create_text(x,y)
        # TODO
        # TODO change font or make selection of few
        wm_text = self.text_entry.get()
        print(wm_text)
        self.canvas.create_text(100, 100, text=wm_text, fill="black")
        self.mainloop()

    def save_image(self):
        # get main window x/y coordinates + canvas x/y
        canvas_x = self.winfo_rootx() + self.canvas.winfo_x()
        canvas_y = self.winfo_rooty() + self.canvas.winfo_y()
        print(canvas_x, canvas_y)
        # get canvas width & height to determine end x/y cor for crop
        canvas_width = canvas_x + self.canvas.winfo_width()
        canvas_height = canvas_y + self.canvas.winfo_height()
        print(canvas_width, canvas_height)
        #  crop canvas with displayed image and save. File path + name of file with extension.
        # TODO implement asksavefile instead manually set file path
        ImageGrab.grab().crop((canvas_x, canvas_y, canvas_width, canvas_height)).save("/Users/Josip/Desktop/canvas.png")


ImageWaterMark()





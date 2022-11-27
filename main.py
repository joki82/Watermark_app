from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageGrab


class ImageWaterMark(Tk):
    """Creating main window, creating two frames - photo and buttons. Placing canvas over the photo frame,
    call widgets method to create and place buttons in buttons frame"""

    def __init__(self):
        super().__init__()
        self.title("test canvas")
        # self.minsize(700, 500)
        self.config(bg="lightgray")

        self.photo_frame = Frame(width=550, height=500, bg="lightgray")
        self.photo_frame.grid(row=0, column=0)
        self.canvas = Canvas(width=500, height=400, bg="white")
        self.canvas.grid(row=0, column=0)

        self.widgets_frame = Frame(width=150, height=500, bg="green")
        self.widgets_frame.grid(row=0, column=1, padx=20)

        self.widgets()
        self.mainloop()

    def widgets(self):
        """Creating buttons, create Frame containing labels, text entry, x_y coordinate sliders, spinboxes for font,
        size and color."""
        COLORS = ("White", "Black", "Gray", "Red", "Blue", "Green", "Yellow")
        FONT = ("Arial", "Broadway", "Century", "Comic Sans MS", "Great Vibes", "Ubuntu", "Times New Roman")
        # Widget frame
        browse_button = Button(self.widgets_frame, text="Browse", command=self.display_image,
                               highlightbackground="lightgray")
        browse_button.grid(row=0, column=0, sticky="wens")

        #  Label frame inside the widget frame containing text entry, X_Y scale and font, size and color spinboxes
        labels_frame = Frame(self.widgets_frame)
        labels_frame.grid(row=1, column=0)

        text_label = Label(labels_frame, text="Text:", bg="lightgray", fg="black")
        text_label.grid(row=0, column=0, sticky="wens")
        self.text_entry = Entry(labels_frame, background="white", highlightbackground="lightgray", fg="black",
                                justify=CENTER, highlightthickness=1)
        self.text_entry.grid(row=0, column=1, sticky="wens")

        xcor_label = Label(labels_frame, text="X cor:", bg="lightgray", fg="black")
        xcor_label.grid(row=1, column=0, sticky="wens")
        self.xcor_entry = Scale(labels_frame, orient=HORIZONTAL, from_=10, to=490, bg="lightgray", fg="black",
                                troughcolor="white")
        self.xcor_entry.grid(row=1, column=1, sticky="wens")

        ycor_label = Label(labels_frame, text="Y cor:", bg="lightgray", fg="black")
        ycor_label.grid(row=2, column=0, sticky="wens")
        self.ycor_entry = Scale(labels_frame, orient=HORIZONTAL, from_=10, to=390, bg="lightgray", fg="black",
                                troughcolor="white")
        self.ycor_entry.grid(row=2, column=1, sticky="wens")

        font_label = Label(labels_frame, text="Font:", bg="lightgray", fg="black")
        font_label.grid(row=3, column=0, sticky="wens")
        self.font_entry = Spinbox(labels_frame, bg="white", highlightbackground="lightgray", values=FONT, fg="black",
                                  justify=CENTER)
        self.font_entry.grid(row=3, column=1, sticky="wens")

        size_label = Label(labels_frame, text="Size:", bg="lightgray", fg="black")
        size_label.grid(row=4, column=0, sticky="wens")
        self.size_entry = Spinbox(labels_frame, bg="white", highlightbackground="lightgray", from_=10, to=36,
                                  fg="black", justify=CENTER)
        self.size_entry.grid(row=4, column=1, sticky="wens")

        # Function to change background and font color of color spinbox
        def change_color():
            color = self.color_entry.get()
            if color != "White":
                self.color_entry.config(fg="white")
            else:
                self.color_entry.config(fg="black")
            self.color_entry.config(bg=f"{color}")

        color_label = Label(labels_frame, text="Color:", bg="lightgray", fg="black")
        color_label.grid(row=5, column=0, sticky="wens")
        self.color_entry = Spinbox(labels_frame, bg="white", highlightbackground="lightgray", justify=CENTER,
                                   fg="black", values=COLORS, command=change_color)
        self.color_entry.grid(row=5, column=1, sticky="wens")

        # Widget frame, add_watermark and save buttons
        add_watermark_button = Button(self.widgets_frame, command=self.add_watermark, text="Add Watermark",
                                      highlightbackground="lightgray")
        add_watermark_button.grid(row=2, column=0, sticky="wens")
        save_button = Button(self.widgets_frame, text="Save", command=self.save_image,
                             highlightbackground="lightgray")
        save_button.grid(row=3, column=0, sticky="wens")

    def browse(self):
        """Browse button opens file dialog to select an image and returns"""
        file = filedialog.askopenfilename(filetypes=(("jpeg files", "*.jpeg"), ("png files", "*.png"),
                                                     ("jpg files", "*.jpg")))
        return file


    def display_image(self):
        """Opens file received from browse method. Checks width/height, resize if necessary and place it on canvas"""
        file = self.browse()
        image = Image.open(file)
        width = image.width
        print(width)
        height = image.height
        print(height)
        while width > 1000 or height > 800:
            width = int(width / 2)
            height = int(height / 2)
        resize_img = image.resize((width, height))
        photo = ImageTk.PhotoImage(resize_img)
        # Remove empty canvas and replace it with image using image width/height
        self.canvas.grid_forget()
        self.canvas = Canvas(width=width, height=height, bg="white", highlightthickness=0)
        self.canvas.grid(row=0, column=0, padx=20, pady=20)
        self.canvas.create_image(width / 2, height / 2, image=photo, anchor="c")
        # Limit X_Y cor entries to not start text in end corners
        self.xcor_entry.config(to=width - 10)
        self.ycor_entry.config(to=height - 10)
        self.mainloop()

    def add_watermark(self):
        """Collecting Text, Font, Size, Color, x & y coordinates and placing text on the canvas as per collected """
        wm_text = self.text_entry.get()
        font_name = self.font_entry.get()
        font_size = self.size_entry.get()
        font_color = self.color_entry.get()
        x_cor = float(self.xcor_entry.get())
        y_cor = float(self.ycor_entry.get())
        self.canvas.create_text(x_cor, y_cor, text=wm_text, fill=font_color, font=(font_name, font_size))
        self.mainloop()

    def save_location(self):
        """Open filedialog to select save location and name the file"""
        save_location = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpeg"), ("png files", "*.png"),
                                                            ("jpg files", "*.jpg")))
        return save_location.name

    def save_image(self):
        """Get canvas start/end coordinates, crop and save image."""
        # Get main window x/y coordinates + canvas x/y
        canvas_x = self.winfo_rootx() + self.canvas.winfo_x()
        canvas_y = self.winfo_rooty() + self.canvas.winfo_y()
        # Get canvas width & height to determine end x/y cor for crop
        canvas_width = canvas_x + self.canvas.winfo_width()
        canvas_height = canvas_y + self.canvas.winfo_height()
        #  Crop canvas with displayed image and save. File path + name of file with extension.
        image_grab = ImageGrab.grab().crop((canvas_x, canvas_y, canvas_width, canvas_height))
        image_final = image_grab.convert('RGB')
        image_final.save(self.save_location())


ImageWaterMark()

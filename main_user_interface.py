from tkinter import RIDGE, DISABLED, CENTER
from tkinter import Tk, Label, Button, Entry, PhotoImage, Toplevel
from tkinter import filedialog
from tkinter import messagebox

from video_or_song import Video, PlaylistVideo, PlaylistAudio, Audio


def download_video():
    def submit_link():
        global LINK
        LINK = entry_link.get()
        print(LINK)
        if len(LINK) == 0:
            messagebox.showerror(title="Empty Link", message="You have to specify a URL!")
            return exit
        entry_link.insert(0, LINK)
        entry_link.config(state=DISABLED)
        return LINK

    def submit_path():
        global PATH  # This is the place where we have to declare the PATH variable
        PATH = None
        try:
            PATH = filedialog.askdirectory()
            print(PATH)
        except ValueError:
            if PATH is None:
                return exit

        entry_path.insert(0, PATH)
        return PATH

    def download():
        video = Video(LINK, PATH)
        video.download_file()

    def cancel():
        download_window.destroy()
        window.deiconify()

    window.withdraw()
    download_window = Toplevel()
    # to center the window based on the screen size in the middle
    download_window.geometry("620x413+300+150")
    download_window.wm_attributes("-topmost", True)
    download_window.resizable(0, 0)
    download_window.title("Download Window")
    # Make the background an image
    image_video = PhotoImage(file="imageFiles/imageresized.png")
    # Add the image as the main background in the label widget
    label_d = Label(download_window, image=image_video)
    label_d.place(x=0, y=0, relwidth=1, relheight=1)  # Place the image as a full size of the window
    # The Entry for the LINK
    entry_link = Entry(download_window,
                       font=("Consolas", 15, "bold"),
                       bg="white",
                       fg="#8265ab",
                       width=25,
                       highlightbackground="#eda1d8",
                       highlightcolor="#eda1d8",
                       highlightthickness=4

                       )
    # entry_link.insert(0, "Enter the Link ")
    entry_link.grid(row=0, column=0, padx=40, pady=20)
    # The Button for submitting the LINK
    button_link = Button(download_window,
                         command=submit_link,
                         text="Submit",
                         font=("Consolas", 15, "bold"),
                         bg="#eda1d8",
                         fg="#8265ab",
                         width=18,
                         bd=3, relief=RIDGE,
                         activeforeground="white",
                         activebackground="#eda1d8")
    button_link.grid(row=0, column=2)
    # The entry for the PATH
    entry_path = Entry(download_window,
                       font=("Consolas", 15, "bold"),
                       bg="white",
                       fg="#8265ab",
                       width=25,
                       highlightbackground="#eda1d8",
                       highlightcolor="#eda1d8",
                       highlightthickness=4,

                       )
    # entry_path.insert(0, "PATH")
    entry_path.grid(row=1, column=0, padx=50, pady=50)
    # The Button for submitting the PATH
    button_path = Button(download_window,
                         command=submit_path,
                         text="Choose Directory",
                         font=("Consolas", 15, "bold"),
                         bg="#eda1d8",
                         fg="#8265ab",
                         width=18,
                         bd=3, relief=RIDGE,
                         activeforeground="white",
                         activebackground="#eda1d8")
    button_path.grid(row=1, column=2)

    # The Button for downloading the file
    download_button = Button(download_window,
                             text="Download",
                             command=download,
                             font=("Consolas", 15, "bold"),
                             bg="#eda1d8",
                             fg="#8265ab",
                             width=18,
                             bd=3, relief=RIDGE,
                             activeforeground="white",
                             activebackground="#eda1d8")
    download_button.grid(row=2, column=0, columnspan=3, pady=20)
    # The Button to cancel and go back
    cancel_button = Button(download_window,
                           text="Cancel",
                           command=cancel,
                           font=("Consolas", 15, "bold"),
                           bg="#eda1d8",
                           fg="#8265ab",
                           width=18,
                           bd=3, relief=RIDGE,
                           activeforeground="white",
                           activebackground="#eda1d8")
    cancel_button.grid(row=3, column=0, columnspan=3, pady=20)

    download_window.mainloop()


def download_audio():
    def submit_link():
        global LINK
        LINK = entry_link.get()
        print(LINK)
        if len(LINK) == 0:
            messagebox.showerror(title="Empty Link", message="You have to specify a URL!")
            return exit
        entry_link.insert(0, LINK)
        entry_link.config(state=DISABLED)
        return LINK

    def submit_path():
        global PATH  # This is the place where we have to declare the PATH variable
        PATH = None
        try:
            PATH = filedialog.askdirectory()
            print(PATH)
        except ValueError:
            if PATH is None:
                return exit

        entry_path.insert(0, PATH)
        return PATH

    def download():
        audio = Audio(LINK, PATH)
        audio.download_file()

    def cancel():
        download_window.destroy()
        window.deiconify()

    window.withdraw()
    download_window = Toplevel()
    # to center the window based on the screen size in the middle
    download_window.geometry("620x413+300+150")
    download_window.wm_attributes("-topmost", True)
    download_window.resizable(0, 0)
    download_window.title("Download Window")
    # Make the background an image
    image_video = PhotoImage(file="imageFiles/imageresized.png")
    # Add the image as the main background in the label widget
    label_d = Label(download_window, image=image_video)
    label_d.place(x=0, y=0, relwidth=1, relheight=1)  # Place the image as a full size of the window
    # The Entry for the LINK
    entry_link = Entry(download_window,
                       font=("Consolas", 15, "bold"),
                       bg="white",
                       fg="#8265ab",
                       width=25,
                       highlightbackground="#eda1d8",
                       highlightcolor="#eda1d8",
                       highlightthickness=4

                       )
    # entry_link.insert(0, "Enter the Link ")
    entry_link.grid(row=0, column=0, padx=40, pady=20)
    # The Button for submitting the LINK
    button_link = Button(download_window,
                         command=submit_link,
                         text="Submit",
                         font=("Consolas", 15, "bold"),
                         bg="#eda1d8",
                         fg="#8265ab",
                         width=18,
                         bd=3, relief=RIDGE,
                         activeforeground="white",
                         activebackground="#eda1d8")
    button_link.grid(row=0, column=2)
    # The entry for the PATH
    entry_path = Entry(download_window,
                       font=("Consolas", 15, "bold"),
                       bg="white",
                       fg="#8265ab",
                       width=25,
                       highlightbackground="#eda1d8",
                       highlightcolor="#eda1d8",
                       highlightthickness=4,

                       )
    # entry_path.insert(0, "PATH")
    entry_path.grid(row=1, column=0, padx=50, pady=50)
    # The Button for submitting the PATH
    button_path = Button(download_window,
                         command=submit_path,
                         text="Choose Directory",
                         font=("Consolas", 15, "bold"),
                         bg="#eda1d8",
                         fg="#8265ab",
                         width=18,
                         bd=3, relief=RIDGE,
                         activeforeground="white",
                         activebackground="#eda1d8")
    button_path.grid(row=1, column=2)

    # The Button for downloading the file
    download_button = Button(download_window,
                             text="Download",
                             command=download,
                             font=("Consolas", 15, "bold"),
                             bg="#eda1d8",
                             fg="#8265ab",
                             width=18,
                             bd=3, relief=RIDGE,
                             activeforeground="white",
                             activebackground="#eda1d8")
    download_button.grid(row=2, column=0, columnspan=3, pady=20)
    # The Button to cancel and go back
    cancel_button = Button(download_window,
                           text="Cancel",
                           command=cancel,
                           font=("Consolas", 15, "bold"),
                           bg="#eda1d8",
                           fg="#8265ab",
                           width=18,
                           bd=3, relief=RIDGE,
                           activeforeground="white",
                           activebackground="#eda1d8")
    cancel_button.grid(row=3, column=0, columnspan=3, pady=20)

    download_window.mainloop()


def download_playlist_v():
    def submit_link():
        global LINK
        LINK = entry_link.get()
        print(LINK)
        if len(LINK) == 0:
            messagebox.showerror(title="Empty Link", message="You have to specify a URL!")
            return exit
        entry_link.insert(0, LINK)
        entry_link.config(state=DISABLED)
        return LINK

    def submit_path():
        global PATH  # This is the place where we have to declare the PATH variable
        PATH = None
        try:
            PATH = filedialog.askdirectory()
            print(PATH)
        except ValueError:
            if PATH is None:
                return exit

        entry_path.insert(0, PATH)
        return PATH

    def download():
        playlist_vid = PlaylistVideo(LINK, PATH)
        playlist_vid.download_playlist()

    def cancel():
        download_window.destroy()
        window.deiconify()

    window.withdraw()
    download_window = Toplevel()
    # to center the window based on the screen size in the middle
    download_window.geometry("620x413+300+150")
    download_window.wm_attributes("-topmost", True)
    download_window.resizable(0, 0)
    download_window.title("Download Window")
    # Make the background an image
    image_video = PhotoImage(file="imageFiles/imageresized.png")
    label_d = Label(download_window, image=image_video)  # Add the image as the main background in the label widget
    label_d.place(x=0, y=0, relwidth=1, relheight=1)  # Place the image as a full size of the window
    # The Entry for the LINK
    entry_link = Entry(download_window,
                       font=("Consolas", 15, "bold"),
                       bg="white",
                       fg="#8265ab",
                       width=25,
                       highlightbackground="#eda1d8",
                       highlightcolor="#eda1d8",
                       highlightthickness=4

                       )
    # entry_link.insert(0, "Enter the Link ")
    entry_link.grid(row=0, column=0, padx=40, pady=20)
    # The Button for submitting the LINK
    button_link = Button(download_window,
                         command=submit_link,
                         text="Submit",
                         font=("Consolas", 15, "bold"),
                         bg="#eda1d8",
                         fg="#8265ab",
                         width=18,
                         bd=3, relief=RIDGE,
                         activeforeground="white",
                         activebackground="#eda1d8")
    button_link.grid(row=0, column=2)
    # The entry for the PATH
    entry_path = Entry(download_window,
                       font=("Consolas", 15, "bold"),
                       bg="white",
                       fg="#8265ab",
                       width=25,
                       highlightbackground="#eda1d8",
                       highlightcolor="#eda1d8",
                       highlightthickness=4,

                       )
    # entry_path.insert(0, "PATH")
    entry_path.grid(row=1, column=0, padx=50, pady=50)
    # The Button for submitting the PATH
    button_path = Button(download_window,
                         command=submit_path,
                         text="Choose Directory",
                         font=("Consolas", 15, "bold"),
                         bg="#eda1d8",
                         fg="#8265ab",
                         width=18,
                         bd=3, relief=RIDGE,
                         activeforeground="white",
                         activebackground="#eda1d8")
    button_path.grid(row=1, column=2)

    # The Button for downloading the file
    download_button = Button(download_window,
                             text="Download",
                             command=download,
                             font=("Consolas", 15, "bold"),
                             bg="#eda1d8",
                             fg="#8265ab",
                             width=18,
                             bd=3, relief=RIDGE,
                             activeforeground="white",
                             activebackground="#eda1d8")
    download_button.grid(row=2, column=0, columnspan=3, pady=20)
    # The Button to cancel and go back
    cancel_button = Button(download_window,
                           text="Cancel",
                           command=cancel,
                           font=("Consolas", 15, "bold"),
                           bg="#eda1d8",
                           fg="#8265ab",
                           width=18,
                           bd=3, relief=RIDGE,
                           activeforeground="white",
                           activebackground="#eda1d8")
    cancel_button.grid(row=3, column=0, columnspan=3, pady=20)

    download_window.mainloop()


def download_playlist_a():
    def submit_link():
        global LINK
        LINK = entry_link.get()
        print(LINK)
        if len(LINK) == 0:
            messagebox.showerror(title="Empty Link", message="You have to specify a URL!")
            return exit
        entry_link.insert(0, LINK)
        entry_link.config(state=DISABLED)
        return LINK

    def submit_path():
        global PATH  # This is the place where we have to declare the PATH variable
        PATH = None
        try:
            PATH = filedialog.askdirectory()
            print(PATH)
        except ValueError:
            if PATH is None:
                return exit

        entry_path.insert(0, PATH)
        return PATH

    def download():
        playlist_aud = PlaylistAudio(LINK, PATH)
        playlist_aud.download_playlist()

    def cancel():
        download_window.destroy()
        window.deiconify()

    window.withdraw()
    download_window = Toplevel()
    download_window.geometry("620x413+300+150")  # to center the window based on the screen size in the middle
    download_window.wm_attributes("-topmost", True)
    download_window.resizable(0, 0)
    download_window.title("Download Window")
    # Make the background an image
    image_video = PhotoImage(file="imageFiles/imageresized.png")
    # Add the image as the main background in the label widget
    label_d = Label(download_window, image=image_video)
    # Place the image as a full size of the window
    label_d.place(x=0, y=0, relwidth=1, relheight=1)
    # The Entry for the LINK
    entry_link = Entry(download_window,
                       font=("Consolas", 15, "bold"),
                       bg="white",
                       fg="#8265ab",
                       width=25,
                       highlightbackground="#eda1d8",
                       highlightcolor="#eda1d8",
                       highlightthickness=4

                       )
    # entry_link.insert(0, "Enter the Link ")
    entry_link.grid(row=0, column=0, padx=40, pady=20)
    # The Button for submitting the LINK
    button_link = Button(download_window,
                         command=submit_link,
                         text="Submit",
                         font=("Consolas", 15, "bold"),
                         bg="#eda1d8",
                         fg="#8265ab",
                         width=18,
                         bd=3, relief=RIDGE,
                         activeforeground="white",
                         activebackground="#eda1d8")
    button_link.grid(row=0, column=2)
    # The entry for the PATH
    entry_path = Entry(download_window,
                       font=("Consolas", 15, "bold"),
                       bg="white",
                       fg="#8265ab",
                       width=25,
                       highlightbackground="#eda1d8",
                       highlightcolor="#eda1d8",
                       highlightthickness=4,

                       )
    # entry_path.insert(0, "PATH")
    entry_path.grid(row=1, column=0, padx=50, pady=50)
    # The Button for submitting the PATH
    button_path = Button(download_window,
                         command=submit_path,
                         text="Choose Directory",
                         font=("Consolas", 15, "bold"),
                         bg="#eda1d8",
                         fg="#8265ab",
                         width=18,
                         bd=3, relief=RIDGE,
                         activeforeground="white",
                         activebackground="#eda1d8")
    button_path.grid(row=1, column=2)

    # The Button for downloading the file
    download_button = Button(download_window,
                             text="Download",
                             command=download,
                             font=("Consolas", 15, "bold"),
                             bg="#eda1d8",
                             fg="#8265ab",
                             width=18,
                             bd=3, relief=RIDGE,
                             activeforeground="white",
                             activebackground="#eda1d8")
    download_button.grid(row=2, column=0, columnspan=3, pady=20)
    # The Button to cancel and go back
    cancel_button = Button(download_window,
                           text="Cancel",
                           command=cancel,
                           font=("Consolas", 15, "bold"),
                           bg="#eda1d8",
                           fg="#8265ab",
                           width=18,
                           bd=3, relief=RIDGE,
                           activeforeground="white",
                           activebackground="#eda1d8")
    cancel_button.grid(row=3, column=0, columnspan=3, pady=20)

    download_window.mainloop()


def exit_root():
    window.destroy()
    exit_window = Tk()

    exit_window.geometry("620x413+300+150")
    exit_window.resizable(0, 0)
    exit_window.title("Exit window")
    image_exit = PhotoImage(file="imageFiles/imageresized.png")
    exit_label = Label(exit_window, image=image_exit)
    exit_label.place(x=0, y=0, relwidth=1, relheight=1)
    text_label=Label(exit_window,
                     text="🙈🙈 THANK YOU FOR USING ME 🙈🙈",
                     font=("Consolas", 25, "bold"),
                     bg="#eda1d8",
                     fg="#8265ab",
                     bd=3, relief=RIDGE,
                     activeforeground="white",
                     activebackground="#eda1d8")

    text_label.place(relx=0.5, rely=0.5,anchor=CENTER)

    exit_window.after(1700, exit_window.destroy)
    exit_window.mainloop()


window = Tk()
window.wm_attributes("-topmost", True)  # To make the window in the screen even if we click outside
window.geometry("620x413+300+150")  # to center the window based on the screen size in the middle
window.resizable(0, 0)
icon = PhotoImage(file="imageFiles/icon1.png")
window.iconphoto(True, icon)
window.title("The Main User Interface")
image = PhotoImage(file="imageFiles/imageresized.png")
label = Label(window, image=image)
label.place(x=0, y=0, relwidth=1, relheight=1)
download_v_button = Button(window,
                           text="Download Videos",
                           command=download_video,
                           font=("Consolas", 15, "bold"),
                           bg="#eda1d8",
                           fg="#8265ab",
                           width=33,
                           bd=3, relief=RIDGE,
                           activeforeground="white",
                           activebackground="#eda1d8"
                           )
download_v_button.pack(pady=20)
download_a_button = Button(window,
                           text="Download audios",
                           command=download_audio,
                           font=("Consolas", 15, "bold"),
                           bg="#eda1d8",
                           fg="#8265ab",
                           width=33,
                           bd=3, relief=RIDGE,
                           activeforeground="white",
                           activebackground="#eda1d8")
download_a_button.pack(pady=20)
download_vp_button = Button(window,
                            text="Download a whole Playlist Video",
                            command=download_playlist_v,
                            font=("Consolas", 15, "bold"),
                            bg="#eda1d8",
                            fg="#8265ab",
                            width=33,
                            bd=3, relief=RIDGE,
                            activeforeground="white",
                            activebackground="#eda1d8"
                            )
download_vp_button.pack(pady=20)
download_va_button = Button(window,
                            text="Download a whole Playlist Audio",
                            command=download_playlist_a,
                            font=("Consolas", 15, "bold"),
                            bg="#eda1d8",
                            fg="#8265ab",
                            width=33,
                            bd=3, relief=RIDGE,
                            activeforeground="white",
                            activebackground="#eda1d8"
                            )
download_va_button.pack(pady=20)
exit_button = Button(window,
                     text="Exit",
                     command=exit_root,
                     font=("Consolas", 15, "bold"),
                     bg="#eda1d8",
                     fg="#8265ab",
                     width=33,
                     bd=3, relief=RIDGE,
                     activeforeground="white",
                     activebackground="#eda1d8")
exit_button.pack(pady=20)

window.mainloop()

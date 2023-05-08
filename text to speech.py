from gtts import gTTS
import os
text="Hey Iam Aby Nice meeting you"
output=gTTS(text=text,lang="en",slow=False)
output.save("audio3.mp3")
os.system("start audio3.mp3")

# from gtts import gTTS
# import os
# text=open("newone.txt",'r',encoding='utf-8').read()
# output=gTTS(text=text,lang="en",slow=False)
# output.save("fileread1.mp3")
# os.system("start fileread1.mp3")

# from gtts import gTTS
# import os
# from tkinter import *
#
# root = Tk()
# root.title("Text to Speech Converter")
# root.geometry("500x400")
#
# # Set up canvas
# canvas = Canvas(root, bg="#fff", width=500, height=400)
# canvas.pack(fill=BOTH, expand=True)
#
# # Set up title label
# title_label = Label(root, text="Text to Speech Converter", font=("Courier New", 20), bg="#fff")
# canvas.create_window(250, 50, window=title_label)
#
# # Set up text entry field
# entry = Entry(root, font=("Courier New", 16))
# canvas.create_window(250, 200, window=entry)
#
# # Set up button with animation
# button = Button(text="Convert to Speech", font=("Courier New", 13), bg="#007bff", fg="#fff", bd=0, activebackground="#0062cc", activeforeground="#fff", command=lambda: animate(button, fun))
# canvas.create_window(250, 230, window=button)
#
# # Animate button
# def animate(widget, command):
#     widget.config( text="Converting...")
#     root.after(1000, lambda: command())
#     root.after(3000, lambda: widget.config(state=NORMAL, text="Convert to Speech"))
#
# # Convert text to speech
# def fun():
#     text = entry.get()
#     output = gTTS(text=text, lang="ja", slow=False)
#     output.save("newone.mp3")
#     os.system("newone.mp3")
#
# # Center all widgets on canvas
# title_label.place(relx=0.5, rely=0.2, anchor=CENTER)
# entry.place(relx=0.5, rely=0.5, anchor=CENTER)
# button.place(relx=0.5, rely=0.6, anchor=CENTER)
#
# root.mainloop()







































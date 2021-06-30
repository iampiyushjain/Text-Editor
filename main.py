from Window import *

TextEditor = Window()

TextEditor.TextBox.pack(expand=1, fill="both")
TextEditor.window.protocol("WM_DELETE_WINDOW", TextEditor.on_closing)
TextEditor.window.bind("<Key>", TextEditor.key_pressed)
TextEditor.window.mainloop()

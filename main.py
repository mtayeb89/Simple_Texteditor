import tkinter as tk
from tkinter import filedialog, messagebox

class SimpleTextEditor:
    def __init__(self, master):
        self.master = master
        self.filename = None  # Stores the current file's path
        self.setup_ui()  # Setup the user interface

    def setup_ui(self):
        # Set up the main window
        self.master.title("Mahmoud Text Editor")
        self.master.geometry("800x600")

        # Create the text area widget where the user can type
        self.text_area = tk.Text(self.master, wrap="word", undo=True)
        self.text_area.pack(expand=True, fill="both")  # Make it fill the entire window

        # Create the menu bar
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        # Create the "File" menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)

        # Create the "Edit" menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"))

        # Create the "Help" menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def new_file(self):
        """Clear the text area to create a new file."""
        self.filename = None
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        """Open an existing file and display its contents."""
        file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, content)
            self.filename = file_path

    def save_file(self):
        """Save the current file or use 'Save As' if no file is open."""
        if self.filename:
            with open(self.filename, "w") as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)
        else:
            self.save_file_as()

    def save_file_as(self):
        """Save the current content as a new file."""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)
            self.filename = file_path

    def show_about(self):
        """Display an 'About' dialog."""
        messagebox.showinfo("About", "Simple Text Editor\nCreated with Python and Tkinter")

def main():
    # Initialize the Tkinter window
    root = tk.Tk()
    # Create an instance of SimpleTextEditor
    SimpleTextEditor(root)
    # Run the application
    root.mainloop()

# If this script is run directly, start the main function
if __name__ == "__main__":
    main()

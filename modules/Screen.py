import tkinter as tk

try:
    from modules.Observer import Observer
except:
    from Observer import Observer


class Screen(Observer):

    def __init__(self, parent):
        self.parent         = parent
        self.current_note   = tk.StringVar()
        self.pure_note      = tk.IntVar()
        self.harmonic       = tk.IntVar()
        
        self.notes          = ['C', 'C#', 'D', 'D#',
                               'E', 'F', 'F#', 'G',
                               'G#', 'A', 'A#', 'B']
        self.current_note.set('C')
        
        self.create_frames()
        self.create_labels()
        self.create_optmenus()
        self.create_spinboxes()
        self.create_buttons()
        self.create_checkboxes()
        self.show_all()

    def create_frames(self):
        self.gen_note_frame = tk.Frame(
            self.parent,
            highlightbackground='#273746',
            highlightcolor='#273746',
            highlightthickness=1.5,
            relief='raised',
            bd=0
        )

        self.gen_mode_frame = tk.Frame(
            self.gen_note_frame,
            highlightbackground='#273746',
            highlightcolor='#273746',
            highlightthickness=1.5,
            relief='raised',
            bd=0
        )

    def create_labels(self):
        self.gen_note_title = tk.Label(
            self.gen_note_frame,
            text='Note Generator',
            fg='white',
            bg='#2E4053',
            justify='center',
            height=3
        )

        self.gen_mode_title = tk.Label(
            self.gen_mode_frame,
            text='Mode',
            fg='white',
            bg='#2E4053',
            justify='center',
            height=2
        )

        self.note_label = tk.Label(
            self.gen_note_frame,
            text='Note to generate :',
            font='Arial 11 bold',
            fg='black',
            highlightbackground='#273746',
            highlightcolor='#273746',
            highlightthickness=1,
            relief='raised',
            bd=1
        )

        self.oct_label  = tk.Label(
            self.gen_note_frame,
            text='Octave :',
            font='Arial 11 bold',
            fg='black',
            highlightbackground='#273746',
            highlightcolor='#273746',
            highlightthickness=1,
            relief='raised',
            bd=1
        )
    
    def create_optmenus(self):
        self.note_menu = tk.OptionMenu(
                                self.gen_note_frame,
                                self.current_note,
                                *self.notes
                            )

        self.note_menu.config(
                        font='Arial 12 bold',
                        highlightbackground='#273746',
                        highlightcolor='#273746',
                        highlightthickness=1,
                        relief='raised',
                        bd=1
                    )

    def create_spinboxes(self):
        self.oct_spin = tk.Spinbox(
                            self.gen_note_frame,
                            font='Arial 12 bold',
                            justify='center',
                            from_=1,
                            to=8,
                            highlightbackground='#273746',
                            highlightcolor='#273746',
                            highlightthickness=1,
                            relief='raised',
                            bd=1
                        )
    
    def create_buttons(self):
        self.save_button = tk.Button(
                                self.gen_note_frame,
                                text='Save',
                                font='Arial 15',
                                justify='center',
                                highlightbackground='#273746',
                                highlightcolor='#273746',
                                highlightthickness=1,
                                relief='raised'
                            )

    def create_checkboxes(self):
        self.pure_note_cb = tk.Checkbutton(
            self.gen_mode_frame,
            text='Pure Note',
            font='Arial 12',
            variable=self.pure_note,
            onvalue=1,
            highlightbackground='#273746',
            highlightcolor='#273746',
            highlightthickness=1,
            relief='flat'
        )

        self.harmonic_cb = tk.Checkbutton(
            self.gen_mode_frame,
            text='Harmonic',
            font='Arial 12',
            variable=self.harmonic,
            onvalue=1,
            highlightbackground='#273746',
            highlightcolor='#273746',
            highlightthickness=1,
            relief='flat'
        )

    def show_all(self):
        self.gen_note_frame.place(relx=0.05, rely=0.05, width=300, height=300)
        self.gen_note_title.pack(fill='x')

        self.note_label.place(relx=0.02, rely=0.2, relheight=0.1, anchor='nw')
        self.oct_label.place(relx=0.02, rely=0.35, relheight=0.1, anchor='nw')
        self.note_menu.place(relx=0.99, rely=0.2, relheight=0.1, anchor='ne')
        self.oct_spin.place(relx=0.99, rely=0.35, relwidth=0.2, relheight=0.1, anchor='ne')

        self.gen_mode_frame.place(relx=0.02, rely=0.65, relwidth=0.4, relheight=0.32)
        self.gen_mode_title.pack(fill='x')
        self.pure_note_cb.pack(fill='x')
        self.harmonic_cb.pack(fill='x')

        self.save_button.place(relx=0.98, rely=0.98, relwidth=0.2, relheight=0.1, anchor='se')


if __name__ == "__main__":
    root = tk.Tk()

    root.resizable(True, True)
    root.title('Generate Notes')
    root.geometry('900x800')

    view    = Screen(root)
    
    root.mainloop()
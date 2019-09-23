class Controller:

    def __init__(self, model, view):
        self.model  = model
        self.view   = view

        self.view.save_button.bind("<Button-1>", self.save_fnc)

    def save_fnc(self, event):
        note            = self.view.current_note.get()
        octa            = self.view.oct_spin.get()
        is_pure_note    = self.view.pure_note.get()
        is_harmonic     = self.view.harmonic.get()
        
        self.model.create_note(octa, note, is_pure_note, is_harmonic)
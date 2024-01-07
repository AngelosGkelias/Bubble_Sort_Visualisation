import tkinter as tk
import random
import time

array = []
interval = 0.1
array_lenght = 0


def random_array(l):
    array = []#καθαρίζει το array ώστε να μην υπάρχουν στοιχεία από προηγούμενες εφαρμογές του αλγ
    for i in range(0, l):
        array.append(random.randint(0,200))#δημιουργεί μία τυχαία λίστα με l στοιχεία ως 200
    return array

def sorting_algorithm():
    array = random_array(array_lenght_chooser.get())#παίρνει στοιχεία από το array_lenght_chooser Scale widget (βλ. gui())
    interval = time_interval.get()/1000#παίρνει στοχεία από το time_interval Scale widget και διαιρεί με 1000 γιατί δίνεται σε ms και θέλουμε s.
    column_width = (canvas_1.width)/len(array)#συνολίκό μήκος το καμβά διά το μήκος της λίστας, το κενό μεταξύ των στηλών δημιουργείται αργότερα
    lenght_scale = canvas_1.height/max(array)#συνολικό μήκος του καμβά διά το μέγιστο στοιχείο της λίστας ώστε τα υπόλοιπα στοιχεία να εκφράζονται ως λόγος του μεγαλύτερου το οποίο θα καταλαμβάνει όλο το ύψος του καμβά
    n = 0
    l = len(array)
    finished = False
    for o in range(l-1):#αν έχουν κατανεμηθεί τα στοιχεία σταματάει
        if finished == True:
            for i in range(len(array)):#οταν τελειώσει ο αλγόρθμος ξανασχεδιάζει με όλες τις σ΄τήλες άσπρες
                canvas_1.create_column(array[i]*lenght_scale, column_width, i*column_width, window.winfo_screenheight(), "white")
            return
        finished = True#θεωρεί ότι έχουν κατανεμηθεί, ενημερώνεται παρακάτω αν δεν ισχύει
        for i in range(l-n-1):#δεν χρειάζεται να ελέγχονται όλα τα στοιχεία αφού το μεγαλύτερο σε κάθε επανάληψη είναι δεδομένο ότι θα κατανεμηθεί σωστά
            time.sleep(interval)
            canvas.delete("all")#καθαρίζει τον καμ΄βά
            for j in range(len(array)):#for loop ώστε να δημιουργηθεί η κάθε στήλη
                if i == j-1:#αλλίως i + 1 == j, αν ισχύει αυτό σημαίνει ότι στην συγκεκριμένη επανάληψη σχεδιάζονται τα στοιχεία που σχεδιάζονται και γίνονται πράσινα
                    canvas_1.create_column(array[j]*lenght_scale, column_width, j*column_width, window.winfo_screenheight(), "green")
                    canvas_1.create_column(array[j-1]*lenght_scale, column_width, (j-1)*column_width, window.winfo_screenheight(), "green")
                else:# αν δεν ισχύει το παραπάνω σχεδιάζονται απλά, άσπρα
                    canvas_1.create_column(array[j]*lenght_scale, column_width, j*column_width, window.winfo_screenheight(), "white")
            canvas.update()#ενημερώνει τον καμβά

            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                finished = False#αν δεν υπάρχουν στοιχεία που ικανοποιούν τη συνθήκη του if loop, η μεταβλητή δεν ενημερώνεται από την κατάσταση True και ο αλγόρθσμος τελειώνει
                time.sleep(interval)
                canvas.delete("all")
                for j in range(len(array)):#δες 12 γραμμές πάνω
                    
                    if i == j-1:
                        canvas_1.create_column(array[j]*lenght_scale, column_width, j*column_width, window.winfo_screenheight(), "green")
                        canvas_1.create_column(array[j-1]*lenght_scale, column_width, (j-1)*column_width, window.winfo_screenheight(), "green")
                    else:
                        canvas_1.create_column(array[j]*lenght_scale, column_width, j*column_width, window.winfo_screenheight(), "white")
                canvas.update()#ενημερώνει τον καμβά
        n += 1
    for i in range(len(array)):#οταν τελειώσει ο αλγόρθμος ξανασχεδιάζει με όλες τις σ΄τήλες άσπρες
        canvas_1.create_column(array[i]*lenght_scale, column_width, i*column_width, window.winfo_screenheight(), "white")


class Canvas():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        global canvas
        canvas = tk.Canvas(window, width=self.width, height = self.height, background="black")#δημουργεί τον καμβά
        canvas.pack(fill=tk.BOTH, expand=True)#ο καμβάς πρέπει να καταλαμβάνει ΄όλον τον διαθέσιμο χώρο
    def create_column(self, lenght, collumn_width_, bottom_left_point_x, bottom_left_point_y, collumn_color):
        self.lenght = lenght
        self.collumn_width = collumn_width_
        self.bottom_left_point_x = bottom_left_point_x
        self.bottom_left_point_y = bottom_left_point_y
        self.collumn_color = collumn_color
        canvas.create_rectangle(bottom_left_point_x + 10, bottom_left_point_y - 50, bottom_left_point_x + collumn_width_ - 10, bottom_left_point_y -50 - lenght, fill = collumn_color, outline = collumn_color)
        #το 50 υπάρχει για να μην σχεδιάζεται τίποτα κάτων από την μπάρα επιλογών που έχει πάχος 50
        #το 10 υπάρχει για το κενό μεταξύ των στηλών


window = tk.Tk()
window.attributes('-fullscreen', True)
options_frame = tk.Frame(width = window.winfo_screenwidth(), height=50)#frame για τις επιλογές χρήστη
options_frame.pack(fill="x", expand=True)
window.title("Bubble Sort Visualization")
canvas_1 = Canvas(window.winfo_screenwidth(), window.winfo_screenheight()-50)


def gui():
    start_button = tk.Button(options_frame, text="Start", command=sorting_algorithm)#κουμπί start
    global array_lenght_chooser
    array_lenght_chooser = tk.Scale(options_frame, from_ = 1, to = 50, orient= "horizontal", variable=array_lenght)#επιλέγει ο χρήστης το μέγεθος της λίστας
    array_lenght_chooser_label = tk.Label(options_frame, text="Array Lenght: ")#
    global time_interval
    time_interval = tk.Scale(options_frame, from_ = 1, to = 1000, orient="horizontal")#επιλέγει ο χρήστις το χρον διάστημα μεταξύ επαναλήψεων σε ms
    time_interval_label = tk.Label(options_frame, text="Time Interval(ms): ")
    options_frame.columnconfigure(0, weight=20)#ορίζονται οι αναλογίες στο grid για τα στοιχεία
    options_frame.columnconfigure(1, weight=1)
    options_frame.columnconfigure(2, weight=1)
    options_frame.columnconfigure(3, weight=1)
    options_frame.columnconfigure(4, weight=1)
    options_frame.rowconfigure(0, weight=1)

    start_button.grid(row=0, column=0, padx=10, sticky="w")# padding ώστε να ΄έχει απόσταση από τα όρια του παραθύρου
    array_lenght_chooser_label.grid(row=0, column=1, sticky="se")
    array_lenght_chooser.grid(row= 0, column=2, sticky="w")
    time_interval_label.grid(row=0, column=3, sticky="se")
    time_interval.grid(row=0, column=4, sticky="w")
    #sticky ώστε να είναι κατάλληλα στοιχισμένα τα scale και τα label
gui()
window.mainloop()
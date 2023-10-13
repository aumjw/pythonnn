import tkinter as tk
import random

#in Tk
window = tk.Tk()
window.title("Guess The number game!")
window.minsize(width=400 ,  height=400)

#condition
x = random.randint(1,5)
y = random.randint(1,5)
result = x + y
count = 0

def clicked_button():
    guess = int(Guess.get())
    global count # ใช้ global เพื่อแก้ปัญหาการไม่สามารถเข้าถึงตัวแปร count ในฟังก์ชัน
    output = ' '
    if count < 5: # ทายได้สูงสุด5ครั้ง
        if guess > result:
            output = "Too High!" #hints
            count += 1 #เมื่อตอบแล้วจะทำการบวกรอบ

        elif guess < result:
            output = "Too Low!"  #hint
            count +=1
        # ถ้าคำตอบถูก
        else:
            output = "Correct Congrat!" #เมื่อตอบแล้วคำตอบถูกต้อง
            button.config(state=tk.DISABLED)  # ปิดปุ่มหลังจากตอบถูก
            x_label.config(text="x = " + str(x)) #แสดงค่าบนหน้าgui when guess finished!
            y_label.config(text="y = " + str(y))
    else:
        output = "You lose!" #เมื่อครบรอบแล้วยังตอบไม่ถูก 
        button.config(state=tk.DISABLED)  # ปิดปุ่มหลังจากตอบถูก
        x_label.config(text="x = " + str(x))
        y_label.config(text="y = " + str(y))
    output_label.configure(text=output)
        
        

label = tk.Label(window, text="Enter your Guess number ?")
Guess = tk.Entry(window)
button = tk.Button(window,text="Clicked me !" ,command= clicked_button)
output_label = tk.Label(master=window)
x_label = tk.Label(window)
y_label = tk.Label(window)


label.pack()
Guess.pack()
button.pack()
output_label.pack()
x_label.pack()
y_label.pack()



window.mainloop()



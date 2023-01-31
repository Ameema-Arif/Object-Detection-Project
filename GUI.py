from tkinter import *
from PIL import ImageTk, Image
import cv2
import sys




class Main(object):
    bg_img = cv2.imread("E:\SE\SELabs\SEProject\OpenCVPractice\Main.png")
    
    
    def __init__(self,master):
        #self.master = master
        #master.title("Object Detection System")
        #master.configure(bg="black")
        #root = Tk()
        #root.title("Object Detection System")
        
        
        self.canv = Canvas(root)
        self.img = ImageTk.PhotoImage(Image.open("E:\SE\SELabs\SEProject\OpenCVPractice\Main.png"))
        self.canv.create_image(0,0, anchor=NW, image=self.img)
        self.canv.pack()
        #self.music=Main.music(self)

      
        
        self.play= Button(root, text="Use Camera", command=self.Camera,height=3,width=15)
        cam_button_window = self.canv.create_window(15, 15, anchor='nw', window=self.play)
        self.play.pack()
        
        self.instruction = Button(root, text="Choose Image from Directory",command=self.Directory,height=3,width=25)
        dir_button_window = self.canv.create_window(15, 15, anchor='nw', window=self.instruction)
        self.instruction.pack()

        self.done = Button(root, text="Done",command=self.Done,height=3,width=15)
        done_button_window = self.canv.create_window(15, 15, anchor='nw', window=self.done)
        self.done.pack()

        self.close_button = Button(root, text="EXIT", command=self.Exit,height=3,width=15)
        close_button_window = self.canv.create_window(15, 15, anchor='nw', window=self.close_button)
        self.close_button.pack()
   
    def Camera(self):
        import Camera
            #root.destroy()
            #root1=Tk()
            #root1.title("Camera")
            
            #self.canv = Canvas(root1)
            #self.img = PhotoImage(file=r"D:\Project\puzzle_main.png")
            #self.canv.create_image(0,0, anchor =CENTER, image=self.img)
            #self.canv.pack()
            #root1.configure(bg="black")
       
            #self.easy=Button(root1,text="EASY",command=self.Ease, height=3,width=15).pack()
            #self.medium=Button(root1,text="MEDIUM",command=self.Med,height=3,width=15).pack()
            #self.hard=Button(root1,text="HARD",command=self.Hard,height=3,width=15).pack()
            #cam = cv2.VideoCapture(0)

            #cv2.namedWindow("Camera")

            #img_counter = 0

            #while True:
                #ret, frame = cam.read()
                #cv2.imshow("Camera", frame)
                #if not ret:
                    #break
                #k = cv2.waitKey(1)

                #if k%256 == 27:
                    # ESC pressed
                    #print("Escape hit, closing...")
                    #break
                #elif k%256 == 32:
                    # SPACE pressed
                    #img_name = "opencv_frame_{}.png".format(img_counter)
                    #cv2.imwrite(img_name, frame)
                    #print("{} written!".format(img_name))
                    #cam.release()
                    #cv2.destroyAllWindows()
                    
                    

            #cam.release()

            #cv2.destroyAllWindows()
    
     
    def Done(self):
        return ""

    def Directory(self):
        return ""



    def Exit(self):
        quit()
        
        
    
root = Tk()
root.title("Object Detection System")
my_gui = Main(root)
root.mainloop


from tkinter import *
import instaloader
from tkinter import messagebox

insta=instaloader.Instaloader()

def download():
 username=entryField.get()
 insta.download_profile(username,profile_pic_only=True)
 messagebox.showinfo('Success','Profile Image is successfully downloaded')

root=Tk()  
root.title('Instagram Profile Pic Downloader')

logoImage=PhotoImage(file="D:\Screenshot__863_-removebg-preview.png")

logoLabel=Label(root,image=logoImage)
logoLabel.grid(pady=10)

titleLabel=Label(root,text='Instagram Profile Image Downloader',font=('Times New Roman',30,'bold'))
titleLabel.grid(row=1,column=0,pady=10,padx=30)

enterLabel=Label(root,text='Enter Username:',font=('arial',15,'bold'))
enterLabel.grid(row=2,column=0,pady=10)
entryField=Entry(root,width=40,font=('arial',15,'bold'),bd=5)
entryField.grid(row=3,column=0,pady=10)

downloadButton=Button(root,text='DOWNLOAD',font=('arial',15,'bold'),command=download)
downloadButton.grid(row=4,column=0,pady=10)
root.mainloop()

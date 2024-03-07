from tkinter import *
from tkinter import ttk

from PIL import Image,ImageTk

win=Tk()
win.geometry('1000x1000')
win.title("BITLY")
win.config(bg='white')
togle=True
url_frame=None 
qr_frame=None 
link_frame=None
analytics_frame=None 
bar_frame=None  

def products(e):
    
    heading_first.config(fg='blue',font=('Calibri',12,'underline'))
    url_image=Image.open('url.png')
    url_img1=url_image.resize((80,80))
    url_final=ImageTk.PhotoImage(url_image,master=win)
    # Function example
    def hide_frames():
        if url_frame is not None:
            exists=url_frame.winfo_exists()                
        
        
            if exists==1:
                for widget in url_frame.winfo_children():
                    widget.destroy()
                url_frame.place_forget()
        else:
            pass
        
    
    
    
    def url():
        hide_frames()
        url_frame=Frame(win,bg='white',width=1500,height=1500)
        url_frame.place(x=0,y=60)
        
        url_text=Label(url_frame,text='URL Shortener',bg='white',fg='black',font=("Arial",17))
        url_text.place(x=0,y=140)
        
        url_text1=Label(url_frame,text='Create memorable connections',bg='white',font=("Arial",22,'bold'))
        url_text1.place(x=0,y=190)
        
        url_text2=Label(url_frame,text='with our powerful URL shortener',bg='white',font=("Arial",22,'bold'))
        url_text2.place(x=0,y=230)
        
        url_text3=Label(url_frame,text='Spark instant connections with your audience using',bg='white',font=("Arial",15),fg='gray')
        url_text3.place(x=0,y=270)
        
        url_text4=Label(url_frame,text='trimmed, trustworthy, and trackable links within the Bitly',bg='white',font=("Arial",15),fg='gray')
        url_text4.place(x=0,y=300)
        
        url_text5=Label(url_frame,text='Connections Platform.',bg='white',font=("Arial",15),fg='gray')
        url_text5.place(x=0,y=330)
        
        url_btn_image=Image.open('free.png')
        url_btn_image1=ImageTk.PhotoImage(url_btn_image)
        
        
        url_btn=Button(url_frame,image=url_btn_image1,bd=0,bg='white',command=submit)
        url_btn.image=url_btn_image1
        url_btn.place(x=10,y=380)
        
        url_image=Image.open('url_image.png')
        url_image1=url_image.resize((500,500))
        url_final=ImageTk.PhotoImage(url_image1,master=url_frame)
        
        url_label=Label(url_frame,image=url_final)
        url_label.image=url_final
        url_label.place(x=700,y=140)
        
        
        
    def qr():
        hide_frames()
        qr_frame=Frame(win,bg='white',width=1500,height=1500)
        qr_frame.place(x=0,y=60)
        
        
        qr_text=Label(qr_frame,text='QR Codes',bg='white',fg='black',font=("Arial",17))
        qr_text.place(x=0,y=140)
        
        qr_text1=Label(qr_frame,text='Meet the Bitly QR Code Generator:',bg='white',font=("Arial",22,'bold'))
        qr_text1.place(x=0,y=190)
        
        qr_text2=Label(qr_frame,text='The simplest way to create and',bg='white',font=("Arial",22,'bold'))
        qr_text2.place(x=0,y=230)
        
        qr_text3=Label(qr_frame,text='track QR Codes',bg='white',font=("Arial",22,'bold'))
        qr_text3.place(x=0,y=270)
        
        qr_text4=Label(qr_frame,text='Generate a custom QR Code in seconds, share it with your',bg='white',font=("Arial",15),fg='gray')
        qr_text4.place(x=0,y=300)
        
        qr_text5=Label(qr_frame,text='audience, and instantly access your scan data — all inside',bg='white',font=("Arial",15),fg='gray')
        qr_text5.place(x=0,y=330)
        
        
        qr_text6=Label(qr_frame,text='the Bitly Connections Platform.',bg='white',font=("Arial",15),fg='gray')
        qr_text6.place(x=0,y=360)
        
        
        qr_btn_image=Image.open('free.png')
        qr_btn_image1=ImageTk.PhotoImage(qr_btn_image)
        
        
        qr_btn=Button(qr_frame,image=qr_btn_image1,bd=0,bg='white',command=submit)
        qr_btn.image=qr_btn_image1
        qr_btn.place(x=10,y=400)
        
        qr_image=Image.open('qr_image.png')
        qr_image1=qr_image.resize((500,500))
        qr_final=ImageTk.PhotoImage(qr_image1,master=qr_frame)
        
        qr_label=Label(qr_frame,image=qr_final)
        qr_label.image=qr_final
        qr_label.place(x=700,y=140)
        
        
        
        
        
    def link():
        hide_frames()
        link_frame=Frame(win,bg='white',width=1500,height=1500)
        link_frame.place(x=0,y=60)
        
        
        link_text=Label(link_frame,text='Link-in-bio',bg='white',fg='black',font=("Arial",17))
        link_text.place(x=0,y=140)
        
        link_text1=Label(link_frame,text='Make your social',bg='white',font=("Arial",22,'bold'))
        link_text1.place(x=0,y=190)
        
        link_text2=Label(link_frame,text='media profiles work',bg='white',font=("Arial",22,'bold'))
        link_text2.place(x=0,y=230)
        
        link_text3=Label(link_frame,text='harder',bg='white',font=("Arial",22,'bold'))
        link_text3.place(x=0,y=270)
        
        link_text4=Label(link_frame,text='Curate, organize, and track all your best links, so audiences',bg='white',font=("Arial",15),fg='gray')
        link_text4.place(x=0,y=300)
        
        link_text5=Label(link_frame,text='can discover and engage with more of your content.',bg='white',font=("Arial",15),fg='gray')
        link_text5.place(x=0,y=330)
        
        
        link_btn_image=Image.open('free.png')
        link_btn_image1=ImageTk.PhotoImage(link_btn_image)
        
        
        link_btn=Button(link_frame,image=link_btn_image1,bd=0,bg='white',command=submit)
        link_btn.image=link_btn_image1
        link_btn.place(x=10,y=400)
        
        link_image=Image.open('link_image.png')
        link_image1=link_image.resize((500,500))
        link_final=ImageTk.PhotoImage(link_image1,master=link_frame)
        
        link_label=Label(link_frame,image=link_final)
        link_label.image=link_final
        link_label.place(x=700,y=140)
        
    def analytics():
        hide_frames()
        analytics_frame=Frame(win,bg='white',width=1500,height=1500)
        analytics_frame.place(x=0,y=60)

        analytics_text=Label(analytics_frame,text='Analytics',bg='white',fg='black',font=("Arial",17))
        analytics_text.place(x=0,y=140)
        
        analytics_text1=Label(analytics_frame,text='Tap into click and scan',bg='white',font=("Arial",22,'bold'))
        analytics_text1.place(x=0,y=190)
        
        analytics_text2=Label(analytics_frame,text='data with Bitly Analytics',bg='white',font=("Arial",22,'bold'))
        analytics_text2.place(x=0,y=230)
        
        analytics_text3=Label(analytics_frame,text='Knowing how your short links and QR Codes are',bg='white',font=("Arial",15),fg='gray')
        analytics_text3.place(x=0,y=270)
        
        analytics_text4=Label(analytics_frame,text='performing should be as easy as making them. Track,',bg='white',font=("Arial",15),fg='gray')
        analytics_text4.place(x=0,y=300)
        
        analytics_text5=Label(analytics_frame,text='analyze, and optimize all your connections in one place.',bg='white',font=("Arial",15),fg='gray')
        analytics_text5.place(x=0,y=330)
        
        analytics_btn_image=Image.open('free.png')
        analytics_btn_image1=ImageTk.PhotoImage(analytics_btn_image)
        
        
        analytics_btn=Button(analytics_frame,image=analytics_btn_image1,bd=0,bg='white',command=submit)
        analytics_btn.image=analytics_btn_image1
        analytics_btn.place(x=10,y=380)
        
        analytics_image=Image.open('analytics_image.png')
        analytics_image1=analytics_image.resize((500,500))
        analytics_final=ImageTk.PhotoImage(analytics_image1,master=analytics_frame)
        
        analytics_label=Label(analytics_frame,image=analytics_final)
        analytics_label.image=analytics_final
        analytics_label.place(x=700,y=140)
        




    def bar():
        hide_frames()
        bar_frame=Frame(win,bg='white',width=1500,height=1500)
        bar_frame.place(x=0,y=60)
        
        
        bar_text=Label(bar_frame,text='2D BarCodes',bg='white',fg='black',font=("Arial",17))
        bar_text.place(x=0,y=140)

        bar_text1=Label(bar_frame,text='Enhance consumer knowledge',bg='white',font=("Arial",22,'bold'))
        bar_text1.place(x=0,y=190)

        bar_text2=Label(bar_frame,text='and scannability with 2D',bg='white',font=("Arial",22,'bold'))
        bar_text2.place(x=0,y=230)

        bar_text3=Label(bar_frame,text='Barcodes',bg='white',font=("Arial",22,'bold'))
        bar_text3.place(x=0,y=270)

        bar_text4=Label(bar_frame,text='Add a Global Trade Item Number (GTIN) to QR Codes',bg='white',font=("Arial",15),fg='gray')
        bar_text4.place(x=0,y=300)

        bar_text5=Label(bar_frame,text='designed for product labels and packaging.',bg='white',font=("Arial",15),fg='gray')
        bar_text5.place(x=0,y=330)


        bar_btn_image=Image.open('free.png')
        bar_btn_image1=ImageTk.PhotoImage(bar_btn_image)


        bar_btn=Button(bar_frame,image=bar_btn_image1,bd=0,bg='white',command=submit)
        bar_btn.image=bar_btn_image1
        bar_btn.place(x=10,y=380)

        bar_image=Image.open('bar_image.png')
        bar_image1=bar_image.resize((500,500))
        bar_final=ImageTk.PhotoImage(bar_image1,master=bar_frame)

        bar_label=Label(bar_frame,image=bar_final)
        bar_label.image=bar_final
        bar_label.place(x=700,y=140)
        
    icon1=Image.open('url.png')
    icon_resize=icon1.resize((30,30))
    icon_final=ImageTk.PhotoImage(icon_resize)
    
    qr1=Image.open('qr.jpg')
    qr_resize=qr1.resize((30,30))
    qr_final=ImageTk.PhotoImage(qr_resize)
    
    link1=Image.open('link.png')
    link_resize=link1.resize((30,30))
    link_final=ImageTk.PhotoImage(link_resize)
    
    analytics1=Image.open('analytics.jpg')
    analytics_resize=analytics1.resize((30,30))
    analytics_final=ImageTk.PhotoImage(analytics_resize)
    
    bar1=Image.open('bar.png')
    bar_resize=bar1.resize((30,30))
    bar_final=ImageTk.PhotoImage(bar_resize)
        
    
    popup = Menu(win, tearoff=0,activeforeground='blue',activebackground='white',bg='white',bd=10,font=("Calibri",17))
    
    popup.add_command(label="  URL Shortener",image=icon_final, compound='left',command=url)# , command=next) etc...
    popup.icon_final=icon_final
    
    popup.add_command(label="  QR Codes",image=qr_final,compound='left',command=qr)
    popup.qr_final=qr_final
    
    popup.add_command(label="  Link-in-bio",image=link_final,compound='left',command=link)
    popup.link_final=link_final
    
    popup.add_command(label="  Analytics",image=analytics_final,compound='left',command=analytics)
    popup.analytics_final=analytics_final
    
    popup.add_command(label="  2D-Bar codes",image=bar_final,compound='left',command=bar)
    popup.bar_final=bar_final
    
    
    def do_popup(event):

        try:
            popup.tk_popup(event.x_root, event.y_root+25, 0)
        finally:
            popup.grab_release()

    heading_first.bind("<Enter>", do_popup)

  
def submit():
    
    text1_label.config(text='')
    text2_label.config(text='')
    text3_label.config(text='')
    text4_label.config(text='')
    text5_label.config(text='')
    text6_label.config(text='')
    image_label.place_forget()
    submit_btn.place_forget()
    quote_btn.place_forget()
    
      
    def toggle():
        global togle
        if togle==True:
            toggle_button.config(image=toggle_btn_img2)
                      
            frame_big_second_text.config(bg='grey')
            frame_big_second.config(bg='grey')
            frame_small_second_text1.config(fg='grey')
            frame_small_second_text2.config(text='Annual plan only',font=("Arial",12))
            frame_small_second_text3.config(text='')
            frame_small_second_text4.config(text='')
            frame_small_second_text5.config(fg='grey')
            frame_small_second_text6.config(fg='grey')
            frame_small_second_text7.config(fg='grey')
            start_btn2.config(state='disabled',bg='grey',fg='white')
            start_btn2.unbind('<Enter>')
            start_btn2.unbind('<Leave>')
            frame_third_text2.config(text='$35')
            frame_third_text3_1.config(text='')
            frame_fourth_text2.config(text='$300')
            frame_fourth_text3_1.config(text='')
            
            togle=False
            
        else:
            
            toggle_button.config(image=toggle_btn_img)
            
            frame_big_second_text.config(bg='black')
            frame_big_second.config(bg='black')
            frame_small_second_text1.config(fg='black')
            frame_small_second_text2.config(text='$8',font=("Arial",22,'bold'))
            frame_small_second_text3.config(text='/month')
            frame_small_second_text4.config(text='(annual charge of $96)')
            frame_small_second_text5.config(fg='black')
            frame_small_second_text6.config(fg='black')
            frame_small_second_text7.config(fg='black')
            start_btn2.config(state='normal',bg='blue',fg='white')
            start_btn2.bind("<Enter>",lambda e: start_btn2.config(bg='dark blue'))
            start_btn2.bind("<Leave>",lambda e: start_btn2.config(bg='blue'))
            frame_third_text2.config(text='$29')
            frame_third_text3_1.config(text='(annual charge of $348)')
            frame_fourth_text2.config(text='$199')
            frame_fourth_text3_1.config(text='(annual charge of $2,388)')
            
            
  
            togle=True
            
            
    
    price1_label=Label(win,text='Pricing for brands and businesses of all sizes',font=('Aharoni',30,'bold'),bg='white')
    price1_label.place(x=20,y=80)
    
    price2_label=Label(win,text='Connect to your audience with branded links, QR Codes, and a Link-in-bio that will get their attention.',font=("Calibri",17),bg='white')
    price2_label.place(x=20,y=140)
    
    frame1=Frame(win,bg='gray98',bd=0,width=1350,height=500)
    frame1.place(x=0,y=200)
    
    
    
    save_label=Label(frame1,bg='gray98',text='Save up to 34% when you pay annually',font=("Arial",12))
    save_label.place(x=10,y=20)
    
    monthly_label=Label(frame1,bg='gray98', text='Monthly',font=("Arial",12))
    monthly_label.place(x=10,y=50)
    
    toggle_btn1=Image.open('toggle_on.png')
    toggle_btn1=toggle_btn1.resize((60,30))
    toggle_btn_img=ImageTk.PhotoImage(toggle_btn1)
    
    toggle_btn2=Image.open('toggle_off.png')
    toggle_btn2=toggle_btn2.resize((60,30))
    toggle_btn_img2=ImageTk.PhotoImage(toggle_btn2)
    
    toggle_button=Button(frame1,bd=0,bg='gray98',image=toggle_btn_img,command=toggle)
    toggle_button.image=toggle_btn_img
    toggle_button.place(x=90,y=50)
    
    annually_label=Label(frame1,bg='gray98', text='Annually',font=("Arial",12))
    annually_label.place(x=180,y=50)  
    
    # First Frame
    
    frame_first=Frame(frame1,width=200,bd=5,highlightthickness=5,height=300,bg='white')
    frame_first.place(x=30,y=100)
    
    frame_first_text1=Label(frame_first,text='FREE',font=("Arial",22),bg='white')
    frame_first_text1.place(x=50,y=10)
    
     
    frame_first_text2=Label(frame_first,text='$0',font=("Arial",22,'bold'),bg='white')
    frame_first_text2.place(x=45,y=50)  
    
    frame_first_text3=Label(frame_first,text='/month',font=("Arial",12),bg='white')
    frame_first_text3.place(x=95,y=60)
    
    frame_first_text4=Label(frame_first,text='2 QR Codes/month',font=("Arial",10),bg='white')
    frame_first_text4.place(x=20,y=100)
    
    frame_first_text5=Label(frame_first,text='10 links/month',font=("Arial",10),bg='white')
    frame_first_text5.place(x=30,y=120)
    
    frame_first_text6=Label(frame_first,text='1 Link-in-bio page',font=("Arial",10),bg='white')
    frame_first_text6.place(x=25,y=140)
    
    start_btn=Button(frame_first,text='Get Started',width=20,height=2,fg='blue',bg='lightsteelblue1',bd=0)
    start_btn.place(x=10,y=200)
    
    start_btn.bind("<Enter>",lambda e: start_btn.config(bg='lightskyblue'))
    start_btn.bind("<Leave>",lambda e: start_btn.config(bg='lightsteelblue1'))
    
    # Second Frame
    
    frame_big_second = Frame(frame1,bg='black',width=200,height=325,bd=5,highlightthickness=5,)
    frame_big_second.place(x=280,y=75)
    
    frame_big_second_text=Label(frame_big_second,bg='black',text="MOST POPULAR",fg='white',font=("Arial",15,'bold'))
    frame_big_second_text.place(x=10,y=0)
    
    # Second small frame
    
    frame_small_second=Frame(frame_big_second,width=180,height=275,bg='white')
    frame_small_second.place(x=0,y=30)
    
    frame_small_second_text1=Label(frame_small_second,text='CORE',font=("Arial",22),bg='white')
    frame_small_second_text1.place(x=50,y=10)
    
    frame_small_second_text2=Label(frame_small_second,text='$8',font=("Arial",22,'bold'),bg='white')
    frame_small_second_text2.place(x=45,y=50)
    
    frame_small_second_text3=Label(frame_small_second,text='/month',font=("Arial",12),bg='white')
    frame_small_second_text3.place(x=95,y=60)
    
    frame_small_second_text4=Label(frame_small_second,text='(annual charge of $96)',font=("Arial",10),bg='white')
    frame_small_second_text4.place(x=35,y=80)
    
    frame_small_second_text5=Label(frame_small_second,text='5 QR Codes/month',font=("Arial",10),bg='white')
    frame_small_second_text5.place(x=20,y=130)
    
    frame_small_second_text6=Label(frame_small_second,text='100 links/month',font=('Arial',10),bg='white')
    frame_small_second_text6.place(x=30,y=150)
    
    frame_small_second_text7=Label(frame_small_second,text='1 Link-in-bio page',font=("Arial",10),bg='white')
    frame_small_second_text7.place(x=25,y=170)
    
    
    start_btn2=Button(frame_small_second,text='Get Started',width=20,height=2,fg='white',bg='blue',bd=0)
    start_btn2.place(x=10,y=200)
    
    start_btn2.bind("<Enter>",lambda e: start_btn2.config(bg='dark blue'))
    start_btn2.bind("<Leave>",lambda e: start_btn2.config(bg='blue'))
    
    
    # Third Frame
    
    frame_third=Frame(frame1,width=200,bd=5,highlightthickness=5,height=300,bg='white')
    frame_third.place(x=520,y=100)
    
    frame_third_text1=Label(frame_third,text='GROWTH',font=("Arial",22),bg='white')
    frame_third_text1.place(x=30,y=10)
         
    frame_third_text2=Label(frame_third,text='$29',font=("Arial",22,'bold'),bg='white')
    frame_third_text2.place(x=45,y=50)  
    
    frame_third_text3=Label(frame_third,text='/month',font=("Arial",12),bg='white')
    frame_third_text3.place(x=95,y=60)
        
    frame_third_text3_1=Label(frame_third,text='(annual charge of $348)',font=("Arial",10),bg='white')
    frame_third_text3_1.place(x=35,y=80)
        
    frame_third_text4=Label(frame_third,text='10 QR Codes/month',font=("Arial",10),bg='white')
    frame_third_text4.place(x=20,y=130)
    
    frame_third_text5=Label(frame_third,text='500 links/month',font=("Arial",10),bg='white')
    frame_third_text5.place(x=30,y=150)
    
    frame_third_text6=Label(frame_third,text='2 Link-in-bio page',font=("Arial",10),bg='white')
    frame_third_text6.place(x=25,y=170)
    
    start_btn3=Button(frame_third,text='Get Started',width=20,height=2,fg='blue',bg='lightsteelblue1',bd=0)
    start_btn3.place(x=10,y=200)
    
    start_btn3.bind("<Enter>",lambda e: start_btn3.config(bg='lightskyblue'))
    start_btn3.bind("<Leave>",lambda e: start_btn3.config(bg='lightsteelblue1'))
    
    # Fourth Button
    
    frame_fourth=Frame(frame1,width=200,bd=5,highlightthickness=5,height=300,bg='white')
    frame_fourth.place(x=750,y=100)
    
    frame_fourth_text1=Label(frame_fourth,text='PREMIUM',font=("Arial",22),bg='white')
    frame_fourth_text1.place(x=30,y=10)
         
    frame_fourth_text2=Label(frame_fourth,text='$199',font=("Arial",22,'bold'),bg='white')
    frame_fourth_text2.place(x=30,y=50)  
    
    frame_fourth_text3=Label(frame_fourth,text='/month',font=("Arial",12),bg='white')
    frame_fourth_text3.place(x=95,y=60)
        
    frame_fourth_text3_1=Label(frame_fourth,text='(annual charge of $2,388)',font=("Arial",10),bg='white')
    frame_fourth_text3_1.place(x=25,y=80)
        
    frame_fourth_text4=Label(frame_fourth,text='200 QR Codes/month',font=("Arial",10),bg='white')
    frame_fourth_text4.place(x=20,y=130)
    
    frame_fourth_text5=Label(frame_fourth,text='3,000 links/month',font=("Arial",10),bg='white')
    frame_fourth_text5.place(x=30,y=150)
    
    frame_fourth_text6=Label(frame_fourth,text='5 Link-in-bio page',font=("Arial",10),bg='white')
    frame_fourth_text6.place(x=25,y=170)
    
    start_btn4=Button(frame_fourth,text='Get Started',width=20,height=2,fg='blue',bg='lightsteelblue1',bd=0)
    start_btn4.place(x=10,y=200)
    
    start_btn4.bind("<Enter>",lambda e: start_btn4.config(bg='lightskyblue'))
    start_btn4.bind("<Leave>",lambda e: start_btn4.config(bg='lightsteelblue1'))
    
    
title_label=Label(win,bg='white', text='Bitly', font=("Ink Free",23,'bold'),fg='orange')
title_label.place(x=20,y=10)

text1_label=Label(win,bg='white', text='Build stronger digital',font=("Aharoni",25,'bold'))
text1_label.place(x=20,y=80)

text2_label=Label(win, bg='white',text='connections',font=("Aharoni",25,'bold'),fg='orange')
text2_label.place(x=20,y=120)

text3_label=Label(win, bg='white',text='Use our URL shortener, QR Codes, and Link-in-bio pages',font=("Calibri",20))
text3_label.place(x=20,y=160)

text4_label=Label(win, bg='white',text='to engage your audience and connect them to the right',font=("Calibri",20))
text4_label.place(x=20,y=200)

text5_label=Label(win,bg='white', text='information. Build, edit, and track everything inside the',font=("Calibri",20))
text5_label.place(x=20,y=240)

text6_label=Label(win,bg='white', text='Bitly Connections Platform.',font=("Calibri",20))
text6_label.place(x=20,y=280)

heading_first=Label(win,bg='white',text="Products", fg='black',font=("Calibri",12))
heading_first.place(x=400,y=10)

heading_second=Button(win,bd=0,activebackground='white',bg='white',cursor='hand2',text="Pricing", fg='black',font=("Calibri",12),command=submit)
heading_second.place(x=550,y=10)

heading_third=Button(win,bd=0,activebackground='white',bg='white',cursor='hand2',text="Resources", fg='black',font=("Calibri",12))
heading_third.place(x=700,y=10)


heading_first.bind("<Enter>",products)
heading_first.bind("<Leave>",lambda e: heading_first.config(fg='black',font=('Calibri',12)))


#heading_first.bind("<Enter>",lambda e: heading_first.config(fg='blue',font=('Calibri',12,'underline')))
#heading_first.bind("<Leave>",lambda e: heading_first.config(fg='black',font=('Calibri',12)))
              

heading_second.bind("<Enter>",lambda e: heading_second.config(fg='blue',font=('Calibri',12,'underline')))
heading_second.bind("<Leave>",lambda e: heading_second.config(fg='black',font=('Calibri',12)))


heading_third.bind("<Enter>",lambda e: heading_third.config(fg='blue',font=('Calibri',12,'underline')))
heading_third.bind("<Leave>",lambda e: heading_third.config(fg='black',font=('Calibri',12)))


image1=Image.open('bitly.png')
image_size=image1.resize((500,500))
image_final=ImageTk.PhotoImage(image_size,master=win)

image2=Image.open('bitly_submit.png')
image2_final=ImageTk.PhotoImage(image2,master=win)

image_label=Label(win,image=image_final)
image_label.place(x=700,y=80)

submit_btn=Button(win,image=image2_final,bg='white',bd=0,command=submit)
submit_btn.place(x=20,y=340)

quote_btn=Button(win,text='Get a Quote',bg='white',cursor='hand2',fg='blue',bd=0,font=("Arial",12),activebackground='white')
quote_btn.place(x=90,y=430)

win.mainloop()

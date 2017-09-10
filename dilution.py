#!/usr/bin/python3


'''
----------------------------------------------------------------------
Name: dilution.py
Purpose: Calculate how much reagent and water are needed to dilute reagent grade acids and bases
to various molarities

Author: John Duchek, john.duchek@asemonline.org

Created:   long time ago
Last Updated:  Sept 5, 2017
Copyright: In the public domain

 Version 0.10
 
# -*- coding: utf-8 -*-


'''

from tkinter import *
import string
global molarity
global reagname
class App:
    def __init__(self,reagent):
        self.reagent=reagent
        self.create_widgets()
        
        
    def create_widgets(self):
        
        self.l1=Label(self.reagent,font=14,text="Common Acids").grid(row=0,column=0)
        self.l2=Label(self.reagent,font=14,text="Common Bases").grid(row=0,column=1)
        self.l3=Label(self.reagent,font=14,text="mLs required: ").grid(row=1,column=3)
        self.l4=Label(self.reagent,font=14,text="Molarity desired: ").grid(row=3,column=3)
        self.ans=Label(self.reagent,font=14,text="Take ").grid(row=5,column=3)
        self.ans1=Label(self.reagent,font=14,text="      ",bg="white").grid(row=5,column=4)
        self.ans2=Label(self.reagent,font=14,text="mLs of reagent.",anchor="w").grid(row=5,column=5)
        self.ans3=Label(self.reagent,font=14,text="Dilute to: ").grid(row=6,column=3)
        self.ans4=Label(self.reagent,font=14,text="      ",bg="white").grid(row=6,column=4)
        self.ans=Label(self.reagent,font=14,text="mLs final volume.   ",anchor="w").grid(row=6,column=5)

        
        answer=StringVar(self.ans)
        self.b1=Button(self.reagent,text="Quit",fg="red",
            command=self.reagent.quit)
        self.b1.grid(row=0,column=3)
        self.mLs=Entry(self.reagent)
        self.mLs.grid(row=1,column=4)
        ml=DoubleVar(self.mLs)
        self.desired_M=Entry(self.reagent)
        self.desired_M.grid(row=3,column=4)
        dMolar=DoubleVar(self.desired_M)
        
        #acids
        self.acetic=Button(self.reagent,height=1,width=40,text="Acetic Acid glacial (100%...17.4M)",
        bg="pink",command=self.ac)
        self.acetic.grid(row=1,column=0)
        
           
        self.HF=Button(self.reagent,height=1,width=40,text="Hydrofluoric Acid (50%...25.7M)",
        bg="pink",command=self.hf)
        self.HF.grid(row=2,column=0)
        
        
        self.HCl=Button(self.reagent,height=1,width=40,text="Hydrochloric Acid (37%...12.1M)",
        bg="pink",command=self.hcl)
        self.HCl.grid(row=3,column=0)
        
        
        self.HBr=Button(self.reagent,height=1,width=40,text="Hydrobromic Acid (48%...8.8M)",
        bg="pink",command=self.hbr)
        self.HBr.grid(row=4,column=0)
        
        
        self.HI=Button(self.reagent,height=1,width=40,text="Hydroiodic Acid (47%...5.5M)",
        bg="pink",command=self.hi)
        self.HI.grid(row=5,column=0)
        
        
        self.HNO3=Button(self.reagent,height=1,width=40,text="Nitric Acid (70%...15.4M)",
        bg="pink",command=self.hno3)
        self.HNO3.grid(row=6,column=0)
     
        
        self.HClO4=Button(self.reagent,height=1,width=40,text="Perchloric Acid (70%...11.6M)",
        bg="pink",command=self.hclo4 )
        self.HClO4.grid(row=7,column=0)
      

        self.H3PO4=Button(self.reagent,height=1,width=40,text="Phosphoric Acid (85%...14.7M)",
        bg="pink",command=self.hpo4 )
        self.H3PO4.grid(row=8,column=0)
     
        
        self.H2SO4=Button(self.reagent,height=1,width=40,text="Sulfuric Acid (100%...17.6M)",
        bg="pink",command=self.hso4)
        self.H2SO4.grid(row=9,column=0)
      
        
        #bases
        self.ammonia=Button(self.reagent,height=1,width=40,text="Aqueous Ammonia (29%...14.8M)",
        bg="lightblue",command=self.nh3)
        self.ammonia.grid(row=1,column=1)
     
        
        self.NaOH=Button(self.reagent,height=1,width=40,text="Sodium Hydroxide (50%...19.1M)",
        bg="lightblue",command=self.naoh)
        self.NaOH.grid(row=2,column=1)
        
        self.KOH=Button(self.reagent,height=1,width=40,text="Potassium Hydroxide (45%...11.7M)",
        bg="lightblue",command=self.koh)
        self.KOH.grid(row=3,column=1)
        
        self.Me4NOH=Button(self.reagent,height=1,width=40,text="Tetramethylammonium Hydroxide (25%...2.4M)",
        bg="lightblue",command=self.me4noh)
        self.Me4NOH.grid(row=4,column=1)
        
        self.Et4NOH=Button(self.reagent,height=1,width=40,text="Tetraethylammonium Hydroxide (35%...2.43M)",
        bg="lightblue",command=self.me4noh)
        self.Et4NOH.grid(row=5,column=1)
        
        self.Bu4NOH=Button(self.reagent,height=1,width=40,text="Tetrabutylammonium Hydroxide (40%...1.57M)",
        bg="lightblue",command=self.me4noh)
        self.Bu4NOH.grid(row=6,column=1)

    def ac(self):
        reagname="HOAc    "
        self.calculate(17.4,reagname)
    def hf(self):
        reagname="HF      "
        self.calculate(25.7,reagname)
    def hcl(self):
        reagname="HCl     "
        self.calculate(12.1,reagname)
    def hbr(self):
        reagname="HBr     "
        self.calculate(8.8,reagname)
    def hi(self):
        reagname="HI      "
        self.calculate(5.5,reagname)
    def hno3(self):
        reagname="HNO3    "
        self.calculate(15.4,reagname)
    def hclo4(self):
        reagname="HClO4   "
        self.calculate(11.6,reagname)
    def hpo4(self):
        reagname="HPO4    "
        self.calculate(14.7,reagname)
    def hso4(self):
        reagname="H2SO4   "
        self.calculate(17.6,reagname)
        
    def nh3(self):
        reagname="NH3     "
        self.calculate(14.8,reagname)
    def naoh(self):
        reagname="NaOH    "
        self.calculate(19.1,reagname)
    def koh(self):
        reagname="KOH     "
        self.calculate(11.7,reagname)    
    def me4noh(self):
        reagname="Me4NOH  "
        self.calculate(2.4,reagname)
    def et4noh(self):
        reagname="Et4NOH  "
        self.calculate(2.43,reagname)
    def bu4noh(self):
        reagname="Bu4NOH  "
        self.calculate(1.57,reagname)
    
        
                                
    def calculate(self,molarity,reagname):
        ml=self.mLs.get()
        dMolar=self.desired_M.get()
        #if dMolar>molarity:
            #return
        #moles_needed=string.atof(dMolar)*(string.atof(ml)/1000)
        moles_needed=float(dMolar)*float(ml)/1000
        mls_needed=(moles_needed/float(molarity))*1000
        answer='%3.2f'%mls_needed
        phrase="  mLs of "+reagname
        
        self.ans1=Label(self.reagent,font=14,text=str(answer),bg="white",anchor="w").grid(row=5,column=4)

        self.ans2=Label(self.reagent,font=14,text=phrase,anchor="w").grid(row=5,column=5)

        self.ans4=Label(self.reagent,font=14,text=ml,bg="white",anchor="w").grid(row=6,column=4)

        
if __name__=='__main__':
    root=Tk()
    app=App(root)
    root.title("Dilution")
    root.mainloop()

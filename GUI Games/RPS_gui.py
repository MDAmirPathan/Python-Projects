import random
from tkinter import * 




img_list = ['Rock.png','Paper.png','sci.png']
rps_list = ['Rock','Paper','Scissor']

comp_score=0
player_score=0
def reset():
	global comp_score,player_score
	comp_score = 0
	player_score =0
	cwin_score['text'] = str(comp_score)
	pwin_score['text'] = str(player_score)
	rf['bg'] = 'pink'
	scif['bg'] = 'pink'
	pf['bg'] = 'pink'

	clabel['text'] = ''


def game(w):
	global comp_score,player_score
	computer_choice = random.choice(rps_list)
	clabel['text'] = computer_choice
	if w=='Rock':
		rf['bg'] = 'green'
		scif['bg'] = 'pink'
		pf['bg'] = 'pink'
	elif w=='Paper':
		rf['bg'] = 'pink'
		scif['bg'] = 'pink'
		pf['bg'] = 'green'
		
	else:
		rf['bg'] = 'pink'
		scif['bg'] = 'green'
		pf['bg'] = 'pink'



	if computer_choice == 'Rock' and w == 'Scissor':
		print("Computer win")
		comp_score = comp_score + 1
		cwin_score['text'] = str(comp_score)
	elif computer_choice == 'Paper' and w=='Rock':
		print('Computer Win')
		comp_score = comp_score + 1
		cwin_score['text'] = str(comp_score)
	elif computer_choice == 'Scissor' and w=='Paper':
		print('Computer WIn')
		comp_score = comp_score + 1
		cwin_score['text'] = str(comp_score)
	elif w==computer_choice:
		print('Tie')
	else:
		print('Player Won')
		player_score = player_score + 1
		pwin_score['text'] = str(player_score)
 


root = Tk()
root.title('Rock Paper Scissor')

canvas =Canvas(root,height=400,width=600)
canvas.pack()


#Player Choides

#scissor
scif = Frame(root,height=20,width=120,bg="pink")
scif.place(x=20,y=130)
simg = PhotoImage(file = 'sci.png')
smaller_simage = simg.subsample(12, 12)   
s = Label(root,image= smaller_simage,height = 120,width = 120,text = 'Image')
s.place(x=20,y=150)

#rock
rf = Frame(root,height=20,width=120,bg="pink")
rf.place(x=140,y=130)
rimg = PhotoImage(file = 'Rock.png')
smaller_rimage = rimg.subsample(10, 10)   
r = Label(root,image= smaller_rimage,height = 120,width = 120,text = 'Image')
r.place(x=140,y=150)


#paper

pf = Frame(root,height=20,width=120,bg="pink")
pf.place(x=260,y=130)
pimg = PhotoImage(file = 'Paper.png')
smaller_pimage = pimg.subsample(10, 10)   
p = Label(root,image= smaller_pimage,height = 120,width = 120,text = 'Image')
p.place(x=260,y=150)

#Computer Frame
cframe = Frame(root,height = 60,width=120)
cframe.place(x=400,y=150)
c = Label(cframe,text= 'Computer Coice',height = 30,width = 120)
c.place(rely=0,relheight=0.5,relwidth=1)
clabel = Label(cframe,text='',height = 30,width = 120)
clabel.place(rely=0.5,relheight=0.5,relwidth=1)


#Buttons
bframe = Frame(root,height=100,width=200)
bframe.place(x=100,y=300)
brock = Button(bframe,text='Rock',bg='grey',command = lambda:game('Rock'))
brock.place(relwidth=0.5, relheight=0.5)
bpaper = Button(bframe,text='Paper',bg='white',command =lambda:game('Paper'))
bpaper.place(x=100,relwidth=0.5, relheight=0.5)
bscissor = Button(bframe,text='Scissor',bg='cyan',command =lambda :game('Scissor'))
bscissor.place(y=50,relwidth=1, relheight=0.5)

#rest button
resetb = Button(root,text="Reset",command = reset)
resetb.pack(side='top')


#Score
sframe = Frame(root,height=100,width =200,bg='pink')
sframe.place(x=350,y=300)
cwin_label = Label(sframe,text = 'Computer Score:',height = 50,width = 200)
cwin_label.place(rely=0,relheight=0.5,relwidth=0.5)

cwin_score = Label(sframe,text='0', height=50,width = 200)
cwin_score.place(relx=0.5,relheight= 0.5,relwidth = 0.5)

pwin_score = Label(sframe,text='0', height=50,width = 200)
pwin_score.place(relx=0.5,rely=0.5,relheight= 0.5,relwidth = 0.5)

pwin = Label(sframe,text='Player Score:',height = 50,width=200)
pwin.place(rely=0.5,relheight=0.5,relwidth=0.5)







root.mainloop()
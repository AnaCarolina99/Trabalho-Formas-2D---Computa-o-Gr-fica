"""
 * @author Ana Carolina Medeiros Gonçalves 
 * @date:15/03/21
 * Matricula: 591513
"""

#biblioteca responsavel pela criacao da interface  
from tkinter import* 

#Lista para armazenar as coordenadas de um retangulo e repassar para as transformaçoes geometricas 
ret =[]
#Lista para armazenar as coordenadas de um circulo e repassar para as transformaçoes geometricas 
circle = []
#Lista para armazenar as coordenadas do Bresnham e repassar para as transformaçoes geometricas 
listBres = []
#Lista para armazenar as coordenadas do DDA e repassar para as transformaçoes geometricas 
listDda = []

listLiang = []


#Inicializando a interface do Canvas
my_window = Tk()
my_window.title("Trabalho Prático - Computação Gráfica")
my_window.geometry("1366x720")
my_canvas = Canvas(my_window, width=1366,height=720,background='white')


#Funcao responsavel por arredondar os valores dos pontos da reta
def ROUND(a):
	return int(a + 0.5)

#Função resposável por calcular os pontos de DDA e printar a reta(s) obtida
def criarLinhaDDA(event):
	global click_dda
	global xDDA,yDDA
	if click_dda == 0:
		xDDA=event.x
		yDDA=event.y
		click_dda=1
	else:
		#algoritmo DDA
		x2=event.x
		y2=event.y
		x,y = xDDA,yDDA
		length = abs((x2-xDDA) if abs(x2-xDDA) > abs(y2-yDDA) else (y2-yDDA))
		dx = (x2-xDDA)/float(length)
		dy = (y2-yDDA)/float(length)
		my_canvas.create_oval(x,y,x,y,fill='black',width=5) #desenha o primeiro ponto na tela
		for i in range(length):
			x += dx
			y += dy
			my_canvas.create_oval(x,y,x,y,fill='black',width=5) #desenha os pontos seguintes
		click_dda=0

		listDda2 = []
		listDda2 = [x,y, x,y]
		listDda.append(listDda2)	

#Função resposável por chamar a função "criarLinhaDDA" e habilitar a função de cliques na tela
def printLinhaDDA():
	my_canvas.bind('<Button-1>', criarLinhaDDA)
	my_canvas.grid(row=1,column=1)


#Função resposável por receber os valores do Bressnham e printar os valores na tela
def criarLinhaBres(event):
	#drawDDA(x1,x2,x3,x5)
	x_ini = 0 
	x_final = 0
	y_ini = 0
	y_final = 0

	global click_Bres
	global xBres,yBres

	if click_Bres == 0:
		xBres=event.x
		yBres=event.y
		click_Bres=1

	else:
		#algoritmo Bresnenhams
		dx = x_final-x_ini
		dy = y_final-y_ini

		D = 2*dy - dx
		y = y_ini

		for x in range(x_ini+1,x_final+1):
			if D > 0:
				y += 1
				D += (2*dy-2*dx)
			else:
				D += 2*dy

		x1=event.x
		y1=event.y
		my_canvas.create_line(xBres,yBres,x1,y1,fill='black',width=5)#desenha os pontos seguintes
		click_Bres=0

		listBres2 = []
		listBres2 = [xBres,yBres, x1,y1]
		listBres.append(listBres2)

#Função resposável por chamar a função "criarLinhaDDA" e habilitar a função de cliques na tela
def printLinhaBres():
	my_canvas.bind('<Button-1>', criarLinhaBres)
	
	my_canvas.grid(row=1,column=1)

#Função resposável por receber os valores do retangulo e printar na tela
def criarRetangulo(event):
	global click_Ret
	global xRet,yRet

	if click_Ret == 0:
		xRet=event.x
		yRet=event.y
		click_Ret=1
	else:
		x1=event.x
		y1=event.y
		my_canvas.create_rectangle(xRet,yRet,x1,y1,fill='black',width=5)#desenha os pontos de acordo com os cliques
		click_Ret=0

		ret2=[]
		ret2 = [xRet,yRet, x1,y1]
		ret.append(ret2)

#Função resposável por chamar a função "criarRetangulo" e habilitar a função de cliques na tela
def printRetangulo():
	my_canvas.bind('<Button-1>', criarRetangulo)
	my_canvas.grid(row=1,column=1)

#Algoritmo do Bres circle que pega as coordenadas do ponto e retorna as coordenadas da circunferencia
def bresCircle(x, y, raio):
	
	xFinal = 0
	yFinal = 0

	ponto = 0 
	raio = 0 
	raioFinal = 1-raio

	listC = []
	listC.append(x)
	listC.append(y)

	for x in range(int(raio)):

		if ponto < 0:
			ponto = ponto + 2 * x + 3
		else:
			y -= 1
			ponto = ponto + 2 * x + 3 - 2 * y

			listC.append(xFinal)
			listC.append(yFinal)

		if x >= y: break

	listN = listC[:]

	for i in listC:
		listN.append((i[1], i[0]))

	listC = listN[:]

	listL = listC[:]

	for i in listN:
		listL.append((-i[0], i[1]))
		listL.append((i[0], -i[1]))
		listL.append((-i[0], -i[1]))

	listP = []

	for i in listL:
		listP.append((x+i[0], y+i[1]))

	return listP

#Função resposável por receber os valores da circunferencia e printar na tela
def criarCircle(event):
	global click_Circle
	global xCircle,yCircle
	#bresCircle(x1,y1,xCircle)

	if click_Circle == 0:
		xCircle=event.x
		yCircle=event.y
		click_Circle=1
	else:
		x1=event.x
		y1=event.y


		my_canvas.create_oval(xCircle,yCircle,x1,y1,fill='black',width=5)
		click_Circle=0

		circle2=[]
		circle2 = [xCircle,yCircle, x1,y1]
		circle.append(circle2)
		
#Função resposável por chamar a função "criarCircle" e habilitar a função de cliques na tela
def printCircle():
	my_canvas.bind('<Button-1>', criarCircle)
	my_canvas.grid(row=1,column=1)

#Função responsável para clicar na tela
def click(click_event):
    global prev
    prev = click_event

#Função responsável para criar desenho na tela
def move(move_event):
    global prev
    my_canvas.create_line(prev.x, prev.y, move_event.x, move_event.y, width=4)
    prev = move_event 

#Função resposável por chamar as funções "click" e "move" e habilitar a função de desenho livre na tela
def printPaint():
	my_canvas.bind('<Button-1>', click)
	my_canvas.bind('<B1-Motion>', move)
	my_canvas.grid(row=1,column=1)

#implementando o codigo Cohen-Sutherland, baseado no slide passado na materia computação Grafica
def regiaoCodigo(x,y):
	cod = 0
	if(x<Xmin):
		cod = cod + 1
	if(x>Xmax):
		cod = cod + 2
	if(y<yMin):
		cod = cod + 4
	if(y>yMax):
		cod = cod + 8
	return codigo
	

#implementando o codigo Cohen-Sutherland, baseado no slide passado na materia computação Grafica
def cohen_Suth(x0,y0,x,y):
	aceito = False
	feito = False

	XMin = 0
	Xint = 0

	while(feito==False):
		p1 = regiaoCodigo(x0,y0)
		p2 = regiaoCodigo(x,y)
		if(p1==0 and p2 == 0):
			aceito = True
			feito = True
		else:
			if(p1 == 0):
				pfora = p1
			else:
				pfora = p2

				if(pfora ==1):
					xInt = xMin
					yInt = y0+(y-y0)*(Xmin-x0)/(x-x0)
				elif(pfora == 2):
					yInt = Ymin
					XInt = x0+(x-x0)*(Ymin-y0)/(y-y0)
				elif(pfora == 3):
					yInt = Ymax
					XInt = x0+(x-x0)*(Ymax-y0)/(y-y0)
					if(p1 == pfora):
						x = Xint
						y=yInt


#Função resposável por receber os valores do Cohen–Sutherland e printar os valores na tela
def criarCohen(event):

	global click_Cohen
	global xCohen,yCohen

	if click_Cohen == 0:
		xCohen=event.x
		yCohen=event.y
		click_Cohen=1
	else:
		x1=event.x
		y1=event.y

		my_canvas.create_rectangle(0,0,1360,menorLiang(yCohen,y1),fill='white',width=0)
		my_canvas.create_rectangle(0,BigLiang(yCohen,y1),1360,720,fill='white',width=0)
		my_canvas.create_rectangle(BigLiang(xCohen,x1),0,1360,720,fill='white',width=0)
		my_canvas.create_rectangle(0,0,menorLiang(xCohen,x1),720,fill='white',width=0)
		click_Cohen=0

#Função resposável por chamar a função "criarCohen" e habilitar a função de cliques na tela
def printCohen():
	my_canvas.bind('<Button-1>', criarCohen)
	my_canvas.grid(row=1,column=1)

#Função resposável por receber os valores do Cohen–Sutherland e printar os valores na tela
def criarLiang(event):
	#drawDDA(x1,x2,x3,x5)

	global click_Liang
	global xLiang,yLiang

	if click_Liang == 0:
		xLiang=event.x
		yLiang=event.y
		click_Liang=1
	else:
		x1=event.x
		y1=event.y


		my_canvas.create_rectangle(0,0,1360,menorLiang(yLiang,y1),fill='white',width=0)
		my_canvas.create_rectangle(0,BigLiang(yLiang,y1),1360,720,fill='white',width=0)
		my_canvas.create_rectangle(BigLiang(xLiang,x1),0,1360,720,fill='white',width=0)
		my_canvas.create_rectangle(0,0,menorLiang(xLiang,x1),720,fill='white',width=0)
		click_Liang=0
		


#Função resposável por chamar a função "criarCohen" e habilitar a função de cliques na tela
def printLiang():
	my_canvas.bind('<Button-1>', criarLiang)
	my_canvas.grid(row=1,column=1)

def menorLiang(y1,y2):
	if(y1<y2):
		return y1
	else:
		return y2

def BigLiang(y1,y2):
	if(y1>y2):
		return y1
	else:
		return y2


#Funcao de translacao para a direita
def translacao_Right():
	my_canvas.delete("all")
	for i in ret:
		my_canvas.delete("all")
		i[0] = i[0] + 50
		i[2] = i[2] + 50
		my_canvas.create_rectangle(i[0] ,i[1],i[2],i[3],fill='black',width=5)

	for i in circle:
		my_canvas.delete("all")
		i[0] = i[0] + 50
		i[2] = i[2] + 50
		my_canvas.create_oval(i[0] ,i[1],i[2],i[3],fill='black',width=5)

	for i in listDda:
		my_canvas.delete("all")
		i[0] = i[0] + 50
		i[2] = i[2] + 50
		my_canvas.create_line(i[0] ,i[1],i[2],i[3],fill='black',width=5)

	for i in listBres:
		my_canvas.delete("all")
		i[0] = i[0] + 50
		i[2] = i[2] + 50
		my_canvas.create_line(i[0] ,i[1],i[2],i[3],fill='black',width=5)


#Funcao de translacao para a esquerda
def translacao_Left():
	my_canvas.delete("all")
	for i in ret:
		my_canvas.delete("all")
		i[0] = i[0] - 50
		i[2] = i[2] - 50
		my_canvas.create_rectangle(i[0] ,i[1],i[2],i[3],fill='black',width=5)

	for i in circle:
		my_canvas.delete("all")
		i[0] = i[0] - 50
		i[2] = i[2] - 50
		my_canvas.create_oval(i[0] ,i[1],i[2],i[3],fill='black',width=5)

	for i in listDda:
		my_canvas.delete("all")
		i[0] = i[0] - 50
		i[2] = i[2] - 50
		my_canvas.create_line(i[0] ,i[1],i[2],i[3],fill='black',width=5)

	for i in listBres:
		my_canvas.delete("all")
		i[0] = i[0] - 50
		i[2] = i[2] - 50
		my_canvas.create_line(i[0] ,i[1],i[2],i[3],fill='black',width=5)


#Funcao de translacao para cima
def translacao_Up():
	my_canvas.delete("all")
	for i in ret:
		my_canvas.delete("all")
		i[1] = i[1] - 50
		i[3] = i[3] - 50
		my_canvas.create_rectangle(i[0] ,i[1],i[2],i[3],fill='black',width=5)

	for i in circle:
		my_canvas.delete("all")
		i[1] = i[1] - 50
		i[3] = i[3] - 50
		my_canvas.create_oval(i[0] ,i[1],i[2],i[3],fill='black',width=5)

	for i in listDda:
		my_canvas.delete("all")
		i[1] = i[1] - 50
		i[3] = i[3] - 50
		my_canvas.create_line(i[0] ,i[1],i[2],i[3],fill='black',width=5)

	for i in listBres:
		my_canvas.delete("all")
		i[1] = i[1] - 50
		i[3] = i[3] - 50
		my_canvas.create_line(i[0] ,i[1],i[2],i[3],fill='black',width=5)


#Funcao de translacao para baixo
def translacao_Down():
	my_canvas.delete("all")
	for i in ret:
		my_canvas.delete("all")
		i[1] = i[1] + 50
		i[3] = i[3] + 50
		my_canvas.create_rectangle(i[0] ,i[1],i[2],i[3],fill='black',width=5)

	for i in circle:
		my_canvas.delete("all")
		i[1] = i[1] + 50
		i[3] = i[3] + 50
		my_canvas.create_oval(i[0] ,i[1],i[2],i[3],fill='black',width=5)

	for i in listDda:
		my_canvas.delete("all")
		i[1] = i[1] + 50
		i[3] = i[3] + 50
		my_canvas.create_line(i[0] ,i[1],i[2],i[3],fill='black',width=5)

	for i in listBres:
		my_canvas.delete("all")
		i[1] = i[1] + 50
		i[3] = i[3] + 50
		my_canvas.create_line(i[0] ,i[1],i[2],i[3],fill='black',width=5)

#Funcao de adicionar um botao e chamar os respectivos metodos de translacao
def translacao():

	button_up= Button(my_window, text="UP", width=6, command = translacao_Up)
	button_up.grid(row=0,column=1)
	button_up.place(x = 0, y = 80)

	button_down= Button(my_window, text="DOWN", width=6, command = translacao_Down)
	button_down.grid(row=0,column=1)
	button_down.place(x = 80, y = 80)

	button_left= Button(my_window, text="LEFT", width=6, command = translacao_Left)
	button_left.grid(row=0,column=1)
	button_left.place(x = 160, y = 80)

	button_right= Button(my_window, text="RIGHT", width=6, command = translacao_Right)
	button_right.grid(row=0,column=1)
	button_right.place(x = 240, y = 80)

	my_canvas.delete("all")

#Funcao para diminuir escala 
def escala_Down():
	my_canvas.delete("all")

	for i in listDda:
		my_canvas.delete("all")
		i[0] = i[0] *0.5
		i[1] = i[1] *0.5
		i[2] = i[2] *0.5
		i[3] = i[3] *0.5
		i[0] = i[0] +200
		i[1] = i[1] +200
		i[2] = i[2] +200
		i[3] = i[3] +200
		my_canvas.create_line(i[0] ,i[1],i[2],i[3],fill='black',width=5)

	for i in listBres:
		my_canvas.delete("all")
		i[0] = i[0] *0.5
		i[1] = i[1] *0.5
		i[2] = i[2] *0.5
		i[3] = i[3] *0.5
		i[0] = i[0] +200
		i[1] = i[1] +200
		i[2] = i[2] +200
		i[3] = i[3] +200
		my_canvas.create_line(i[0] ,i[1],i[2],i[3],fill='black',width=5)

	for i  in circle:
		my_canvas.delete("all")
		i[0] = i[0] *0.5
		i[1] = i[1] *0.5
		i[2] = i[2] *0.5
		i[3] = i[3] *0.5
		i[0] = i[0] +200
		i[1] = i[1] +200
		i[2] = i[2] +200
		i[3] = i[3] +200
		my_canvas.create_oval(i[0] ,i[1],i[2],i[3],fill='black',width=5)
			
	for i in ret:
		my_canvas.delete("all")
		i[0] = i[0] *0.5
		i[1] = i[1] *0.5
		i[2] = i[2] *0.5
		i[3] = i[3] *0.5
		i[0] = i[0] +200
		i[1] = i[1] +200
		i[2] = i[2] +200
		i[3] = i[3] +200
		my_canvas.create_rectangle(i[0] ,i[1],i[2],i[3],fill='black',width=5)

#Funcao para aumentar escala
def escala_up():
	my_canvas.delete("all")

	for i in listDda:
		my_canvas.delete("all")
		i[0] = i[0] *1.5
		i[1] = i[1] *1.5
		i[2] = i[2] *1.5
		i[3] = i[3] *1.5
		i[0] = i[0] +25
		i[1] = i[1] +25
		i[2] = i[2] +25
		i[3] = i[3] +25
		my_canvas.create_line(i[0] ,i[1],i[2],i[3],fill='black',width=5)

	for i in listBres:
		my_canvas.delete("all")
		i[0] = i[0] *1.5
		i[1] = i[1] *1.5
		i[2] = i[2] *1.5
		i[3] = i[3] *1.5
		i[0] = i[0] +25
		i[1] = i[1] +25
		i[2] = i[2] +25
		i[3] = i[3] +25
		my_canvas.create_line(i[0] ,i[1],i[2],i[3],fill='black',width=5)

	for i  in circle:
		my_canvas.delete("all")
		i[0] = i[0] *1.5
		i[1] = i[1] *1.5
		i[2] = i[2] *1.5
		i[3] = i[3] *1.5
		i[0] = i[0] +25
		i[1] = i[1] +25
		i[2] = i[2] +25
		i[3] = i[3] +25
		my_canvas.create_oval(i[0] ,i[1],i[2],i[3],fill='black',width=5)
			
	for i in ret:
		my_canvas.delete("all")
		i[0] = i[0] *1.5
		i[1] = i[1] *1.5
		i[2] = i[2] *1.5
		i[3] = i[3] *1.5
		i[0] = i[0] +25
		i[1] = i[1] +25
		i[2] = i[2] +25
		i[3] = i[3] +25
		my_canvas.create_rectangle(i[0] ,i[1],i[2],i[3],fill='black',width=5)

#Funcao de adicionar um botao e chamar os respectivos metodos de translacao
def escala():

	button_up= Button(my_window, text="UP", width=6, command = escala_up)
	button_up.grid(row=0,column=1)
	button_up.place(x = 0, y = 80)

	button_down= Button(my_window, text="DOWN", width=6, command = escala_Down)
	button_down.grid(row=0,column=1)
	button_down.place(x = 80, y = 80)


def rotacao():
	my_canvas.delete("all")

	for i in ret:
		my_canvas.delete("all")
		i[2] = (i[3] * 1)
		i[3] = (i[2] * 1)  
		my_canvas.create_rectangle(i[0] ,i[1],i[2],i[3],fill='black',width=5)

	for j  in circle:
		my_canvas.delete("all")
		j[2] = (j[3] * 1)
		j[3] = (j[2] * 1)  
		my_canvas.create_oval(j[0] ,j[1],j[2],j[3],fill='black',width=5)

	for i in listDda:
		my_canvas.delete("all")
		i[2] = (i[3] * 1)
		i[3] = (i[2] * 1)  
		my_canvas.create_line(i[0] ,i[1],i[2],i[3],fill='black',width=5)

	for j  in listBres:
		my_canvas.delete("all")
		j[2] = (j[3] * 1)
		j[3] = (j[2] * 1)  
		my_canvas.create_line(j[0] ,j[1],j[2],j[3],fill='black',width=5)


def reflexão():
	my_canvas.delete("all")
	for i in listDda:
		my_canvas.delete("all")
		i[2] = (i[3] * 1)
		i[3] = (i[2] * 1)  
		my_canvas.create_line(i[0] +300 ,i[1],i[2] + 300,i[3],fill='black',width=5)

	for i in ret:
		my_canvas.delete("all")
		i[2] = (i[3] * 1)
		i[3] = (i[2] * 1)  
		my_canvas.create_rectangle(i[0] +300 ,i[1],i[2] + 300,i[3],fill='black',width=5)

	for j  in listBres:
		my_canvas.delete("all")
		j[2] = (j[3] * 1)
		j[3] = (j[2] * 1)  
		my_canvas.create_line(j[0] +300 ,j[1],j[2] +300,j[3],fill='black',width=5)

	for j  in circle:
		my_canvas.delete("all")
		i[2] = (i[3] * 1)
		i[3] = (i[2] * 1)  
		my_canvas.create_oval(j[0] +300 ,j[1],j[2]+ 300,j[3],fill='black',width=5)



#Função responsável por limpar a interface do canvas
def canvasDelete():
	my_canvas.delete("all")

#criação do botão para usar o algoritmo DDA  
button_dda= Button(my_window, text="DDA", width=6, command= printLinhaDDA)
button_dda.grid(row=0,column=1)
button_dda.place(x = 0, y = 10)
click_dda=0

#criação do botão para usar o algoritmo Bressnham 
button_Bres= Button(my_window, text="Bressnham", width=8, command= printLinhaBres)
button_Bres.grid(row=0,column=1)
button_Bres.place(x = 70, y = 10)
click_Bres=0

#criação do botão para direcionar e chamar o "printRetangulo"
button_ret= Button(my_window, text="Retangulo", width=8, command= printRetangulo)
button_ret.grid(row=0,column=3)
button_ret.place(x = 160, y = 10)
click_Ret=0

#criação do botão para direcionar e chamar o "printCircle"
button_circle= Button(my_window, text="Circulo", width=8, command= printCircle)
button_circle.grid(row=0,column=4)
button_circle.place(x = 240, y = 10)
click_Circle=0

#criação do botão para direcionar e chamar o "printPaint"
button_paint= Button(my_window, text="Livre", width=8, command= printPaint)
button_paint.grid(row=0,column=5)
button_paint.place(x = 330, y = 10)
click_=0

#criação do botão para direcionar e chamar o "printCohen"
button_Cohen= Button(my_window, text="Cohen-Sutherland", width=15, command= printCohen)
button_Cohen.grid(row=0,column=6)
button_Cohen.place(x = 410 , y = 10)
click_Cohen=0

#criação do botão para direcionar e chamar o "printLiang"
button_Liang= Button(my_window, text="Liang-Barsky", width=10, command= printLiang)
button_Liang.grid(row=0,column=7)
button_Liang.place(x = 550, y = 10)
click_Liang=0

#criação do botão para direcionar e chamar a "translacao"
button_trans= Button(my_window, text="Translacao", width=8, command = translacao)
button_trans.grid(row=0,column=8)
button_trans.place(x = 650, y = 10)
click_=0

#criação do botão para direcionar e chamar a "rotacao"
button_rot= Button(my_window, text="Rotacao", width=8, command= rotacao)
button_rot.grid(row=0,column=9)
button_rot.place(x = 740, y = 10)
click_=0

#criação do botão para direcionar e chamar a "escala"
button_esc= Button(my_window, text="Escala", width=8, command= escala)
button_esc.grid(row=0,column=10)
button_esc.place(x = 820, y = 10)
click_=0

#criação do botão para direcionar e chamar a "reflexao"
button_refle= Button(my_window, text="Reflexão", width=8, command= reflexão)
button_refle.grid(row=0,column=11)
button_refle.place(x = 900, y = 10)
click_=0

#criação do botão para limpar a tela do canvas
button_Del= Button(my_window, text="Limpar Quadro", width=12, command= canvasDelete)
button_Del.grid(row=0,column=12)
button_Del.place(x = 980, y = 10)

my_window.mainloop()
  
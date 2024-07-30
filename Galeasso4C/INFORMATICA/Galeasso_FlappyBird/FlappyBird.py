#GALEASSO FEDERICO 4C - FLAPPY BIRD

#Librerie necessarie
import pygame
import random
import os
#Inizializzazione della pygame
pygame.init()

os.system("clear")

pygame.display.set_caption('Flappy Bird - Galeasso')  

#Caricamento delle immagini
sfondo=pygame.image.load('./immagini/sfondo.png')
uccello=pygame.image.load('./immagini/uccello.png')
base=pygame.image.load('./immagini/base.png')
gameover=pygame.image.load('./immagini/gameover.png')
tubo_giu=pygame.image.load('./immagini/tubo.png')
# Per cerare il tubo superiore facciamo l'immagine specchio del tubo_giu
tubo_su=pygame.transform.flip(tubo_giu, False, True)

#https://www.101soundboards.com/boards/10178-flappy-bird-sounds
suono_gameover = pygame.mixer.Sound('./suoni/hit.mp3')
suono_ala = pygame.mixer.Sound('./suoni/wing.mp3')
suono_punto = pygame.mixer.Sound('./suoni/point.mp3')

#Creazione della finestra di gioco (larghezza e altezza)
SCHERMO=pygame.display.set_mode((288,512))

#Frame per secondo (fps)
FPS=50

#Velocità di avanzamento della base
VEL_AVANZ=3

#Flag di uscita (GAME OVER)
flagq=False

#Classe per creare l'oggetto tubo
class tubi_classe():
	def __init__(self):
		self.x=300
		self.y=random.randint(-75,150)
		print("-inf-", self.y+210)
		print("-sup-", self.y-210)
		
	def avanza_e_disegna(self):
		self.x -= VEL_AVANZ
		SCHERMO.blit(tubo_giu, (self.x, self.y+210))
		SCHERMO.blit(tubo_su, (self.x, self.y-210))
		
	def collisione(self, uccello, uccellox, uccelloy):
		tolleranza=5
		uccello_lato_dx=uccellox+uccello.get_width()-tolleranza
		uccello_lato_sx=uccellox+tolleranza
		
		tubi_lato_dx=self.x+tubo_giu.get_width()
		tubi_lato_sx=self.x
		
		uccello_lato_su=uccelloy+tolleranza
		uccello_lato_giu=uccelloy+uccello.get_height()-tolleranza
		
		tubi_lato_su=self.y+110
		tubi_lato_giu=self.y+210
		
		if uccello_lato_dx > tubi_lato_sx and uccello_lato_sx < tubi_lato_dx:
			if uccello_lato_su < tubi_lato_su or uccello_lato_giu > tubi_lato_giu:
				haiperso()
			

#Coordinate di partenza dell'uccello
def inizializza():
	global uccellox, uccelloy, uccello_vely, basex, tubi
	
	uccellox,uccelloy=60,150
	uccello_vely=0
	basex=0
	tubi=[]
	tubi.append(tubi_classe())

#Posizione degli oggetti sullo schermo
def disegna_oggetti():
	SCHERMO.blit(sfondo,(0,0))
	
	punteggio=0
	for t in tubi:
		t.avanza_e_disegna()
		
		#If per controllare se la x dell'uccello è maggiore della x del tubo: se è maggiore vuol dire che l'uccello è entrato nel tubo e quindi il punteggio viene incrementato di 1
		if uccellox > t.x:
			punteggio += 1
			#suono_punto.play()
			
	SCHERMO.blit(uccello,(uccellox,uccelloy))
	SCHERMO.blit(base,(basex,400))
	
	#Visualizzazione del punteggio
	stile = pygame.font.Font(None, 50)
	testo = stile.render(str(punteggio), True, (255, 255, 255))
	SCHERMO.blit(testo, (130,20))

#Aggiornamento dello schermo (in base agli FPS)
def aggiorna():
	pygame.display.update()
	pygame.time.Clock().tick(FPS)
	
#Funzione di GAME OVER
def haiperso():
	global flagq
	if flagq==True:
		pygame.quit()
	else:
		SCHERMO.blit(gameover,(45,150))
		aggiorna()
		ricominciamo=False
		flagq=False
		suono_gameover.play()
		while not ricominciamo:
			for evento in pygame.event.get():
				if(evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE):
					inizializza()
					ricominciamo=True
				if evento.type == pygame.QUIT:
					flagq=True
					ricominciamo=True

inizializza()

#Ciclo infinito
while True:
	uccello_vely+=1
	uccelloy+=uccello_vely
	
	disegna_oggetti()
	aggiorna()
	
	#Verifica del tasto premuto
	for evento in pygame.event.get():
		if(evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP):
			uccello_vely=-10
			suono_ala.play()
			
		if evento.type == pygame.QUIT:
			pygame.quit()
	
	#Spostamento e riposizionamento della base (per dare l'effetto di movimento)
	basex-=VEL_AVANZ
	if basex < -45:
		basex=0
	
	#Se l'uccello entra in collisione con la base --> GAME OVER
	if uccelloy > 380:
		haiperso()
	
	if tubi[-1].x < 150:
		tubi.append(tubi_classe())
	
	for t in tubi:
		t.collisione(uccello, uccellox, uccelloy)

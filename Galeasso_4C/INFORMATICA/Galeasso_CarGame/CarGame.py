#GALEASSO FEDERICO 4C - CARGAME

#Librerie necessarie
import pygame
import random
import os

#Installazione: pip install pygame-menu
import pygame_menu

#Inizializzazione della pygame
pygame.init()

#Pulizia dello schermo
os.system("clear")

#Nome della finestra
pygame.display.set_caption('Car Game - Galeasso')

#Caricamento delle immagini
player=pygame.image.load('./img/Player.png')
nemico=pygame.image.load('./img/Enemy.png')
strada=pygame.image.load('./img/road.png')
hearts_0=pygame.image.load('./img/0.png')
hearts_1=pygame.image.load('./img/1.png')
hearts_2=pygame.image.load('./img/2.png')
hearts_3=pygame.image.load('./img/3.png')
hearts_4=pygame.image.load('./img/4.png')
hearts_5=pygame.image.load('./img/5.png')
start=pygame.image.load('./img/start.png')
money1=pygame.image.load('./img/money.png')
#Ridimensionamento dell'immagine della moneta
money=pygame.transform.scale(money1, (40, 40))

#Caricamento dei suoni
suono_gioco = pygame.mixer.Sound('./sound/background.wav')
suono_gameover = pygame.mixer.Sound('./sound/crash.wav')
suono_punto = pygame.mixer.Sound('./sound/point.wav')
suono_clacson = pygame.mixer.Sound('./sound/clacson.wav')
start_sound = pygame.mixer.Sound('./sound/start_sound.wav')

#Creazione della finestra di gioco (larghezza e altezza)
SCHERMO=pygame.display.set_mode((445,700))

#Frame per secondo (fps)
FPS=50

#Velocità di avanzamento della strada
VEL_AVANZ=10

#Inizializzazione variabili
def inizializza():
	global playerx, playery, player_velx, straday, nemicox, nemicoy, punteggio, flag, cont_vite, nemico_vel, moneyx, moneyy, flag_monete
	playerx,playery=200,560
	nemicox,nemicoy=200,0
	moneyx,moneyy=110,-200
	player_velx=0
	straday=0
	punteggio=0
	flag=False
	flag_monete=False
	cont_vite=5
	nemico_vel=15

#Posizione degli oggetti sullo schermo
def disegna_oggetti():
	SCHERMO.blit(strada,(0,straday))
	SCHERMO.blit(strada, (0, straday - strada.get_height()))
	SCHERMO.blit(player,(playerx,playery))
	SCHERMO.blit(nemico,(nemicox,nemicoy))
	SCHERMO.blit(money,(moneyx,moneyy))
	
	# Visualizzazione del punteggio
	stile = pygame.font.Font(None, 50)
	testo_senza_padding = stile.render(str(punteggio), True, (223,168,75))
	larghezza_testo = testo_senza_padding.get_width() + 20
	altezza_testo = testo_senza_padding.get_height() + 10
	testo_con_padding = pygame.Surface((larghezza_testo, altezza_testo))
	testo_con_padding.fill((255, 255, 255))
	testo_con_padding.blit(testo_senza_padding, (10, 5))
	SCHERMO.blit(testo_con_padding, (200, 15))

	
	#Controllo delle vite
	if cont_vite == 5:
		SCHERMO.blit(hearts_5,(115,665))
	if cont_vite == 4:
		SCHERMO.blit(hearts_4,(115,665))
	if cont_vite == 3:
		SCHERMO.blit(hearts_3,(115,665))
	if cont_vite == 2:
		SCHERMO.blit(hearts_2,(115,665))
	if cont_vite == 1:
		SCHERMO.blit(hearts_1,(115,665))
	if cont_vite == 0:			
		SCHERMO.blit(hearts_0,(115,665))
		suono_gioco.stop()
		suono_gameover.play()
		pygame.time.wait(2000)
		GAMEOVER()

#Aggiornamento dello schermo (in base agli FPS)
def aggiorna():
	pygame.display.update()
	pygame.time.Clock().tick(FPS)
	
#Start del gioco
SCHERMO.blit(start,(0,0))
aggiorna()
pygame.time.wait(1000)
start_sound.play()
pygame.time.wait(3000)

#Funzione di gameover
def GAMEOVER():
	#Creazione del menu di game over
	global menu_gameover
	menu_gameover = pygame_menu.Menu('Game Over', 445, 700, theme=pygame_menu.themes.THEME_DARK)
	def restart():
		menu_gameover.disable()
		money.set_alpha(255)
		suono_gioco.play(-1)
		inizializza()
	menu_gameover.add.button('Your final score: '+str(punteggio))
	menu_gameover.add.button('Restart', restart)
	menu_gameover.add.button('Quit', pygame_menu.events.EXIT)
	menu_gameover.enable()
	menu_gameover.mainloop(SCHERMO)

inizializza()

#Creazione del menu iniziale
menu = pygame_menu.Menu('Car Game Menu', 445, 700, theme=pygame_menu.themes.THEME_DARK)
#Funzione per iniziare il gioco
def inizia_gioco():
	global menu
	menu.disable()
	suono_gioco.play(-1)
menu.add.button('Play', inizia_gioco)
menu.add.button('Quit', pygame_menu.events.EXIT)

#Evento personalizzato per incrementare la velocità del nemico ogni secondo
inc_vel = pygame.USEREVENT + 1
pygame.time.set_timer(inc_vel, 1000)

#Creazione del menu di pausa
menu_pausa = pygame_menu.Menu('Pause', 445, 700, theme=pygame_menu.themes.THEME_DARK)
def resume():
	global menu_pausa
	menu_pausa.disable()
	suono_gioco.play(-1)
	
def restart():
		menu_pausa.disable()
		money.set_alpha(255)
		suono_gioco.play(-1)
		inizializza()
menu_pausa.add.button('Resume', resume)
menu_pausa.add.button('Restart', restart)
menu_pausa.add.button('Quit', pygame_menu.events.EXIT)

#Ciclo infinito
while True:
	#Verifica se il menu è attivo o meno
	if not menu.is_enabled():
		disegna_oggetti()
		aggiorna()
		
		#Verifica del tasto premuto
		if pygame.key.get_pressed()[pygame.K_LEFT]:
			player_velx = -15
			player = pygame.transform.rotate(pygame.image.load('./img/Player.png'), 10)
		elif pygame.key.get_pressed()[pygame.K_RIGHT]:
			player_velx = 15
			player = pygame.transform.rotate(pygame.image.load('./img/Player.png'), -10)
		else:
			player_velx = 0
			player = pygame.transform.rotate(pygame.image.load('./img/Player.png'), 0)
		 
		#Aggiornamento della posizione della macchina
		playerx += player_velx
		
		#Limitazione della posizione del giocatore all'interno della finestra di gioco
		if playerx<50:
			playerx=50
		if playerx>350:
			playerx=350
		
		#Rallentamento del player sulla sabbia
		if playerx < 70:
			VEL_AVANZ=5
		elif playerx > 320:
			VEL_AVANZ=5
		else:
			VEL_AVANZ=10
		
		for evento in pygame.event.get():
			#Controllo dell'evento di chiusura della finestra di gioco
			if evento.type == pygame.QUIT:
				pygame.quit()
				quit()
			#Incremento della velocità del nemico
			if evento.type == inc_vel:
				nemico_vel += 1
			#Apertura del menu di pausa quando viene premuto Invio
			if(evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN):
				menu_pausa.enable()
				suono_gioco.stop()
				menu_pausa.mainloop(SCHERMO)
			#Play del suono del clacson quando viene premuto Spazio
			if(evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE):
				suono_clacson.play()
		
		#Effetto di movimento della strada		
		straday += VEL_AVANZ
		if straday >= strada.get_height():
			straday = 0
		
		#Controllo di collisione con il nemico
		if pygame.Rect(playerx, playery, player.get_width(), player.get_height()).colliderect(pygame.Rect(nemicox, nemicoy, nemico.get_width(), nemico.get_height())):
			if not flag:
				cont_vite -= 1
				flag = True
		else:
			flag=False
			
		#Controllo di collisione con la moneta
		if pygame.Rect(playerx, playery, player.get_width(), player.get_height()).colliderect(pygame.Rect(moneyx, moneyy, money.get_width(), money.get_height())):
			if not flag_monete:
				punteggio+=3
				suono_punto.play()
				flag_monete = True
				money.set_alpha(0)
		else:
			flag_monete=False
				
		#Movimento del nemico
		nemicoy += nemico_vel
		if nemicoy > 700:
			punteggio+=1
			nemicox = random.randint(50, 350)
			nemicoy = -200
			
		#Movimento della moneta
		moneyy += nemico_vel
		if moneyy > 5000:
			money.set_alpha(255)
			moneyx = random.randint(50, 350)
			moneyy = -200
			
	else:
		#Visualizzazione del menu
		menu.enable()
		menu.mainloop(SCHERMO)

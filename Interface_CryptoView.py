#!/usr/bin/env python
# -*- coding: utf-8 -*-

#PYTHON 3.x EDITION
#AIDES: https://pythonconverter.com/

#AIDES: https://github.com/Franck1333/ProjetBrassard
#AIDES: https://gist.github.com/Franck1333/f80936044088cb50aec1c1aad9de1803
#AIDES: http://apprendre-python.com/page-tkinter-interface-graphique-python-tutoriel
#AIDES: https://stackoverflow.com/questions/14824163/how-to-get-the-input-from-the-tkinter-text-box-widget
#AIDES: https://stackoverflow.com/questions/11040098/cannot-pass-arguments-from-the-tkinter-widget-after-function



#---------------------------------------Importante LIB---------------------------------------
import os                                                   #Blibliotheque permettant l'interaction avec le systeme
import sys                                                  #Blibliotheque permettant l'interaction avec le systeme
import datetime                                             #Blibliotheque permettant d'obtenir la date
import time                                                 #Blibliotheque permettant d'obtenir la date

import getpass                                              #On importe la blibliotheque "getpass"
global USERNAME
USERNAME = getpass.getuser()                                #On enregistre le Nom de l'Utilisateur

from tkinter import *                                       #Blibliotheque permettant d'obtenir Tkinter(G.U.I)
from tkinter.messagebox import *                            #Blibliotheque permettant d'obtenir les boites de dialogues (G.U.I)
import tkinter.ttk                                          #Blibliotheque permettant de charger un composant Tkinter(G.U.I)

from pydub import AudioSegment                              #Bibliotheque permettant de jouer des Sons et Jingles
from pydub.playback import play                             #""""""""""""""""""""""""""""""""""""""""""""""""""""
#---------------------------------------Importante LIB---------------------------------------

#-----------------------------------------------------Localisation de l'emplacement des fichiers necessaires-----------------------------------------------------
print("\n Bonjour/Bonsoir, ne pas faire fonctionner ce programme en utilisant les droits/commandes administrateur si l'utilisateur n'est pas l'Admin au quel cas le programme ne fonctionnera pas correctement. \n") #Information a lire dans la console
sys.path.append("/home/"+USERNAME+"/CryptoWatch-Tkinter/Services")  #On indique au systeme ou ce situe le repertoire "Services" dans l'Appareil
#print(USERNAME)                                            #Test debug

from nettoyage_du_cache import clear_cache                  #Bibliotheque permettant de nettoyer les fichiers cache PYTHON

from Infos_Hardware import CPU_usage                        #Obtention de l'utilisation du Processeur par le Systeme d'exploitation et ses programmes autour
from Infos_Hardware import CPU_temp                         #Obtention de la Temperature du Processeur sur la carte mere
from Infos_Hardware import SoC_info                         #Obtention des informations concernant le package CPU+GPU
from Infos_Hardware import MEM_info                         #Obtention de l'utilisation de la Memoire Vive du Systeme

from Infos_complementaires import Get_Marche_BTC            #Obtention de la Valeur du BTC sur le Marche
from Infos_complementaires import Get_Fear_Greed_Index      #Obtention d'une image indicant les sentiments des acteurs du Marche

from Infos_Coins import Recherche_Info_Coin                 #Obtention des Informations detaillee concernant un Monnaie crypto relie a une autre monnaie (Crypto/Fiat)
from Infos_Coins import Recherche_Et_Surveillance_Coin      #Permet la Surveillance d'une paire

from Graph import Dessiner_Graph                            #Avec cette fontcion nous pouvons obtenir un graph en rapport avec la crypto-monnaie definie

#-----------------------------------------------------Localisation de l'emplacement des fichiers necessaires-----------------------------------------------------

#-------------Fenetre Maitre-------------
fenetre = Tk()              #Creation d'une Fenetre Maîtresse TK appeler "fenetre"
#-------------Fenetre Maitre-------------

#-------------------------------------------------------------------Contenue Fenetre Principale-------------------------------------------------------------------
#------------------------------------------------------------------------------     #Affichage du Temps HEURES/MINUTES/SECONDES
def temps_actuel():   
    #OBTENTION DE L'HEURE ACTUEL sous format HEURE,MINUTE,SECONDE
    #-- DEBUT -- Heure,Minute,Seconde
    tt = time.time()
    system_time = datetime.datetime.fromtimestamp(tt).strftime('%H:%M:%S')
    print(("Voici l'heure:",system_time))
    return system_time
    #-- FIN -- Heure,Minute,Seconde
#---------------------------------------------
status_temps_actuel = Label(fenetre, text=temps_actuel())                   #Affichage du Temps (Label)
status_temps_actuel.pack()                                                  #Pour obtenir un affichage dynamique , Il faut utiliser pack/grid de cette façon
#---------------------------------------------
def update_temps_actuel():                                                  #Fonctionnalité permettant de mettre à jour l'Heure en fonction du Temps Réel
    # On met à jour le temps actuel dans le champs text du Widget LABEL pour afficher l'heure
    status_temps_actuel["text"] = temps_actuel()

    # Après une seconde , on met à jour le contenue text du LABEL
    fenetre.after(1000, update_temps_actuel)    
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
def information_Materiel():
    #Obtention des Informations Materiel de l'Ordinateur
    global tk_UtilisationCPU
    global tk_tk_cputemp
    global tk_MemoireUtilise

    #--        
    UtilisationCPU = CPU_usage()                                                #Obtention du Niveau d'utilisation du Processeur.
    MemoireUtilise = MEM_info()                                                 #Obtention d'information par rapport à la Memoire Vive.
    tk_cputemp = CPU_temp()                                                     #Obtention de la Temperature du Package Processeur/GPU.
    mesure_voltage,memoire_processeur,memoire_gpu  = SoC_info()                 #Obtention d'information par rapport au Couple CPU/GPU.
    
    #--

    #--Affichage--
    EnveloppeInfoMateriel = LabelFrame(fenetre, text="Informations Relatives aux Matériels", padx=5, pady=5)    #Création d'une "Zone Frame" à Label
    EnveloppeInfoMateriel.pack(fill="both", expand="no")                                                        #Position de la "Zone Frame" à Label dans la fenêtre

    tk_UtilisationCPU = Label(EnveloppeInfoMateriel, text=UtilisationCPU)
    tk_MemoireUtilise = Label(EnveloppeInfoMateriel, text=MemoireUtilise)
    tk_tk_cputemp = Label(EnveloppeInfoMateriel, text=tk_cputemp)
    
    tk_UtilisationCPU.pack()
    tk_MemoireUtilise.pack()
    tk_tk_cputemp.pack()    
    #--Affichage--

def update_information_Materiel():
    #Mise a Jour des Informations a Propos du Materiel
    tk_UtilisationCPU["text"] = CPU_usage()
    tk_MemoireUtilise["text"] = MEM_info()
    tk_tk_cputemp["text"] = CPU_temp()    

    # Après une seconde , on met à jour le contenue text du LABEL
    fenetre.after(1000, update_information_Materiel)
#---
information_Materiel() #Lancement de la Fonctionnalitée.
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def information_Complementaire():
    global tk_info_supp
    #Recuperation des Informations  

    #INFOS = "Aucune Informations Supp. à affichée pour le moment."
    tk_BTC_Market = Get_Marche_BTC()

    
    #--Affichage--
    EnveloppeInfoComplementaire = LabelFrame(fenetre, text="Informations Complémentaires", padx=5, pady=5)    #Création d'une "Zone Frame" à Label
    EnveloppeInfoComplementaire.pack(fill="both", expand="no")


    #---Affichage Infos---
    tk_info_supp = Label(EnveloppeInfoComplementaire, text= tk_BTC_Market)
    tk_info_supp.pack()
    #---Affichage Infos---

    
    #--Affichage--

def update_information_Complementaire():
    #Mise à Jour des Informations reçues
    tk_info_supp["text"] = Get_Marche_BTC()

    # Après 2,16 minutes , on met à jour le contenue text du LABEL
    fenetre.after(130000, update_information_Complementaire)
#---
information_Complementaire() #Lancement de la Fonctionnalitée.
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
def Affichage_Fear_Greed_Index():
    #Affichage du Fear / Greed index sous format d'Image PNG
    global tk_image_FGI
    
    #Recuperation des Informations
    Get_Fear_Greed_Index()

    #Zone d'Affichage
    EnveloppeFGI = LabelFrame(fenetre, text="Indice Fear and Greed du Jour", padx=5, pady=5)                                            #Création d'une "Zone Frame" à Label
    EnveloppeFGI.pack(fill="both", expand="no")

    #---Affichage Infos---
    canvas = Canvas(EnveloppeFGI,width=320, height=287, bg='black')                                                                     #Creer le CANVAS (Parent,Largeur,Hauteur,couleur de font)

    canvas.pack(expand=NO, fill=None)                                                                                                   #Placement du CANVAS de l'espace

    Image_Telechargee = PhotoImage(file='/home/'+USERNAME+'/CryptoWatch-Tkinter/Services/Telechargements/Fear_Greed_Index.png')                 #Chargement de l'image

    canvas.file = Image_Telechargee                                                                                                     #REFERENCE A GARDER pour pas perdre Tkinter sinon sans cette Reference , il perd l'image (Voir Explication ici: http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm)
    
    image_on_canvas = canvas.create_image(0,0,image=Image_Telechargee , anchor=NW)  
    #---Affichage Infos---

    #--UPDATE--
    def update_refresh_FGI():
     print("Mise a Jour de l'Image 'Fear_Greed_Index.png' ")                                                                             #Message dans la Console
     Get_Fear_Greed_Index()                                                                                                              #Obtention de l'Image a afficher
     Image_Telechargee = PhotoImage(file='/home/'+USERNAME+'/CryptoWatch-Tkinter/Services/Telechargements/Fear_Greed_Index.png')                 #Chargement de l'Image 
     canvas.file = Image_Telechargee                                                                                                     #REFERENCE A GARDER pour pas perdre Tkinter sinon sans cette Reference , il perd l'image (Voir Explication ici: http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm)
     canvas.itemconfig(image_on_canvas,image= Image_Telechargee)                                                                         #Permet la mise a jour de l'image
     #Après X secondes , on met à jour le contenue text du LABEL
     fenetre.after(73113, update_refresh_FGI)
    #--UPDATE--

    update_refresh_FGI()   #Fonctionnalité permettant de mettre à jours dans l'interface la Carte Geographique de la position de l'Utilisateur
Affichage_Fear_Greed_Index()
#------------------------------------------------------------------------------

#-------------------------------------------------------------------Contenue Fenetre Principale-------------------------------------------------------------------

#-------------------------------------------------------------------Contenue Fenetres Secondaires-------------------------------------------------------------------
def Fenetre_Selection_de_la_Paire():
 #create child window
 Selection_de_la_Paire = Toplevel()

 #Zone d'Affichage
 EnveloppeSelection = LabelFrame(Selection_de_la_Paire, text="Les Paires à Surveiller", padx=5, pady=5)     #Création d'une "Zone Frame" à Label
 EnveloppeSelection.pack(fill="both", expand="no")                                                          #Positionnement Automatique avec des parametres pour la éZone Frame"

 #Recuperation et Affichage des Informations Pour les Boutons
 #---BTC_USD---
 def Recherche_BTC_USD():
  #create child window
  Fenetre_Paire_BTC_USD = Toplevel()

  #Recuperation des Informations
  tk_Symbole_Coin_cryptonator,tk_Prix_Actuel_cryptonator,tk_Volume_24h_cryptonator,tk_Difference_Prix_24h_cryptonator,tk_Volume_Monnaie_30DAY,tk_Prix_Moins_Eleve_24h,tk_Prix_Actuel,tk_Prix_Plus_Eleve_24h,tk_Liquidite_Achat,tk_Liquidite_Vente = Recherche_Info_Coin("BTC-USD")

  #Traitement de l'Affichage des Informations
  tk_tk_Symbole_Coin_cryptonator = Label(Fenetre_Paire_BTC_USD, text=tk_Symbole_Coin_cryptonator)

  #---Zone Cryptonator---
  EnveloppeCryptonator = LabelFrame(Fenetre_Paire_BTC_USD, text="D'après Cryptonator", padx=5, pady=5)      #Création d'une "Zone Frame" à Label
  EnveloppeCryptonator.pack(fill="both", expand="no")
  
  tk_tk_Prix_Actuel_cryptonator = Label(EnveloppeCryptonator, text=tk_Prix_Actuel_cryptonator)              #Affichage des Informations
  tk_tk_Volume_24h_cryptonator = Label(EnveloppeCryptonator, text=tk_Volume_24h_cryptonator)
  tk_tk_Difference_Prix_24h_cryptonator = Label(EnveloppeCryptonator, text=tk_Difference_Prix_24h_cryptonator)

  tk_tk_Prix_Actuel_cryptonator.pack()                                                                      #Positionement automatique des WIDGETS a affiches
  tk_tk_Volume_24h_cryptonator.pack()
  tk_tk_Difference_Prix_24h_cryptonator.pack()
  #---Zone Cryptonator---

  #---Zone CoinbasePro---
  EnveloppeCoinbasePro = LabelFrame(Fenetre_Paire_BTC_USD, text="D'après CoinbasePro", padx=5, pady=5)    #Création d'une "Zone Frame" à Label
  EnveloppeCoinbasePro.pack(fill="both", expand="no")

  tk_tk_Prix_Moins_Eleve_24h = Label(EnveloppeCoinbasePro, text=tk_Prix_Moins_Eleve_24h)                  #Affichage des Informations
  tk_tk_Prix_Actuel = Label(EnveloppeCoinbasePro, text=tk_Prix_Actuel)
  tk_tk_Prix_Plus_Eleve_24h = Label(EnveloppeCoinbasePro, text=tk_Prix_Plus_Eleve_24h)
  tk_tk_Volume_Monnaie_30DAY = Label(EnveloppeCoinbasePro, text=tk_Volume_Monnaie_30DAY)
  tk_tk_Liquidite_Achat = Label(EnveloppeCoinbasePro, text=tk_Liquidite_Achat)
  tk_tk_Liquidite_Vente = Label(EnveloppeCoinbasePro, text=tk_Liquidite_Vente)

  tk_tk_Prix_Moins_Eleve_24h.pack()                                                                       #Positionement automatique des WIDGETS a affiches
  tk_tk_Prix_Actuel.pack()
  tk_tk_Prix_Plus_Eleve_24h.pack()
  tk_tk_Volume_Monnaie_30DAY.pack()
  tk_tk_Liquidite_Achat.pack()
  tk_tk_Liquidite_Vente.pack()

  Button(Fenetre_Paire_BTC_USD, text="Fermer", command=Fenetre_Paire_BTC_USD.destroy).pack()
  #---Zone CoinbasePro---
  #---BTC_USD---

  #---BTC_EUR---
 def Recherche_BTC_EUR():
  #create child window
  Fenetre_Paire_BTC_EUR = Toplevel()
  #Recuperation des Informations
  tk_Symbole_Coin_cryptonator,tk_Prix_Actuel_cryptonator,tk_Volume_24h_cryptonator,tk_Difference_Prix_24h_cryptonator,tk_Volume_Monnaie_30DAY,tk_Prix_Moins_Eleve_24h,tk_Prix_Actuel,tk_Prix_Plus_Eleve_24h,tk_Liquidite_Achat,tk_Liquidite_Vente = Recherche_Info_Coin("BTC-EUR")
  #Traitement de l'Affichage des Informations
  tk_tk_Symbole_Coin_cryptonator = Label(Fenetre_Paire_BTC_EUR, text=tk_Symbole_Coin_cryptonator)
  #---Zone Cryptonator---
  EnveloppeCryptonator = LabelFrame(Fenetre_Paire_BTC_EUR, text="D'après Cryptonator", padx=5, pady=5)    #Création d'une "Zone Frame" à Label
  EnveloppeCryptonator.pack(fill="both", expand="no")
  tk_tk_Prix_Actuel_cryptonator = Label(EnveloppeCryptonator, text=tk_Prix_Actuel_cryptonator)
  tk_tk_Volume_24h_cryptonator = Label(EnveloppeCryptonator, text=tk_Volume_24h_cryptonator)
  tk_tk_Difference_Prix_24h_cryptonator = Label(EnveloppeCryptonator, text=tk_Difference_Prix_24h_cryptonator)
  tk_tk_Prix_Actuel_cryptonator.pack()
  tk_tk_Volume_24h_cryptonator.pack()
  tk_tk_Difference_Prix_24h_cryptonator.pack()
  #---Zone Cryptonator---
  #---Zone CoinbasePro---
  EnveloppeCoinbasePro = LabelFrame(Fenetre_Paire_BTC_EUR, text="D'après CoinbasePro", padx=5, pady=5)    #Création d'une "Zone Frame" à Label
  EnveloppeCoinbasePro.pack(fill="both", expand="no")
  tk_tk_Prix_Moins_Eleve_24h = Label(EnveloppeCoinbasePro, text=tk_Prix_Moins_Eleve_24h)
  tk_tk_Prix_Actuel = Label(EnveloppeCoinbasePro, text=tk_Prix_Actuel)
  tk_tk_Prix_Plus_Eleve_24h = Label(EnveloppeCoinbasePro, text=tk_Prix_Plus_Eleve_24h)
  tk_tk_Volume_Monnaie_30DAY = Label(EnveloppeCoinbasePro, text=tk_Volume_Monnaie_30DAY)
  tk_tk_Liquidite_Achat = Label(EnveloppeCoinbasePro, text=tk_Liquidite_Achat)
  tk_tk_Liquidite_Vente = Label(EnveloppeCoinbasePro, text=tk_Liquidite_Vente)
  tk_tk_Prix_Moins_Eleve_24h.pack()
  tk_tk_Prix_Actuel.pack()
  tk_tk_Prix_Plus_Eleve_24h.pack()
  tk_tk_Volume_Monnaie_30DAY.pack()
  tk_tk_Liquidite_Achat.pack()
  tk_tk_Liquidite_Vente.pack()
  Button(Fenetre_Paire_BTC_EUR, text="Fermer", command=Fenetre_Paire_BTC_EUR.destroy).pack()
  #---Zone CoinbasePro---
  #---BTC_EUR---

  #---ETH_USD---
 def Recherche_ETH_USD():
  #create child window
  Fenetre_Paire_ETH_USD = Toplevel()
  #Recuperation des Informations
  tk_Symbole_Coin_cryptonator,tk_Prix_Actuel_cryptonator,tk_Volume_24h_cryptonator,tk_Difference_Prix_24h_cryptonator,tk_Volume_Monnaie_30DAY,tk_Prix_Moins_Eleve_24h,tk_Prix_Actuel,tk_Prix_Plus_Eleve_24h,tk_Liquidite_Achat,tk_Liquidite_Vente = Recherche_Info_Coin("ETH-USD")
  #Traitement de l'Affichage des Informations
  tk_tk_Symbole_Coin_cryptonator = Label(Fenetre_Paire_ETH_USD, text=tk_Symbole_Coin_cryptonator)
  #---Zone Cryptonator---
  EnveloppeCryptonator = LabelFrame(Fenetre_Paire_ETH_USD, text="D'après Cryptonator", padx=5, pady=5)    #Création d'une "Zone Frame" à Label
  EnveloppeCryptonator.pack(fill="both", expand="no")
  tk_tk_Prix_Actuel_cryptonator = Label(EnveloppeCryptonator, text=tk_Prix_Actuel_cryptonator)
  tk_tk_Volume_24h_cryptonator = Label(EnveloppeCryptonator, text=tk_Volume_24h_cryptonator)
  tk_tk_Difference_Prix_24h_cryptonator = Label(EnveloppeCryptonator, text=tk_Difference_Prix_24h_cryptonator)
  tk_tk_Prix_Actuel_cryptonator.pack()
  tk_tk_Volume_24h_cryptonator.pack()
  tk_tk_Difference_Prix_24h_cryptonator.pack()
  #---Zone Cryptonator---
  #---Zone CoinbasePro---
  EnveloppeCoinbasePro = LabelFrame(Fenetre_Paire_ETH_USD, text="D'après CoinbasePro", padx=5, pady=5)    #Création d'une "Zone Frame" à Label
  EnveloppeCoinbasePro.pack(fill="both", expand="no")
  tk_tk_Prix_Moins_Eleve_24h = Label(EnveloppeCoinbasePro, text=tk_Prix_Moins_Eleve_24h)
  tk_tk_Prix_Actuel = Label(EnveloppeCoinbasePro, text=tk_Prix_Actuel)
  tk_tk_Prix_Plus_Eleve_24h = Label(EnveloppeCoinbasePro, text=tk_Prix_Plus_Eleve_24h)
  tk_tk_Volume_Monnaie_30DAY = Label(EnveloppeCoinbasePro, text=tk_Volume_Monnaie_30DAY)
  tk_tk_Liquidite_Achat = Label(EnveloppeCoinbasePro, text=tk_Liquidite_Achat)
  tk_tk_Liquidite_Vente = Label(EnveloppeCoinbasePro, text=tk_Liquidite_Vente)
  tk_tk_Prix_Moins_Eleve_24h.pack()
  tk_tk_Prix_Actuel.pack()
  tk_tk_Prix_Plus_Eleve_24h.pack()
  tk_tk_Volume_Monnaie_30DAY.pack()
  tk_tk_Liquidite_Achat.pack()
  tk_tk_Liquidite_Vente.pack()
  Button(Fenetre_Paire_ETH_USD, text="Fermer", command=Fenetre_Paire_ETH_USD.destroy).pack()
  #---Zone CoinbasePro---
  #---ETH_USD---

  #---ETH_EUR---
 def Recherche_ETH_EUR():
  #create child window
  Fenetre_Paire_ETH_EUR = Toplevel()
  #Recuperation des Informations
  tk_Symbole_Coin_cryptonator,tk_Prix_Actuel_cryptonator,tk_Volume_24h_cryptonator,tk_Difference_Prix_24h_cryptonator,tk_Volume_Monnaie_30DAY,tk_Prix_Moins_Eleve_24h,tk_Prix_Actuel,tk_Prix_Plus_Eleve_24h,tk_Liquidite_Achat,tk_Liquidite_Vente = Recherche_Info_Coin("ETH-EUR")
  #Traitement de l'Affichage des Informations
  tk_tk_Symbole_Coin_cryptonator = Label(Fenetre_Paire_ETH_EUR, text=tk_Symbole_Coin_cryptonator)
  #---Zone Cryptonator---
  EnveloppeCryptonator = LabelFrame(Fenetre_Paire_ETH_EUR, text="D'après Cryptonator", padx=5, pady=5)    #Création d'une "Zone Frame" à Label
  EnveloppeCryptonator.pack(fill="both", expand="no")
  tk_tk_Prix_Actuel_cryptonator = Label(EnveloppeCryptonator, text=tk_Prix_Actuel_cryptonator)
  tk_tk_Volume_24h_cryptonator = Label(EnveloppeCryptonator, text=tk_Volume_24h_cryptonator)
  tk_tk_Difference_Prix_24h_cryptonator = Label(EnveloppeCryptonator, text=tk_Difference_Prix_24h_cryptonator)
  tk_tk_Prix_Actuel_cryptonator.pack()
  tk_tk_Volume_24h_cryptonator.pack()
  tk_tk_Difference_Prix_24h_cryptonator.pack()
  #---Zone Cryptonator---
  #---Zone CoinbasePro---
  EnveloppeCoinbasePro = LabelFrame(Fenetre_Paire_ETH_EUR, text="D'après CoinbasePro", padx=5, pady=5)    #Création d'une "Zone Frame" à Label
  EnveloppeCoinbasePro.pack(fill="both", expand="no")
  tk_tk_Prix_Moins_Eleve_24h = Label(EnveloppeCoinbasePro, text=tk_Prix_Moins_Eleve_24h)
  tk_tk_Prix_Actuel = Label(EnveloppeCoinbasePro, text=tk_Prix_Actuel)
  tk_tk_Prix_Plus_Eleve_24h = Label(EnveloppeCoinbasePro, text=tk_Prix_Plus_Eleve_24h)
  tk_tk_Volume_Monnaie_30DAY = Label(EnveloppeCoinbasePro, text=tk_Volume_Monnaie_30DAY)
  tk_tk_Liquidite_Achat = Label(EnveloppeCoinbasePro, text=tk_Liquidite_Achat)
  tk_tk_Liquidite_Vente = Label(EnveloppeCoinbasePro, text=tk_Liquidite_Vente)
  tk_tk_Prix_Moins_Eleve_24h.pack()
  tk_tk_Prix_Actuel.pack()
  tk_tk_Prix_Plus_Eleve_24h.pack()
  tk_tk_Volume_Monnaie_30DAY.pack()
  tk_tk_Liquidite_Achat.pack()
  tk_tk_Liquidite_Vente.pack()
  Button(Fenetre_Paire_ETH_EUR, text="Fermer", command=Fenetre_Paire_ETH_EUR.destroy).pack()
  #---Zone CoinbasePro---
  #---ETH_EUR---

  #---LINK_USD---
 def Recherche_LINK_USD():
  #create child window
  Fenetre_Paire_LINK_USD = Toplevel()
  #Recuperation des Informations
  tk_Symbole_Coin_cryptonator,tk_Prix_Actuel_cryptonator,tk_Volume_24h_cryptonator,tk_Difference_Prix_24h_cryptonator,tk_Volume_Monnaie_30DAY,tk_Prix_Moins_Eleve_24h,tk_Prix_Actuel,tk_Prix_Plus_Eleve_24h,tk_Liquidite_Achat,tk_Liquidite_Vente = Recherche_Info_Coin("LINK-USD")
  #Traitement de l'Affichage des Informations
  tk_tk_Symbole_Coin_cryptonator = Label(Fenetre_Paire_LINK_USD, text=tk_Symbole_Coin_cryptonator)
  #---Zone Cryptonator---
  EnveloppeCryptonator = LabelFrame(Fenetre_Paire_LINK_USD, text="D'après Cryptonator", padx=5, pady=5)    #Création d'une "Zone Frame" à Label
  EnveloppeCryptonator.pack(fill="both", expand="no")
  tk_tk_Prix_Actuel_cryptonator = Label(EnveloppeCryptonator, text=tk_Prix_Actuel_cryptonator)
  tk_tk_Volume_24h_cryptonator = Label(EnveloppeCryptonator, text=tk_Volume_24h_cryptonator)
  tk_tk_Difference_Prix_24h_cryptonator = Label(EnveloppeCryptonator, text=tk_Difference_Prix_24h_cryptonator)
  tk_tk_Prix_Actuel_cryptonator.pack()
  tk_tk_Volume_24h_cryptonator.pack()
  tk_tk_Difference_Prix_24h_cryptonator.pack()
  #---Zone Cryptonator---
  #---Zone CoinbasePro---
  EnveloppeCoinbasePro = LabelFrame(Fenetre_Paire_LINK_USD, text="D'après CoinbasePro", padx=5, pady=5)    #Création d'une "Zone Frame" à Label
  EnveloppeCoinbasePro.pack(fill="both", expand="no")
  tk_tk_Prix_Moins_Eleve_24h = Label(EnveloppeCoinbasePro, text=tk_Prix_Moins_Eleve_24h)
  tk_tk_Prix_Actuel = Label(EnveloppeCoinbasePro, text=tk_Prix_Actuel)
  tk_tk_Prix_Plus_Eleve_24h = Label(EnveloppeCoinbasePro, text=tk_Prix_Plus_Eleve_24h)
  tk_tk_Volume_Monnaie_30DAY = Label(EnveloppeCoinbasePro, text=tk_Volume_Monnaie_30DAY)
  tk_tk_Liquidite_Achat = Label(EnveloppeCoinbasePro, text=tk_Liquidite_Achat)
  tk_tk_Liquidite_Vente = Label(EnveloppeCoinbasePro, text=tk_Liquidite_Vente)
  tk_tk_Prix_Moins_Eleve_24h.pack()
  tk_tk_Prix_Actuel.pack()
  tk_tk_Prix_Plus_Eleve_24h.pack()
  tk_tk_Volume_Monnaie_30DAY.pack()
  tk_tk_Liquidite_Achat.pack()
  tk_tk_Liquidite_Vente.pack()
  Button(Fenetre_Paire_LINK_USD, text="Fermer", command=Fenetre_Paire_LINK_USD.destroy).pack()
  #---Zone CoinbasePro---
  #---LINK_USD---

  #---LINK_EUR---
 def Recherche_LINK_EUR():
  #create child window
  Fenetre_Paire_LINK_EUR = Toplevel()
  #Recuperation des Informations
  tk_Symbole_Coin_cryptonator,tk_Prix_Actuel_cryptonator,tk_Volume_24h_cryptonator,tk_Difference_Prix_24h_cryptonator,tk_Volume_Monnaie_30DAY,tk_Prix_Moins_Eleve_24h,tk_Prix_Actuel,tk_Prix_Plus_Eleve_24h,tk_Liquidite_Achat,tk_Liquidite_Vente = Recherche_Info_Coin("LINK-EUR")
  #Traitement de l'Affichage des Informations
  tk_tk_Symbole_Coin_cryptonator = Label(Fenetre_Paire_LINK_EUR, text=tk_Symbole_Coin_cryptonator)
  #---Zone Cryptonator---
  EnveloppeCryptonator = LabelFrame(Fenetre_Paire_LINK_EUR, text="D'après Cryptonator", padx=5, pady=5)    #Création d'une "Zone Frame" à Label
  EnveloppeCryptonator.pack(fill="both", expand="no")
  tk_tk_Prix_Actuel_cryptonator = Label(EnveloppeCryptonator, text=tk_Prix_Actuel_cryptonator)
  tk_tk_Volume_24h_cryptonator = Label(EnveloppeCryptonator, text=tk_Volume_24h_cryptonator)
  tk_tk_Difference_Prix_24h_cryptonator = Label(EnveloppeCryptonator, text=tk_Difference_Prix_24h_cryptonator)
  tk_tk_Prix_Actuel_cryptonator.pack()
  tk_tk_Volume_24h_cryptonator.pack()
  tk_tk_Difference_Prix_24h_cryptonator.pack()
  #---Zone Cryptonator---
  #---Zone CoinbasePro---
  EnveloppeCoinbasePro = LabelFrame(Fenetre_Paire_LINK_EUR, text="D'après CoinbasePro", padx=5, pady=5)    #Création d'une "Zone Frame" à Label
  EnveloppeCoinbasePro.pack(fill="both", expand="no")
  tk_tk_Prix_Moins_Eleve_24h = Label(EnveloppeCoinbasePro, text=tk_Prix_Moins_Eleve_24h)
  tk_tk_Prix_Actuel = Label(EnveloppeCoinbasePro, text=tk_Prix_Actuel)
  tk_tk_Prix_Plus_Eleve_24h = Label(EnveloppeCoinbasePro, text=tk_Prix_Plus_Eleve_24h)
  tk_tk_Volume_Monnaie_30DAY = Label(EnveloppeCoinbasePro, text=tk_Volume_Monnaie_30DAY)
  tk_tk_Liquidite_Achat = Label(EnveloppeCoinbasePro, text=tk_Liquidite_Achat)
  tk_tk_Liquidite_Vente = Label(EnveloppeCoinbasePro, text=tk_Liquidite_Vente)
  tk_tk_Prix_Moins_Eleve_24h.pack()
  tk_tk_Prix_Actuel.pack()
  tk_tk_Prix_Plus_Eleve_24h.pack()
  tk_tk_Volume_Monnaie_30DAY.pack()
  tk_tk_Liquidite_Achat.pack()
  tk_tk_Liquidite_Vente.pack()
  Button(Fenetre_Paire_LINK_EUR, text="Fermer", command=Fenetre_Paire_LINK_EUR.destroy).pack()
  #---Zone CoinbasePro---
  #---LINK_EUR---


 #Les Boutons de Selections
 Button(EnveloppeSelection, text="BTC-USD", command=Recherche_BTC_USD).pack()
 Button(EnveloppeSelection, text="BTC-EUR", command=Recherche_BTC_EUR).pack()

 Button(EnveloppeSelection, text="ETH-USD", command=Recherche_ETH_USD).pack()
 Button(EnveloppeSelection, text="ETH-EUR", command=Recherche_ETH_EUR).pack()

 Button(EnveloppeSelection, text="LINK-USD", command=Recherche_LINK_USD).pack()
 Button(EnveloppeSelection, text="LINK-EUR", command=Recherche_LINK_EUR).pack()

 #----------------------------------------Zone de Recherche Manuel----------------------------------------
 #Bar de Recherche
 #Fonction permettant de recuperer la valeur écrite dans la bar de recherche par l'Utilisateur
 #--Recherche_de_la_Paire----
 def Recherche_de_la_Paire(Paire_Indiquee):
  #create child window
  Fenetre_Recherche_de_la_Paire = Toplevel()

  #Recuperation des Informations
  tk_Symbole_Coin_cryptonator,tk_Prix_Actuel_cryptonator,tk_Volume_24h_cryptonator,tk_Difference_Prix_24h_cryptonator,tk_Volume_Monnaie_30DAY,tk_Prix_Moins_Eleve_24h,tk_Prix_Actuel,tk_Prix_Plus_Eleve_24h,tk_Liquidite_Achat,tk_Liquidite_Vente = Recherche_Info_Coin(Paire_Indiquee)

  #Traitement de l'Affichage des Informations
  tk_tk_Symbole_Coin_cryptonator = Label(Fenetre_Recherche_de_la_Paire, text=tk_Symbole_Coin_cryptonator)

  #---Zone Cryptonator---
  EnveloppeCryptonator = LabelFrame(Fenetre_Recherche_de_la_Paire, text="D'après Cryptonator", padx=5, pady=5)    #Création d'une "Zone Frame" à Label
  EnveloppeCryptonator.pack(fill="both", expand="no")
  
  tk_tk_Prix_Actuel_cryptonator = Label(EnveloppeCryptonator, text=tk_Prix_Actuel_cryptonator)
  tk_tk_Volume_24h_cryptonator = Label(EnveloppeCryptonator, text=tk_Volume_24h_cryptonator)
  tk_tk_Difference_Prix_24h_cryptonator = Label(EnveloppeCryptonator, text=tk_Difference_Prix_24h_cryptonator)

  tk_tk_Prix_Actuel_cryptonator.pack()
  tk_tk_Volume_24h_cryptonator.pack()
  tk_tk_Difference_Prix_24h_cryptonator.pack()
  #---Zone Cryptonator---

  #---Zone CoinbasePro---
  EnveloppeCoinbasePro = LabelFrame(Fenetre_Recherche_de_la_Paire, text="D'après CoinbasePro", padx=5, pady=5)    #Création d'une "Zone Frame" à Label
  EnveloppeCoinbasePro.pack(fill="both", expand="no")

  tk_tk_Prix_Moins_Eleve_24h = Label(EnveloppeCoinbasePro, text=tk_Prix_Moins_Eleve_24h)
  tk_tk_Prix_Actuel = Label(EnveloppeCoinbasePro, text=tk_Prix_Actuel)
  tk_tk_Prix_Plus_Eleve_24h = Label(EnveloppeCoinbasePro, text=tk_Prix_Plus_Eleve_24h)
  tk_tk_Volume_Monnaie_30DAY = Label(EnveloppeCoinbasePro, text=tk_Volume_Monnaie_30DAY)
  tk_tk_Liquidite_Achat = Label(EnveloppeCoinbasePro, text=tk_Liquidite_Achat)
  tk_tk_Liquidite_Vente = Label(EnveloppeCoinbasePro, text=tk_Liquidite_Vente)

  tk_tk_Prix_Moins_Eleve_24h.pack()
  tk_tk_Prix_Actuel.pack()
  tk_tk_Prix_Plus_Eleve_24h.pack()
  tk_tk_Volume_Monnaie_30DAY.pack()
  tk_tk_Liquidite_Achat.pack()
  tk_tk_Liquidite_Vente.pack()

  Button(Fenetre_Recherche_de_la_Paire, text="Fermer", command=Fenetre_Recherche_de_la_Paire.destroy).pack()
  #---Zone CoinbasePro---
  #--Recherche_de_la_Paire----     

 def recuperation_input():
     Paire_Selectionee=textBox.get("1.0","end-1c")      #Recuperation de la Valeur saisie dans la boite a texte
     print(Paire_Selectionee)                           #Affichage de cette valeur dans la console
     Recherche_de_la_Paire(Paire_Selectionee)           #Obtention des Informations du Coin/Token sur le marché par rapport au Informations saisie dans la boite a texte

 Exemple_Paires = Label(EnveloppeSelection, text= "Effectué une Recherche \n Ex: XLM-EUR")              #Affichage d'un texte d'information
 Exemple_Paires.pack()                                                                                  #Positionement Automatique du widget
 textBox=Text(EnveloppeSelection,height=1, width=13)                                                    #Affichage de la boite a texte
 textBox.pack()                                                                                         #Positionnement Automatique de la boite a texte
 Button(EnveloppeSelection, height=1, width=13, text="Go!",command=lambda: recuperation_input()).pack() #Affichage et Positionnement automatique du Bouton d'envoie de la valeur contenue dans la boite a texte
 #command=lambda: recuperation_input() >>> just means do this when i press the button
#----------------------------------------Zone de Recherche Manuel----------------------------------------
 Button(Selection_de_la_Paire, text="Fermer", command=Selection_de_la_Paire.destroy).pack()                                   #Affichage et Positionnement automatique du Bouton permettant de Fermer la fenetre "Selection_de_la_Paire"
#------------------------------------------------------------------------------
def Fenetre_Surveillance_de_la_Paire():
 #create child window
 global Surveillance_de_la_Paire

 Surveillance_de_la_Paire = Toplevel()                                                                                        #Declaration d'une Nouvelle fenetre

 #Zone d'Affichage
 #ALPHA_STATE_Label = Label(Surveillance_de_la_Paire, text="PRE-ALPHA \n")
 #ALPHA_STATE_Label.pack() 
 Presentation_Label = Label(Surveillance_de_la_Paire, text="Votre Alerte \n")
 Presentation_Label.pack()  
 EnveloppeSurveillance = LabelFrame(Surveillance_de_la_Paire, text="Etablir une Surveillance", padx=5, pady=5)                #Création d'une "Zone Frame" à Label
 EnveloppeSurveillance.pack(fill="both", expand="no")                                                                         #Positionnement Automatique avec des parametres pour la éZone Frame"

 #Zone de Saisie
 #Saisir la Paire a Surveiller
 Saisie_Paire = Label(EnveloppeSurveillance, text="Saisir la Paire à Surveiller en Temps-Réel:")
 Saisie_Paire.pack()

 Saisie_Paire_textBox=Text(EnveloppeSurveillance,height=1, width=13)                                                          #Affichage de la boite a texte
 Saisie_Paire_textBox.pack()                                                                                                  #Positionnement Automatique de la boite a texte

 #Button(EnveloppeSurveillance, height=1, width=13, text="Enregistrement",command=lambda: recuperation_input()).pack()        #Affichage et Positionnement automatique du Bouton d'envoie de la valeur contenue dans la boite a texte
 ##command=lambda: recuperation_input() >>> just means do this when i press the button

 #Saisir le Montant a Surveiller
 Saisie_Montant = Label(EnveloppeSurveillance, text="Saisir le Montant à Surveiller en Temps-Réel:")
 Saisie_Montant.pack()

 Saisie_Montant_textBox=Text(EnveloppeSurveillance,height=1, width=13)                                                        #Affichage de la boite a texte
 Saisie_Montant_textBox.pack()                                                                                                #Positionnement Automatique de la boite a texte
 
 #Saisir un Message Personnaliser a afficher
 Saisie_Message_Personnaliser = Label(EnveloppeSurveillance, text="Indiquer un Message? ")
 Saisie_Message_Personnaliser.pack()

 Saisie_Message_Personnaliser_textBox=Text(EnveloppeSurveillance,height=3, width=33)                                          #Affichage de la boite a texte
 Saisie_Message_Personnaliser_textBox.pack()                                                                                  #Positionnement Automatique de la boite a texte

 Button(EnveloppeSurveillance, height=1, width=16, text="Placer la Surveillance",command=lambda: recuperation_input()).pack() #Affichage et Positionnement automatique du Bouton d'envoie de la valeur contenue dans la boite a texte
 ##command=lambda: recuperation_input() >>> just means do this when i press the button

 #Recuperation    
 def recuperation_input():
  Recuperation_Paire=Saisie_Paire_textBox.get("1.0","end-1c")                                                              #Recuperation de la Valeur saisie dans la boite a texte
  Recuperation_Montant=Saisie_Montant_textBox.get("1.0","end-1c")                                                          #Recuperation de la Valeur saisie dans la boite a texte
  Recuperation_Message_Personnaliser=Saisie_Message_Personnaliser_textBox.get("1.0","end-1c")                              #Recuperation de la Valeur saisie dans la boite a texte
  print(Recuperation_Paire +" " + Recuperation_Montant +" "+ Recuperation_Message_Personnaliser)                           #Affichage de cette valeur dans la console
  Affichage_Etat_Surveillance(Recuperation_Paire,Recuperation_Montant,Recuperation_Message_Personnaliser)                  #On donne les information saisie a cette fonction pour traitement

 def Affichage_Etat_Surveillance(Recuperation_Paire,Recuperation_Montant,Recuperation_Message_Personnaliser):
  global Surveillance_en_cours_de_la_Paire
  Surveillance_en_cours_de_la_Paire = Toplevel()
  Enveloppe_Etat_Surveillance = LabelFrame(Surveillance_en_cours_de_la_Paire, text="Surveillance En Cours", padx=5, pady=5) #Création d'une "Zone Frame" à Label
  Enveloppe_Etat_Surveillance.pack(fill="both", expand="no")                                                                #Positionnement Automatique avec des parametres pour la éZone Frame"

  #Recuperation des Informations
  tk_Annonce_0 , tk_Annonce_1 , tk_Message_Personnaliser, boolean_popup = Recherche_Et_Surveillance_Coin(Recuperation_Paire,Recuperation_Montant,Recuperation_Message_Personnaliser)
  
  #Affichage
  tk_tk_Annonce_0 = Label(Enveloppe_Etat_Surveillance, text=tk_Annonce_0)
  tk_tk_Annonce_1 = Label(Enveloppe_Etat_Surveillance, text=tk_Annonce_1)
  tk_tk_Message_Personnaliser = Label(Enveloppe_Etat_Surveillance, text=tk_Message_Personnaliser)

  tk_tk_Annonce_0.pack()
  tk_tk_Annonce_1.pack()

  tk_tk_Message_Personnaliser.pack()

  #Rafraichissement des Informations
  def update_Affichage_Etat_Surveillance(Recuperation_Paire,Recuperation_Montant,Recuperation_Message_Personnaliser):
   tk_tk_Annonce_0["text"] , tk_tk_Annonce_1["text"] , tk_tk_Message_Personnaliser["text"] , boolean_popup = Recherche_Et_Surveillance_Coin(Recuperation_Paire,Recuperation_Montant,Recuperation_Message_Personnaliser)
   #Activation du Pop-up sous condition
   if boolean_popup  == True:                                                                                  #Si le boolean retournée par le fonction de recherche est vrai alors un jingle retentie et un pop-up apparait
    print("Surveillance Fruictueuse, Lancement du Jingle + Pop-Up d'Alerte!")                                  #Message visible dans la console
    #~Jingle
    Alerte_popup= AudioSegment.from_mp3("/home/"+USERNAME+"/CryptoWatch-Tkinter/Services/Sounds/MSN_WIZZ.mp3")         #Chargement du Jingle d'Alerte
    play(Alerte_popup)                                                                                         #Lecture de ce Jingle d'Alerte
    #~Jingle
    showinfo(tk_Annonce_0 , tk_Annonce_1 +"\nMessage Personnaliser: "+ tk_Message_Personnaliser)               #Declenchement du Pop-up d'Alerte
    
   Surveillance_en_cours_de_la_Paire.after(2048 , lambda: update_Affichage_Etat_Surveillance(Recuperation_Paire,Recuperation_Montant,Recuperation_Message_Personnaliser)) #Raffraichissement des informations inclue dans la fenetre de surveillance de la paire toute les 2,48 secondes
   
  #Button de la Fenetre de Surveillance en cours
  Button(Surveillance_en_cours_de_la_Paire, text="Démarrer la Surveillance Maintenant", command=lambda: update_Affichage_Etat_Surveillance(Recuperation_Paire,Recuperation_Montant,Recuperation_Message_Personnaliser)).pack()  #Le mot-cle "LAMBDA" suivi de ":" permet de lancer le deroulement (l'actualisation) d'une fonction ayant des membre comme dans ce cas precis
  Button(Surveillance_en_cours_de_la_Paire,text="Arrêter la Surveillance Maintenant", command=Surveillance_en_cours_de_la_Paire.destroy).pack()
 #Bouton de Fermeture
 Button(Surveillance_de_la_Paire, text="Fermer", command=Surveillance_de_la_Paire.destroy).pack()               #Affichage et Positionnement automatique du Bouton permettant de Fermer la fenetre "Selection_de_la_Paire"

#------------------------------------------------------------------------------
def Fenetre_Graph_de_la_Crypto():
 #create child window
 global Graph_de_la_Crypto
 Graph_de_la_Crypto = Toplevel()

 #Zone d'Affichage
 Presentation_Label = Label(Graph_de_la_Crypto, text="Obtenir un Graphique avec CoinMarketCap \n")
 Presentation_Label.pack()
 
 #Un Bug a ete signaler a l'equipe de developpement , en attente de correction (https://tinyurl.com/bugCMC19)
 BugSignale_Label = Label(Graph_de_la_Crypto, text="The Bug reported here: https://tinyurl.com/bugCMC19")
 BugSignale_Label.pack()

 EnveloppeGraph = LabelFrame(Graph_de_la_Crypto, text="Informations Necessaires", padx=5, pady=5)        #Création d'une "Zone Frame" à Label
 EnveloppeGraph.pack(fill="both", expand="no")                                                           #Positionnement Automatique avec des parametres pour la éZone Frame"

 #Zone de Saisie
 #Saisir la Crypto-Monnaie a Observer
 Saisie_Crypto = Label(EnveloppeGraph, text="Saisir le Nom ENTIER de la crypto à Observer: \n Ex: Bitcoin")
 Saisie_Crypto.pack()
 Saisie_Crypto_textBox=Text(EnveloppeGraph,height=1, width=13)                                           #Affichage de la boite a texte
 Saisie_Crypto_textBox.pack()                                                                            #Positionnement Automatique de la boite a texte

 #Saisir la Date du Debut du Graphique a afficher
 Saisie_Date_Debut = Label(EnveloppeGraph, text="Saisir la Date du début du Graph: \n Ex: YYYY-MM-DD")
 Saisie_Date_Debut.pack()
 Saisie_Date_Debut_textBox=Text(EnveloppeGraph,height=1, width=13)                                       #Affichage de la boite a texte
 Saisie_Date_Debut_textBox.pack()                                                                        #Positionnement Automatique de la boite a texte
 
 #Saisir la Date de Fin du Graphique a afficher
 Saisie_Date_Fin = Label(EnveloppeGraph, text="Saisir la Date de Fin du Graph")
 Saisie_Date_Fin.pack()
 Saisie_Date_Fin_textBox=Text(EnveloppeGraph,height=1, width=13)                                         #Affichage de la boite a texte
 Saisie_Date_Fin_textBox.pack() 

 Button(EnveloppeGraph, height=1, width=16, text="Obtention du Graph",command=lambda: recuperation_input()).pack() #Affichage et Positionnement automatique du Bouton d'envoie de la valeur contenue dans la boite a texte
 ##command=lambda: recuperation_input() >>> just means do this when i press the button

 #Recuperation    
 def recuperation_input():
  Recuperation_Crypto=Saisie_Crypto_textBox.get("1.0","end-1c")                                           #Recuperation de la Valeur saisie dans la boite a texte
  Recuperation_Date_Debut=Saisie_Date_Debut_textBox.get("1.0","end-1c")                                   #Recuperation de la Valeur saisie dans la boite a texte
  Recuperation_Date_Fin=Saisie_Date_Fin_textBox.get("1.0","end-1c")                                       #Recuperation de la Valeur saisie dans la boite a texte
  print(Recuperation_Crypto +" " + Recuperation_Date_Debut +" "+ Recuperation_Date_Fin)                   #Affichage de cette valeur dans la console
  Dessiner_Graph(Recuperation_Crypto,Recuperation_Date_Debut,Recuperation_Date_Fin)                       #On donne les information saisie a cette fonction pour traitement

 #Bouton de Fermeture
 Button(Graph_de_la_Crypto, text="Fermer", command=Graph_de_la_Crypto.destroy).pack() 
#------------------------------------------------------------------------------
Button(fenetre, text="En Direct du Marché", command=Fenetre_Selection_de_la_Paire).pack()        #Bouton pour Ouvrir la fenêtre "En Direct du Marche"
Button(fenetre, text="Surveillance du Marché", command=Fenetre_Surveillance_de_la_Paire).pack()  #Bouton pour Ouvrir la fenêtre "Surveillance du Marche" 
Button(fenetre, text="Visualiser le Cours du Marché", command=Fenetre_Graph_de_la_Crypto).pack() #Bouton pour Ouvrir la fenêtre "Visualiser le Cours du Marche"
#-------------------------------------------------------------------Contenue Fenetres Secondaires-------------------------------------------------------------------


if __name__ == "__main__":
    try:
        clear_cache()
        #-------------------------------------------------------------------Demarrage des fonctions operant sur la Fenetre Principale-------------------------------------------------------------------
        #Récupération des informations pour la Mise à jour du LABEL toute les 1 milliseconde quand la fenêtre Maitre est lancée
        fenetre.after(1, update_temps_actuel)               #update_temps_actuel()
        fenetre.after(1, update_information_Materiel)       #update_information_Materiel()
        fenetre.after(1, update_information_Complementaire) #update_information_Complementaire()
        #fenetre.after(1, update_refresh_FGI)               #update_refresh_FGI()        
        fenetre.mainloop()                                  #Boucle de Lancement de la Fenêtre PRINCIPAL
        #-------------------------------------------------------------------Demarrage des fonctions operant sur la Fenetre Principale---------------------------------------------------------------       
        #Surveillance_en_cours_de_la_Paire.after(2048 , None)
        pass
    #---!!!GESTION DES ERREURS!!!---
    except TypeError:
     print("Code Erreur: TypeError")
     clear_cache()
    except KeyError:
     print("Code Erreur: KeyError")
     clear_cache()      
    except ValueError:
     print("Code Erreur: ValueError")
     clear_cache()
    except AssertionError:
     print("Code Erreur: AssertionError")
     clear_cache()
    except NameError:
     print("Il est necessaire de Redemarrez le Programme!")                          #On affiche ce message dans la console
     print("Code Erreur: NameError")
     clear_cache()
    except:
     print("Il est necessaire de Redemarrez le Logiciel!")                           #On affiche ce message dans la console
     print("Code Erreur: Aucun")
     clear_cache()
    #---!!!GESTION DES ERREURS!!!---

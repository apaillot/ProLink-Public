# -*- coding: utf-8 -*-
#============================================================================#
# Fichier .........: "HTTPUpdate.py"
# Auteur ..........: Alexandre Paillot
# Date de création : 2024/06/17
#----------------------------------------------------------------------------#
''' Description :
    Mise à jour du logiciel PC.

'''
#============================================================================#

#============================================================================#
# Librairies système
#============================================================================#
import sys, os, time
from urllib.request import urlopen
import ssl
import subprocess

#============================================================================#
# Librairies Qt
#============================================================================#
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, Slot, QThread, Signal, QObject )
from PySide6.QtWidgets import *

#============================================================================#
# Librairies Utilisateur
#============================================================================#

#============================================================================#
# Variable
#============================================================================#

#============================================================================#
# Code
#============================================================================#
try:
 _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
 # Legacy Python that doesn't verify HTTPS certificates by default
 pass
else:
 # Handle target environment that doesn't support HTTPS verification
 ssl._create_default_https_context = _create_unverified_https_context

#============================================================================#
# Classe
#============================================================================#

#------------------------------------------------------------------------
# Classe HTTP Update
#------------------------------------------------------------------------
class Downloader(QThread):
 # Taille fichier
 setTotalProgress = Signal(int)
 # Avancement téléchargement
 setCurrentProgress = Signal(int)
 # Fin de téléchargement
 succeeded = Signal(bytes)

 #----------------------------------------------
 # Init
 #----------------------------------------------
 def __init__(self, url, filename, bReadOnly):
  super().__init__()
  self._url = url
  self._filename = filename
  self.bReadOnly = bReadOnly

 #----------------------------------------------
 # Lancement du téléchargement
 #----------------------------------------------
 def run(self):
  # URL complète
  url = self._url+self._filename
  filename = self._filename
  readBytes = 0
  uiChunkSize = 1024*32
  sContent  = bytearray()

  # Si pas lecture seul
  if( not self.bReadOnly ):
   # Réinit du fichier
   with open(filename, "wb") as f:
    f.write(b"")

  print(url)
  # Open the URL address.
  with urlopen(url) as r:
   # Tell the window the amount of bytes to be downloaded.
   print( int(r.info()["Content-Length"]) )
   self.setTotalProgress.emit(int(r.info()["Content-Length"]))
   # Pas lecture seul
   if( not self.bReadOnly ):
    with open(filename, "ab") as f:
     # On boucle
     while True:
      # Read a piece of the file we are downloading.
      xChunk = r.read(uiChunkSize)
      # If the result is `None`, that means data is not
      # downloaded yet. Just keep waiting.
      if xChunk is None:
       print("xChunk is None")
       continue
      # If the result is an empty `bytes` instance, then
      # the file is complete.
      elif xChunk == b"":
       print('xChunk == b""')
       break
      # Write into the local file the downloaded chunk.
      f.write(xChunk)
      readBytes += uiChunkSize
      sContent  += xChunk
      # Tell the window how many bytes we have received.
      self.setCurrentProgress.emit(readBytes)
   # Lecture seul
   else:
    # On boucle
    while True:
     # Read a piece of the file we are downloading.
     xChunk = r.read(uiChunkSize)
     # If the result is `None`, that means data is not
     # downloaded yet. Just keep waiting.
     if xChunk is None:
      print("xChunk is None")
      continue
     # If the result is an empty `bytes` instance, then
     # the file is complete.
     elif xChunk == b"":
      print('xChunk == b""')
      break
     readBytes += uiChunkSize
     sContent  += xChunk
     # Tell the window how many bytes we have received.
     self.setCurrentProgress.emit(readBytes)

  ''''''
  # If this line is reached then no exception has ocurred in
  # the previous lines.
  self.succeeded.emit(sContent)

#------------------------------------------------------------------------
# Classe HTTP Update
#------------------------------------------------------------------------
class HTTPUpdate(QObject):
 # Signaux
 siUpdateDetected   = Signal(str)
 siUpdateEndSuccess = Signal()
 siUpdateError      = Signal(str)
 siCurrentProgress  = Signal(int, int)
 siTotalProgress    = Signal(int, str, int)

 #----------------------------------------------
 # Init
 #----------------------------------------------
 def __init__( self, tINIConfig, parent=None ):
  # Init héritage
  super().__init__(parent)

  print("Init HTTP Update")
  # Variable
  #self.sHTTPPath    = "https://support.nke-instrumentation.com/Update/Aquaread/SondeLinkV2/TestBE/"
  self.sHTTPPath        = tINIConfig.tConfig["UPDATE"]["httppath"]
  self.sFileVersion     = "Version.txt"
  self.sReceivedVersion = ""

  #self._view.ui.connect_btn.clicked.connect(self.testClicked3)
  # Init thread
  self.downloader = None

 #-------------------------------------------------------------
 # Démarrage de la vérification de mise à jour
 #-------------------------------------------------------------
 def startUpdateCheck( self, sSoftwareVersion ):
  print("-- startUpdateCheck --")
  # Conservation numéro de version
  self.sSoftwareVersion = sSoftwareVersion
  # Création d'un thread pour le télechargement
  self.downloader = Downloader( self.sHTTPPath,
                                self.sFileVersion,
                                bReadOnly=True )
  # Connexion signaux de fin
  self.downloader.succeeded.connect(self.startUpdateCheckDownloadSucceeded)
  self.downloader.finished.connect(self.startUpdateCheckDownloadFinished)
  self.downloader.start()
 #-------------------------------------------------------------
 # Fin du téléchargement
 #-------------------------------------------------------------
 def startUpdateCheckDownloadSucceeded(self, sFileContent):
  print("-- startUpdateCheckDownloadSucceeded --")
  print(sFileContent)
  # Conservation numéro de version
  self.sReceivedVersion = sFileContent.decode("utf-8")
  # Set the progress at 100%.
  #self.progressBar.setValue(self.progressBar.maximum())
  #self.label.setText("The file has been downloaded!")
 #-------------------------------------------------------------
 # Fin du thread
 #-------------------------------------------------------------
 def startUpdateCheckDownloadFinished(self):
  print("-- startUpdateCheckDownloadFinished --")
  # Restore the button.
  #self.button.setEnabled(True)
  # Delete the thread when no longer needed.
  del self.downloader
  # Comparaison version
  if(   ( self.sReceivedVersion != "" )
    and ( self.sSoftwareVersion != self.sReceivedVersion ) ):
   print("Différent")
   self.siUpdateDetected.emit(self.sReceivedVersion)

 #-------------------------------------------------------------
 # Démarrage de mise à jour
 #-------------------------------------------------------------
 def startUpdate( self ):
  print("-- startUpdate --")
  # On va demander la liste des fichiers
  print(self.sHTTPPath+"V"+self.sReceivedVersion+"/")
  # Création d'un thread pour le télechargement
  self.downloader = Downloader( self.sHTTPPath+"V"+self.sReceivedVersion+"/",
                                "updatelist.txt",
                                bReadOnly=True )
  # Connexion signaux de fin
  self.downloader.succeeded.connect(self.startUpdateDownloadSucceeded)
  self.downloader.finished.connect(self.startUpdateDownloadFinished)
  self.downloader.start()
 #-------------------------------------------------------------
 def startUpdateDownloadSucceeded( self, sFileContent ):
  print("-- startUpdateDownloadSucceeded --")
  self.sFileList = sFileContent.decode("utf-8")
  print(sFileContent)
  # Conservation numéro de version
  #self.sReceivedVersion = sFileContent
 #-------------------------------------------------------------
 def startUpdateDownloadFinished( self ):
  print("-- startUpdateDownloadFinished --")
  # Delete the thread when no longer needed.
  del self.downloader
  # Controle
  if(len(self.sFileList)<3):
   print("Pas de fichier de mise à jour")
   return
  # Trie de la liste de fichier reçu
  tFileList = self.sFileList.split("\r\n")
  print( tFileList )
  self.tFileObj = []
  print("len(tFileList) = %d"%len(tFileList))
  # Parcourt de la liste
  for uiFileCpt in range(len(tFileList)):
   tLine = tFileList[uiFileCpt].split(",")
   self.tFileObj.append({ "size":tLine[0], "filename":tLine[1], "dummy":tLine[2] })
  print("-- Objet final --")
  # Parcourt de la liste
  for uiFileCpt in range(len(self.tFileObj)):
   print(self.tFileObj[uiFileCpt]["filename"])
   print(self.tFileObj[uiFileCpt]["size"])

  # Init du compteur de téléchargement de fichier
  self.uiFileDownloadCpt = 0
  # Lancement télechargement des fichiers
  self.startUpdateFileDownload()

 #-------------------------------------------------------------
 # Téléchargement des différents fichiers
 #-------------------------------------------------------------
 def startUpdateFileDownload( self ):
  print("-- startUpdateFileDownload --")
  # Test s'il reste des fichiers à télécharger
  if( self.uiFileDownloadCpt < len(self.tFileObj) ):
   print("self.uiFileDownloadCpt = %d" % self.uiFileDownloadCpt)

   # Création d'un thread pour le télechargement
   self.downloader = Downloader( self.sHTTPPath+"V"+self.sReceivedVersion+"/",
                                 self.tFileObj[self.uiFileDownloadCpt]["filename"],
                                 bReadOnly=False )
   # Connexion signaux de fin
   self.downloader.succeeded.connect(self.startUpdateFileDownloadSucceeded)
   self.downloader.finished.connect(self.startUpdateFileDownloadFinished)
   self.downloader.setCurrentProgress.connect(self.startUpdateFileDownloadProgress)

   self.downloader.setTotalProgress.connect(self.startUpdateFileDownloadTotalProgress)


   self.downloader.start()
   return
  print("== FINI ==")

  # Controle des fichiers télechargés
  for uiCpt in range( len(self.tFileObj) ):
   # Test si fichier bien créé
   if( not os.path.exists( self.tFileObj[uiCpt]["filename"] ) ):
    # Erreur
    self.siUpdateError.emit("Error file not downloaded")
    return
   if( int(os.path.getsize( self.tFileObj[uiCpt]["filename"]) ) != int(self.tFileObj[uiCpt]["size"]) ):
    # Erreur
    self.siUpdateError.emit("Error wrong file size")
    print('os.path.getsize( self.tFileObj[uiCpt]["filename"] )')
    print(os.path.getsize( self.tFileObj[uiCpt]["filename"] ))
    print('self.tFileObj[uiCpt]["size"]')
    print( self.tFileObj[uiCpt]["size"] )

    return

  # Envoi du signal de fin
  self.siUpdateEndSuccess.emit()
  try:
   print( "TRY .\ProLink.exe" )
   # Lancement du launcher
   subprocess.Popen([r".\ProLink.exe"])
   # On quitte l'application
   QCoreApplication.quit()
  except Exception as err:
   print(err)

 #-------------------------------------------------------------
 def startUpdateFileDownloadTotalProgress( self, uiTotalBytes ):
  print("-- startUpdateFileDownloadTotalProgress --")
  print("uiTotalBytes = %d"%uiTotalBytes)
  self.siTotalProgress.emit( uiTotalBytes, self.tFileObj[self.uiFileDownloadCpt]["filename"], len(self.tFileObj) )
  #self.siCurrentProgress.emit( uiReadBytes, uiTotalBytes, self.uiFileDownloadCpt]["filename"] )
 #-------------------------------------------------------------
 def startUpdateFileDownloadProgress( self, uiReadBytes ):
  #print("-- startUpdateFileDownloadProgress --")
  #print("uiReadBytes = %d"%uiReadBytes)
  self.siCurrentProgress.emit( uiReadBytes, self.uiFileDownloadCpt )
 #-------------------------------------------------------------
 def startUpdateFileDownloadSucceeded( self, sFileContent ):
  # Ouverture/Ecriture fichier
  with open(self.tFileObj[self.uiFileDownloadCpt]["filename"], "wb") as f:
   f.write(sFileContent)
  # Incrément du compteur de fichier
  self.uiFileDownloadCpt = self.uiFileDownloadCpt + 1
 #-------------------------------------------------------------
 def startUpdateFileDownloadFinished( self ):
  print("-- startUpdateFileDownloadFinished --")
  # Delete the thread when no longer needed.
  del self.downloader
  # Relance
  self.startUpdateFileDownload()



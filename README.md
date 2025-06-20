# Aquaread tool
***

* **Projet** : Aquaread tool
* **Auteur** : Alexandre Paillot
* **Date de création** : 2024.01

## Description

IHM de controle sonde Aquaread pour :

* **Page Dashboard** : gestion de configuration.
* **Live view** : visualisation temps réel des mesures des capteurs et des indicateurs.
* **Measurement Files** : accès aux mesures.

## Version/Evolution

### V Proto - 2024 - Développment

#### 2024.06.20  
* Ajout d'une non-restriction de certificat pour mise à jour.  
* Ajout télechargement fichiers pour mise à jour, lancement launcher et coupure logiciel.

#### 2024.06.21 
* Correction bug sur mise à jour : updatelist.txt était à la place de la liste des fichiers. 
* Fin mise à jour : création fenêtres progression et d'erreur.

#### 2024.10.29 
* Résolu problème cadence.
* Corrigé estimatif conso.

#### V0.0.7 - 2024.10.31 - Livré à Aquaread
* Première version béta officielle.

#### V0.0.8 - 2024.11.18
* Liveview - Enregistrement dans fichier du liveview.
* Calibration - Enregistrement dans fichier de la calibration.
* Dashboard - New battery fitted > Rajouter une lecture de configuration après validation. 
* DATA - Par défaut désactiver voies "EMPTY". Ces voies ne sont plus visibles.

### V0.0.9 - 2025.01.09 livré à Aquaread en version Beta.
* General - Début refonte pour intégration Probe et LevelLine.
* General - Refait le positionnement de la fenêtre background sombre.
* General - Mise en place d'une relance quand timeout sur requête.
* General - Changement de theme en "windowvista" pour affichage correct des spinbox dans Windows 11.
* General - Ajout message d'erreur sur requête.
* General - Ajout d'un onglet PC configuration avec changement EC Ref temp/Temp unit/Depth unit/TDS Factor + Grapical Depth.
* General - Lecture/conservation PC Conf dans fichier config.ini.
* General - Ajout de la gestion de la voie Ammonia (Liveview et data).
* Connection - Correction d'un problème de timeout trop court quand deux interrogations successives.
* Connection - Quand ouverture fichier RAW : passer à l'onglet Dashboard une fois ouvert.
* Connection - Disparition des boutons détections quand un type de produit a été sélectionné pour éviter conflit et simplifier la gestion. Relancer le logiciel pour changer.
* Dashboard - Modification du texte "set up logging rate" en "Event logging" pour la dernière boite.
* Dashboard - Renommer titre fenêtre modification paramètre Date et Time.
* Dashboard - Renommer titre fenêtre modification paramètre Event logging.
* Dashboard - Ajout Optical averaging constant paramètre.
* Dashboard - Event logging non autorisé si cadence d'enregistrement est inférieure à la minutes.
* Liveview - Depth - Correction du calcul de la valeur.
* Liveview - ORP - Correction du calcul de la valeur. 
* Liveview - Les axes sont maintenant de la même couleur que les courbes.
* Liveview - Affichage voie calculée paramétrable avec PC Conf.
* Liveview- Export, problème dans le formatage fichier .tab voie SSG et salinity, 
* Liveview - Quand liveview en cours bloquer le changement d'onglet.
* Calibration - Ajout bouton pour reset pour chaque point de calibration.
* Calibration - Ajout du détail des messages d'erreur quand retour flag erreur sonde.
* Calibration - Ajout bouton pour mode RapidCal.
* Calibration - Retour sur la page capteur si erreur calibration.
* Calibration - Création rapport texte calibration.
* Calibration - Wiper - Amélioration/correction fonctionnement avec prise en compte des flags de retour de la sonde.
* Calibration - DO - Utilisation de la valeur saturation (%) au lieu de la concentration pour la calibration.
* Calibration - EC - Prise en compte et affichage du paramètre EC Calibration value.
* Calibration - EC - EC Cal user value n'était pas rempli et ajout des bornes de 100 à 99999.
* Calibration - EC - Bug: mauvaise prise en compte de la valeur EC Cal value.
* Calibration - EC - Au démarrage l'EC Value est sur la valeur de SC35 au lieu de Rapidcal quand calibration fait ainsi.
* Calibration - ORP - Prise en compte du bit de poids fort pour les valeurs négatives.
* Calibration - PH - PH7 Prise en compte du bit de poids fort pour les valeurs négatives.
* Calibration - PH - pHmv n'était pas rempli durant la mesure/calibration pH.
* Calibration - AUX - Prise en compte du bit de poids fort pour les valeurs négatives.
* Calibration - Quand calibration en cours bloquer le changement d'onglet.
* Calibration - pH - pH7 obligatoire avant pH4.01 et pH10 dans la même session.
* Calibration - Tbd - 0 NTU obligatoire avant 1000 NTU et/ou 20 NTU dans la même session.
* Calibration - AUX - Point 1 obligatoire avant point 2 et/ou point 3 dans la même session.
* Data - Les axes sont maintenant de la même couleur que les courbes.
* Data - Ajout de l'export de donnée brut format Aquaread.
* Data - Affichage au format RAW de donnée venant d'un fichier brut.
* Data - Ajout de la lecture de la configuration après lecture mesure pour éviter température aberrante en Liveview ensuite.
* Data - Gérer la réponse de la requête quand 0 donnée dans la sonde.

### V0.0.10 - 2025.01.24 Livré à Aquaread en version Béta
* Calib - DO - Problème sur point 0%, timeout car requête longue.

### V1.0.0 - 2025.03.03 - Livraison Aquaread (première version client)
Sonde :
* Général - Problème sur blocage changement d'onglet quand en Liveview ou calibration en cours.
* Général - >=5.11 - Les anciennes sondes n'étaient pas gérer pour le paramètre Optical Averaging time.
* Général - Actuellement les anciennes sondes ne sont pas gérer pour le paramètre Optical Averaging time.
* Dashboard - Log data period - Valeur maximum à 59 secondes, 59 minutes, 119 heures.
* Dashboard - Cleaning period - Valeur doit être supérieur ou égal à log data period.
* Dashboard - Event logging every - Valeur à 0 minute + 0 heure interdite.
* Dashboard - Event logging every - Valeur à 0 minute + 0 heure interdite.
* Liveview - Cacher bouton set Baro.
* Calibration - Cacher bouton set Baro.
* Config - Les unités ne sont pas modifiées dans les cadres Liveview, faire un lecture configuration après modification de paramètre.

## V1.1.0 - 2025.03.31 - Ajout Probe au logiciel
Probe :
* Général - Ajout Probe au logiciel.
* Général - Problème sur blocage changement d'onglet quand en Liveview ou calibration en cours.
* Général - >=5.11 - Les anciennes probes n'étaient pas gérer pour le paramètre Optical Averaging time.
* General - Ajout AquaPlus - DO/EC uniquement.
* General - Ajout AP-Lite - AUX 1 uniquement.
* General - Si inférieur à V4.5x sur probe autre que AquaPlus => Erreur.
* Calibration - Prise en compte de la pression pour O2. Ajout du paramètre.
* Dashboard - AP-Lite - Gérer requête changement AUX spécifique pour AP-Lite.
* Dashboard - AP-Lite - Bloquer capteur non-optique dans le choix des voies.
* Dashboard - Cacher réglage période balai sur probe différente de AP6K/7K/Pro.
* Liveview - Gérer si présence Depth sur AP-700/AP-700-D ou AP-800/AP-800-D dans bloc affichage.
* Liveview - Gérer si présence Depth sur AP-2000 dans bloc affichage.
* Liveview - Gérer si présence Depth sur AP-700/AP-700-D ou AP-800/AP-800-D dans fichier mesure.
* Liveview - Gérer si présence Depth sur AP-2000 dans fichier mesure.
* Liveview - Start logging bouton : problème couleur quand activé plus d'une fois.
* Liveview - AP-Lite - Température valeur négative/flag pas géré.
* Calibration - Ecriture date/GS Factor différent selon la version logiciel.
* Calibration - Cacher commande balai sur probe différente de AP6K/7K/Pro.
* Calibration - AP-Lite - Ajouter valeur par défaut pour valeur calibration AUX1_P2.
* Calibration - AP-Lite - Gérer calibration spécifique pour Tbd.
* Calibration - AP-Lite - Pas de clean balai.
* Calibration - AP-Lite - Pas de RapidCal.
* Calibration - Bloquer commande balai quand la probe est en mesure calibration.
* Calibration - AP-Lite/AquaPlus - Problème d'export rapport après restauration des points par défaut.
* Calibration - Ajout fonction clear graph.
* Calibration - NON-TESTE - AP-700 (ID:17) / AP-800 (ID:08) / AP-700-D (ID:27) / AP-800-D (ID:28) - Pas de point pH10.
* Calibration - Vérifier donnée rapport calibration : retour en fin de calibration ou valeur du point ?.
* Calibration - AquaPlus - Sélection 1413 uS : Pb valeur affiché 53065.
* Calibration - ORP - Pour version ProBE_SW < 3, pas de sélection de la valeur ORP.
* Calibration - Adapter rapport au nombre d'AUX présent.
* Config - Les unités ne sont pas modifiées dans les cadres Liveview, faire un lecture configuration après modification de paramètre.
Sonde :
* Dashboard - Cacher réglage période balai sur sonde différente de AS6K/7K/Pro.
* Liveview - Start logging bouton : problème couleur quand activé plus d'une fois.
* Calibration - Cacher commande balai sur sonde différente de AS6K/7K/Pro.
* Calibration - Bloquer commande balai quand la sonde est en mesure calibration.
* Calibration - Ajout fonction clear graph.
* Calibration - Correction régression sur restauration calibration sur AUX (partait en timeout).
* Update - Fin du téléchargement de Version.txt et Updatelist.txt.


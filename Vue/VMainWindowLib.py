# This Python file uses the following encoding: utf-8

#============================================================================#
# Librairies système
#============================================================================#
import sys
import io, csv
import time
from enum import Enum, IntEnum

#============================================================================#
# Constante
#============================================================================#
# Calibration - Index du menu capteur sélectionné
class TECalibSensorNavIndex(IntEnum):
 PH        = 0
 ORP       = 1
 DO_EC     = 2

# Index des onglets de point de calibration
class TECalibPointNavIndex(IntEnum):
 MAIN      = 0
 PH_7      = 1
 PH_4      = 2
 PH_10     = 3
 DO_EC     = 4
 TURBIDITY = 5


#============================================================================#
# Fonction outil
#============================================================================#
#-------------------------------------
# ID selon le Nom de la voie
#-------------------------------------
def uiFGetIDWithChannelNameWith( sChannelName ):
 uiAUXAssign = 0
 if( sChannelName == "Baro"        ): uiAUXAssign = -9
 if( sChannelName == "Pressure"    ): uiAUXAssign = -8
 if( sChannelName == "ORP"         ): uiAUXAssign = -7
 if( sChannelName == "pH"          ): uiAUXAssign = -6
 if( sChannelName == "pH"          ): uiAUXAssign = -5
 if( sChannelName == "DO Sat"      ): uiAUXAssign = -4
 if( sChannelName == "DO"          ): uiAUXAssign = -3
 if( sChannelName == "EC"          ): uiAUXAssign = -2
 if( sChannelName == "Temperature" ): uiAUXAssign = -1
 if( sChannelName == "EMPTY"       ): uiAUXAssign = 0
 if( sChannelName == "Ammonium"    ): uiAUXAssign = 1
 if( sChannelName == "Chloride"    ): uiAUXAssign = 2
 if( sChannelName == "Fluoride"    ): uiAUXAssign = 3
 if( sChannelName == "Nitrate"     ): uiAUXAssign = 4
 if( sChannelName == "Calcium"     ): uiAUXAssign = 5
 if( sChannelName == "Turbidity"   ): uiAUXAssign = 16
 if( sChannelName == "Chlorophyll" ): uiAUXAssign = 17
 if( sChannelName == "BGA-PC"      ): uiAUXAssign = 18
 if( sChannelName == "BGA-PE"      ): uiAUXAssign = 19
 if( sChannelName == "Rhodamine"   ): uiAUXAssign = 20
 if( sChannelName == "Fluorescein" ): uiAUXAssign = 21
 if( sChannelName == "Refined Oil" ): uiAUXAssign = 22
 if( sChannelName == "CDOM"        ): uiAUXAssign = 23
 if( sChannelName == "Crude Oil"   ): uiAUXAssign = 24
 if( sChannelName == "Tryptophan"  ): uiAUXAssign = 25
 return( int(uiAUXAssign) )


#============================================================================#
# Variable globale
#============================================================================#

# Création de l'objet principal
tCalibChannelInfo = {}

#--------------------
# Empty
#--------------------
tCalibChannelInfo["EMPTY"]             = {}
tCalibChannelInfo["EMPTY"]["ucPoint"]  = 0

#--------------------
# pH
#--------------------
tCalibChannelInfo["pH"]             = {}
tCalibChannelInfo["pH"]["ucPoint"]  = 3
tCalibChannelInfo["pH"]["sNetwork"] = '''<strong>Calibrating pH</strong>
<p>pH electrodes should be calibrated fully at least once a week to ensure optimum accuracy. Full calibration involves calibrating at pH 7.00 first, then at pH 4.01 and/or pH 10.00.
The sonde/probe allows for both two and three point pH calibration. Should you decide to carry out just a two point calibration, the sonde/probe will automatically calculate and save
a calibration value for the un-calibrated third point in order to maintain the electrode's linearity over the full range of 0 – 14.
For best results, calibrate all three points as close to 25°C as possible.</p>

<strong>Calibrating the First Point (pH 7.00)</strong>

<p>Due to the way in which pH calibration works, the sonde/probe must be calibrated at pH 7.00 before calibrating at pH 4.01 or pH 10.00. Never calibrate at pH 4.01 or pH 10.00
before first calibrating at pH 7.00.</p>
'''
tCalibChannelInfo["pH"]["Point"]   = []
tCalibChannelInfo["pH"]["Point"].append({})
tCalibChannelInfo["pH"]["Point"].append({})
tCalibChannelInfo["pH"]["Point"].append({})
tCalibChannelInfo["pH"]["Point"][0]["sName"]          = "7.00"
tCalibChannelInfo["pH"]["Point"][0]["sCalReportUnit"] = "mV"
tCalibChannelInfo["pH"]["Point"][0]["sNetwork"] = '''<strong>To calibrate the pH electrode folow these steps :</strong>
<ul>
<li>Pour RapidCal solution or pH 7.00 calibration solution into the calibration vessel.</li>
<li>Remove the storage cap from the pH electrode if fitted. Fit the red rubber caps to any ISE electrodes fitted. Wash the sonde/probe in deionised water,
then gently lower the sonde/probe into calibration vessel and screw into place.</li>
<li>If available activate the sonde/probe cleaning feature in order to remove any bubbles that may be clinging to the electrodes. To do this click the Clean button.</li>
<li>Wait until the temperature and pH measurements are completely stable.</li>
<li>Ensure temperature of the solution is between 5°C and 40°C (41°F – 104°F).</li>
<li>Click on the calibrate button.</li>
</ul>'''
tCalibChannelInfo["pH"]["Point"][1]["sName"] = "4.01"
tCalibChannelInfo["pH"]["Point"][1]["sCalReportUnit"] = "mV/pH"
tCalibChannelInfo["pH"]["Point"][1]["sNetwork"] = '''<strong>Calibrating the Second Point</strong>
The pH electrode can now be calibrated at either pH 4.01 or pH 10.00. If you intend to calibrate at both pH 4.01 and pH 10.00,
both points must be calibrated in the same session, without disconnecting the sonde/probe.

If the sonde/probe is disconnected after calibrating just one additional point (pH 4.00 for example),
the sonde/probe will automatically calculate and save a calibration value for the un-calibrated third point in order to maintain the electrode's linearity.

To calibrate the second point, pour fresh pH 4.01 or pH 10.00 solution into the clean calibration vessel and screw the sonde/probe in all the way.
Follow the procedure detailed above, but at step 6, click the Cal button for either pH4.01 or pH10.0, dependent upon the solution you are using.
'''
tCalibChannelInfo["pH"]["Point"][2]["sName"] = "10.0"
tCalibChannelInfo["pH"]["Point"][2]["sCalReportUnit"] = "mV/pH"
tCalibChannelInfo["pH"]["Point"][2]["sNetwork"] = '''<strong>Calibrating the Third Point</strong>
Without disconnecting the sonde/probe, pour fresh pH 4.01 or pH 10.00 solution into the calibration vessel
and screw the sonde/probe in all the way.
Follow the last pH 7.00 procedure, but, select either pH4.01 or pH10.0 dependent upon the solution you are using.
Wait while the sonde/probe stabilises and calibrates.
If the pH electrode in millivolts (mV) per pH unit goes below 45mV/pH at 25°C, the pH electrode should be serviced.

Remove the sonde/probe from the calibration vessel and wash both the sonde/probe and calibration vessel in fresh or deionised water.
Dry all parts with the lint-free cloth provided.

Dampen the sponge in the storage cap with storage solution and fit it to the pH/ORP electrode. pH calibration is now complete.
'''

#--------------------
# ORP
#--------------------
tCalibChannelInfo["ORP"]             = {}
tCalibChannelInfo["ORP"]["ucPoint"]  = 1
tCalibChannelInfo["ORP"]["sNetwork"] = '''<strong>Calibrating ORP (REDOX)</strong>

<p>ORP electrodes should be calibrated at least once a month to ensure optimum accuracy.
Full calibration involves calibrating at a single point, either +250mV (at 25°C) using a :<p>
<lu>
<li>+250mV ORP calibration standard such as Reagecon RS250 Redox Standard, or<li>
<li>+229mV (at 25°C) using a +229mV ORP calibration standard such as Zobell Solution.</li>
</lu>
<p>During calibration of the ORP electrode, the variation in the calibration buffer solution due to temperature is automatically corrected for.
During measurement of ORP however, temperature corrections are not applied as the correction factors are system and
chemical dependant and are not easily determined.</p>

<p>ORP potential measurements are mostly made to follow reactions rather than for their own sake. The completion of an ORP reaction is normally
accompanied by a sharp change in the ORP millivolts reading. This change is usually much larger than the errors induced by temperature side effects.</p>'''
tCalibChannelInfo["ORP"]["Point"]   = []
tCalibChannelInfo["ORP"]["Point"].append({})
tCalibChannelInfo["ORP"]["Point"][0]["sName"]          = "Point 1"
tCalibChannelInfo["ORP"]["Point"][0]["sCalReportUnit"] = "mV"
tCalibChannelInfo["ORP"]["Point"][0]["sNetwork"]       = """<strong>To calibrate the ORP electrode follow these steps:</strong>
<ol>
<li>Pour fresh ORP calibration solution into the calibration vessel.</li>
<li>Remove the storage cap from the pH electrode if fitted. Fit the red rubber caps to
any ISE electrodes fitted. Wash the sonde/probe in deionised water, pat dry, then gently
lower the sonde/probe into the calibration vessel and screw into place.</li>
<li>If available activate the sonde/probe cleaning feature in order to remove any air bubbles that may be
clinging to the electrodes. To do this click the Clean button. </li>
<li>Wait until the temperature and pH measurements are completely stable (boxes are
both green).</li>
<li>Ensure the temperature of the solution is between 5°C and 40°C (41°F – 104°F).</li>
<li>Select the correct calibration solution value (either 250mV or 229mV) for the solution
you are using in the Cal Value drop-down box.</li>
<li>Click on the Calibrate button to calibrate the ORP.</li>
</ol>
<p>When calibration is complete, the calibration date and the voltage offset for the ORP
electrode in +/-millivolts (mV) will be written into the calibration box shown above. This
value is stored in the sonde/probe's memory and will be displayed each time the sonde/probe is
connected to ProLink.</p>
<p>Remove the sonde/probe from the calibration vessel and wash both the sonde/probe and calibration
vessel in fresh or deionised water. Dry all parts with the lint-free cloth provided.</p>
"""

#--------------------
# DO
#--------------------
tCalibChannelInfo["DO"]             = {}
tCalibChannelInfo["DO"]["ucPoint"]  = 2
tCalibChannelInfo["DO"]["sNetwork"] = '''<strong>Calibrating the DO Electrode</strong>

<p>The DO section of the electrode should be calibrated at the Zero saturation point at least once every six months.
Before each day’s use, the 100% saturation point should be checked in moist air and re-calibrated if necessary. For optimum accuracy,
calibrate the DO100% point as near to your sample temperature as possible (within the calibration temperature limits of 5°C - 40°C).</p>

<p>If you are going to calibrate both the Zero and 100% points at the same time, ALWAYS calibrate the Zero point first, then the 100% point.</p>
'''
tCalibChannelInfo["DO"]["Point"]    = []
tCalibChannelInfo["DO"]["Point"].append({})
tCalibChannelInfo["DO"]["Point"].append({})
tCalibChannelInfo["DO"]["Point"][0]["sName"]          = "Zero"
tCalibChannelInfo["DO"]["Point"][0]["sCalReportUnit"] = "V"
tCalibChannelInfo["DO"]["Point"][0]["sNetwork"]       = """<strong>Calibrating the DO Zero Point</strong>
<ol>
<li>Create the calibration vessel.</li>
<li>Pour DO Zero calibration solution into the calibration vessel.</li>
<li>Remove the storage cap from the pH/ORP electrode. Fit the red rubber caps to
any ISE electrodes fitted. Wash the sonde/probe in deionised water, then gently lower
the sonde/probe into the calibration vessel and screw into place.</li>
<li>If available activate the sonde/probe cleaning feature in order to remove any air bubbles that may be
clinging to the electrodes. To do this click the Clean button.</li>
<li>Wait until the temperature and DO readings are completely stable. The longer you
can leave the sonde/probe to achieve thermal equilibrium before proceeding, the better.
A minimum of ten minutes is recommended.</li>
<li>Ensure the temperature of the solution is between 5°C and 40°C (41°F - 104°F).</li>
<li>Click the Calibrate button.</li>
</ol>
<p>When calibration is complete, the calibration date and a voltage will be written into the
calibration box. The voltage value represents the health of the luminophore.
This value should be between 3.5 and 4.5 (at 25°C). If the value returned is less than 3.5,
the Optical DO Cap should be replaced.</p>
<p>This value is stored in the sonde/probe's memory and will be displayed each time the sonde/probe is
connected to ProLink</p>"""
tCalibChannelInfo["DO"]["Point"][1]["sName"]          = "100% Cal"
tCalibChannelInfo["DO"]["Point"][1]["sCalReportUnit"] = "V"
tCalibChannelInfo["DO"]["Point"][1]["sNetwork"]       = """<strong>Calibrating the DO 100% Saturation Point in Moist Air</strong>
<ol>
<li>After calibrating the DO Zero point, remove the sonde/probe from the calibration vessel
and wash both the sonde/probe and calibration vessel in fresh water. Shake off any water
from the sonde/probe ensuring there are no droplets adhering to the DO membrane.
If droplets remain, blot the membrane with the lint free cloth provided, do not wipe
membrane with abrasive material.</li>
<li>Screw the sonde/probe back into the moist calibration vessel and sit it upright. Do not hold
the sonde/probe, the heat from your hands will warm the sonde/probe up and interfere with
calibration.</li>
<li>Wait until the temperature and DO measurements are both completely stable. This
is very important. If the DO measurement is 100% +/-1%, there is no need to
recalibrate.</li>
</ol>
<p>ProLink will wait until all readings are stable, then it will send the calibration command to
the sonde/probe, where the calibration takes place.</p>
<p>During stabilisation and calibration, progress is reported on screen with a progress bar.</p>
<p>When calibration is complete, the calibration date and a voltage will be written into the
calibration box. The voltage value represents the health of the luminophore.
This value should be between 0.8 and 1.5 (at 25°C). If the value returned is less than 0.8,
the Optical DO Cap should be replaced.</p>
"""

#--------------------
# EC
#--------------------
tCalibChannelInfo["EC"] = {}
tCalibChannelInfo["EC"]["ucPoint"] = 1
tCalibChannelInfo["EC"]["sNetwork"] = '''<strong>Calibrating the EC Electrode</strong>

<p>EC calibration is always carried out at a single point.
There is a choice of two pre-set calibration standards or you can enter any calibration standard value between 100µS/cm
and 99,999µS/cm manually.</p>

<p>The pre-set standards are: Aquaread® RapidCal (EC value 2570µS/cm) and Aquaread® SC- 35 (35ppt sodium chloride solution),
which is specifically for use when measuring EC and salinity in sea water. Both solutions are readily available from all Aquaread® dealers.</p>

<p>The calibration solution value you use to calibrate EC should always be chosen to be a near to the readings
you expect to see in the field as possible. If you are not sure what values to expect, RapidCal is a good choice
as this will give reasonably accurate readings across a wide range of EC values.</p>

<p>SC-35 calibration solution is available from Aquaread® dealers or can be made by adding 35 grams of laboratory grade
sodium chloride (99.9% pure) to a 1 Litre volumetric flask and topping it up with DEIONISED water (approx 965g of water) to make 1Litre.</p>

<p>The sonde/probe's central wiper forms an integral, working part of the sonde/probe’s EC
measurement system, and MUST be fitted during calibration and measurement for
correct operation. If you try to calibrate the sonde/probe without the wiper fitted, you will
get erroneous results.</p>

<p>For best results, calibrate as close to 25°C as possible. The sonde/probe will compensate for
temperature variation in the calibration standard during calibration.</p>'''
tCalibChannelInfo["EC"]["Point"]   = []
tCalibChannelInfo["EC"]["Point"].append({})
tCalibChannelInfo["EC"]["Point"][0]["sName"]          = "Point 1"
tCalibChannelInfo["EC"]["Point"][0]["sCalReportUnit"] = "(Cell)"
tCalibChannelInfo["EC"]["Point"][0]["sNetwork"]       = """<strong>Calibrating the EC Electrode</strong>
<ol>
<li>Create the calibration vessel.</li>
<li>Pour EC calibration solution into the calibration vessel. It is very important that all
four gold EC rings are covered during this calibration and at least 1cm above
the rings are submerged. Ensure the calibration cup is FULL to the top when
the sonde/probe is screwed into place, depending on the number of optional
electrodes installed the volume required will be between 275mL and 325mL.</li>
<li>Remove the storage cap from the pH electrode if fitted. If you have ISE electrodes
installed, the red protective caps should be fitted now. Wash the sonde/probe in
deionised water, then gently lower the sonde/probe onto the calibration vessel and screw
into place.</li>
<li>If available activate the sonde/probe cleaning feature in order to remove any air bubbles that may be
clinging to the electrodes. To do this click the Clean button.</li>
<li>Wait until the EC and temperature readings are completely stable. The longer you
can leave the sonde/probe to achieve thermal equilibrium before proceeding, the better. A
minimum of two minutes is recommended.</li>
<li>Ensure the temperature of the solution is between 5°C and 40°C (41°F – 104°F).
Ideally, the solution should be as close to 25°C as possible.</li>
<li>In the Cal Value drop-down box, select the calibration solution you are using. Your
choices are 'RapidCal', 'SC-35' or 'User'. If you select 'User', a new box will appear
into which you must enter the EC value of your calibration solution AT 25°C. This
information will be printed on the label of the EC calibration standard bottle.</li>
<li>Click on the Cal button adjacent to the EC Cal box.</li>
</ol>
<p>When calibration is complete, the calibration date and the EC electrode's cell constant will
be written into the calibration box. This value is stored in the sonde/probe's memory and will be
displayed each time the sonde/probe is connected to ProLink.</p>
<p>Remove the sonde/probe from the calibration vessel and wash both the sonde/probe and calibration
vessel in fresh water. Dry all parts with the lint-free cloth provided.</p>
"""

#--------------------
# Ammonium
#--------------------
tCalibChannelInfo["Ammonium"]             = {}
tCalibChannelInfo["Ammonium"]["ucPoint"]  = 3
tCalibChannelInfo["Ammonium"]["sNetwork"] = '''
<strong>Ammonium Calibration Solution Preparation</strong>
<p>When an Ammonium ISE electrode is first installed, it must be calibrated at three points. In order to achieve this, three batches of Ammonium calibration solution must be prepared.</p>

<p>The solutions required are two 400mL batches of Ammonium (as NH4) at a concentration of 10ppm and one 400mL batch of Ammonium (as NH4) at a concentration of 100ppm.</p>

<p>The three calibration solutions should be freshly prepared by serial dilution from 1000ppm calibration standard if Aquaread pre-diluted solutions have not been purchased.
The 1000ppm solution is available from Aquaread Dealers (part number AMM-CAL) but it is highly recommended to purchase the pre-diluted solutions if you are not equipped
to use high accuracy volumetric liquid handling techniques or have access to high quality grade Deionised water.</p>

<strong>Be sure to handle chemicals with care and to read and comply with all health and safety advice</strong>
'''
tCalibChannelInfo["Ammonium"]["Point"]   = []
tCalibChannelInfo["Ammonium"]["Point"].append({})
tCalibChannelInfo["Ammonium"]["Point"].append({})
tCalibChannelInfo["Ammonium"]["Point"].append({})
tCalibChannelInfo["Ammonium"]["Point"][0]["sName"]          = "10ppm T1"
tCalibChannelInfo["Ammonium"]["Point"][0]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Ammonium"]["Point"][0]["sNetwork"]       = """
<strong>Preparing the 10ppm solution</strong>
<p>A total of 800mL of 10ppm solution is required. To prepare this, mix 80mL of the 100ppm
solution you have just prepared with 720mL of deionised water. Dispense the 10ppm
solution into two calibration cups (400mL each).</p>

<strong>Achieving the correct temperature</strong>
<p>During three point calibration, the 100ppm solution and one batch of the 10ppm solution
must be at exactly the same temperature. The second batch of 10ppm solution must be at
least 10°C cooler.</p>
<p>In order to achieve this, one batch of the 10ppm solution should be put into a refrigerator
and the other two solutions should be put into a water bath at 25°C. Once all three
solutions are at a stable temperature, calibration can begin.</p>
"""
tCalibChannelInfo["Ammonium"]["Point"][1]["sName"]          = "100ppm T1+/-1C"
tCalibChannelInfo["Ammonium"]["Point"][1]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Ammonium"]["Point"][1]["sNetwork"]       = """
<strong>Preparing the 100ppm solution</strong>
<p>500mL of 100ppm solution is required. To prepare this, mix 50mL of 1000ppm calibration
standard with 450mL of deionised water.</p>
<p>Dispense 400mL of the 100ppm solution into a calibration cup and retain 100mL for
preparation of the 10ppm solution.</p>
"""
tCalibChannelInfo["Ammonium"]["Point"][2]["sName"]          = "10ppm T1-10C"
tCalibChannelInfo["Ammonium"]["Point"][2]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Ammonium"]["Point"][2]["sNetwork"]       = """
<strong>Preparing the 10ppm solution</strong>
<p>A total of 800mL of 10ppm solution is required. To prepare this, mix 80mL of the 100ppm
solution you have just prepared with 720mL of deionised water. Dispense the 10ppm
solution into two calibration cups (400mL each).</p>

<strong>Achieving the correct temperature</strong>
<p>During three point calibration, the 100ppm solution and one batch of the 10ppm solution
must be at exactly the same temperature. The second batch of 10ppm solution must be at
least 10°C cooler.</p>
<p>In order to achieve this, one batch of the 10ppm solution should be put into a refrigerator
and the other two solutions should be put into a water bath at 25°C. Once all three
solutions are at a stable temperature, calibration can begin.</p>
"""

#--------------------
# Chloride
#--------------------
tCalibChannelInfo["Chloride"] = {}
tCalibChannelInfo["Chloride"]["ucPoint"] = 3
tCalibChannelInfo["Chloride"]["sNetwork"] = '''<strong>Chloride Calibration Solution Preparation</strong>
<p>When a Chloride ISE electrode is first installed, it must be calibrated at three points. In order to achieve this, three batches of Chloride calibration solution must be prepared.</p>

<p>The solutions required are two 400mL batches of Chloride at a concentration of 10ppm and one 500mL batch of Chloride at a concentration of 100ppm.</p>

<p>The three calibration solutions should be freshly prepared by serial dilution from 1000ppm calibration standard if Aquaread pre-diluted solutions have not been purchased. The 1000ppm solution is available from Aquaread Dealers (part number CHL-CAL) but it is highly recommended to purchase the pre-diluted solutions if you are not equipped to use high accuracy volumetric liquid handling techniques or have access to high quality grade Deionised water.</p>
'''
tCalibChannelInfo["Chloride"]["Point"]   = []
tCalibChannelInfo["Chloride"]["Point"].append({})
tCalibChannelInfo["Chloride"]["Point"].append({})
tCalibChannelInfo["Chloride"]["Point"].append({})
tCalibChannelInfo["Chloride"]["Point"][0]["sName"]          = "10ppm T1"
tCalibChannelInfo["Chloride"]["Point"][0]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Chloride"]["Point"][0]["sNetwork"]       = ""
tCalibChannelInfo["Chloride"]["Point"][1]["sName"]          = "100ppm T1+/-1C"
tCalibChannelInfo["Chloride"]["Point"][1]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Chloride"]["Point"][1]["sNetwork"]       = ""
tCalibChannelInfo["Chloride"]["Point"][2]["sName"]          = "10ppm T1-10C"
tCalibChannelInfo["Chloride"]["Point"][2]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Chloride"]["Point"][2]["sNetwork"]       = ""

#--------------------
# Fluoride
#--------------------
tCalibChannelInfo["Fluoride"] = {}
tCalibChannelInfo["Fluoride"]["ucPoint"] = 3
tCalibChannelInfo["Fluoride"]["sNetwork"] = '''<strong>Fluoride Calibration </strong>
<p>When a Fluoride ISE electrode is first installed, it must be calibrated at three points. In
order to achieve this, three batches of Fluoride calibration solution must be prepared.</p>

<p>The solutions required are two 400mL batches of Fluoride at a concentration of 0.5ppm and
one 500mL batch of Fluoride at a concentration of 5ppm.</p>

<p>The three calibration solutions should be freshly prepared by serial dilution from 1000ppm
calibration standard if Aquaread pre-diluted solutions have not been purchased. The
1000ppm solution is available from Aquaread Dealers (part number FLU-CAL) but it is
highly recommended to purchase the pre-diluted solutions if you are not equipped to use
high accuracy volumetric liquid handling techniques or have access to high quality grade
Deionised water</p>'''
tCalibChannelInfo["Fluoride"]["Point"]   = []
tCalibChannelInfo["Fluoride"]["Point"].append({})
tCalibChannelInfo["Fluoride"]["Point"].append({})
tCalibChannelInfo["Fluoride"]["Point"].append({})
tCalibChannelInfo["Fluoride"]["Point"][0]["sName"]          = "0.5ppm T1"
tCalibChannelInfo["Fluoride"]["Point"][0]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Fluoride"]["Point"][0]["sNetwork"]       = ""
tCalibChannelInfo["Fluoride"]["Point"][1]["sName"]          = "5ppm T1+/-1C"
tCalibChannelInfo["Fluoride"]["Point"][1]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Fluoride"]["Point"][1]["sNetwork"]       = ""
tCalibChannelInfo["Fluoride"]["Point"][2]["sName"]          = "0.5ppm T1-10C"
tCalibChannelInfo["Fluoride"]["Point"][2]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Fluoride"]["Point"][2]["sNetwork"]       = ""

#--------------------
# Nitrate
#--------------------
tCalibChannelInfo["Nitrate"] = {}
tCalibChannelInfo["Nitrate"]["ucPoint"] = 3
tCalibChannelInfo["Nitrate"]["sNetwork"] = ''''''
tCalibChannelInfo["Nitrate"]["Point"]   = []
tCalibChannelInfo["Nitrate"]["Point"].append({})
tCalibChannelInfo["Nitrate"]["Point"].append({})
tCalibChannelInfo["Nitrate"]["Point"].append({})
tCalibChannelInfo["Nitrate"]["Point"][0]["sName"]          = "10ppm T1"
tCalibChannelInfo["Nitrate"]["Point"][0]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Nitrate"]["Point"][0]["sNetwork"]       = """<strong>Preparing the 10ppm solution</strong>
<p>A total of 800mL of 10ppm solution is required. To prepare this, mix 80mL of the 100ppm
solution you have just prepared with 720mL of deionised water.</p>
<p>Dispense the 10ppm solution into two calibration cups (400mL each).</p>

<strong>Achieving the correct temperature</strong>
<p>During three point calibration, the 100ppm solution and one batch of the 10ppm solution
must be at exactly the same temperature. The second batch of 10ppm solution must be at
least 10°C cooler.</p>
<p>In order to achieve this, one batch of the 10ppm solution should be put into a refrigerator
and the other two solutions should be put into a water bath at 25°C.</p>
<p>Once all three solutions are at a stable temperature, calibration can begin.</p>
"""
tCalibChannelInfo["Nitrate"]["Point"][1]["sName"]          = "100ppm T1+/-1C"
tCalibChannelInfo["Nitrate"]["Point"][1]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Nitrate"]["Point"][1]["sNetwork"]       = """<strong>Preparing the 100ppm solution</strong>
<p>500mL of 100ppm solution is required. To prepare this, mix 50mL of 1000ppm calibration
standard with 450mL of deionised water.</p>
<p>Dispense 400mL of the 100ppm solution into a calibration cup and retain 100mL for
preparation of the 10ppm solution.</p>

<strong>Achieving the correct temperature</strong>
<p>During three point calibration, the 100ppm solution and one batch of the 10ppm solution
must be at exactly the same temperature. The second batch of 10ppm solution must be at
least 10°C cooler.</p>
<p>In order to achieve this, one batch of the 10ppm solution should be put into a refrigerator
and the other two solutions should be put into a water bath at 25°C.</p>
<p>Once all three solutions are at a stable temperature, calibration can begin.</p>
"""
tCalibChannelInfo["Nitrate"]["Point"][2]["sName"]          = "10ppm T1-10C"
tCalibChannelInfo["Nitrate"]["Point"][2]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Nitrate"]["Point"][2]["sNetwork"]       = """<strong>Preparing the 10ppm solution</strong>
<p>A total of 800mL of 10ppm solution is required. To prepare this, mix 80mL of the 100ppm
solution you have just prepared with 720mL of deionised water.</p>
<p>Dispense the 10ppm solution into two calibration cups (400mL each).</p>

<strong>Achieving the correct temperature</strong>
<p>During three point calibration, the 100ppm solution and one batch of the 10ppm solution
must be at exactly the same temperature. The second batch of 10ppm solution must be at
least 10°C cooler.</p>
<p>In order to achieve this, one batch of the 10ppm solution should be put into a refrigerator
and the other two solutions should be put into a water bath at 25°C.</p>
<p>Once all three solutions are at a stable temperature, calibration can begin.</p>
"""
#--------------------
# Calcium
#--------------------
tCalibChannelInfo["Calcium"] = {}
tCalibChannelInfo["Calcium"]["ucPoint"] = 3
tCalibChannelInfo["Calcium"]["sNetwork"] = '''<strong>AL Calcium Electrode</strong>
<p>Calcium (Ca2) can be measured using the optional CAL ISE electrode within a pH range of
4 – 9. The Calcium ISE electrode will suffer interference from Magnesium, Barium, Lead,
Zinc and Sodium ions, which are similar in nature.</p>

<strong>Pre-Prepared Calibration Solutions</strong>
<p>Pre-prepared calibration solutions are available from your Aquaread dealer. Order codes
CAL-CAL-10 and CAL-CAL-100. These are recommended. If you wish to formulate your
own solutions, please follow the procedure.<p>

<strong>Calcium Calibration Solution Preparation</strong>
<p>When a Calcium ISE electrode is first installed, it must be calibrated at three points. In
order to achieve this, three batches of Calcium calibration solution must be prepared.</p>
<p>The solutions required are two 400mL batches of Calcium at a concentration of 10ppm and
one 500mL batch of Calcium at a concentration of 100ppm.</p>
<p>The three calibration solutions should be freshly prepared by serial dilution from 1000ppm
calibration standard if Aquaread pre-diluted solutions have not been purchased. The
1000ppm solution is available from Aquaread Dealers (part number CAL-CAL) but it is
highly recommended to purchase the pre-diluted solutions if you are not equipped to use
high accuracy volumetric liquid handling techniques or have access to high quality grade
Deionised water.</p>

<p>Be sure to handle chemicals with care and to read and comply with all health and
safety advice.</p>'''
tCalibChannelInfo["Calcium"]["Point"]   = []
tCalibChannelInfo["Calcium"]["Point"].append({})
tCalibChannelInfo["Calcium"]["Point"].append({})
tCalibChannelInfo["Calcium"]["Point"].append({})
tCalibChannelInfo["Calcium"]["Point"][0]["sName"]          = "10ppm T1"
tCalibChannelInfo["Calcium"]["Point"][0]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Calcium"]["Point"][0]["sNetwork"]       = """
<strong>Preparing the 10ppm solution</strong>
<p>A total of 800mL of 10ppm solution is required. To prepare this, mix 80mL of the 100ppm
solution you have just prepared with 720mL of deionised water. Dispense the 10ppm
solution into two calibration cups (400mL each).</p>

<strong>Achieving the correct temperature</strong>
<p>During three point calibration, the 100ppm solution and one batch of the 10ppm solution
must be at exactly the same temperature. The second batch of 10ppm solution must be at
least 10°C cooler.</p>
<p>In order to achieve this, one batch of the 10ppm solution should be put into a refrigerator
and the other two solutions should be put into a water bath at 25°C.</p>
<p>Once all three solutions are at a stable temperature, calibration can begin.</p>
"""
tCalibChannelInfo["Calcium"]["Point"][1]["sName"]          = "100ppm T1+/-1C"
tCalibChannelInfo["Calcium"]["Point"][1]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Calcium"]["Point"][1]["sNetwork"]       = """
<strong>Preparing the 100ppm solution</strong>
<p>500mL of 100ppm solution is required. To prepare this, mix 50mL of 1000ppm calibration
standard with 450mL of deionised water.</p>
<p>Dispense 400mL of the 100ppm solution into a calibration cup and retain 100mL for
preparation of the 10ppm solution.</p>

<strong>Achieving the correct temperature</strong>
<p>During three point calibration, the 100ppm solution and one batch of the 10ppm solution
must be at exactly the same temperature. The second batch of 10ppm solution must be at
least 10°C cooler.</p>
<p>In order to achieve this, one batch of the 10ppm solution should be put into a refrigerator
and the other two solutions should be put into a water bath at 25°C.</p>
<p>Once all three solutions are at a stable temperature, calibration can begin.</p>
"""
tCalibChannelInfo["Calcium"]["Point"][2]["sName"]          = "10ppm T1-10C"
tCalibChannelInfo["Calcium"]["Point"][2]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Calcium"]["Point"][2]["sNetwork"]       = """
<strong>Preparing the 10ppm solution</strong>
<p>A total of 800mL of 10ppm solution is required. To prepare this, mix 80mL of the 100ppm
solution you have just prepared with 720mL of deionised water. Dispense the 10ppm
solution into two calibration cups (400mL each).</p>

<strong>Achieving the correct temperature</strong>
<p>During three point calibration, the 100ppm solution and one batch of the 10ppm solution
must be at exactly the same temperature. The second batch of 10ppm solution must be at
least 10°C cooler.</p>
<p>In order to achieve this, one batch of the 10ppm solution should be put into a refrigerator
and the other two solutions should be put into a water bath at 25°C.</p>
<p>Once all three solutions are at a stable temperature, calibration can begin.</p>
"""
#--------------------
# Turbidité
#--------------------
tCalibChannelInfo["Turbidity"] = {}
tCalibChannelInfo["Turbidity"]["ucPoint"]  = 3
tCalibChannelInfo["Turbidity"]["sNetwork"] = '''
<strong>Calibrating the Turbidity Electrode</strong>
<p>The sonde/probe Sleeve, Measurement Chamber and Wiper all form an integral, working
part of the Sonde’s turbidity measurement system, and MUST be fitted during
calibration and measurement for correct operation.</p>

<strong>Calibration Points</strong>
<p>Turbidity electrodes have three calibration points. Careful calibration is essential in order to
ensure consistent and reliable results across the full measurement range.</p>
<p>When a turbidity electrode is first installed, it should be calibrated at the Zero point in
order to correct for any small differences in the Measurement Chamber.</p>
<p>The Turbidity electrode should subsequently be Zeroed (calibrated at the Zero NTU point)
before each day’s use. A three point calibration should be carried out once a month to
ensure optimum accuracy.</p>
<p>During full calibration, the Zero NTU point must always be calibrated first, followed
by the 1000NTU point, both within the same calibration session (i.e. without turning
the Aquameter® off). The third calibration point (20NTU) is optional and can be used if
enhanced accuracy is required at very low levels.</p>
'''
tCalibChannelInfo["Turbidity"]["Point"]    = []
tCalibChannelInfo["Turbidity"]["Point"].append({})
tCalibChannelInfo["Turbidity"]["Point"].append({})
tCalibChannelInfo["Turbidity"]["Point"].append({})
tCalibChannelInfo["Turbidity"]["Point"][0]["sName"]          = "Zero NTU"
tCalibChannelInfo["Turbidity"]["Point"][0]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Turbidity"]["Point"][0]["sNetwork"]       = """
<strong>Turbidity Zero Point Calibration</strong>
<p>To calibrate the Turbidity zero point (zero the electrode), follow these steps:</p>
<ol>
<li>Create the calibration vessel</li>
<li>Pour clean water into the calibration vessel (bottled still mineral water is ideal).</li>
<li>Remove the storage cap from the pH electrode if fitted. Wash the sonde/probe in clean
water, then gently lower the sonde/probe onto the calibration vessel and screw into place.</li>
<li>If available activate the sonde/probe cleaning feature in order to remove any air bubbles that may be
clinging to the electrode. To do this click the Clean button.</li>
<li>Wait until the temperature and turbidity readings are completely stable. The longer
you can leave the sonde/probe to achieve thermal equilibrium before proceeding, the
better. A minimum of two minutes is recommended.</li>
<li>Ensure the temperature of the solution is between 5°C and 40°C (41°F - 104°F).</li>
<li>Click on the Calibrate button.
When calibration is complete, the calibration date and the voltage output from the electrode
in millivolts (mV) will be written into the calibration box.
This value is stored in the sonde/probe's memory and will be displayed each time the sonde/probe is
connected to ProLink.</li>
</ol>

<strong>Verifying the Zero Calibration</strong>
<p>An accurate zero point calibration is essential to the correct operation of the turbidity
electrode. The zero point calibration can sometimes be erroneous due to small air bubbles
or microscopic suspended solids in the calibration solution. For this reason, it is important
to verify the zero point calibration before proceeding to calibrate the other points.</p>
<p>After calibrating the zero point, activate the sonde/probe cleaning feature then allow the reading
to settle. Check the turbidity reading is within +/- 1NTU of zero. If not, re-calibrate the zero
point.</p>
"""
tCalibChannelInfo["Turbidity"]["Point"][1]["sName"]          = "1000 NTU"
tCalibChannelInfo["Turbidity"]["Point"][1]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Turbidity"]["Point"][1]["sNetwork"]       = """
<strong>Calibrating the Turbidity 20 NTU & 1000 NTU Points</strong>
<p>When calibrating the 20 NTU and/or 1000 NTU points, the Zero point must be calibrated
first within the same calibration session (i.e. without turning the Aquameter® off).</p>
<p>Remove and empty the Measurement Chamber and shake off any excess water from the Sonde.</p>
<p>Gently invert, do not shake, a bottle of 20 NTU or 1000 NTU Stabilised Formazin
Turbidity Standard solution (available from most lab supply companies) several times to
thoroughly mix.</p>
<p>Formazin Turbidity Standard is hazardous to your health. Be sure to handle with care
and to read and comply with all health and safety advice.</p>
<p>Gently pour the solution into the calibration vessel then screw the sonde/probe in all the way.
If available activate the sonde/probe cleaning feature in order to remove any air bubbles that may be clinging
to the electrodes.</p>
<p>Follow the procedure detailed above for Zero point calibration as far as step 6, then select
either 20 or 1000, dependant upon the solution the electrode is in. Wait while the sonde/probe
stabilises and calibrates.</p>
<p>Rinse the calibration vessel and sonde/probe thoroughly then repeat this procedure for the third
point.</p>
"""
tCalibChannelInfo["Turbidity"]["Point"][2]["sName"]          = "20 NTU"
tCalibChannelInfo["Turbidity"]["Point"][2]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Turbidity"]["Point"][2]["sNetwork"]       = """
<strong>Calibrating the Turbidity 20 NTU & 1000 NTU Points</strong>
<p>When calibrating the 20 NTU and/or 1000 NTU points, the Zero point must be calibrated
first within the same calibration session (i.e. without turning the Aquameter® off).</p>
<p>Remove and empty the Measurement Chamber and shake off any excess water from the sonde/probe.</p>
<p>Gently invert, do not shake, a bottle of 20 NTU or 1000 NTU Stabilised Formazin
Turbidity Standard solution (available from most lab supply companies) several times to
thoroughly mix.</p>
<p>Formazin Turbidity Standard is hazardous to your health. Be sure to handle with care
and to read and comply with all health and safety advice.</p>
<p>Gently pour the solution into the calibration vessel then screw the sonde/probe in all the way.
Activate the sonde/probe cleaning feature in order to remove any air bubbles that may be clinging
to the electrodes.</p>
<p>Follow the procedure detailed above for Zero point calibration as far as step 6, then select
either 20 or 1000, dependant upon the solution the electrode is in. Wait while the Sonde
stabilises and calibrates.</p>
<p>Rinse the calibration vessel and sonde/probe thoroughly then repeat this procedure for the third
point.</p>
"""
#--------------------
# Chlorophylle
#--------------------
tCalibChannelInfo["Chlorophyll"] = {}
tCalibChannelInfo["Chlorophyll"]["ucPoint"] = 2
tCalibChannelInfo["Chlorophyll"]["sNetwork"] = '''
<strong>Calibration Points</strong>
<p>All fluorescent electrodes have two calibration points. Careful calibration is essential in
order to ensure consistent and reliable results across the full measurement range.</p>
<p>When a fluorescent electrode is first installed, it should be calibrated at the Zero point in
order to correct for any small differences in the Measurement Chamber.</p>
<p>The electrode should subsequently be Zeroed (calibrated at Point 1 in clean water) before
each day’s use. A two point calibration should be carried out once a month to ensure
optimum accuracy.</p>
'''
tCalibChannelInfo["Chlorophyll"]["Point"]   = []
tCalibChannelInfo["Chlorophyll"]["Point"].append({})
tCalibChannelInfo["Chlorophyll"]["Point"].append({})
tCalibChannelInfo["Chlorophyll"]["Point"][0]["sName"]          = "Clean water"
tCalibChannelInfo["Chlorophyll"]["Point"][0]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Chlorophyll"]["Point"][0]["sNetwork"]       = """
<strong>Zero Point Calibration</strong>
<p>To calibrate the zero point (Point 1), follow these steps:</p>
<ol>
<li>Create the calibration vessel.</li>
<li>Pour clean water into the calibration vessel (bottled still mineral water is ideal).</li>
<li>Remove the storage cap from the pH electrode if fitted. Wash the sonde/probe in clean
water, then gently lower the sonde/probe onto the calibration vessel and screw into place.</li>
<li>If available activate the sonde/probe cleaning feature in order to remove any air bubbles that may be
clinging to the electrode. To do this click the Clean button.</li>
<li>Wait until the temperature and electrode readings are completely stable. The longer
you can leave the sonde/probe to achieve thermal equilibrium before proceeding, the
better. A minimum of two minutes is recommended.</li>
<li>Ensure the temperature of the solution is between 5°C and 40°C (41°F – 104°F).</li>
<li>Click on the Calibrate button adjacent.
When Point 1 calibration is complete, the calibration date and the voltage output from the
electrode in millivolts (mV) will be written into the calibration box.
This value is stored in the sonde/probe's memory and will be displayed each time the sonde/probe is
connected to ProLink.</li>
</ol>

<strong>Verifying the Zero Calibration</strong>
<p>An accurate zero point calibration is essential to the correct operation of the fluorescent
electrodes. The zero point calibration can sometimes be erroneous due to small air bubbles
or microscopic suspended solids in the calibration solution. For this reason, it is important
to verify the zero point calibration before proceeding to calibrate the other points.</p>
"""
tCalibChannelInfo["Chlorophyll"]["Point"][1]["sName"]          = "500ug/L Rhod"
tCalibChannelInfo["Chlorophyll"]["Point"][1]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Chlorophyll"]["Point"][1]["sNetwork"]       = """
<strong>Calibrating the Second Point</strong>
<p>When calibrating any fluorescent electrode, the Zero point must be calibrated first
within the same calibration session (i.e. without disconnecting the sonde/probe).
<p>A Point 2 calibration standard must be prepared to suit each electrode being calibrated.
Each electrode type has a specific requirement, which is detailed in manual.</p>
<p>Once calibrated at Point 1 (the zero point), remove the sonde/probe from the calibration vessel
and dry all wetted parts thoroughly with the lint-free cloth provided.</p>
<p>Gently pour the pre-prepared Point 2 solution into the calibration vessel then screw the
Sonde in all the way. Activate the cleaning system in order to remove any air bubbles that
may be clinging to the electrodes.</p>
<p>Follow the general procedure detailed above for Zero point calibration as far as step 6, then
click on the button for Point 2. Wait while the readings stabilise and the electrode calibrates.
<p>The Calibration Report on the top line displays the voltage output from the electrode in
millivolts (mV). This value is stored in the electrode's memory and can be recalled at any
time.</p>
"""
#--------------------
# BGA-PC
#--------------------
tCalibChannelInfo["BGA-PC"] = {}
tCalibChannelInfo["BGA-PC"]["ucPoint"] = 2
tCalibChannelInfo["BGA-PC"]["sNetwork"] = '''
<strong>Calibration Points</strong>
<p>All fluorescent electrodes have two calibration points. Careful calibration is essential in
order to ensure consistent and reliable results across the full measurement range.</p>
<p>When a fluorescent electrode is first installed, it should be calibrated at the Zero point in
order to correct for any small differences in the Measurement Chamber.</p>
<p>The electrode should subsequently be Zeroed (calibrated at Point 1 in clean water) before
each day’s use. A two point calibration should be carried out once a month to ensure
optimum accuracy.</p>
'''
tCalibChannelInfo["BGA-PC"]["Point"]   = []
tCalibChannelInfo["BGA-PC"]["Point"].append({})
tCalibChannelInfo["BGA-PC"]["Point"].append({})
tCalibChannelInfo["BGA-PC"]["Point"][0]["sName"]          = "Clean water"
tCalibChannelInfo["BGA-PC"]["Point"][0]["sCalReportUnit"] = "mV"
tCalibChannelInfo["BGA-PC"]["Point"][0]["sNetwork"]       = """
<strong>Zero Point Calibration</strong>
<p>To calibrate the zero point (Point 1), follow these steps:</p>
<ol>
<li>Create the calibration vessel as described in section 5.4. Calibration Vessel.</li>
<li>Pour clean water into the calibration vessel (bottled still mineral water is ideal).</li>
<li>Remove the storage cap from the pH electrode if fitted. Wash the sonde/probe in clean
water, then gently lower the sonde/probe onto the calibration vessel and screw into place.</li>
<li>Activate the sonde/probe cleaning feature in order to remove any air bubbles that may be
clinging to the electrode. To do this click the Clean sonde/probe button.</li>
<li>Wait until the temperature and electrode readings are completely stable. The longer
you can leave the sonde/probe to achieve thermal equilibrium before proceeding, the
better. A minimum of two minutes is recommended.</li>
<li>Ensure the temperature of the solution is between 5°C and 40°C (41°F – 104°F).</li>
<li>Click on the Cal button adjacent to the Point 1 Cal box.
When Point 1 calibration is complete, the calibration date and the voltage output from the
electrode in millivolts (mV) will be written into the calibration box.
This value is stored in the sonde/probe's memory and will be displayed each time the sonde/probe is
connected to ProLink.</li>
</ol>

<strong>Verifying the Zero Calibration</strong>
<p>An accurate zero point calibration is essential to the correct operation of the fluorescent
electrodes. The zero point calibration can sometimes be erroneous due to small air bubbles
or microscopic suspended solids in the calibration solution. For this reason, it is important
to verify the zero point calibration before proceeding to calibrate the other points.</p>

<p>After calibrating the zero point, activate the sonde/probe cleaning feature then allow the reading
to settle. Check the reading is zero. If not, re-calibrate the zero point.</p>
"""
tCalibChannelInfo["BGA-PC"]["Point"][1]["sName"]          = "100ug/L Rhod"
tCalibChannelInfo["BGA-PC"]["Point"][1]["sCalReportUnit"] = "mV"
tCalibChannelInfo["BGA-PC"]["Point"][1]["sNetwork"]       = """
<strong>Calibrating the Second Point</strong>
<p>When calibrating any fluorescent electrode, the Zero point must be calibrated first
within the same calibration session (i.e. without disconnecting the AS-Pro™).
<p>A Point 2 calibration standard must be prepared to suit each electrode being calibrated.
Each electrode type has a specific requirement, which is detailed in manual.</p>
<p>Once calibrated at Point 1 (the zero point), remove the sonde/probe from the calibration vessel
and dry all wetted parts thoroughly with the lint-free cloth provided.</p>
<p>Gently pour the pre-prepared Point 2 solution into the calibration vessel then screw the
Sonde in all the way. Activate the cleaning system in order to remove any air bubbles that
may be clinging to the electrodes.</p>
<p>Follow the general procedure detailed above for Zero point calibration as far as step 6, then
click on the button for Point 2. Wait while the readings stabilise and the electrode calibrates.
<p>The Calibration Report on the top line displays the voltage output from the electrode in
millivolts (mV). This value is stored in the electrode's memory and can be recalled at any
time.</p>
"""
#--------------------
# BGA-PE
#--------------------
tCalibChannelInfo["BGA-PE"] = {}
tCalibChannelInfo["BGA-PE"]["ucPoint"]  = 2
tCalibChannelInfo["BGA-PE"]["sNetwork"] = '''
<strong>Calibration Points</strong>
<p>All fluorescent electrodes have two calibration points. Careful calibration is essential in
order to ensure consistent and reliable results across the full measurement range.</p>
<p>When a fluorescent electrode is first installed, it should be calibrated at the Zero point in
order to correct for any small differences in the Measurement Chamber.</p>
<p>The electrode should subsequently be Zeroed (calibrated at Point 1 in clean water) before
each day’s use. A two point calibration should be carried out once a month to ensure
optimum accuracy.</p>
'''
tCalibChannelInfo["BGA-PE"]["Point"]    = []
tCalibChannelInfo["BGA-PE"]["Point"].append({})
tCalibChannelInfo["BGA-PE"]["Point"].append({})
tCalibChannelInfo["BGA-PE"]["Point"][0]["sName"]          = "Clean water"
tCalibChannelInfo["BGA-PE"]["Point"][0]["sCalReportUnit"] = "mV"
tCalibChannelInfo["BGA-PE"]["Point"][0]["sNetwork"]       = """
<strong>Zero Point Calibration</strong>
<p>To calibrate the zero point (Point 1), follow these steps:</p>
<ol>
<li>Create the calibration vessel as described in section 5.4. Calibration Vessel.</li>
<li>Pour clean water into the calibration vessel (bottled still mineral water is ideal).</li>
<li>Remove the storage cap from the pH electrode if fitted. Wash the sonde/probe in clean
water, then gently lower the sonde/probe onto the calibration vessel and screw into place.</li>
<li>Activate the sonde/probe cleaning feature in order to remove any air bubbles that may be
clinging to the electrode. To do this click the Clean sonde/probe button.</li>
<li>Wait until the temperature and electrode readings are completely stable. The longer
you can leave the sonde/probe to achieve thermal equilibrium before proceeding, the
better. A minimum of two minutes is recommended.</li>
<li>Ensure the temperature of the solution is between 5°C and 40°C (41°F – 104°F).</li>
<li>Click on the Cal button adjacent to the Point 1 Cal box.
When Point 1 calibration is complete, the calibration date and the voltage output from the
electrode in millivolts (mV) will be written into the calibration box.
This value is stored in the sonde/probe's memory and will be displayed each time the sonde/probe is
connected to ProLink.</li>
</ol>

<strong>Verifying the Zero Calibration</strong>
<p>An accurate zero point calibration is essential to the correct operation of the fluorescent
electrodes. The zero point calibration can sometimes be erroneous due to small air bubbles
or microscopic suspended solids in the calibration solution. For this reason, it is important
to verify the zero point calibration before proceeding to calibrate the other points.</p>

<p>After calibrating the zero point, activate the sonde/probe cleaning feature then allow the reading
to settle. Check the reading is zero. If not, re-calibrate the zero point.</p>
"""
tCalibChannelInfo["BGA-PE"]["Point"][1]["sName"]          = "8ug/L Rhod"
tCalibChannelInfo["BGA-PE"]["Point"][1]["sCalReportUnit"] = "mV"
tCalibChannelInfo["BGA-PE"]["Point"][1]["sNetwork"]       = """
<strong>Calibrating the Second Point</strong>
<p>When calibrating any fluorescent electrode, the Zero point must be calibrated first
within the same calibration session (i.e. without disconnecting the AS-Pro™).
<p>A Point 2 calibration standard must be prepared to suit each electrode being calibrated.
Each electrode type has a specific requirement, which is detailed in manual.</p>
<p>Once calibrated at Point 1 (the zero point), remove the sonde/probe from the calibration vessel
and dry all wetted parts thoroughly with the lint-free cloth provided.</p>
<p>Gently pour the pre-prepared Point 2 solution into the calibration vessel then screw the
Sonde in all the way. Activate the cleaning system in order to remove any air bubbles that
may be clinging to the electrodes.</p>
<p>Follow the general procedure detailed above for Zero point calibration as far as step 6, then
click on the button for Point 2. Wait while the readings stabilise and the electrode calibrates.
<p>The Calibration Report on the top line displays the voltage output from the electrode in
millivolts (mV). This value is stored in the electrode's memory and can be recalled at any
time.</p>
"""
#--------------------
# Rhodamine
#--------------------
tCalibChannelInfo["Rhodamine"] = {}
tCalibChannelInfo["Rhodamine"]["ucPoint"]  = 2
tCalibChannelInfo["Rhodamine"]["sNetwork"] = '''
<strong>Calibration Points</strong>
<p>All fluorescent electrodes have two calibration points. Careful calibration is essential in
order to ensure consistent and reliable results across the full measurement range.</p>
<p>When a fluorescent electrode is first installed, it should be calibrated at the Zero point in
order to correct for any small differences in the Measurement Chamber.</p>
<p>The electrode should subsequently be Zeroed (calibrated at Point 1 in clean water) before
each day’s use. A two point calibration should be carried out once a month to ensure
optimum accuracy.</p>
'''
tCalibChannelInfo["Rhodamine"]["Point"]    = []
tCalibChannelInfo["Rhodamine"]["Point"].append({})
tCalibChannelInfo["Rhodamine"]["Point"].append({})
tCalibChannelInfo["Rhodamine"]["Point"][0]["sName"]          = "Clean water"
tCalibChannelInfo["Rhodamine"]["Point"][0]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Rhodamine"]["Point"][0]["sNetwork"]       = """
<strong>Zero Point Calibration</strong>
<p>To calibrate the zero point (Point 1), follow these steps:</p>
<ol>
<li>Create the calibration vessel as described in section 5.4. Calibration Vessel.</li>
<li>Pour clean water into the calibration vessel (bottled still mineral water is ideal).</li>
<li>Remove the storage cap from the pH electrode if fitted. Wash the sonde/probe in clean
water, then gently lower the sonde/probe onto the calibration vessel and screw into place.</li>
<li>Activate the sonde/probe cleaning feature in order to remove any air bubbles that may be
clinging to the electrode. To do this click the Clean sonde/probe button.</li>
<li>Wait until the temperature and electrode readings are completely stable. The longer
you can leave the sonde/probe to achieve thermal equilibrium before proceeding, the
better. A minimum of two minutes is recommended.</li>
<li>Ensure the temperature of the solution is between 5°C and 40°C (41°F – 104°F).</li>
<li>Click on the Cal button adjacent to the Point 1 Cal box.
When Point 1 calibration is complete, the calibration date and the voltage output from the
electrode in millivolts (mV) will be written into the calibration box.
This value is stored in the sonde/probe's memory and will be displayed each time the sonde/probe is
connected to ProLink.</li>
</ol>

<strong>Verifying the Zero Calibration</strong>
<p>An accurate zero point calibration is essential to the correct operation of the fluorescent
electrodes. The zero point calibration can sometimes be erroneous due to small air bubbles
or microscopic suspended solids in the calibration solution. For this reason, it is important
to verify the zero point calibration before proceeding to calibrate the other points.</p>

<p>After calibrating the zero point, activate the sonde/probe cleaning feature then allow the reading
to settle. Check the reading is zero. If not, re-calibrate the zero point.</p>
"""
tCalibChannelInfo["Rhodamine"]["Point"][1]["sName"]          = "100ug/L Rhod"
tCalibChannelInfo["Rhodamine"]["Point"][1]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Rhodamine"]["Point"][1]["sNetwork"]       = """
<strong>Calibrating the Second Point</strong>
<p>When calibrating any fluorescent electrode, the Zero point must be calibrated first
within the same calibration session (i.e. without disconnecting the AS-Pro™).
<p>A Point 2 calibration standard must be prepared to suit each electrode being calibrated.
Each electrode type has a specific requirement, which is detailed in manual.</p>
<p>Once calibrated at Point 1 (the zero point), remove the sonde/probe from the calibration vessel
and dry all wetted parts thoroughly with the lint-free cloth provided.</p>
<p>Gently pour the pre-prepared Point 2 solution into the calibration vessel then screw the
Sonde in all the way. Activate the cleaning system in order to remove any air bubbles that
may be clinging to the electrodes.</p>
<p>Follow the general procedure detailed above for Zero point calibration as far as step 6, then
click on the button for Point 2. Wait while the readings stabilise and the electrode calibrates.
<p>The Calibration Report on the top line displays the voltage output from the electrode in
millivolts (mV). This value is stored in the electrode's memory and can be recalled at any
time.</p>
"""
#--------------------
# Fluorescein
#--------------------
tCalibChannelInfo["Fluorescein"] = {}
tCalibChannelInfo["Fluorescein"]["ucPoint"]  = 2
tCalibChannelInfo["Fluorescein"]["sNetwork"] = '''
<strong>Calibration Points</strong>
<p>All fluorescent electrodes have two calibration points. Careful calibration is essential in
order to ensure consistent and reliable results across the full measurement range.</p>
<p>When a fluorescent electrode is first installed, it should be calibrated at the Zero point in
order to correct for any small differences in the Measurement Chamber.</p>
<p>The electrode should subsequently be Zeroed (calibrated at Point 1 in clean water) before
each day’s use. A two point calibration should be carried out once a month to ensure
optimum accuracy.</p>
'''
tCalibChannelInfo["Fluorescein"]["Point"]    = []
tCalibChannelInfo["Fluorescein"]["Point"].append({})
tCalibChannelInfo["Fluorescein"]["Point"].append({})
tCalibChannelInfo["Fluorescein"]["Point"][0]["sName"]          = "Clean water"
tCalibChannelInfo["Fluorescein"]["Point"][0]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Fluorescein"]["Point"][0]["sNetwork"]       = """
<strong>Zero Point Calibration</strong>
<p>To calibrate the zero point (Point 1), follow these steps:</p>
<ol>
<li>Create the calibration vessel as described in section 5.4. Calibration Vessel.</li>
<li>Pour clean water into the calibration vessel (bottled still mineral water is ideal).</li>
<li>Remove the storage cap from the pH electrode if fitted. Wash the sonde/probe in clean
water, then gently lower the sonde/probe onto the calibration vessel and screw into place.</li>
<li>Activate the sonde/probe cleaning feature in order to remove any air bubbles that may be
clinging to the electrode. To do this click the Clean sonde/probe button.</li>
<li>Wait until the temperature and electrode readings are completely stable. The longer
you can leave the sonde/probe to achieve thermal equilibrium before proceeding, the
better. A minimum of two minutes is recommended.</li>
<li>Ensure the temperature of the solution is between 5°C and 40°C (41°F – 104°F).</li>
<li>Click on the Cal button adjacent to the Point 1 Cal box.
When Point 1 calibration is complete, the calibration date and the voltage output from the
electrode in millivolts (mV) will be written into the calibration box.
This value is stored in the sonde/probe's memory and will be displayed each time the sonde/probe is
connected to ProLink.</li>
</ol>

<strong>Verifying the Zero Calibration</strong>
<p>An accurate zero point calibration is essential to the correct operation of the fluorescent
electrodes. The zero point calibration can sometimes be erroneous due to small air bubbles
or microscopic suspended solids in the calibration solution. For this reason, it is important
to verify the zero point calibration before proceeding to calibrate the other points.</p>

<p>After calibrating the zero point, activate the sonde/probe cleaning feature then allow the reading
to settle. Check the reading is zero. If not, re-calibrate the zero point.</p>
"""
tCalibChannelInfo["Fluorescein"]["Point"][1]["sName"]          = "100ug/L Fscein"
tCalibChannelInfo["Fluorescein"]["Point"][1]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Fluorescein"]["Point"][1]["sNetwork"]       = """
<strong>Calibrating the Second Point</strong>
<p>When calibrating any fluorescent electrode, the Zero point must be calibrated first
within the same calibration session (i.e. without disconnecting the AS-Pro™).
<p>A Point 2 calibration standard must be prepared to suit each electrode being calibrated.
Each electrode type has a specific requirement, which is detailed in manual.</p>
<p>Once calibrated at Point 1 (the zero point), remove the sonde/probe from the calibration vessel
and dry all wetted parts thoroughly with the lint-free cloth provided.</p>
<p>Gently pour the pre-prepared Point 2 solution into the calibration vessel then screw the
Sonde in all the way. Activate the cleaning system in order to remove any air bubbles that
may be clinging to the electrodes.</p>
<p>Follow the general procedure detailed above for Zero point calibration as far as step 6, then
click on the button for Point 2. Wait while the readings stabilise and the electrode calibrates.
<p>The Calibration Report on the top line displays the voltage output from the electrode in
millivolts (mV). This value is stored in the electrode's memory and can be recalled at any
time.</p>
"""
#--------------------
# Refined Oil
#--------------------
tCalibChannelInfo["Refined Oil"] = {}
tCalibChannelInfo["Refined Oil"]["ucPoint"]  = 2
tCalibChannelInfo["Refined Oil"]["sNetwork"] = '''
<strong>Calibration Points</strong>
<p>All fluorescent electrodes have two calibration points. Careful calibration is essential in
order to ensure consistent and reliable results across the full measurement range.</p>
<p>When a fluorescent electrode is first installed, it should be calibrated at the Zero point in
order to correct for any small differences in the Measurement Chamber.</p>
<p>The electrode should subsequently be Zeroed (calibrated at Point 1 in clean water) before
each day’s use. A two point calibration should be carried out once a month to ensure
optimum accuracy.</p>
'''
tCalibChannelInfo["Refined Oil"]["Point"]    = []
tCalibChannelInfo["Refined Oil"]["Point"].append({})
tCalibChannelInfo["Refined Oil"]["Point"].append({})
tCalibChannelInfo["Refined Oil"]["Point"][0]["sName"]          = "Clean water"
tCalibChannelInfo["Refined Oil"]["Point"][0]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Refined Oil"]["Point"][0]["sNetwork"]       = """
<strong>Zero Point Calibration</strong>
<p>To calibrate the zero point (Point 1), follow these steps:</p>
<ol>
<li>Create the calibration vessel as described in section 5.4. Calibration Vessel.</li>
<li>Pour clean water into the calibration vessel (bottled still mineral water is ideal).</li>
<li>Remove the storage cap from the pH electrode if fitted. Wash the sonde/probe in clean
water, then gently lower the sonde/probe onto the calibration vessel and screw into place.</li>
<li>Activate the sonde/probe cleaning feature in order to remove any air bubbles that may be
clinging to the electrode. To do this click the Clean sonde/probe button.</li>
<li>Wait until the temperature and electrode readings are completely stable. The longer
you can leave the sonde/probe to achieve thermal equilibrium before proceeding, the
better. A minimum of two minutes is recommended.</li>
<li>Ensure the temperature of the solution is between 5°C and 40°C (41°F – 104°F).</li>
<li>Click on the Cal button adjacent to the Point 1 Cal box.
When Point 1 calibration is complete, the calibration date and the voltage output from the
electrode in millivolts (mV) will be written into the calibration box.
This value is stored in the sonde/probe's memory and will be displayed each time the sonde/probe is
connected to ProLink.</li>
</ol>

<strong>Verifying the Zero Calibration</strong>
<p>An accurate zero point calibration is essential to the correct operation of the fluorescent
electrodes. The zero point calibration can sometimes be erroneous due to small air bubbles
or microscopic suspended solids in the calibration solution. For this reason, it is important
to verify the zero point calibration before proceeding to calibrate the other points.</p>

<p>After calibrating the zero point, activate the sonde/probe cleaning feature then allow the reading
to settle. Check the reading is zero. If not, re-calibrate the zero point.</p>
"""
tCalibChannelInfo["Refined Oil"]["Point"][1]["sName"]          = "10ppm Naphtha"
tCalibChannelInfo["Refined Oil"]["Point"][1]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Refined Oil"]["Point"][1]["sNetwork"]       = """
<strong>Calibrating the Second Point</strong>
<p>When calibrating any fluorescent electrode, the Zero point must be calibrated first
within the same calibration session (i.e. without disconnecting the AS-Pro™).
<p>A Point 2 calibration standard must be prepared to suit each electrode being calibrated.
Each electrode type has a specific requirement, which is detailed in manual.</p>
<p>Once calibrated at Point 1 (the zero point), remove the sonde/probe from the calibration vessel
and dry all wetted parts thoroughly with the lint-free cloth provided.</p>
<p>Gently pour the pre-prepared Point 2 solution into the calibration vessel then screw the
Sonde in all the way. Activate the cleaning system in order to remove any air bubbles that
may be clinging to the electrodes.</p>
<p>Follow the general procedure detailed above for Zero point calibration as far as step 6, then
click on the button for Point 2. Wait while the readings stabilise and the electrode calibrates.
<p>The Calibration Report on the top line displays the voltage output from the electrode in
millivolts (mV). This value is stored in the electrode's memory and can be recalled at any
time.</p>
"""
#--------------------
# CDOM
#--------------------
tCalibChannelInfo["CDOM"] = {}
tCalibChannelInfo["CDOM"]["ucPoint"]  = 2
tCalibChannelInfo["CDOM"]["sNetwork"] = '''
<strong>Calibration Points</strong>
<p>All fluorescent electrodes have two calibration points. Careful calibration is essential in
order to ensure consistent and reliable results across the full measurement range.</p>
<p>When a fluorescent electrode is first installed, it should be calibrated at the Zero point in
order to correct for any small differences in the Measurement Chamber.</p>
<p>The electrode should subsequently be Zeroed (calibrated at Point 1 in clean water) before
each day’s use. A two point calibration should be carried out once a month to ensure
optimum accuracy.</p>
'''
tCalibChannelInfo["CDOM"]["Point"]    = []
tCalibChannelInfo["CDOM"]["Point"].append({})
tCalibChannelInfo["CDOM"]["Point"].append({})
tCalibChannelInfo["CDOM"]["Point"][0]["sName"]          = "Clean water"
tCalibChannelInfo["CDOM"]["Point"][0]["sCalReportUnit"] = "mV"
tCalibChannelInfo["CDOM"]["Point"][0]["sNetwork"]       = """
<strong>Zero Point Calibration</strong>
<p>To calibrate the zero point (Point 1), follow these steps:</p>
<ol>
<li>Create the calibration vessel as described in section 5.4. Calibration Vessel.</li>
<li>Pour clean water into the calibration vessel (bottled still mineral water is ideal).</li>
<li>Remove the storage cap from the pH electrode if fitted. Wash the sonde/probe in clean
water, then gently lower the sonde/probe onto the calibration vessel and screw into place.</li>
<li>Activate the sonde/probe cleaning feature in order to remove any air bubbles that may be
clinging to the electrode. To do this click the Clean sonde/probe button.</li>
<li>Wait until the temperature and electrode readings are completely stable. The longer
you can leave the sonde/probe to achieve thermal equilibrium before proceeding, the
better. A minimum of two minutes is recommended.</li>
<li>Ensure the temperature of the solution is between 5°C and 40°C (41°F – 104°F).</li>
<li>Click on the Cal button adjacent to the Point 1 Cal box.
When Point 1 calibration is complete, the calibration date and the voltage output from the
electrode in millivolts (mV) will be written into the calibration box.
This value is stored in the sonde/probe's memory and will be displayed each time the sonde/probe is
connected to ProLink.</li>
</ol>

<strong>Verifying the Zero Calibration</strong>
<p>An accurate zero point calibration is essential to the correct operation of the fluorescent
electrodes. The zero point calibration can sometimes be erroneous due to small air bubbles
or microscopic suspended solids in the calibration solution. For this reason, it is important
to verify the zero point calibration before proceeding to calibrate the other points.</p>

<p>After calibrating the zero point, activate the sonde/probe cleaning feature then allow the reading
to settle. Check the reading is zero. If not, re-calibrate the zero point.</p>
"""
tCalibChannelInfo["CDOM"]["Point"][1]["sName"]          = "100ppb Quinine"
tCalibChannelInfo["CDOM"]["Point"][1]["sCalReportUnit"] = "mV"
tCalibChannelInfo["CDOM"]["Point"][1]["sNetwork"]       = """
<strong>Calibrating the Second Point</strong>
<p>When calibrating any fluorescent electrode, the Zero point must be calibrated first
within the same calibration session (i.e. without disconnecting the AS-Pro™).
<p>A Point 2 calibration standard must be prepared to suit each electrode being calibrated.
Each electrode type has a specific requirement, which is detailed in manual.</p>
<p>Once calibrated at Point 1 (the zero point), remove the sonde/probe from the calibration vessel
and dry all wetted parts thoroughly with the lint-free cloth provided.</p>
<p>Gently pour the pre-prepared Point 2 solution into the calibration vessel then screw the
Sonde in all the way. Activate the cleaning system in order to remove any air bubbles that
may be clinging to the electrodes.</p>
<p>Follow the general procedure detailed above for Zero point calibration as far as step 6, then
click on the button for Point 2. Wait while the readings stabilise and the electrode calibrates.
<p>The Calibration Report on the top line displays the voltage output from the electrode in
millivolts (mV). This value is stored in the electrode's memory and can be recalled at any
time.</p>
"""
#--------------------
# Crude Oil
#--------------------
tCalibChannelInfo["Crude Oil"] = {}
tCalibChannelInfo["Crude Oil"]["ucPoint"]  = 2
tCalibChannelInfo["Crude Oil"]["sNetwork"] = '''
<strong>Calibration Points</strong>
<p>All fluorescent electrodes have two calibration points. Careful calibration is essential in
order to ensure consistent and reliable results across the full measurement range.</p>
<p>When a fluorescent electrode is first installed, it should be calibrated at the Zero point in
order to correct for any small differences in the Measurement Chamber.</p>
<p>The electrode should subsequently be Zeroed (calibrated at Point 1 in clean water) before
each day’s use. A two point calibration should be carried out once a month to ensure
optimum accuracy.</p>
'''
tCalibChannelInfo["Crude Oil"]["Point"]    = []
tCalibChannelInfo["Crude Oil"]["Point"].append({})
tCalibChannelInfo["Crude Oil"]["Point"].append({})
tCalibChannelInfo["Crude Oil"]["Point"][0]["sName"]          = "Clean water"
tCalibChannelInfo["Crude Oil"]["Point"][0]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Crude Oil"]["Point"][0]["sNetwork"]       = """
<strong>Zero Point Calibration</strong>
<p>To calibrate the zero point (Point 1), follow these steps:</p>
<ol>
<li>Create the calibration vessel as described in section 5.4. Calibration Vessel.</li>
<li>Pour clean water into the calibration vessel (bottled still mineral water is ideal).</li>
<li>Remove the storage cap from the pH electrode if fitted. Wash the sonde/probe in clean
water, then gently lower the sonde/probe onto the calibration vessel and screw into place.</li>
<li>Activate the sonde/probe cleaning feature in order to remove any air bubbles that may be
clinging to the electrode. To do this click the Clean sonde/probe button.</li>
<li>Wait until the temperature and electrode readings are completely stable. The longer
you can leave the sonde/probe to achieve thermal equilibrium before proceeding, the
better. A minimum of two minutes is recommended.</li>
<li>Ensure the temperature of the solution is between 5°C and 40°C (41°F – 104°F).</li>
<li>Click on the Cal button adjacent to the Point 1 Cal box.
When Point 1 calibration is complete, the calibration date and the voltage output from the
electrode in millivolts (mV) will be written into the calibration box.
This value is stored in the sonde/probe's memory and will be displayed each time the sonde/probe is
connected to ProLink.</li>
</ol>

<strong>Verifying the Zero Calibration</strong>
<p>An accurate zero point calibration is essential to the correct operation of the fluorescent
electrodes. The zero point calibration can sometimes be erroneous due to small air bubbles
or microscopic suspended solids in the calibration solution. For this reason, it is important
to verify the zero point calibration before proceeding to calibrate the other points.</p>

<p>After calibrating the zero point, activate the sonde/probe cleaning feature then allow the reading
to settle. Check the reading is zero. If not, re-calibrate the zero point.</p>
"""
tCalibChannelInfo["Crude Oil"]["Point"][1]["sName"]          = "Point 2"
tCalibChannelInfo["Crude Oil"]["Point"][1]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Crude Oil"]["Point"][1]["sNetwork"]       = """
<strong>Calibrating the Second Point</strong>
<p>When calibrating any fluorescent electrode, the Zero point must be calibrated first
within the same calibration session (i.e. without disconnecting the AS-Pro™).
<p>A Point 2 calibration standard must be prepared to suit each electrode being calibrated.
Each electrode type has a specific requirement, which is detailed in manual.</p>
<p>Once calibrated at Point 1 (the zero point), remove the sonde/probe from the calibration vessel
and dry all wetted parts thoroughly with the lint-free cloth provided.</p>
<p>Gently pour the pre-prepared Point 2 solution into the calibration vessel then screw the
Sonde in all the way. Activate the cleaning system in order to remove any air bubbles that
may be clinging to the electrodes.</p>
<p>Follow the general procedure detailed above for Zero point calibration as far as step 6, then
click on the button for Point 2. Wait while the readings stabilise and the electrode calibrates.
<p>The Calibration Report on the top line displays the voltage output from the electrode in
millivolts (mV). This value is stored in the electrode's memory and can be recalled at any
time.</p>
"""
#--------------------
# Tryptophan
#--------------------
tCalibChannelInfo["Tryptophan"] = {}
tCalibChannelInfo["Tryptophan"]["ucPoint"]  = 2
tCalibChannelInfo["Tryptophan"]["sNetwork"] = '''
<strong>Calibration Points</strong>
<p>All fluorescent electrodes have two calibration points. Careful calibration is essential in
order to ensure consistent and reliable results across the full measurement range.</p>
<p>When a fluorescent electrode is first installed, it should be calibrated at the Zero point in
order to correct for any small differences in the Measurement Chamber.</p>
<p>The electrode should subsequently be Zeroed (calibrated at Point 1 in clean water) before
each day’s use. A two point calibration should be carried out once a month to ensure
optimum accuracy.</p>
'''
tCalibChannelInfo["Tryptophan"]["Point"]    = []
tCalibChannelInfo["Tryptophan"]["Point"].append({})
tCalibChannelInfo["Tryptophan"]["Point"].append({})
tCalibChannelInfo["Tryptophan"]["Point"][0]["sName"]          = "Clean water"
tCalibChannelInfo["Tryptophan"]["Point"][0]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Tryptophan"]["Point"][0]["sNetwork"]       = """
<strong>Zero Point Calibration</strong>
<p>To calibrate the zero point (Point 1), follow these steps:</p>
<ol>
<li>Create the calibration vessel as described in section 5.4. Calibration Vessel.</li>
<li>Pour clean water into the calibration vessel (bottled still mineral water is ideal).</li>
<li>Remove the storage cap from the pH electrode if fitted. Wash the sonde/probe in clean
water, then gently lower the sonde/probe onto the calibration vessel and screw into place.</li>
<li>Activate the sonde/probe cleaning feature in order to remove any air bubbles that may be
clinging to the electrode. To do this click the Clean sonde/probe button.</li>
<li>Wait until the temperature and electrode readings are completely stable. The longer
you can leave the sonde/probe to achieve thermal equilibrium before proceeding, the
better. A minimum of two minutes is recommended.</li>
<li>Ensure the temperature of the solution is between 5°C and 40°C (41°F – 104°F).</li>
<li>Click on the Cal button adjacent to the Point 1 Cal box.
When Point 1 calibration is complete, the calibration date and the voltage output from the
electrode in millivolts (mV) will be written into the calibration box.
This value is stored in the sonde/probe's memory and will be displayed each time the sonde/probe is
connected to ProLink.</li>
</ol>

<strong>Verifying the Zero Calibration</strong>
<p>An accurate zero point calibration is essential to the correct operation of the fluorescent
electrodes. The zero point calibration can sometimes be erroneous due to small air bubbles
or microscopic suspended solids in the calibration solution. For this reason, it is important
to verify the zero point calibration before proceeding to calibrate the other points.</p>

<p>After calibrating the zero point, activate the sonde/probe cleaning feature then allow the reading
to settle. Check the reading is zero. If not, re-calibrate the zero point.</p>
"""
tCalibChannelInfo["Tryptophan"]["Point"][1]["sName"]          = "Point 2"
tCalibChannelInfo["Tryptophan"]["Point"][1]["sCalReportUnit"] = "mV"
tCalibChannelInfo["Tryptophan"]["Point"][1]["sNetwork"]       = """
<strong>Calibrating the Second Point</strong>
<p>When calibrating any fluorescent electrode, the Zero point must be calibrated first
within the same calibration session (i.e. without disconnecting the AS-Pro™).
<p>A Point 2 calibration standard must be prepared to suit each electrode being calibrated.
Each electrode type has a specific requirement, which is detailed in manual.</p>
<p>Once calibrated at Point 1 (the zero point), remove the sonde/probe from the calibration vessel
and dry all wetted parts thoroughly with the lint-free cloth provided.</p>
<p>Gently pour the pre-prepared Point 2 solution into the calibration vessel then screw the
Sonde in all the way. Activate the cleaning system in order to remove any air bubbles that
may be clinging to the electrodes.</p>
<p>Follow the general procedure detailed above for Zero point calibration as far as step 6, then
click on the button for Point 2. Wait while the readings stabilise and the electrode calibrates.
<p>The Calibration Report on the top line displays the voltage output from the electrode in
millivolts (mV). This value is stored in the electrode's memory and can be recalled at any
time.</p>
"""







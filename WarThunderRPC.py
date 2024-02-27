import requests
import urllib.request
import json
import time
from PIL import Image, ImageDraw
from pypresence import Presence
import telemetry
import mapinfo
from pprint import pprint


clockTimer = int(time.time())
client_id = "1211769535468937237"  # Replace this with your own client id
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop


# ------ VARIABLES ------ #
#  isinVehicle(boolean), vehicleType(str), vehicleName(str),
#  inMatch(boolean), mainObjective(str->int),

# ------ INDICATORS.json ------ #
while True:
    urlIndicators = "http://127.0.0.1:8111/indicators"
    try:
        indicators = requests.get(urlIndicators)
    except:
        print("War Thunder is not running, or port 8111 is already occupied!")
        time.sleep(1)
        print("Exiting...")
        time.sleep(4)
        exit()

    textIndicators=indicators.text
    info = json.loads(textIndicators)

    isinVehicle = info['valid'] #is game active
    try:
        vehicleType = info['army'] # is vehicle tank or air
        vehicleName = info['type'] # what vehicle is it
    except:
        vehicleType = "Unknown"
        vehicleName = "Unknown"

# ------ MISSION.json ------ #

    urlMission = "http://127.0.0.1:8111/mission.json"
    mission = requests.get(urlMission)
    
    try:
        textMission=mission.text
        info = json.loads(textMission)
        print (info["objectives"][0]['text'])
        mainObjective = info["objectives"][0]['text']
        inMatch = info["objectives"][0]['primary']
    except:
        mainObjective = "false"
        inMatch = False

    # ------ MAP_INFO.json ------ #

    urlMap = "http://127.0.0.1:8111/map_info.json"
    map = requests.get(urlMap)

    textMap=map.text
    info = json.loads(textMap)
    inMap = info['valid'] # is player in a map

    strippedVehicleName = vehicleName.replace("tankModels/", "")
    truncatedVehicleName = strippedVehicleName.replace('_', ' ')

    # --- FANCY DOODADS --- #
    urllib.request.urlretrieve('http://127.0.0.1:8111/map.img', "map.jpg")
    img = Image.open("map.jpg")

    def find_map_info():
        return(telemetry.mapinfo.get_grid_info(map_img=img))

    x = find_map_info()
    currentMap = x['name'].replace('_', ' ')

    # ------ RPC UPDATE ------ #

    if isinVehicle is True and inMap is False:
        RPC.update(state="In the hangar", details="Browsing vehicles..", start=clockTimer, large_image="logo")  # Set the presence

    # --- AIR --- #
    elif isinVehicle is True and inMap is True and inMatch is True and vehicleType=="air":
        if mainObjective.startswith("Capture the enemy point"):
            RPC.update(state="Piloting a "+truncatedVehicleName.upper(), details="Ground Battle Match", start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())
        elif mainObjective.startswith("Capture and maintain superiority over the points"):
            RPC.update(state="Piloting a "+truncatedVehicleName.upper(), details="Ground Domination Match", start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())
        elif mainObjective.startswith("Capture and maintain superiority over the airfields"):
            RPC.update(state="Piloting a "+truncatedVehicleName.upper(), details="Air Domination Match on "+currentMap, start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())
        elif mainObjective.startswith("Capture and hold airfields."):
            RPC.update(state="Piloting a "+truncatedVehicleName.upper(), details="Air Domination Match on "+currentMap, start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())   
        elif mainObjective.startswith("Prevent capture of allied point"):
            RPC.update(state="Piloting a "+truncatedVehicleName.upper(), details="Ground Battle Match", start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())
        elif mainObjective.startswith("Capture and keep hold of the point"):    
            RPC.update(state="Piloting a "+truncatedVehicleName.upper(), details="Ground Conquest Match", start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())
        elif mainObjective.startswith("Capture and hold the airfield"):
            RPC.update(state="Piloting a "+truncatedVehicleName.upper(), details="Air Domination Match on "+currentMap, start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())
        elif mainObjective.startswith("Destroy the enemy ground vehicles"):
            RPC.update(state="Piloting a "+truncatedVehicleName.upper(), details="Air Ground Strike Match on "+currentMap, start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())
        elif mainObjective.startswith("Destroy the highlighted targets"):
            RPC.update(state="Piloting a "+truncatedVehicleName.upper(), details="Air Frontline Match on "+currentMap, start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())
        elif currentMap=="UNKNOWN":
            RPC.update(state="Piloting a "+truncatedVehicleName.upper(), details="Air Match", start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())
        else:
            RPC.update(state="Piloting a "+truncatedVehicleName.upper(), details="Air Match", start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())    

    # --- TANKS --- #
    elif isinVehicle is True and vehicleType=="tank" and inMap is True and inMatch is True:
            if mainObjective.startswith("Capture and maintain superiority over the points"):
                RPC.update(state="Driving a "+truncatedVehicleName.upper(), details="Ground Domination Match on "+currentMap, start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())
            elif mainObjective.startswith("Capture the enemy point"):
                RPC.update(state="Driving a "+truncatedVehicleName.upper(), details="Ground Battle Match on "+currentMap, start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())
            elif mainObjective.startswith("Prevent the capture of the allied point"):
                RPC.update(state="Driving a "+truncatedVehicleName.upper(), details="Ground Battle Match on "+currentMap, start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())    
            elif mainObjective.startswith("Capture and keep hold of the point"):
                RPC.update(state="Driving a "+truncatedVehicleName.upper(), details="Ground Conquest Match on "+currentMap, start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())
            else:
                RPC.update(state="Driving a "+truncatedVehicleName.upper(), details="Ground Match on "+currentMap, start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())

    # --- CATCH-ALL --- #
    elif isinVehicle is False and inMap is True:
        RPC.update(state="Unknown vehicle", details="In-game", start=clockTimer, large_image="logo", large_text="War Thunder")

    # --- TEST DRIVE --- #
    elif isinVehicle is True and inMap is True and inMatch is False and vehicleType=="tank" or inMatch is False:
        RPC.update(state="Driving a "+truncatedVehicleName.upper(), details="In Test Drive", start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())
    elif isinVehicle is True and inMap is True and inMatch is False and vehicleType=="air" or inMatch is False:
        RPC.update(state="Piloting a "+truncatedVehicleName.upper(), details="In Test Drive", start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())
    print("Updated Presence")

    time.sleep(3) # Update rich presence every 10 seconds
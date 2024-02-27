import requests
import json
from pypresence import Presence
import time

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

    textMission=mission.text
    info = json.loads(textMission)
    try:
        for doc in info["objectives"]:
            inMatch = doc['primary'] # is player in a match
            mainObjective = doc['text'] # what game mode is player in
    except:
        print("ive done goofed)")

    # ------ MAP_INFO.json ------ #

    urlMap = "http://127.0.0.1:8111/map_info.json"
    map = requests.get(urlMap)

    textMap=map.text
    info = json.loads(textMap)
    inMap = info['valid'] # is player in a map

    strippedVehicleName = vehicleName.replace("tankModels/", "")
    truncatedVehicleName = strippedVehicleName.replace('_', ' ')



    # ------ RPC UPDATE ------ #

    if isinVehicle is True and inMap is False:
        RPC.update(state="In the hangar", details="Browsing vehicles..", start=clockTimer, large_image="logo")  # Set the presence

    # --- AIR --- #
    elif isinVehicle is True and inMap is True and inMatch is True and vehicleType=="air":
        if mainObjective.startswith("Capture the enemy point"):
            RPC.update(state="Piloting a "+truncatedVehicleName.upper()+"..", details="In a Ground Match", start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())
        elif mainObjective.startswith("Prevent capture of allied point"):
            RPC.update(state="Piloting a "+truncatedVehicleName.upper()+"..", details="In a Ground Match", start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())
        elif mainObjective.startswith("Capture and keep hold of the point"):
            RPC.update(state="Piloting a "+truncatedVehicleName.upper()+"..", details="In a Ground Match", start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())
        elif mainObjective.startswith("Capture and hold the airfield"):
            RPC.update(state="Piloting a "+truncatedVehicleName.upper()+"..", details="In a Air Match", start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())
        elif mainObjective.startswith("Destroy the enemy ground vehicles"):
            RPC.update(state="Piloting a "+truncatedVehicleName.upper()+"..", details="In a Air Match", start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())
        elif mainObjective.startswith("Destroy the highlighted targets"):
            RPC.update(state="Piloting a "+truncatedVehicleName.upper()+"..", details="In a Air Match", start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())
        else:
            RPC.update(state="Piloting a "+truncatedVehicleName.upper()+"..", details="In a Air Match", start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())

    # --- TANKS --- #
    elif isinVehicle is True and inMap is True and inMatch is True and vehicleType=="tank":
            RPC.update(state="Driving a "+truncatedVehicleName.upper()+"..", details="In a Ground Match", start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())
    
    # --- CATCH-ALL --- #
    elif isinVehicle is False and inMap is True:
        RPC.update(state="Unknown vehicle..", details="In-game", start=clockTimer, large_image="logo", large_text="War Thunder")

    # --- TEST DRIVE --- #
    elif isinVehicle is True and inMap is True and inMatch is False and vehicleType=="tank":
        RPC.update(state="Driving a "+truncatedVehicleName.upper()+"..", details="In Test Drive", start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())
    elif isinVehicle is True and inMap is True and inMatch is False and vehicleType=="air":
        RPC.update(state="Piloting a "+truncatedVehicleName.upper()+"..", details="In Test Drive", start=clockTimer, large_image="logo", large_text="War Thunder", small_image="https://encyclopedia.warthunder.com/i/images/"+strippedVehicleName+".png",small_text=truncatedVehicleName.upper())
    print("Updated Presence")


    time.sleep(10) # Update rich presence every 10 seconds
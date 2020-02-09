from htbapi.core import getRequest, postRequest, postHTTPC

def ownMachine(machineid, apitoken, hash, difficulty):
    # /machines/own
    # {"flag": hash, "difficulty": difficulty * 10, "id": machineid}
    pass

def getAllMachines(apitoken):
    return getRequest("/machines/get/all/", apitoken)
        
def getAllActiveMachines(apitoken):
    activemachines = []
    allmachines = getAllMachines(apitoken)
    for machine in allmachines:
        if machine["retired"] == False:
            activemachines.append(machine)
    return activemachines

def getAllRetiredMachines(apitoken):
    retiredmachines = []
    allmachines = getAllMachines(apitoken)
    for machine in allmachines:
        if machine["retired"] == True:
            retiredmachines.append(machine)
    return retiredmachines

def resetMachine(machineid, apitoken):
    # /vm/reset/machineid
    pass

def startMachine(machineid, apitoken):
    # /vm/vip/assign/machineid/
    postHTTPC("/vm/vip/assign/" + machineid, "", apitoken)

def stopMachine(machineid, apitoken):
    # /vm/vip/remove/machineid/
    pass

def getSpawnedMachines(apitoken):
    # /api/machines/spawned/
    pass

def getTerminatingMachines(apitoken):
    # /api/machines/terminating/
    pass

def getResettingMachines(apitoken):
    # /api/machines/resetting/
    pass


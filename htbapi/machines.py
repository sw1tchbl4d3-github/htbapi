from htbapi.core import getRequest, postRequest, rawPostSSL

def ownMachine(machineid, apitoken, hash, difficulty):
    # /machines/own
    # {"flag": hash, "difficulty": difficulty * 10, "id": machineid}
    pass

def getAllMachines(apitoken):
    return getRequest("/machines/get/all/", apitoken).json()
        
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
    rawPostSSL("/vm/vip/reset/" + str(machineid), apitoken)

def startMachine(machineid, apitoken):
    rawPostSSL("/vm/vip/assign/" + str(machineid), apitoken)

def stopMachine(machineid, apitoken):
    rawPostSSL("/vm/vip/remove/" + str(machineid), apitoken)

def extendMachine(machineid, apitoken):
    rawPostSSL("/vm/vip/extend/" + str(machineid), apitoken)

def getSpawnedMachines(apitoken):
    # /api/machines/spawned/
    pass

def getTerminatingMachines(apitoken):
    # /api/machines/terminating/
    pass

def getResettingMachines(apitoken):
    # /api/machines/resetting/
    pass


from htbapi.core import getRequest, postRequest, rawPostSSL

def ownMachine(machineid, apitoken, flag, difficulty):
    # return rawPostSSL("/machines/own", '{"flag":"' + flag + '","difficulty":' + str(difficulty * 10) + ',"id":' + str(machineid) + "}", apitoken)
    # currently this function doesnt work, gonna fix it soon.
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
    return rawPostSSL("/vm/vip/reset/" + str(machineid), "", apitoken)

def assignMachine(machineid, apitoken):
    return rawPostSSL("/vm/vip/assign/" + str(machineid), "", apitoken)

def stopMachine(machineid, apitoken):
    return rawPostSSL("/vm/vip/remove/" + str(machineid), "", apitoken)

def extendMachine(machineid, apitoken):
    return rawPostSSL("/vm/vip/extend/" + str(machineid), "", apitoken)

def getSpawnedMachines(apitoken):
    return getRequest("/machines/spawned/", apitoken).json()

def getTerminatingMachines(apitoken):
    return getRequest("/machines/terminating/", apitoken).json()

def getResettingMachines(apitoken):
    return getRequest("/machines/resetting/", apitoken).json()


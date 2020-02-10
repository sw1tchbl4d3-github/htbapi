from htbapi.core import getRequest, rawPostSSL

def ownRoot(machineid, apitoken, flag, difficulty):
    return rawPostSSL(f"/machines/own/root/{machineid}", f'{{"hash":"{flag}","difficulty":{difficulty * 10}}}', apitoken, "json", "")

def ownUser(machineid, apitoken, flag, difficulty):
    return rawPostSSL(f"/machines/own/user/{machineid}", f'{{"hash":"{flag}","difficulty":{difficulty * 10}}}', apitoken, "json", "")

def ownMachine(machineid, apitoken, flag, difficulty):
    return rawPostSSL(f"/machines/own", f'{{"hash":"{flag}","difficulty":{difficulty * 10}, "id":{machineid}}}', apitoken, "json", "")

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
    return rawPostSSL(f"/vm/vip/reset/{machineid}", "", apitoken, "", "")

def assignMachine(machineid, apitoken):
    return rawPostSSL(f"/vm/vip/assign/{machineid}", "", apitoken, "", "")

def stopMachine(machineid, apitoken):
    return rawPostSSL(f"/vm/vip/remove/{machineid}", "", apitoken, "", "")

def extendMachine(machineid, apitoken):
    return rawPostSSL(f"/vm/vip/extend/{machineid}", "", apitoken, "", "")

def getSpawnedMachines(apitoken):
    return getRequest("/machines/spawned/", apitoken).json()

def getTerminatingMachines(apitoken):
    return getRequest("/machines/terminating/", apitoken).json()

def getResettingMachines(apitoken):
    return getRequest("/machines/resetting/", apitoken).json()


from htbapi.core import getRequest, rawPostSSL

def ownRoot(machineid, apitoken, flag, difficulty):
    response = rawPostSSL(f"/machines/own/root/{machineid}", f'{{"flag":"{flag}","difficulty":{difficulty * 10}}}', apitoken, "json", "")
    if '"success":"1"'.encode() in response:
        return "success"
    elif "Incorrect hash".encode() in response:
        return "flag_invalid"
    else:
        return "failed"

def ownUser(machineid, apitoken, flag, difficulty):
    response =  rawPostSSL(f"/machines/own/user/{machineid}", f'{{"flag":"{flag}","difficulty":{difficulty * 10}}}', apitoken, "json", "")
    if '"success":"1"'.encode() in response:
        return "success"
    elif "Incorrect hash".encode() in response:
        return "flag_invalid"
    else:
        return "failed"

def ownMachine(machineid, apitoken, flag, difficulty):
    response =  rawPostSSL(f"/machines/own", f'{{"flag":"{flag}","difficulty":{difficulty * 10},"id":{machineid}}}', apitoken, "json", "")
    if '"success":"1"'.encode() in response:
        return "success"
    elif "Incorrect flag".encode() in response:
        return "flag_invalid"
    else:
        return "failed"

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
    response =  rawPostSSL(f"/vm/reset/{machineid}", "", apitoken, "", "")
    if "was not reset. Another reset from this user is pending.".encode() in response:
        return "reset_pending"
    elif "will be reset".encode() in response:
        return "success"
    else:
        return "failed"

def assignMachine(machineid, apitoken):
    response = rawPostSSL(f"/vm/vip/assign/{machineid}", "", apitoken, "", "")
    if "Machine deployed to lab.".encode() in response:
        return "success"
    elif "You already have an active machine.".encode() in response:
        return "already_have_machine"
    elif "Incorrect lab type.".encode() in response:
        return "no_vip"
    else:
        return "failed"


def stopMachine(machineid, apitoken):
    response = rawPostSSL(f"/vm/vip/remove/{machineid}", "", apitoken, "", "")
    if "Machine scheduled for termination.".encode() in response:
        return "success"
    elif "This machine is not active.".encode() in response:
        return "machine_not_active"
    elif "Incorrect lab type.".encode() in response:
        return "no_vip"
    else:
        return "failed"

def extendMachine(machineid, apitoken):
    response = rawPostSSL(f"/vm/vip/extend/{machineid}", "", apitoken, "", "")
    if "Machine not assigned to this lab.".encode() in response:
        return "machine_not_active"
    elif "Machine extended by 24 hours.".encode() in response:
        return "success"
    elif "Incorrect lab type.".encode() in response:
        return "no_vip"
    else: 
        return "failed"

def getSpawnedMachines(apitoken):
    return getRequest("/machines/spawned/", apitoken).json()

def getTerminatingMachines(apitoken):
    return getRequest("/machines/terminating/", apitoken).json()

def getResettingMachines(apitoken):
    return getRequest("/machines/resetting/", apitoken).json()


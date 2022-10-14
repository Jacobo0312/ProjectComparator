
class Project:
    def __init__(self, name,flows, vpn, tir):
        self.name = name
        self.flows = flows
        self.vpn = vpn
        self.tir = tir


    ##Getters and setters

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getFlows(self):
        return self.flows
    
    def setFlows(self, flows):
        self.flows = flows

    def getVpn(self):
        return self.vpn
    
    def setVpn(self, vpn):
        self.vpn = vpn

    def getTir(self):
        return self.tir


    ##To String

    def __str__(self):
        return "Project NAME:" + self.name + "\nFLOWS:" + str(self.flows) + "\nVPN:" + str(self.vpn) + "\nTIR:" + str(self.tir)+"\n-------------------"

    ##Equals

    def __eq__(self, other):
        if isinstance(other, Project):
            return self.name == other.name
        return False
import numpy_financial as npf
from Project import Project

#Input file

file=open("input.txt","r")


#Leer la TIR

#TIR=input("Introduce la TIR: ")
TIR=float(file.readline())
TIR=float(TIR)



#Leer cantidad de proyectos

#PROJECTS=input("Introduce la cantidad de proyectos: ")
PROJECTS=int(file.readline())
PROJECTS=int(PROJECTS)

#Leer cantidad de años

#YEARS=input("Introduce la cantidad de años: ")
YEARS=int(file.readline())
YEARS=int(YEARS)


#Ingresas flujos de cada proyecto
FLOWS=list()

for i in range(0,PROJECTS):
    FLOWS.append(list())
    for j in range(0,YEARS+1):
        if (j==0):
            #flow=input("Ingresa la inversion inicial del proyecto ")
            flow=file.readline()
        else:
            #flow=input("Introduce el flujo del proyecto "+str(i)+" en el año "+str(j)+": ")
            flow=file.readline()

        FLOWS[i].append(int(flow))

"""
#Mostrar todos los flujos

for i in range(0,PROJECTS):
    print(FLOWS[i])

"""


#Calcular el valor presente de cada proyecto

VPS=list()

for i in range(0,PROJECTS):
    VPS.append(list())
    for j in range(1,YEARS+1):
        vps=FLOWS[i][j]/(1+TIR)**(j)
        VPS[i].append(float(vps))


#Calcular vpn y tir de cada proyecto

VPN=list()
TIR=list()

for i in range(0,PROJECTS):
    VPN.append(sum(VPS[i]))
    TIR.append(npf.irr(FLOWS[i]))


#Crear lista de proyectos

PROJECTS_LIST=list()

for i in range(0,PROJECTS):
    PROJECTS_LIST.append(Project("Proyecto "+chr(65+i),FLOWS[i],VPN[i],TIR[i]))


#Mostrar lista de proyectos

for i in range(0,PROJECTS):
    print(str(PROJECTS_LIST[i]))

#Raking por tir

PROJECTS_LIST.sort(key=lambda x: x.getTir(), reverse=True)
rankingTir=PROJECTS_LIST

#Raking por vpn

PROJECTS_LIST.sort(key=lambda x: x.getVpn(), reverse=True)
rankingVpn=PROJECTS_LIST


#Ranking final

rankingFinal=list()

def compareProjects(rankingTir, rankingVpn):
    for i in range(0,PROJECTS):
        if(rankingTir[i]==rankingVpn[i]):
            rankingFinal.append(rankingTir[i])
            rankingTir.remove(rankingTir[i])
            rankingVpn.remove(rankingVpn[i])
            break
        else:
            print("TEST")


#Project 1 VPN > Project 2 VPN
def vs(project1, project2):
    flows=list()

    for i in range(0,YEARS+1):
        flows.append(project1.getFlows()[i]-project2.getFlows()[i])

    vpn=(project1.getVpn()-project2.getVpn())+flows[0]

    tir=npf.irr(flows)

    return vpn,tir


print(vs(PROJECTS_LIST[0],PROJECTS_LIST[1]))


#compareProjects(rankingTir, rankingVpn)






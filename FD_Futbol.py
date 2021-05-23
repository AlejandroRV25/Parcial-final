#Importar librerÃ­as.
import pandas as p
from matplotlib import pyplot as pl
import geopandas as gp
#Lectura de archivo .xlsx
Arch=p.read_excel('Futbol_Partidos.xlsx')
#Suma goles locales. 1
def suma_local():
    suma_l=Arch['goles_local'].sum()
    return suma_l
#Suma goles visitantes. 2
def suma_visitante():
    suma_v=Arch['goles_visita'].sum()
    return suma_v
#Graficar goles locales VS visitantes. Unión 1 y 2
def graf_gol():
    x=['Locales', 'Visitantes']
    y=[suma_local(),suma_visitante()]
    colors=['purple','orange']
    pl.bar(x,y,color=colors)
    pl.title('Locales VS Visitantes.')
    pl.ylabel('Goles')
    pl.grid(True)
    pl.show
#Suma de goles total. 3
def suma_total():
    suma=suma_local()+suma_visitante()
    print('La suma total de goles en todos los partidos es igual a:',suma)
    goles=[]
    partido=[]
    for i in range(len(Arch.iloc[:,0])):
        sumando_1=Arch.iloc[i,3]
        sumando_2=Arch.iloc[i,4]
        sumaT=sumando_1+sumando_2
        goles.append(sumaT)
        partido.append(i+1)    
    pl.scatter(partido,goles,color='purple')
    pl.title('Goles totales por partido.')
    pl.xlabel('Número de partido.')
    pl.ylabel('Goles.')
    pl.show
#Goles locales por campeonato. 4
def gol_l_camp():
    col=Arch.iloc[:,5]
    camp=set(col)
    camp=list(camp)
    goles=[]
    tags=[1,2,3,4,5,6,7,8,9,10]
    for i in range(len(camp)):
        suma=0
        for j in range(len(col)):
            comp=camp[i]
            search=Arch.iloc[j,5]
            if search==comp:
                if search in camp:
                    gol=Arch.iloc[j,3]
                    suma=suma+gol
        print('La suma de goles locales en el campeonato',comp,'es igaul a:',suma)
        goles.append(suma)
    pl.bar(tags,goles,color='purple')
    pl.title('Goles locales por campeonato.')
    pl.ylabel('Goles.')
    pl.xlabel(' Kirin    CFD   PdC   AFC    GC      Fr      CA    FWC    FWCQ   CP')
    pl.grid(True)
    pl.show
#Goles visitantes por campeonato. 5
def gol_v_camp():
    col=Arch.iloc[:,5]
    camp=set(col)
    camp=list(camp)
    goles=[]
    tags=[1,2,3,4,5,6,7,8,9,10]
    for i in range(len(camp)):
        suma=0
        for j in range(len(col)):
            comp=camp[i]
            search=Arch.iloc[j,5]
            if search==comp:
                if search in camp:
                    gol=Arch.iloc[j,4]
                    suma=suma+gol
        print('La suma de goles visitantes en el campeonato',comp,'es igaul a:',suma)
        goles.append(suma)
    pl.bar(tags,goles,color='purple')
    pl.title('Goles visitantes por campeonato.')
    pl.ylabel('Goles.')
    pl.xlabel(' Kirin    CFD   PdC   AFC    GC      Fr      CA    FWC    FWCQ   CP')
    pl.grid(True)
    pl.show
#Goles por campeonato. 6
def gol_t_camp():
    col=Arch.iloc[:,5]
    camp=set(col)
    camp=list(camp)
    goles=[]
    tags=[1,2,3,4,5,6,7,8,9,10]
    for i in range(len(camp)):
            suma=0
            total=0
            for j in range(len(col)):
                comp=camp[i]
                search=Arch.iloc[j,5]
                if search==comp:
                    if search in camp:
                        gol1=Arch.iloc[j,3]
                        gol2=Arch.iloc[j,4]
                        suma=gol1+gol2
                        total=total+suma
            print('La suma de goles en el campeonato',comp,'es igual a:',total)
            goles.append(total)
    pl.bar(tags,goles,color='purple')
    pl.title('Goles totales por campeonato.')
    pl.xlabel(' Kirin    CFD   PdC   AFC    GC      Fr      CA    FWC    FWCQ   CP')
    pl.ylabel('Goles.')
    pl.grid(True)
    pl.show
#Cantidad de partidos por selección. 7
def partidos_s():
    tags=[1,2,3,4,5,6,7,8,9,10,11,12]
    campeonatos=[]
    col=Arch.iloc[:,1]
    col2=Arch.iloc[:,2]
    seleccion=set(col)
    seleccion=list(seleccion)
    s1=list(col);s2=list(col2)
    s1.extend(s2)
    for i in range(len(seleccion)):
        cont=0
        for j in range(len(s1)):
            comp=seleccion[i]
            search=s1[j]
            if search==comp:
                cont=cont+1
        print(comp,'participó en',cont,'campeonatos.')
        campeonatos.append(cont)
    pl.bar(tags,campeonatos,color='purple')
    pl.title('Campeonatos por selección.')
    pl.xlabel('J     AR    BR    CO    PA    BO    EC    CH    UR    PE    VE    Q')
    pl.ylabel('Cantidad de campeonatos')
    pl.grid(True)
    pl.show
#Partidos local y visitante por selección. 8
def partido_sele():
    local=[]
    visitante=[]
    col=Arch.iloc[:,1]
    col2=Arch.iloc[:,2]
    sel=set(col);sel=list(sel)
    s1=list(col);s2=list(col2)
    for i in range(len(sel)):
            cont=0
            cont2=0
            for j in range(len(s1)):
                comp=sel[i]
                search=s1[j]
                if search==comp:
                    cont=cont+1
            for h in range(len(s2)):
                    comp1=sel[i]
                    search1=s2[h]
                    if search1==comp1:
                        cont2=cont2+1
            visitante.append(cont2)
            local.append(cont)
            print(comp,'jugó',cont,'veces como local, y',cont2,'como visitante.')
    fig,ax=pl.subplots()
    ax.barh(sel,local,color='purple',label='Partidos locales.')
    ax.barh(sel,visitante,color='orange',left=local,label='Partidos visitantes.')
    ax.invert_yaxis()
    ax.legend(loc=(1.1,0.8))
    pl.grid(True)
    pl.show()
#Selección con más goles. 9
def mas_goles():
    col=Arch.iloc[:,1]
    col2=Arch.iloc[:,3]
    sel=set(col);sel=list(sel)
    s1=list(col);s2=list(col2)
    col3=Arch.iloc[:,2]
    col4=Arch.iloc[:,4]
    s3=list(col3);s4=list(col4)
    mayor=0
    sel_n=None
    for i in sel:
        suma=0
        for j in range(len(s1)):
            comp=s1[j]
            comp2=s3[j]
            if comp==i:
                gol=s2[j]
                suma=suma+gol
            if comp2==i:
                gol2=s4[j]
                suma=suma+gol2
        if suma>mayor:
            mayor=suma
            sel_n=i
    print('La selección con más goles fue',sel_n,'con',mayor,'goles en total.')
#Selección con más goles en contra. 10
def mas_goles_contra():
    col=Arch.iloc[:,1]
    col2=Arch.iloc[:,4]
    sel=set(col);sel=list(sel)
    s1=list(col);s2=list(col2)
    col3=Arch.iloc[:,2]
    col4=Arch.iloc[:,3]
    s3=list(col3);s4=list(col4)
    mayor=0
    sel_n=None
    for i in sel:
        suma=0
        for j in range(len(s1)):
            comp=s1[j]
            comp2=s3[j]
            if comp==i:
                gol=s2[j]
                suma=suma+gol
            if comp2==i:
                gol2=s4[j]
                suma=suma+gol2
        if suma>mayor:
            mayor=suma
            sel_n=i
    print('La selección con más goles en contra fue',sel_n,'con',mayor,'goles en total.')
#Partidos de selección por ingreso de datos. 11
def ingreso_sel():
    seleccion=input('Ingrese el nombre de la selección que desea buscar: ')
    col_n1=Arch.iloc[:,1];col_n2=Arch.iloc[:,2];fecha=Arch.iloc[:,0];torneo=Arch.iloc[:,5]
    s1=list(col_n1);s2=list(col_n2);fecha=list(fecha);torneo=list(torneo)
    for i in range(len(s1)):
        cont=None
        tor_p=None
        fec_p=None
        loc=s1[i];vis=s2[i]
        while seleccion not in s1 or seleccion not in s2:
            seleccion=input('Esa selección no está registrada en este programa, intente con otra: ')
        if loc==seleccion:
            cont=vis
        elif vis==seleccion:
            cont=loc
        if loc==seleccion or vis==seleccion:
            fec_p=fecha[i]
            tor_p=torneo[i]
            print('El',fec_p,seleccion,'jugó contra',cont,'en un torneo de',tor_p)
#Partidos local-visitante por ingreso de datos. 12
def loc_vis():
    seleccion=input('Ingrese el nombre de la selección que desea buscar: ')
    nomb=Arch.iloc[:,1];nomb2=Arch.iloc[:,2];s1=list(nomb);s2=list(nomb2)
    cont_local=0;cont_visi=0
    for i in range(len(s1)):
        loc=s1[i];vis=s2[i]
        while seleccion not in s1 or seleccion not in s2:
            seleccion=input('Esa selección no está registrada en este programa, intente con otra: ')
        if loc==seleccion:
            cont_local=cont_local+1
        elif vis==seleccion:
            cont_visi=cont_visi+1
    print('La selección de',seleccion,'jugó',cont_local,'partidos como local, y',cont_visi,'como visitante.')
#Ciudades donde se ha jugado por ingreso de datos. 13
def ciudades():
    seleccion=input('Ingrese el nombre de la selección que desea buscar: ')
    nomb=Arch.iloc[:,1];nomb2=Arch.iloc[:,2];ciud=Arch.iloc[:,6]
    s1=list(nomb);s2=list(nomb2);ciudad=list(ciud)
    for i in range(len(s1)):
        comp1=s1[i];comp2=s2[i];comp_c=ciudad[i]
        while seleccion not in s1 or seleccion not in s2:
            seleccion=input('Esa selección no está registrada en este programa, intente con otra: ')
        if comp1==seleccion:
            print(seleccion,'jugó como local en',comp_c)
        elif comp2==seleccion:
            print(seleccion,'jugó como visitante en',comp_c)

#14 Repetido.

#Partidos perdidos y ganados. 15
def partidos_general():
    nomb=Arch.iloc[:,1];nomb2=Arch.iloc[:,2];torneo=Arch.iloc[:,5];win_loc=Arch.iloc[:,10];win_vis=Arch.iloc[:,11]
    s1=list(nomb);s2=list(nomb2);tor=list(torneo);win_l=list(win_loc);win_v=list(win_vis)
    seleccion=input('Ingrese el nombre de la selección que desea buscar: ')
    while seleccion not in s1 or seleccion not in s2:
        seleccion=input('Esa selección no está registrada en este programa, intente con otra: ')
    torneo=set(tor)
    cont_w=0
    cont_l=0
    for j in torneo: 
        for i in range(len(s1)):
            comp1=s1[i];comp2=s2[i];comp_wl=win_l[i];comp_wv=win_v[i];torneo=tor[i]
            if torneo==j:
                if comp1==seleccion and comp_wl==1:
                    cont_w=cont_w+1
                elif comp2==seleccion and comp_wv==1:
                    cont_w=cont_w+1
                elif comp1==seleccion and comp_wv==1:
                    cont_l=cont_l+1
                elif comp2==seleccion and comp_wl==1:
                    cont_l=cont_l+1
        print('En el torneo de',j,'la selección de',seleccion,'ganó',cont_w,'partidos y perdió',cont_l,'pardidos.')
    print('La selección de',seleccion,'ganó un total de',cont_w,'partidos y perdió un total de',cont_l,'partidos.')
#Partidos, goles, por selección. 16
def todo_sobre_goles():
    nomb=Arch.iloc[:,1];nomb2=Arch.iloc[:,2];gol=Arch.iloc[:,3];gol2=Arch.iloc[:,4]
    s1=list(nomb);s2=list(nomb2);goles=list(gol);goles2=list(gol2)
    seleccion=input('Ingrese el nombre de la selección que desea buscar: ')
    while seleccion not in s1 or seleccion not in s2:
        seleccion=input('Esa selección no está registrada en este programa, intente con otra: ')
    cont_p=0
    cont_w=0
    cont_l=0
    cont_d=0
    gol=0
    gol_rival=0
    for i in range(len(s1)):
        comp1=s1[i];comp2=s2[i];gol_l=goles[i];gol_v=goles2[i]
        if comp1==seleccion or comp2==seleccion:
            cont_p=cont_p+1
            if comp1==seleccion:
                gol=gol+gol_l
                gol_rival=gol_rival+gol_v
            elif comp2==seleccion:
                gol=gol+gol_v
                gol_rival=gol_rival+gol_l
            if comp1==seleccion and gol_l>gol_v:
                cont_w=cont_w+1
            elif comp2==seleccion and gol_v>gol_l:
                cont_w=cont_w+1
            elif gol_l==gol_v:
                cont_d=cont_d+1
            else:
                cont_l=cont_l+1
    print('La selección de',seleccion,'ganó',cont_w,'empató',cont_d,'y perdió',cont_l,'partidos con',gol,'goles a favor, y',gol_rival,'goles en contra.')
#Mejor selección por ranking. 17
def mejor_seleccion():
    nomb=Arch.iloc[:,1];nomb2=Arch.iloc[:,2];rank_loc=Arch.iloc[:,12];rank_vis=Arch.iloc[:,14];tor=Arch.iloc[:,5]
    s1=list(nomb);s2=list(nomb2);rank_lo=list(rank_loc);rank_vi=list(rank_vis);torneo=list(tor)
    camp=set(torneo)
    mejor_l=None
    mejor_v=None
    
    for j in camp:
        rank_local=999
        rank_visit=999
        for i in range(len(s1)):
            comp1=s1[i];comp2=s2[i];rank1=rank_lo[i];rank2=rank_vi[i];champ=torneo[i]
            if champ==j:
                if rank1<rank_local:
                    mejor_l=comp1
                    rank_local=rank1
                if rank2<rank_visit:
                    mejor_v=comp2
                    rank_visit=rank2
        print('Según el campeonato de',j,'la selección de',mejor_l,'es el mejor equipo local de la lista con el ranking',rank_local,', y la selección de',mejor_v,'es el mejor equipo visitante de la lista con el ranking',rank_visit,'\n**************************************************************')
#Partidos a lo largo del tiempo. 18
def partidos_años():
    fecha=Arch.iloc[:,0];nomb=Arch.iloc[:,1];nomb2=Arch.iloc[:,2];resultado=Arch.iloc[:,10];resultado2=Arch.iloc[:,11]
    año=list(fecha);s1=list(nomb);s2=list(nomb2);win=list(resultado);lose=list(resultado2)
    seleccion=input('Ingrese el nombre de la selección que desea buscar: ')
    fechas=[]
    victorias=0
    derrotas=0
    partidos=[]
    while seleccion not in s1 and seleccion not in s2:
        seleccion=input('Esa selección no está registrada en este programa, intente con otra: ')
    for i in range(len(s1)):
        años=año[i];comp1=s1[i];comp2=s2[i];comp_win=win[i];comp_lose=lose[i]
        if comp1==seleccion or comp2==seleccion:
            if comp_win==1 and comp1==seleccion:
                victorias=victorias+1
                print('En la fecha',años,'la selección de',comp1,'ganó el partido contra la selección de',comp2)
            elif comp_lose==1 and comp1==seleccion:
                derrotas=derrotas+1
                print('En la fecha',años,'la selección de',comp1,'perdió el partido contra la selección de',comp2)
            elif comp_win==1 and comp2==seleccion:
                victorias=victorias+1
                print('En la fecha',años,'la selección de',comp2,'ganó el partido contra la selección de',comp1)
            elif comp_lose==1 and comp2==seleccion:
                derrotas=derrotas+1
                print('En la fecha',años,'la selección de',comp2,'perdió el partido contra la selección de',comp1)
            elif comp_lose==0 and comp_win==0:
                print('En la fecha',años,'la selección de',comp1,'empató el partido contra la selección de',comp2)
            dateTimeObj=años
            dateStr = dateTimeObj.strftime("%Y")
            dateStr=int(dateStr)
            fechas.append(dateStr)
    lista_j=list(range(1993,2019,1))
    excep=[]
    for j in lista_j:
        b=fechas.count(j)
        if b==0:
            excep.append(j)
            fechas.append(j)    
    años_totales=set(fechas);años_total=list(años_totales)
    for h in range(1993,2019,1):
        eliminacion=h-1993
        par=fechas.count(h)
        if h not in excep:
            partidos.append(par)
        else:
            partidos.insert(eliminacion,0)
    pl.bar(años_total,partidos,color='purple')
    pl.title('Partidos de la selección')
    pl.ylabel('Partidos.')
    pl.xlabel('Fecha.')
    pl.grid(True)
    pl.show

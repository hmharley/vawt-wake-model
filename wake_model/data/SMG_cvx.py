from pyoptsparse import Optimization, SNOPT, pyOpt_solution
import csv
import numpy as np
from numpy import pi,sqrt,exp,fabs,log,sin,arctan,cosh
import matplotlib.pyplot as plt
import database_call as dbc
# from matplotlib import rcParams
# rcParams['font.family'] = 'Times New Roman'


def overlay(xt,ys,tsr,sol):
    ntsr = np.size(tsr)
    nsol = np.size(sol)

    dtsr = 'f1 = 0.'
    for i in range(ntsr):
        tpow = '+'+str(tsr[i])+'*xt**'+str(ntsr-1-i)
        dtsr = dtsr+tpow

    dsol = 'f2 = 0.'
    for i in range(nsol):
        spow = '+'+str(sol[i])+'*ys**'+str(nsol-1-i)
        dsol = dsol+spow

    exec(dtsr)
    exec(dsol)
    return f1*f2



def veldist(dn,lat,men,sdv1,sdv2,sdv3,sdv4,rat,tns,spr1,spr2,spr3,spr4,scl1,scl2,scl3):

    sdv_v = sdv3*sdv2*sdv1*exp(sdv2*dn)*exp(sdv1)*exp(-sdv1*exp(sdv2*dn))+sdv4

    spr_v = spr3*spr2*spr1*exp(spr2*dn)*exp(spr1)*exp(-spr1*exp(spr2*dn))+spr4
    # spr_v = 1.

    f1 = -1./(sdv_v*sqrt(2.*pi))*exp(-((lat/spr_v)-men)**2/(2.*sdv_v**2))*(1./(1.+exp(rat*fabs((lat/spr_v))-tns)))
    f2 = scl3*scl2*scl1*exp(scl2*dn)*exp(scl1)*exp(-scl1*exp(scl2*dn))

    return f1*f2 + 1.



def starccm_read(fdata,dia,windd,length,opt_print):
    start = length/30.
    lendat =  np.linspace(start,length,30)/dia

    for j in range(np.size(fdata)):
        for k in range(30):
            name = str(k+1)
            exec('pos'+name+' = np.array([])')
            exec('velo'+name+' = np.array([])')
        wind = windd[j]

        f = open(fdata[j])

        csv_f = csv.reader(f)

        i = 0
        for row in csv_f:
            if row[0] != 'null' and i != 0:
                pos1 = np.append(pos1,float(row[0]))
            if row[2] != 'null' and i != 0:
                pos2 = np.append(pos2,float(row[2]))
            if row[4] != 'null' and i != 0:
                pos3 = np.append(pos3,float(row[4]))
            if row[6] != 'null' and i != 0:
                pos4 = np.append(pos4,float(row[6]))
            if row[8] != 'null' and i != 0:
                pos5 = np.append(pos5,float(row[8]))
            if row[10] != 'null' and i != 0:
                pos6 = np.append(pos6,float(row[10]))
            if row[12] != 'null' and i != 0:
                pos7 = np.append(pos7,float(row[12]))
            if row[14] != 'null' and i != 0:
                pos8 = np.append(pos8,float(row[14]))
            if row[16] != 'null' and i != 0:
                pos9 = np.append(pos9,float(row[16]))
            if row[18] != 'null' and i != 0:
                pos10 = np.append(pos10,float(row[18]))
            if row[20] != 'null' and i != 0:
                pos11 = np.append(pos11,float(row[20]))
            if row[22] != 'null' and i != 0:
                pos12 = np.append(pos12,float(row[22]))
            if row[24] != 'null' and i != 0:
                pos13 = np.append(pos13,float(row[24]))
            if row[26] != 'null' and i != 0:
                pos14 = np.append(pos14,float(row[26]))
            if row[28] != 'null' and i != 0:
                pos15 = np.append(pos15,float(row[28]))
            if row[30] != 'null' and i != 0:
                pos16 = np.append(pos16,float(row[30]))
            if row[32] != 'null' and i != 0:
                pos17 = np.append(pos17,float(row[32]))
            if row[34] != 'null' and i != 0:
                pos18 = np.append(pos18,float(row[34]))
            if row[36] != 'null' and i != 0:
                pos19 = np.append(pos19,float(row[36]))
            if row[38] != 'null' and i != 0:
                pos20 = np.append(pos20,float(row[38]))
            if row[40] != 'null' and i != 0:
                pos21 = np.append(pos21,float(row[40]))
            if row[42] != 'null' and i != 0:
                pos22 = np.append(pos22,float(row[42]))
            if row[44] != 'null' and i != 0:
                pos23 = np.append(pos23,float(row[44]))
            if row[46] != 'null' and i != 0:
                pos24 = np.append(pos24,float(row[46]))
            if row[48] != 'null' and i != 0:
                pos25 = np.append(pos25,float(row[48]))
            if row[50] != 'null' and i != 0:
                pos26 = np.append(pos26,float(row[50]))
            if row[52] != 'null' and i != 0:
                pos27 = np.append(pos27,float(row[52]))
            if row[54] != 'null' and i != 0:
                pos28 = np.append(pos28,float(row[54]))
            if row[56] != 'null' and i != 0:
                pos29 = np.append(pos29,float(row[56]))
            if row[58] != 'null' and i != 0:
                pos30 = np.append(pos30,float(row[58]))

            if row[1] != 'null' and i != 0:
                velo1 = np.append(velo1,float(row[1]))
            if row[3] != 'null' and i != 0:
                velo2 = np.append(velo2,float(row[3]))
            if row[5] != 'null' and i != 0:
                velo3 = np.append(velo3,float(row[5]))
            if row[7] != 'null' and i != 0:
                velo4 = np.append(velo4,float(row[7]))
            if row[9] != 'null' and i != 0:
                velo5 = np.append(velo5,float(row[9]))
            if row[11] != 'null' and i != 0:
                velo6 = np.append(velo6,float(row[11]))
            if row[13] != 'null' and i != 0:
                velo7 = np.append(velo7,float(row[13]))
            if row[15] != 'null' and i != 0:
                velo8 = np.append(velo8,float(row[15]))
            if row[17] != 'null' and i != 0:
                velo9 = np.append(velo9,float(row[17]))
            if row[19] != 'null' and i != 0:
                velo10 = np.append(velo10,float(row[19]))
            if row[21] != 'null' and i != 0:
                velo11 = np.append(velo11,float(row[21]))
            if row[23] != 'null' and i != 0:
                velo12 = np.append(velo12,float(row[23]))
            if row[25] != 'null' and i != 0:
                velo13 = np.append(velo13,float(row[25]))
            if row[27] != 'null' and i != 0:
                velo14 = np.append(velo14,float(row[27]))
            if row[29] != 'null' and i != 0:
                velo15 = np.append(velo15,float(row[29]))
            if row[31] != 'null' and i != 0:
                velo16 = np.append(velo16,float(row[31]))
            if row[33] != 'null' and i != 0:
                velo17 = np.append(velo17,float(row[33]))
            if row[35] != 'null' and i != 0:
                velo18 = np.append(velo18,float(row[35]))
            if row[37] != 'null' and i != 0:
                velo19 = np.append(velo19,float(row[37]))
            if row[39] != 'null' and i != 0:
                velo20 = np.append(velo20,float(row[39]))
            if row[41] != 'null' and i != 0:
                velo21 = np.append(velo21,float(row[41]))
            if row[43] != 'null' and i != 0:
                velo22 = np.append(velo22,float(row[43]))
            if row[45] != 'null' and i != 0:
                velo23 = np.append(velo23,float(row[45]))
            if row[47] != 'null' and i != 0:
                velo24 = np.append(velo24,float(row[47]))
            if row[49] != 'null' and i != 0:
                velo25 = np.append(velo25,float(row[49]))
            if row[51] != 'null' and i != 0:
                velo26 = np.append(velo26,float(row[51]))
            if row[53] != 'null' and i != 0:
                velo27 = np.append(velo27,float(row[53]))
            if row[55] != 'null' and i != 0:
                velo28 = np.append(velo28,float(row[55]))
            if row[57] != 'null' and i != 0:
                velo29 = np.append(velo29,float(row[57]))
            if row[59] != 'null' and i != 0:
                velo30 = np.append(velo30,float(row[59]))
            i += 1

        f.close()

        if opt_print == True:
            print 'Imported Data Set',j+1
        # print 'DATA IMPORTED'

        posdn = np.array([])
        poslt = np.array([])
        velod = np.array([])
        for i in range(30):
            name = str(i+1)
            ind = str(i)

            #Ordering the data numerically by the position
            exec('pos'+name+', velo'+name+' = (list(t) for t in zip(*sorted(zip(pos'+name+', velo'+name+'))))')
            #STAR-CCM+ data contained repeated values; this creates new sets of data with repeats eliminated
            exec('pos'+name+'_0 = np.array([])\nvelo'+name+'_0 = np.array([])\nfor i in range(np.size(pos'+name+')):\n\tif pos'+name+'[i] not in pos'+name+'_0:\n\t\tpos'+name+'_0 = np.append(pos'+name+'_0,pos'+name+'[i])\n\t\tvelo'+name+'_0 = np.append(velo'+name+'_0,velo'+name+'[i])\npos'+name+' = np.copy(pos'+name+'_0)/dia\nvelo'+name+' = np.copy(velo'+name+'_0)/wind')
            #Deleting wall boundary data
            exec('delvec = np.array([])\nfor j in range(np.size(pos'+name+')):\n\tif pos'+name+'[j] > 5. or pos'+name+'[j] < -5.:\n\t\tdelvec = np.append(delvec,j)\ndelvec = delvec[::-1]\nfor j in range(np.size(delvec)):\n\tvelo'+name+' = np.delete(velo'+name+',delvec[j])\n\tpos'+name+' = np.delete(pos'+name+',delvec[j])')
            #Deleting values greater than 1*wind
            exec('delvec = np.array([])\nfor j in range(np.size(pos'+name+')):\n\tif velo'+name+'[j] > 1. or fabs(pos'+name+'[j]) > 1.2:\n\t\tdelvec = np.append(delvec,j)\ndelvec = delvec[::-1]\nfor j in range(np.size(delvec)):\n\tvelo'+name+' = np.delete(velo'+name+',delvec[j])\n\tpos'+name+' = np.delete(pos'+name+',delvec[j])')
            exec('lensize = np.size(pos'+name+')')
            exec('posdn = np.append(posdn,np.ones(lensize)*lendat['+ind+'])\nposlt = np.append(poslt,pos'+name+')\nvelod = np.append(velod,velo'+name+')')

    return posdn,poslt,velod


def obj_func(xdict):
    for s in range(5):
        for t in range(23):
            sname = str(s+1)
            tname = str(t+1)
            exec('global posdns'+sname+'t'+tname)
            exec('global poslts'+sname+'t'+tname)
            exec('global velods'+sname+'t'+tname)

    ment = xdict['ment']
    sdv1t = xdict['sdv1t']
    sdv2t = xdict['sdv2t']
    sdv3t = xdict['sdv3t']
    sdv4t = xdict['sdv4t']
    ratt = xdict['ratt']
    tnst = xdict['tnst']
    spr1t = xdict['spr1t']
    spr2t = xdict['spr2t']
    spr3t = xdict['spr3t']
    spr4t = xdict['spr4t']
    scl1t = xdict['scl1t']
    scl2t = xdict['scl2t']
    scl3t = xdict['scl3t']

    mens = xdict['mens']
    sdv1s = xdict['sdv1s']
    sdv2s = xdict['sdv2s']
    sdv3s = xdict['sdv3s']
    sdv4s = xdict['sdv4s']
    rats = xdict['rats']
    tnss = xdict['tnss']
    spr1s = xdict['spr1s']
    spr2s = xdict['spr2s']
    spr3s = xdict['spr3s']
    spr4s = xdict['spr4s']
    scl1s = xdict['scl1s']
    scl2s = xdict['scl2s']
    scl3s = xdict['scl3s']

    funcs = {}

    error = 0.
    tsrd = np.linspace(1.5,7.,23)
    sold = np.array([0.15,0.25,0.5,0.75,1.0])
    for s in range(5):
        for t in range(23):
            sname = str(s+1)
            tname = str(t+1)
            xt = tsrd[t]
            ys = sold[s]
            men = overlay(xt,ys,ment,mens)
            sdv1 = overlay(xt,ys,sdv1t,sdv1s)
            sdv2 = overlay(xt,ys,sdv2t,sdv2s)
            sdv3 = overlay(xt,ys,sdv3t,sdv3s)
            sdv4 = overlay(xt,ys,sdv4t,sdv4s)
            rat = overlay(xt,ys,ratt,rats)
            tns = overlay(xt,ys,tnst,tnss)
            spr1 = overlay(xt,ys,spr1t,spr1s)
            spr2 = overlay(xt,ys,spr2t,spr2s)
            spr3 = overlay(xt,ys,spr3t,spr3s)
            spr4 = overlay(xt,ys,spr4t,spr4s)
            scl1 = overlay(xt,ys,scl1t,scl1s)
            scl2 = overlay(xt,ys,scl2t,scl2s)
            scl3 = overlay(xt,ys,scl3t,scl3s)

            exec('for i in range(np.size(posdns'+sname+'t'+tname+')):\n\tif posdns'+sname+'t'+tname+'[i] > 0.58:\n\t\tvel = veldist(posdns'+sname+'t'+tname+'[i],poslts'+sname+'t'+tname+'[i],men,sdv1,sdv2,sdv3,sdv4,rat,tns,spr1,spr2,spr3,spr4,scl1,scl2,scl3)\n\t\terror = error + (vel-velods'+sname+'t'+tname+'[i])**2')

    funcs['obj'] = error

    fail = False

    return funcs, fail

if __name__ == "__main__":

    comp = 'mac'
    opt_print = True
    read_data = 4

    for s in range(5):
        for t in range(23):
            sname = str(s+1)
            tname = str(t+1)
            exec('global posdns'+sname+'t'+tname)
            exec('global poslts'+sname+'t'+tname)
            exec('global velods'+sname+'t'+tname)


    s1length = np.array([210,210,205,196,185,178,170,165,160,145,140,123,115,112,108,101,101,90,85,80,78,75,70])
    s2length = np.array([197,193,185,176,140,146,126,114,103,96,100,86,77,72,70,68,60,64,54,50,47,45,44])
    s3length = np.array([185,150,100,95,83,76,72,63,60,49,50,41,39,36,34,33,30,31,28,30,29,28,27])
    s4length = np.array([145,100,73,60,53,44,42,37,38,30,33,26,22,24,23,21,21,19,24,23,22,21,20])
    s5length = np.array([78,70,52,43,37,32,29,27,26,23,20,20,23,21,20,19,19,18,18,16,16,15,14])
    solidity = np.array(['s1','s2','s3','s4','s5'])
    tsr = np.linspace(150,700,23)

    s = np.array([])
    t = np.array([])
    for i in range(np.size(solidity)):
        for j in range(np.size(tsr)):
            s = np.append(s,solidity[i])
            t = np.append(t,str(int(tsr[j])))

    slength = np.array([])
    slength = np.append(slength,s1length)
    slength = np.append(slength,s2length)
    slength = np.append(slength,s3length)
    slength = np.append(slength,s4length)
    slength = np.append(slength,s5length)
    slength = slength*1.

    q = 0
    for i in range(5):
        for j in range(23):
            sname = str(i+1)
            tname = str(j+1)

            t2 = t[q]+'.0'

            wfit = s[q]+'_'+t2
            wfit2 = s[q]+'_'+t2
            wfit3 = s[q]+'_'+t2
            wfit4 = s[q]+'_'+t2
            wfit5 = s[q]+'_'+t2
            wfit6 = s[q]+'_'+t2

            length2 = slength[q]
            length3 = slength[q]
            length4 = slength[q]
            length5 = slength[q]
            length6 = slength[q]
            wind = 15.
            wind2 = 14.
            wind3 = 12.
            wind4 = 16.

            rad = 3.
            dia = rad*2.
            tsr = float(wfit[3]+'.'+wfit[4]+wfit[5])
            rot = tsr*wind/rad
            rot2 = tsr*wind2/rad
            rot3 = tsr*wind3/rad
            rot4 = tsr*wind4/rad
            rot5 = 17.
            rot6 = 18.
            wind5 = rot5*rad/tsr
            wind6 = rot6*rad/tsr

            if comp == 'mac':
                # fdata = '/Users/ning1/Documents/Flow Lab/STAR-CCM+/NACA0021/MoveForward/test.csv'
                fdata = '/Users/ning1/Documents/FLOW Lab/STAR-CCM+/NACA0021/MoveForward/Velocity Sections/'+wfit+'.csv'
                fdata2 = '/Users/ning1/Documents/FLOW Lab/STAR-CCM+/NACA0021/MoveForward/CrossValidate/vel14/Velocity/'+wfit2+'.csv'
                fdata3 = '/Users/ning1/Documents/FLOW Lab/STAR-CCM+/NACA0021/MoveForward/CrossValidate/vel12/Velocity/'+wfit3+'.csv'
                fdata4 = '/Users/ning1/Documents/FLOW Lab/STAR-CCM+/NACA0021/MoveForward/CrossValidate/vel16/Velocity/'+wfit4+'.csv'
                fdata5 = '/Users/ning1/Documents/FLOW Lab/STAR-CCM+/NACA0021/MoveForward/CrossValidate/rot17/Velocity/'+wfit5+'.csv'
                fdata6 = '/Users/ning1/Documents/FLOW Lab/STAR-CCM+/NACA0021/MoveForward/CrossValidate/rot18/Velocity/'+wfit6+'.csv'
            elif comp == 'fsl':
                fdata = '/fslhome/ebtingey/compute/moveForward/Velocity/'+wfit+'.csv'
                fdata2 = '/fslhome/ebtingey/compute/moveForward/vel14/Velocity/'+wfit2+'.csv'
                fdata3 = '/fslhome/ebtingey/compute/moveForward/vel12/Velocity/'+wfit3+'.csv'
                fdata4 = '/fslhome/ebtingey/compute/moveForward/vel16/Velocity/'+wfit4+'.csv'
                fdata5 = '/fslhome/ebtingey/compute/moveForward/rot17/Velocity/'+wfit5+'.csv'
                fdata6 = '/fslhome/ebtingey/compute/moveForward/rot18/Velocity/'+wfit6+'.csv'

            if read_data ==1:
                posdn,poslt,velod = starccm_read(np.array([fdata]),dia,np.array([wind]),slength[q],opt_print)
            if read_data ==2:
                posdn,poslt,velod = starccm_read(np.array([fdata,fdata2]),dia,np.array([wind,wind2]),slength[q],opt_print)
            if read_data ==3:
                posdn,poslt,velod = starccm_read(np.array([fdata,fdata2,fdata3]),dia,np.array([wind,wind2,wind3]),slength[q],opt_print)
            if read_data ==4:
                posdn,poslt,velod = starccm_read(np.array([fdata,fdata2,fdata3,fdata4]),dia,np.array([wind,wind2,wind3,wind4]),slength[q],opt_print)
            if read_data ==5:
                posdn,poslt,velod = starccm_read(np.array([fdata,fdata2,fdata3,fdata4,fdata5]),dia,np.array([wind,wind2,wind3,wind4,wind5]),slength[q],opt_print)
            if read_data ==6:
                posdn,poslt,velod = starccm_read(np.array([fdata,fdata2,fdata3,fdata4,fdata5,fdata6]),dia,np.array([wind,wind2,wind3,wind4,wind5,wind6]),slength[q],opt_print)

            exec('posdns'+sname+'t'+tname+' = posdn')
            exec('poslts'+sname+'t'+tname+' = poslt')
            exec('velods'+sname+'t'+tname+' = velod')

            print t[q],s[q]
            q += 1

    # Optimization
    optProb = Optimization('VAWTWake_Sheet', obj_func)
    optProb.addObj('obj')

    ordt = 5
    ords = 3

    ment0 = np.linspace(1,1,ordt)
    sdv1t0 = np.linspace(1,1,ordt)
    sdv2t0 = np.linspace(1,1,ordt)
    sdv3t0 = np.linspace(1,1,ordt)
    sdv4t0 = np.linspace(1,1,ordt)
    ratt0 = np.linspace(1,1,ordt)
    tnst0 = np.linspace(1,1,ordt)
    spr1t0 = np.linspace(1,1,ordt)
    spr2t0 = np.linspace(1,1,ordt)
    spr3t0 = np.linspace(1,1,ordt)
    spr4t0 = np.linspace(1,1,ordt)
    scl1t0 = np.linspace(1,1,ordt)
    scl2t0 = np.linspace(1,1,ordt)
    scl3t0 = np.linspace(1,1,ordt)

    mens0 = np.linspace(1,1,ords)
    sdv1s0 = np.linspace(1,1,ords)
    sdv2s0 = np.linspace(1,1,ords)
    sdv3s0 = np.linspace(1,1,ords)
    sdv4s0 = np.linspace(1,1,ords)
    rats0 = np.linspace(1,1,ords)
    tnss0 = np.linspace(1,1,ords)
    spr1s0 = np.linspace(1,1,ords)
    spr2s0 = np.linspace(1,1,ords)
    spr3s0 = np.linspace(1,1,ords)
    spr4s0 = np.linspace(1,1,ords)
    scl1s0 = np.linspace(1,1,ords)
    scl2s0 = np.linspace(1,1,ords)
    scl3s0 = np.linspace(1,1,ords)

    optProb.addVarGroup('ment', ordt, 'c', lower=None, upper=None, value=ment0)
    optProb.addVarGroup('sdv1t', ordt, 'c', lower=None, upper=None, value=sdv1t0)
    optProb.addVarGroup('sdv2t', ordt, 'c', lower=None, upper=None, value=sdv2t0)
    optProb.addVarGroup('sdv3t', ordt, 'c', lower=None, upper=None, value=sdv3t0)
    optProb.addVarGroup('sdv4t', ordt, 'c', lower=None, upper=None, value=sdv4t0)
    optProb.addVarGroup('ratt', ordt, 'c', lower=None, upper=None, value=ratt0)
    optProb.addVarGroup('tnst', ordt, 'c', lower=None, upper=None, value=tnst0)
    optProb.addVarGroup('spr1t', ordt, 'c', lower=None, upper=None, value=spr1t0)
    optProb.addVarGroup('spr2t', ordt, 'c', lower=None, upper=None, value=spr2t0)
    optProb.addVarGroup('spr3t', ordt, 'c', lower=None, upper=None, value=spr3t0)
    optProb.addVarGroup('spr4t', ordt, 'c', lower=None, upper=None, value=spr4t0)
    optProb.addVarGroup('scl1t', ordt, 'c', lower=None, upper=None, value=scl1t0)
    optProb.addVarGroup('scl2t', ordt, 'c', lower=None, upper=None, value=scl2t0)
    optProb.addVarGroup('scl3t', ordt, 'c', lower=None, upper=None, value=scl3t0)

    optProb.addVarGroup('mens', ords, 'c', lower=None, upper=None, value=mens0)
    optProb.addVarGroup('sdv1s', ords, 'c', lower=None, upper=None, value=sdv1s0)
    optProb.addVarGroup('sdv2s', ords, 'c', lower=None, upper=None, value=sdv2s0)
    optProb.addVarGroup('sdv3s', ords, 'c', lower=None, upper=None, value=sdv3s0)
    optProb.addVarGroup('sdv4s', ords, 'c', lower=None, upper=None, value=sdv4s0)
    optProb.addVarGroup('rats', ords, 'c', lower=None, upper=None, value=rats0)
    optProb.addVarGroup('tnss', ords, 'c', lower=None, upper=None, value=tnss0)
    optProb.addVarGroup('spr1s', ords, 'c', lower=None, upper=None, value=spr1s0)
    optProb.addVarGroup('spr2s', ords, 'c', lower=None, upper=None, value=spr2s0)
    optProb.addVarGroup('spr3s', ords, 'c', lower=None, upper=None, value=spr3s0)
    optProb.addVarGroup('spr4s', ords, 'c', lower=None, upper=None, value=spr4s0)
    optProb.addVarGroup('scl1s', ords, 'c', lower=None, upper=None, value=scl1s0)
    optProb.addVarGroup('scl2s', ords, 'c', lower=None, upper=None, value=scl2s0)
    optProb.addVarGroup('scl3s', ords, 'c', lower=None, upper=None, value=scl3s0)


    opt = SNOPT()
    opt.setOption('Scale option',0)
    if comp == 'mac':
        opt.setOption('Print file','/Users/ning1/Documents/FLOW Lab/VAWTWakeModel/wake_model/data/OptSheet/SNOPT_print.out')
        opt.setOption('Summary file','/Users/ning1/Documents/FLOW Lab/VAWTWakeModel/wake_model/data/OptSheet/SNOPT_summary.out')
    elif comp == 'fsl':
        opt.setOption('Print file','/fslhome/ebtingey/compute/VAWTWakeModel/SNOPT_OptSheet_print.out')
        opt.setOption('Summary file','/fslhome/ebtingey/compute/VAWTWakeModel/SNOPT_OptSheet_summary.out')
    res = opt(optProb, sens=None)
    if opt_print == True:
        print res

    error = res.fStar

    mentf = res.xStar['ment']
    sdv1tf = res.xStar['sdv1t']
    sdv2tf = res.xStar['sdv2t']
    sdv3tf = res.xStar['sdv3t']
    sdv4tf = res.xStar['sdv4t']
    rattf = res.xStar['ratt']
    tnstf = res.xStar['tnst']
    spr1tf = res.xStar['spr1t']
    spr2tf = res.xStar['spr2t']
    spr3tf = res.xStar['spr3t']
    spr4tf = res.xStar['spr4t']
    scl1tf = res.xStar['scl1t']
    scl2tf = res.xStar['scl2t']
    scl3tf = res.xStar['scl3t']

    mensf = res.xStar['mens']
    sdv1sf = res.xStar['sdv1s']
    sdv2sf = res.xStar['sdv2s']
    sdv3sf = res.xStar['sdv3s']
    sdv4sf = res.xStar['sdv4s']
    ratsf = res.xStar['rats']
    tnssf = res.xStar['tnss']
    spr1sf = res.xStar['spr1s']
    spr2sf = res.xStar['spr2s']
    spr3sf = res.xStar['spr3s']
    spr4sf = res.xStar['spr4s']
    scl1sf = res.xStar['scl1s']
    scl2sf = res.xStar['scl2s']
    scl3sf = res.xStar['scl3s']

    print '\n'
    print 'Total Error:',error,'\n'

    print 'ment = np.array(',mentf.tolist(),')'
    print 'sdv1t = np.array(',sdv1tf.tolist(),')'
    print 'sdv2t = np.array(',sdv2tf.tolist(),')'
    print 'sdv3t = np.array(',sdv3tf.tolist(),')'
    print 'sdv4t = np.array(',sdv4tf.tolist(),')'
    print 'ratt = np.array(',rattf.tolist(),')'
    print 'tnst = np.array(',tnstf.tolist(),')'
    print 'spr1t = np.array(',spr1tf.tolist(),')'
    print 'spr2t = np.array(',spr2tf.tolist(),')'
    print 'spr3t = np.array(',spr3tf.tolist(),')'
    print 'spr4t = np.array(',spr4tf.tolist(),')'
    print 'scl1t = np.array(',scl1tf.tolist(),')'
    print 'scl2t = np.array(',scl2tf.tolist(),')'
    print 'scl3t = np.array(',scl3tf.tolist(),')'

    print 'mens = np.array(',mensf.tolist(),')'
    print 'sdv1s = np.array(',sdv1sf.tolist(),')'
    print 'sdv2s = np.array(',sdv2sf.tolist(),')'
    print 'sdv3s = np.array(',sdv3sf.tolist(),')'
    print 'sdv4s = np.array(',sdv4sf.tolist(),')'
    print 'rats = np.array(',ratsf.tolist(),')'
    print 'tnss = np.array(',tnssf.tolist(),')'
    print 'spr1s = np.array(',spr1sf.tolist(),')'
    print 'spr2s = np.array(',spr2sf.tolist(),')'
    print 'spr3s = np.array(',spr3sf.tolist(),')'
    print 'spr4s = np.array(',spr4sf.tolist(),')'
    print 'scl1s = np.array(',scl1sf.tolist(),')'
    print 'scl2s = np.array(',scl2sf.tolist(),')'
    print 'scl3s = np.array(',scl3sf.tolist(),')'





# from operator import ge
import numpy as np

class Codage:
    def __init__(self, Ts, vect, amp):
        
        self.Ts, self.vect, self.amp = Ts, vect, amp
        global TsData, ampData, vectData
        TsData, ampData, vectData  = self.Ts, self.amp, self.vect
        # self.div = div

    def CLK(self):
        vect, a = [], 1
        for _ in enumerate(self.vect):
            for _ in range(int(self.Ts/2)):
                vect.append(1)
            for _ in range(int(self.Ts/2)):
                vect.append(-1)
        return vect

    def normal_coder(self):
        vect1 = []
        for _, n in enumerate(self.vect):
            for _ in range(self.Ts):
                vect1.append(n)
        return vect1

    def RZ(self):
        vect1 = []
        for _, n in enumerate(self.vect):
            for _ in range(int(self.Ts/2)):
                vect1.append(n)
            for _ in range(int(self.Ts/2)):
                vect1.append(0)
        return vect1

    def manchester(self):
        vect1 = []
        for _, n in enumerate(self.vect):
            if n :
                for _ in range(int(self.Ts/2)):
                    vect1.append(n)
                for _ in range(int(self.Ts/2)):
                    vect1.append(-1)
            else:
                for _ in range(int(self.Ts/2)):
                    vect1.append(-1)
                for _ in range(int(self.Ts/2)):
                    vect1.append(1)
        return vect1

    def miller(self):
        vect1 = []
        vect1.append(1 if self.vect[0] else -1)
        for i, _ in enumerate(self.vect):
            if self.vect[i-1]:
                if self.vect[i]:
                    for i in range(int(self.Ts/2)):
                        vect1.append(vect1[-1])
                    vect1.append(-vect1[-1])
                    for i in range(int(self.Ts/2-1)):
                        vect1.append(vect1[-1])
                else:
                    for i in range(self.Ts):
                        vect1.append(vect1[-1])
            else:
                if self.vect[i]:
                    for i in range(int(self.Ts/2)):
                        vect1.append(vect1[-1])
                    vect1.append(-vect1[-1])
                    for i in range(int(self.Ts/2-1)):
                        vect1.append(vect1[-1])
                else:
                    vect1.append(-vect1[-1])
                    for i in range(int(self.Ts-1)):
                        vect1.append(vect1[-1])
        return vect1[0:-1]

    def bipolaire(self):
        a, vect1 = 0, []
        for i, n in enumerate(self.vect):
            if self.vect[i]:
                for i in range(self.Ts):
                    vect1.append(-1 if a else 1) 
                a = not a
            else:
                for i in range(self.Ts):
                    vect1.append(0)
        return vect1

    def HDBn(self, n):
        vect1, a, t, b = self.bipolaire(), 1, 0, 1
        for i, nom in enumerate(self.vect):
            if self.vect[i]==0 and not t==n+1:
                t+=1
            if t==n+1:
                for j in range(self.Ts):
                    vect1[i*self.Ts+j] = 1 if a else -1
                    if vect1[i+1*self.Ts]==0:
                        vect1[(i+n)*self.Ts+j] = 1 if b else -1
                    if vect1[(i+n+1)*self.Ts] == 1:
                        vect1[i*self.Ts+j] = -1 if a else 1
                t = 0
                a, b = not a, not b
            if self.vect[i]:
                t = 0
        return vect1

    def NRZ(self):
        vect1 = self.normal_coder()
        vect1 = [ (1 if vect1[i] else -1) for i, _ in enumerate(vect1)] 
        return vect1

    def DSP_NRZ(self, f):
        return self.amp**2 * self.Ts *0.001 * np.sinc(np.pi * f * self.Ts *0.001)**2
    
    def DSP_RZ(self, f):
        return self.amp**2 * self.Ts *0.001/4 * np.sinc(np.pi * f * self.Ts *0.001/2)**2
    
    def DSP_bipolaire(self, f):
        return np.abs(self.amp**2 * self.Ts * 0.05 * np.sinc(np.pi * f * self.Ts)**2 * np.sin(np.pi * f * self.Ts/2))
    
    def DSP_manchester(self, f):
        return np.abs(self.amp**2 * self.Ts * 0.66 * 0.01 * np.sinc(np.pi * f * self.Ts*0.001/2)**2 * np.sin(np.pi * f * self.Ts*0.001/2)**2 )
        
    def DSP_HDBN(self, f):
        return np.abs(2/3*self.amp**2 * self.Ts * 0.01 * np.sinc(np.pi * f * self.Ts*0.001)**2 )

    def DSP_miller(self, f):
        return self.amp**2 * self.Ts * 10000/4 * 1/(2*(np.pi*f*self.Ts)**2*(17+8*np.cos(2*np.pi*f*self.Ts*0.001)))\
            *(23-2*np.cos(np.pi*f*self.Ts*0.001)-22*np.cos(2*np.pi*f*self.Ts*0.001)-12*np.cos(3*np.pi*f*self.Ts*0.001)+5*np.cos(4*np.pi*f*self.Ts*0.001)\
                +12*np.cos(5*np.pi*f*self.Ts*0.001)+2*np.cos(6*np.pi*f*self.Ts*0.001)-8*np.cos(7*np.pi*f*self.Ts*0.001)+2*np.cos(8*np.pi*f*self.Ts*0.001))

    def DSP_RZ_theo(self, div=1):
        f, vect = [], []
        Ts = self.Ts / 10**(3)
        for j in np.arange(-10/Ts, 10/Ts, 1/Ts):
            for i in np.arange(0, 1/Ts, Ts/div):
                f.append(j+i)
        k = [ 0 if i%2 else i/Ts for i in range(-10, 10)]
        j=-4

        for i, _ in enumerate(f):
            if f[i]==j/Ts:
                vect.append(self.amp**2 * Ts / 4 * np.sinc(np.pi * Ts * f[i] /2)**2 + self.amp**2 / 4 * k[i] * np.sinc(np.pi * f[i] * Ts/2)**2)
                j+=1
            else:
                vect.append(self.amp**2 * Ts / 4 * np.sinc(np.pi * Ts * f[i] /2)**2)
        return vect

    def diagramOeil(self, Ts):
        pass

    def HDBN(self,HDB):                
        # Ts=self.Ts
        x=self.vect
        y=[]
        suite_zero=0     #pour compter le nb de bit 0
        v=1              # pour respectant la loi d'alternance(bits de viol)
        # b=1              # pour respectant la loi d'alternance(bits de borage)
        a=0
        etat_debut=0

        for i in range(0,len(x)):
            if abs(x[i]):
                y.append( (-1)**a )
                a+=1
                etat_1 = x[i] #"pour premier bit de viol "
            else:
                y.append(0)

        for i in range(0,len(x)):
            if abs(y[i]):
                suite_zero=0
            else:
                suite_zero+=1
                if(suite_zero==HDB+1):
                    etat_debut+=1
                    # cette bloc execite un seul fois *
                    if(etat_debut==1):
                        y[i]=etat_1
                        v = etat_1
                        if(v<0):
                            a=0
                        else:
                            a=1
                    #************
                    else:
                        y[i]= v*(-1)**a
                        a+=1
                        #BORAGE *********
                    j=i
                    while(True):
                        if( abs(y[j-HDB+1]) ):

                            if( y[i] == y[j-HDB+1] ):
                                break
                            else:
                                y[i-HDB] = y[i] 
                                break
                            
                        j=j-1        
                        #BORAGE *********
                    suite_zero=0
                else:
                    continue 
        c = Codage(self.Ts, y, 1)
        y = c.normal_coder()        
        return y   


class Filtre_emi:

    global TsData, ampData, vectData

    def __init__(self) -> None:
        pass

    def filtre_blanch(self, vect):
        vect1, a = [], 0
        for _, n in enumerate(vect):
            if a == TsData or a == 0:
                vect1.append(n)
                a = 1
            else:
                vect1.append(0)
                a += 1
        return vect1

    def filre_ideal_alpha(self, vect1, alpha, t, coef):
        f = lambda c, alpha, t, Ts, n, k : c * np.sinc(np.pi*(t-Ts*n)/(Ts*k)) * np.cos(np.pi*alpha*(t-Ts*n)/(Ts*k)) / (1-(2*alpha*(t-Ts*n)/(Ts*k))**2)
        a, i, vect0, vect = 1, 0, [ 0 for _ in enumerate(vect1)], []
        for i, n in enumerate(vect1):
            
            if abs(n):
                vect2 = f(n, alpha, t, TsData, int(i/(TsData)), coef)
                if a:
                    vect = np.array(vect2)
                    a=0
                else: 
                    vect = np.array(vect) + np.array(vect2)
                    # break
        return vect

    def DSP_FE(self, f, Ts, alpha=0.5):
        # dsp = (1-np.sin(np.pi/(2*alpha)*np.abs(f)*Ts-1))
        dsp = np.zeros(int(4/Ts*10000))
        if alpha == 0:
            dsp[int(1/Ts*10000):int(3/Ts*10000)] = 1
        elif alpha == 0.5:
            # dsp[int(1/Ts*10000):int(3/Ts*10000)] = (1-np.sin(np.pi/(2*alpha)*np.abs(f[int(1/Ts*10000):int(3/Ts*10000)])*Ts-1.5))
            dsp = np.cos(f*0.4)**2
            dsp[int(1.2/Ts*10000):int(2.8/Ts*10000)] = 1
            dsp[0:int(0.83/Ts*10000)] = 0
            dsp[int((4-0.83)/Ts*10000):int(4/Ts*10000)] = 0
        else:
            # dsp[int(1/Ts*10000):int(3/Ts*10000)] = (1-np.sin(np.pi/(2*alpha)*np.abs(f[int(1/Ts*10000):int(3/Ts*10000)])*Ts-1.5))
            dsp = np.cos(f*0.2+4.7)**2
            dsp[int(1.2/Ts*10000):int(2.8/Ts*10000)] = 1
            dsp[0:int(0.45/Ts*10000)] = 0
            dsp[int((4-0.45)/Ts*10000):int(4/Ts*10000)] = 0
        return dsp

    def filtre_r(self, vect):
        return vect + Modulation.noise(len(vect), 0.02)


class Modulation:

    global TsData, ampData, vectData

    def __init__(self):
        pass

    def ASK(self, f0, vect, t):
        amp = 1
        f = lambda f0, vect, amp, i : amp * (vect * np.cos(2 * np.pi * f0 * i)) 
        return np.array([ f(f0, n, amp, t[i]) for i, n in enumerate(vect) ])

    def DSP_mod(self, f0, t, Ts):
        f = lambda c, alpha, t, Ts, n, k : c * np.sinc(np.pi*5*(t-Ts*n)/(Ts*k)) 
        return f(1, 0.5, t, TsData, f0/(TsData), 2)

    def __DEMUX(self, vect, amp):
        I, Q, a, k, Ts = [], [], 1, 0, TsData
        while True:
            if a:
                I.append(vect[k])
                k += 1
                a = 0
                if k == len(vect):
                    break
            else:
                Q.append(vect[k])   
                k += 1
                a = 1
                if k == len(vect):
                    break
        print(I, 'aczda', Q)
        # code = Codage(2*Ts, I, amp)
        # I = code.normal_coder()
        # code = Codage(2*Ts, Q, amp)
        # Q = code.normal_coder()
        # print(I, 'aczda', Q)

        return I, Q

    def PSK(self, f0, vect, t):
        f = lambda f0, i : np.cos(2 * np.pi * f0 * i)
        # f1 = lambda f0, i : np.cos(2 * np.pi * f0 * i + np.pi / 2)
        # I = np.array([ n for i, n in enumerate(vectI)])# * f(f0, t))
        Q = np.array([ n for _, n in enumerate(vect)] * f(f0, t))
        return Q

    def FSK(self, f0, deltaF, vect, t):
        f = lambda a, m, t : a * np.cos(t * np.pi * f0)
        # return [ f(ampData, n, i) for i, n in enumerate(vect)]
        return np.cos(2 * np.pi * f0 * t/TsData + deltaF * t/TsData * np.pi * np.array(vect))


    def noise(num_samples, var):
        return np.random.normal(0, var, size=num_samples)

    def noise_noise(self, vect, num_samples, var):
        return np.array(vect) + np.random.normal(0, var, size=num_samples)

    def demodulation(self, vect):
        return vect + Modulation.noise(len(vect), 0.2)

    def decision(self, vect, ts, seuil):
        j, v = 0, []
        for i, n in enumerate(vect):
            if i == 0 or i == j*ts:
                j += 1
                for _ in range(ts):
                    if n > seuil :
                        v.append(1)
                    else :
                        v.append(0)
        return v

    # def decision(self, vect, ts, seuil):
    #     j, v = 0, []
    #     for i, n in enumerate(vect):
    #         if i == j*ts:
                
    #             if np.mean(vect[j*ts:(j+1)*ts])>seuil:
    #                 for _ in range(ts):
    #                     v.append(1)
    #             else:
    #                 for _ in range(ts):
    #                     v.append(0)
    #             j += 1







































'''
This program is intended to generate teeth combinations for
differential planetary gearboxes with sun1 as input, ring1 fixed and 
ring2 as output. For more information visit:
https://juanggengineering.blogspot.ca/2018/02/split-ring-compound-epicyclicplanetary.html
It just tries a bunch of possible combiantions and prints the closest
ones within the parameters and restrictions specified.
Use it at your own risk.

Equations that rule this gearbox:

 gr = 1/((1-(zr1*zp2)/(zr2*zp1))/(1+(zr1/zs1)))
 zr = zs+2*zp
 zp2 = zp1*k
 m1*(zp1+zs1) = m2*(zp2+zs2)
 (zs+zr)%np = 0
 zr2 = zr1*k+np

'''

#Welcome and instructions:
print('''************************************************
*   Differential planetary gearbox calculator   *
*      By Juan Gg                              *
************************************************''')
#Input parameters:
while True:
    try:
        print('>>> Enter parameters:')
        od = float(input(' Outside diameter: '))
        mtr = float(input(' Min target ratio: '))
        Mtr = float(input(' Max target ratio: '))
        mt = int(input(' Min number of teeth: '))
        mm = float(input(' Min teeth module: '))
        mp = int(input(' Min number of planets: '))
        Mp = int(input(' Max number of planets: '))
        if mp > Mp:     #Min number of planets can not be bigger than max number.
            print('  Wrong input!   Try again')
            continue
        if input(' Proceed to calculation? (yes/no): ') == 'yes':
            print('')
            print(' Please wait, it may take several minutes...')
    
#Perform the calculation by trying all posible combinations and showing the "right" ones:
            r = 0
            for np in range(mp,Mp+1):
                k = 0
                while k<= 100:
                    for zs1m in range(0,200):
                        for zr1m in range(zs1m,200):
                            zs1 = np*zs1m
                            zr1 = np*zr1m
                            zp1 = (zr1-zs1)/2
                            zr2 = zr1*k+np
                            zp2 = zp1*k
                            zs2 = zr2-2*zp2
                            m1 = round(od/(zr1+2),6)
                            m2 = round((m1*(zp1+zs1))/(zp2+zs2),6)
                            #Verify that the restrictions apply and that all teeth numbers are integrers.
                            if zr1>=mt and zp1>=mt and zs1>=mt and zr2>=mt and zp2>=mt and zs2>=mt and m1>=mm and m2>=mm and abs(round(zr1)-zr1)<0.01 and abs(round(zp1)-zp1)<0.01 and abs(round(zs1)-zs1)<0.01 and abs(round(zr2)-zr2)<0.01 and abs(round(zp2)-zp2)<0.01 and abs(round(zs2)-zs2)<0.01:
                                #Rounding is to compensate errors in operations. Only rounds numbers closer than 0.01 to the nearest integrer
                                zr1 = round(zr1)
                                zp1 = round(zp1)
                                zs1 = round(zs1)
                                zr2 = round(zr2)
                                zp2 = round(zp2)
                                zs2 = round(zs2)
                                gr = round(1/((1-(zr1*zp2)/(zr2*zp1))/(1+(zr1/zs1))),6)
                                #Calculate final gear ratio and verify that is between min and max specified
                                if mtr<=gr<=Mtr:
                                    r = r+1
                                    #Print the result
                                    print('')
                                    print('')
                                    print(' Result__________________'+str(r))
                                    print('')
                                    print('  GR :  '+str(gr))
                                    print('  np :  '+str(np))
                                    print('  zr1:  '+str(zr1))
                                    print('  zp1:  '+str(zp1))
                                    print('  zs1:  '+str(zs1))
                                    print('  m1 :  '+str(m1))
                                    print('  zr2:  '+str(zr2))
                                    print('  zp2:  '+str(zp2))
                                    print('  zs2:  '+str(zs2))
                                    print('  m2 :  '+str(m2))
                                    print('')
                                    print('')
                    k = k+0.1
            if input('Calculation finished. Do you want to try again?(yes/no)')!='yes':
                print('Good bye!')
                break
            else:
                continue
    except:
        print('  Wrong input!   Try again')

def invertir_numero(n):
    rut = 0
    while n != 0:
        rut = 10*rut+n % 10
        n //= 10
    return rut
total=0
def valores(invertido):
    n1= str(invertido)[0]
    n1= int(n1)*2
    n2= str(invertido)[1]
    n2= int(n2)*3
    n3= str(invertido)[2]
    n3= int(n3)*4
    n4= str(invertido)[3]
    n4= int(n4)*5
    n5= str(invertido)[4]
    n5= int(n5)*6
    n6= str(invertido)[5]
    n6= int(n6)*7
    n7= str(invertido)[6]
    n7= int(n7)*2
    n8= str(invertido)[7]
    n8= int(n8)*3
    return n1+n2+n3+n4+n5+n6+n7+n8
def calculo_dv(total):
    dv= total/11
    dv= int(dv)
    dv*=11
    dv-= total
    dv-=11
    dv = abs(dv)
    return dv
def dv_final(dv):
    if dv == 10:
        dv = 'K'
    elif dv == 11:
        dv = 0
    return dv

menu = True

while menu == True:
    print('Ingrese su rut, sin digito verificador')
    rut = int(input('>>'))
    invertido = invertir_numero(rut)

    total = valores(invertido)
    dv = calculo_dv(total)
    dv = dv_final(dv)
   
    print(f"Su Digito verificador es de {dv}")
    print(f"Su rut es: {rut}-{dv}")


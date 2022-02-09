def aumento(sueldo):
    return sueldo+200

def bonificacion(sueldo):
    return sueldo*0.1

def SueldoTotal(aum,boni):
    return aum+boni

def Mostrar(aum,boni,total):
    m="Sueldo + 200 --> S/."+str(aum)
    #m=m+"\nBonificacion --> S/."+str(round(boni,2))----recomendable usar el round
    m=m+"\nBonificacion --> S/."+str('{0:.2f}'.format(boni))
    m=m+"\n-----------------------------------"
    m=m+"\nSueldo Total --> S/."+str(total)
    return m
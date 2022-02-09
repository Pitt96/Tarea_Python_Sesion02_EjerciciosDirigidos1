def sueldoBasico(horas,pagoXhora):
    sueldo=horas*pagoXhora
    return sueldo

def sueldoExtra(horasE,pagoXhora):
    sueldo=horasE*(pagoXhora+pagoXhora*0.15)
    return sueldo

def descuento(sueldoB):
    return sueldoB*0.13

def sueldoNeto(sueldoB,sueldoE,descuento):
    return sueldoB+sueldoE-descuento

def mostrar(sueldoB,sueldoE,descuento,sueldoN):
    m=  "Sueldo Basico                :              S/."+str(sueldoB)
    m=m+"\nSueldo Extra               :              S/."+str(sueldoE)
    m=m+"\nDescuento                  :              S/."+str(descuento)
    m=m+"\n***********************************************************"
    m=m+"\nSueldo Neto                :              S/."+str(sueldoN)
    return m
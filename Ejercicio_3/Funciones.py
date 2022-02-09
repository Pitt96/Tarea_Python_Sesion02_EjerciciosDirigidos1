def promedio(n1,n2,n3,n4,n5,n6):
    return ((n1+n2+n3+n4+n5+n6)/6)

def Mostrar(curso,n1,n2,n3,n4,n5,n6,prom):
    m="****************CURSO --> "+curso+"****************"
    m=m+"\nNota 1\tNota 2\tNota 3\tNota 4\tNota 5\tNota 6\n"
    m=m+str(n1)+"\t    "+str(n2)+"\t    "+str(n3)+"\t    "+str(n4)+"\t    "+str(n5)+"\t    "+str(n6)
    m=m+"\n************************************************"
    m=m+"\nPromedio --> "+str(round(prom,2))
    return m
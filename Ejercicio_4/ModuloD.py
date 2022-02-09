
def PagoPorCuotas (precio_producto,cantidad_cuotas,interes):

    pago_cuotas=(precio_producto/cantidad_cuotas)+((interes/100)*precio_producto)
    return pago_cuotas



def PagoNeto(pago_cuotas,cantidad_cuotas):
    pago_neto= pago_cuotas*cantidad_cuotas
    return pago_neto


def Diferencia(pago_neto,precio_producto):
    dif=pago_neto-precio_producto
    return dif

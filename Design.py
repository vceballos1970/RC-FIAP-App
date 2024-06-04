from math import floor, sqrt, pi

from Units import Units as U

def AvColumn(EleTag, Vu, b, h, nbH, nbB, dst, Ast=None, Nu_min=None, db=None, fys=None, Vc=None, Vc1=None, fcC=None, cover=None, MPa=None):
    fiv = 0.75
    Ag = b * h
    if Ast is None:
        Ast = pi * dst ** 2 / 4  # Calculo del área de acero transversal (si no se provee)
    
    dp = cover + dst + db / 2
    d = h - dp
    dbc = b - dp if 'dbc' in locals() else None  # Solo usado en la primera versión

    neH = floor(nbH / 2) + 1
    neB = floor(nbB / 2) + 1
    Ash_H = neH * Ast
    Ash_B = neB * Ast
    
    # Determinar Vc según se provea o no
    if Vc is None:
        Vc = min((0.17 * sqrt(fcC * U.MPa) + min(Nu_min / 6 / Ag, 0.05 * fcC)) * b * d, 0.42 * sqrt(fcC * U.MPa) * b * d)
    
    Vs = (Vu - fiv * Vc) / fiv

    # Determinar el espaciamiento según las condiciones de corte
    if Vs > 4. * Vc:
        print("reshape by shear in Column " + str(EleTag))
    elif 2. * Vc < Vs <= 4. * Vc:
        se_1 = min(h / 4, b / 2)
    elif Vs <= 2. * Vc:
        se_1 = min(h / 2, b / 2)
    else:
        se_1 = min(8. * db, b / 2., h / 2., 200. * U.mm)  # Espaciamiento mínimo
    
    Ave = Ash_B  # Área transversal del estribo
    if Vs <= 0.:
        se = se_1
        sem = min(2 * se_1, b / 2)
    else:
        se_2 = Ave * fys * d / Vs
        se = min(se_1, se_2)
        sem = min(se_2, b / 2)

    if se < 60. * U.mm:
        print('Minimum spacing of stirrups is not met in column ' + str(EleTag))

    Vn = Vc + Ave * fys * d / se
    return se, neB, neH, Vn, dst, sem if 'sem' in locals() else None

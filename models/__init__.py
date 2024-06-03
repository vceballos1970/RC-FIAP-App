class AcceptanceCriteria:
    def __init__(self, IO_1, LS_1, CP_1, IO_2, LS_2, CP_2):
        self.IO_1 = IO_1
        self.LS_1 = LS_1
        self.CP_1 = CP_1
        self.IO_2 = IO_2
        self.LS_2 = LS_2
        self.CP_2 = CP_2


class PlasticHingeLength:
    def __init__(self, phl1, phl2):
        self.phl1 = phl1
        self.phl2 = phl2


class WallDesign:
    def __init__(self, EleTag, b, h, nbH, nbB, db, dst, As, Pu_v, Mu_v, fiPn, fiMn, Mn_i, d, dist, ro_t, ro_l, Mu_i,
                 sst, Nod_ini, Nod_end, NUD1, NUD2, NUG1, NUG2, MUD1, MUD2, VUD1, VUD2, Vn, cMaxS, sigma_c, BE, lbe,
                 nsH_BE, nsB_BE, se_BE):
        self.EleTag = EleTag
        self.b = b
        self.h = h
        self.nbH = nbH
        self.nbB = nbB
        self.db = db
        self.dst = dst
        self.As = As
        self.Pu_v = Pu_v
        self.Mu_v = Mu_v
        self.fiPn = fiPn
        self.fiMn = fiMn
        self.Mn_i = Mn_i
        self.d = d
        self.dist = dist
        self.ro_t = ro_t
        self.ro_l = ro_l
        self.Mu_i = Mu_i
        self.sst = sst
        self.Nod_ini = Nod_ini
        self.Nod_end = Nod_end
        self.NUD1 = NUD1
        self.NUD2 = NUD2
        self.NUG1 = NUG1
        self.NUG2 = NUG2
        self.MUD1 = MUD1
        self.MUD2 = MUD2
        self.VUD1 = VUD1
        self.VUD2 = VUD2
        self.Vn = Vn
        self.cMaxS = cMaxS
        self.sigma_c = sigma_c
        self.BE = BE
        self.lbe = lbe
        self.nsH_BE = nsH_BE
        self.nsB_BE = nsB_BE
        self.se_BE = se_BE


class ColDesign:
    def __init__(self, EleTag, b, h, nbH, nbB, db, de, As, Pu_v, Mu_v, fiPn, fiMn, Mn_i, d, dist, ro, Mu_i,
                 sst, nsB, nsH, Nod_ini, Nod_end, NUD1, NUD2, NUG1, NUG2, MUD1, MUD2, VUD1, VUD2, ColBeamStr, Vn, VI6,
                 Vu_Vn, VnCol, sem, sigma_IF, wIF):
        self.EleTag = EleTag
        self.b = b
        self.h = h
        self.nbH = nbH
        self.nbB = nbB
        self.db = db
        self.de = de
        self.As = As
        self.Pu_v = Pu_v
        self.Mu_v = Mu_v
        self.fiPn = fiPn
        self.fiMn = fiMn
        self.Mn_i = Mn_i
        self.d = d
        self.dist = dist
        self.ro = ro
        self.Mu_i = Mu_i
        self.sst = sst
        self.nsB = nsB
        self.nsH = nsH
        self.Nod_ini = Nod_ini
        self.Nod_end = Nod_end
        self.NUD1 = NUD1
        self.NUD2 = NUD2
        self.NUG1 = NUG1
        self.NUG2 = NUG2
        self.MUD1 = MUD1
        self.MUD2 = MUD2
        self.VUD1 = VUD1
        self.VUD2 = VUD2
        self.ColBeamStr = ColBeamStr
        self.Vn = Vn
        self.Vy = VI6
        self.Vu_Vn = Vu_Vn
        self.VnCol = VnCol
        self.sem = sem
        self.sigma_IF = sigma_IF
        self.wIF = wIF


class BeamDesign:
    def __init__(self, EleTag, b, h, Ast1, dt1, Mn_n1, Asb1, db1, Mn_p1, ns1, ss1, Ast2, dt2, Mn_n2, Asb2, db2, Mn_p2,
                 ns2, ss2, Nod_ini, Nod_end, db_t1, db_b1, db_t2, db_b2, Vpr, VU1, VU2, Mpr_n1, Mpr_p1, Mpr_n2, Mpr_p2,
                 Vun):
        self.EleTag = EleTag
        self.b = b
        self.h = h
        self.Ast1 = Ast1
        self.dt1 = dt1
        self.Mn_n1 = Mn_n1
        self.Asb1 = Asb1
        self.db1 = db1
        self.Mn_p1 = Mn_p1
        self.ns1 = ns1
        self.ss1 = ss1
        self.Ast2 = Ast2
        self.dt2 = dt2
        self.Mn_n2 = Mn_n2
        self.Asb2 = Asb2
        self.db2 = db2
        self.Mn_p2 = Mn_p2
        self.ns2 = ns2
        self.ss2 = ss2
        self.Nod_ini = Nod_ini
        self.Nod_end = Nod_end
        self.db_t1 = db_t1
        self.db_b1 = db_b1
        self.db_t2 = db_t2
        self.db_b2 = db_b2
        self.Vpr = Vpr
        self.VU1 = VU1
        self.VU2 = VU2
        self.Mpr_n1 = Mpr_n1
        self.Mpr_p1 = Mpr_p1
        self.Mpr_n2 = Mpr_n2
        self.Mpr_p2 = Mpr_p2
        self.Vun = Vun

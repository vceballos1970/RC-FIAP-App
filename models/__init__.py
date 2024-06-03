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

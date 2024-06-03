from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5 import QtCore


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


class ZeroLengthElement:
    def __init__(self, EleTag, Nod_ini, Nod_end):
        self.EleTag = EleTag
        self.Nod_ini = Nod_ini
        self.Nod_end = Nod_end


class BeamElasticElement:
    def __init__(self, EleTag, Nod_ini, Nod_end, AEle, EcEle, IzEle, LEle, BEle, HEle, ElegTr, RZi, RZe):
        self.EleTag = EleTag
        self.Nod_ini = Nod_ini
        self.Nod_end = Nod_end
        self.AEle = AEle
        self.EcEle = EcEle
        self.IzEle = IzEle
        self.LEle = LEle
        self.BEle = BEle
        self.HEle = HEle
        self.ElegTr = ElegTr
        self.RZi = RZi
        self.RZe = RZe


class RegistroWalls:
    def __init__(self, tbl_data_design_walls, id_, tw, lw, ro_l, ro_t, db, de, Sst, cMaxS, sigma_c, BE):
        fila = tbl_data_design_walls.rowCount()
        tbl_data_design_walls.insertRow(fila)

        self.spx_id = QLineEdit(tbl_data_design_walls)
        self.spx_id.setValidator(QIntValidator(0, 1000))
        self.spx_id.setText(f'W{id_}')

        self.spx_b = QLineEdit(tbl_data_design_walls)
        self.spx_b.setValidator(QIntValidator(15, 1000))
        self.spx_b.setText('{:d}'.format(int(tw)))

        self.spx_h = QLineEdit(tbl_data_design_walls)
        self.spx_h.setValidator(QIntValidator(20, 2000))
        self.spx_h.setText('{:d}'.format(int(lw)))

        self.spx_ro_l = QLineEdit(tbl_data_design_walls)
        self.spx_ro_l.setValidator(QDoubleValidator(0.1, 8., 3))
        self.spx_ro_l.setText('{:.2f}'.format(ro_l * 100))

        self.spx_ro_t = QLineEdit(tbl_data_design_walls)
        self.spx_ro_t.setValidator(QDoubleValidator(0.1, 8., 3))
        self.spx_ro_t.setText('{:.2f}'.format(ro_t * 100))

        self.spx_db = QLineEdit(tbl_data_design_walls)
        self.spx_db.setValidator(QDoubleValidator(1., 100., 2))
        self.spx_db.setText('{:.2f}'.format(db))

        self.spx_de = QLineEdit(tbl_data_design_walls)
        self.spx_de.setValidator(QDoubleValidator(1., 100., 2))
        self.spx_de.setText('{:.2f}'.format(de))

        self.spx_Sst = QLineEdit(tbl_data_design_walls)
        self.spx_Sst.setValidator(QIntValidator(2, 100))
        self.spx_Sst.setText('{:d}'.format(int(Sst)))

        self.spx_cMaxS = QLineEdit(tbl_data_design_walls)
        # self.spx_cMaxS.setValidator(QDoubleValidator(0.1, 100))
        self.spx_cMaxS.setAlignment(QtCore.Qt.AlignCenter)
        self.spx_cMaxS.setText('{:1.3f}'.format(cMaxS))

        self.spx_sigma_c = QLineEdit(tbl_data_design_walls)
        # self.spx_sigma_c.setValidator(QDoubleValidator(0.01, 100))
        # self.spx_sigma_c.setAlignment(Qt.AlignHCenter)
        self.spx_sigma_c.setAlignment(QtCore.Qt.AlignCenter)
        self.spx_sigma_c.setText('{:1.3f}'.format(sigma_c))

        self.spx_BE = QLineEdit(tbl_data_design_walls)
        # self.spx_id.setValidator(QIntValidator(0, 1000))
        self.spx_BE.setText(BE)

        tbl_data_design_walls.setCellWidget(fila, 0, self.spx_id)
        tbl_data_design_walls.setCellWidget(fila, 1, self.spx_b)
        tbl_data_design_walls.setCellWidget(fila, 2, self.spx_h)
        tbl_data_design_walls.setCellWidget(fila, 3, self.spx_ro_l)
        tbl_data_design_walls.setCellWidget(fila, 4, self.spx_ro_t)
        tbl_data_design_walls.setCellWidget(fila, 5, self.spx_db)
        tbl_data_design_walls.setCellWidget(fila, 6, self.spx_de)
        tbl_data_design_walls.setCellWidget(fila, 7, self.spx_cMaxS)
        tbl_data_design_walls.setCellWidget(fila, 8, self.spx_sigma_c)
        tbl_data_design_walls.setCellWidget(fila, 9, self.spx_BE)

        tbl_data_design_walls.setColumnWidth(0, 40)
        tbl_data_design_walls.setColumnWidth(1, 40)
        tbl_data_design_walls.setColumnWidth(2, 40)
        tbl_data_design_walls.setColumnWidth(3, 40)
        tbl_data_design_walls.setColumnWidth(4, 60)
        tbl_data_design_walls.setColumnWidth(5, 60)
        tbl_data_design_walls.setColumnWidth(6, 40)
        tbl_data_design_walls.setColumnWidth(7, 60)
        tbl_data_design_walls.setColumnWidth(8, 60)
        tbl_data_design_walls.setColumnWidth(9, 60)

        stylesheet = "::section{border-style: solid;" \
                     "border-width: 1px;}"
        tbl_data_design_walls.horizontalHeader().setStyleSheet(stylesheet)

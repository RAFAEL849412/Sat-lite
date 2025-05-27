class ECDH:
    def __init__(self):
        from sympy import mod_inverse
        self.mod_inverse = mod_inverse

        self.p = 606341371901192354470259703076328716992246317693812238045286463

        self.g = [160057538006753370699321703048317480466874572114764155861735009,
                  255466303302648575056527135374882065819706963269525464635673824]

        self.connecte = [
            [460868776123995205521652669050817772789692922946697572502806062,
             263320455545743566732526866838203345604600592515673506653173727],

            [270400597838364567126384881699673470955074338456296574231734133,
             526337866156590745463188427547342121612334530789375115287956485]
        ]

        self.dns = ["1.1.1.1", "1.0.0.1"]

    def point_add(self, P, Q):
        if P == Q:
            l = (3 * P[0] * P[0]) * self.mod_inverse(2 * P[1], self.p) % self.p
        else:
            l = (Q[1] - P[1]) * self.mod_inverse(Q[0] - P[0], self.p) % self.p
        x = (l * l - P[0] - Q[0]) % self.p
        y = (l * (P[0] - x) - P[1]) % self.p
        return [x, y]

    def scalar_mult(self, k, P):
        R = None
        for i in reversed(bin(k)[2:]):
            if R is not None:
                R = self.point_add(R, R)
            if i == '1':
                R = P if R is None else self.point_add(R, P)
        return R

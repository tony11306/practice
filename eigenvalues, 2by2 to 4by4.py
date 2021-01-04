import math

ans = []

def getSquareRoot(matrix=[], a=1, b=math.inf, c=math.inf):
    if b == math.inf and c == math.inf:
        b = -matrix[0] - matrix[3]
        c = -matrix[1]*matrix[2] + matrix[0]*matrix[3]
    det = b**2 - 4*a*c
    if det < 0:
        return
    else :
        x1 = (-b + math.sqrt(det)) / (2*a)
        x2 = (-b - math.sqrt(det)) / (2*a)
        ans.append(x1)
        ans.append(x2)
        print(x1, x2)

def getCubeRoot(matrix=[], a=-1, b=math.inf, c=math.inf, d=math.inf):
    if b == math.inf and c == math.inf and d == math.inf:
        b = matrix[0] + matrix[4] + matrix[8]
        c = matrix[1]*matrix[3] - matrix[0]*matrix[4] + matrix[2]*matrix[6] + matrix[5]*matrix[7] - matrix[0]*matrix[8] - matrix[4]*matrix[8]
        d = -matrix[2]*matrix[4]*matrix[6] + matrix[1]*matrix[5]*matrix[6]+matrix[2]*matrix[3]*matrix[7] - matrix[0]*matrix[5]*matrix[7] - matrix[1]*matrix[3]*matrix[8] + matrix[0]*matrix[4]*matrix[8]
    
    b /= a
    c /= a
    d /= a
    print(b, c, d)
    if(abs(d) < 0.00000000001):
        print(0, end=' ')
        ans.append(0.0)
        getSquareRoot(a=a, b=b, c=c)
        return
    q = (3*c - b**2) / 9
    r = -27*d + b*(9*c - 2*b**2)
    r /= 54
    delta = q**3 + r**2
    term = b/3
    if delta > 0:
        s = r + math.sqrt(delta)
        s = -math.pow(-s, 1/3) if s < 0 else math.pow(s, 1/3)
        t = r - math.sqrt(delta)
        t = -math.pow(-t, 1/3) if t < 0 else math.pow(t, 1/3)
        
        x1 = -term + s + t
        term += (s+t)/2
        x2 = -term
        x3 = x2
        term = math.sqrt(3)*(-t+s)/2
        if abs(term) < 0.0000001:
            ans.append(x2)
            ans.append(x3)
        ans.append(x1)
        print(x1)
        return
    elif abs(delta) < 0.0000000001:
        r13 = -math.pow(-r, 1/3) if r < 0 else math.pow(r, 1/3)
        x1 = -term + 2*r13
        x2 = -(r13 + term)
        x3 = x2
        print(x1, x2, x3)
        ans.append(x1)
        ans.append(x2)
        ans.append(x3)
        return
    q = -q
    dum = q**3
    dum = math.acos(r/math.sqrt(dum))
    r13 = 2*math.sqrt(q)
    x1 = (-term + r13*math.cos(dum / 3))
    x2 = (-term + r13*math.cos((dum + 2*math.pi)/3))
    x3 = (-term + r13*math.cos((dum + 4*math.pi)/3))
    ans.append(x1)
    ans.append(x2)
    ans.append(x3)
    print(x1, x2, x3)

def getQuad4Root(matrix=[], a=1, b=math.inf, c=math.inf, d=math.inf, e=math.inf):
    if b == math.inf and c == math.inf and d == math.inf and e == math.inf:
        b = -matrix[0] - matrix[5] - matrix[10] - matrix[15]
        c = - matrix[1] * matrix[4]+ matrix[0] * matrix[5]- matrix[2] * matrix[8]- matrix[6] * matrix[9]+ matrix[0] * matrix[10]+ matrix[5] * matrix[10]- matrix[3] * matrix[12]- matrix[7] * matrix[13]- matrix[11] * matrix[14]+ matrix[0] * matrix[15]+ matrix[5] * matrix[15]+ matrix[10] * matrix[15]
        d = matrix[2] * matrix[5] * matrix[8] - matrix[1] * matrix[6] * matrix[8] - matrix[2] * matrix[4] * matrix[9] + matrix[0] * matrix[6] * matrix[9] + matrix[1] * matrix[4] * matrix[10] - matrix[0] * matrix[5] * matrix[10] + matrix[3] * matrix[5] * matrix[12] - matrix[1] * matrix[7] * matrix[12] + matrix[3] * matrix[10] * matrix[12] - matrix[2] * matrix[11] * matrix[12] - matrix[3] * matrix[4] * matrix[13] + matrix[0] * matrix[7] * matrix[13] + matrix[7] * matrix[10] * matrix[13] - matrix[6] * matrix[11] * matrix[13] - matrix[3] * matrix[8] * matrix[14] - matrix[7] * matrix[9] * matrix[14] + matrix[0] * matrix[11] * matrix[14] + matrix[5] * matrix[11] * matrix[14] + matrix[1] * matrix[4] * matrix[15] - matrix[0] * matrix[5] * matrix[15] + matrix[2] * matrix[8] * matrix[15] + matrix[6] * matrix[9] * matrix[15] - matrix[0] * matrix[10] * matrix[15] - matrix[5] * matrix[10] * matrix[15]
        e = matrix[3] * matrix[6] * matrix[9] * matrix[12] - matrix[2] * matrix[7] * matrix[9] * matrix[12] - matrix[3] * matrix[5] * matrix[10] * matrix[12] + matrix[1] * matrix[7] * matrix[10] * matrix[12] + matrix[2] * matrix[5] * matrix[11] * matrix[12] - matrix[1] * matrix[6] * matrix[11] * matrix[12] - matrix[3] * matrix[6] * matrix[8] * matrix[13] + matrix[2] * matrix[7] * matrix[8] * matrix[13] + matrix[3] * matrix[4] * matrix[10] * matrix[13] - matrix[0] * matrix[7] * matrix[10] * matrix[13] - matrix[2] * matrix[4] * matrix[11] * matrix[13] + matrix[0] * matrix[6] * matrix[11] * matrix[13] + matrix[3] * matrix[5] * matrix[8] * matrix[14] - matrix[1] * matrix[7] * matrix[8] * matrix[14] - matrix[3] * matrix[4] * matrix[9] * matrix[14] + matrix[0] * matrix[7] * matrix[9] * matrix[14] + matrix[1] * matrix[4] * matrix[11] * matrix[14] - matrix[0] * matrix[5] * matrix[11] * matrix[14] - matrix[2] * matrix[5] * matrix[8] * matrix[15] + matrix[1] * matrix[6] * matrix[8] * matrix[15] + matrix[2] * matrix[4] * matrix[9] * matrix[15] - matrix[0] * matrix[6] * matrix[9] * matrix[15] - matrix[1] * matrix[4] * matrix[10] * matrix[15] + matrix[0] * matrix[5] * matrix[10] * matrix[15]

    if abs(e) < 0.00000000001:
        print(0.0, end=' ')
        ans.append(0.0)
        getCubeRoot(a=a,b=b,c=c,d=d)
        return
    
    b /= a
    c /= a
    d /= a
    e /= a
    print(a,b,c,d,e)
    cb = -c
    cc = -4*e + d*b
    cd = -(b*b*e + d*d) + 4*c*e
    q = (3*cc - (cb**2)) / 9
    r = -(27*cd) + cb*(9*cc - 2*(cb**2))
    r /= 54
    discrim = q**3 + r**2
    term = cb/3
    if discrim > 0:
        s = r + math.sqrt(discrim)
        s = -math.pow(-s, 1/3) if s < 0 else math.pow(s, 1/3)
        t = r - math.sqrt(discrim)
        t = -math.pow(-t, 1/3) if s < 0 else math.pow(t, 1/3)
        y1 = -term + s + t
    else:
        if(abs(discrim) < 0.000000001):
            r13 = -math.pow(-r, 1/3) if r < 0 else math.pow(r, 1/3)
            y1 = -term + 2*r13
        else:
            q = -q
            dum = q**3
            dum = math.acos(r/math.sqrt(dum))
            r13 = 2*math.sqrt(q)
            y1 = -term + r13*math.cos(dum/3)
    
    term = b/4
    sqr = -c + term*b + y1
    rre = 0
    rim = 0
    dre = 0
    dim = 0
    ere = 0
    eim = 0
    z1re = 0
    z1im = 0
    z2re = 0
    if sqr >= 0:
        if abs(sqr) < 0.000000000001:
            dum = -(4*e) + y1**2
            if dum < 0:
                z1im = 2*math.sqrt(-dum)
            else:
                z1re = 2*math.sqrt(dum)
                z2re = -z1re
        else:
            rre = math.sqrt(sqr)
            z1re = -(8.0*d + b*b*b)/4.0 + b*c
            z1re /= rre
            z2re = -z1re

    else:
        rim = math.sqrt(-sqr)
        z1im = -(8.0*d + b*b*b)/4.0 + b*c
        z1im /= rim
        z1im = -z1im
    
    z1re += -(2*c + sqr) + 3*b*term
    z2re += -(2*c + sqr) + 3*b*term
    if abs(z1im) < 0.00000000001:
        if z1re >= 0:
            dre = math.sqrt(z1re)
        else:
            dim = math.sqrt(-z1re)
        
        if z2re >= 0:
            ere = math.sqrt(z2re)
        else:
            eim = math.sqrt(-z2re)
    else:
        r = math.sqrt(z1re**2 + z1im**2)
        r = math.sqrt(r)
        dum = math.atan2(z1im, z1re)
        dum /= 2
        ere = r*math.cos(dum)
        dre = ere
        dim = r*math.sin(dum)
        eim = -dim
    x1 = complex(-term+(rre+dre)/2, (rim+dim)/2)
    x2 = complex(-(term + dre/2)+rre/2, (-dim+rim)/2)
    x3 = complex(-(term + rre/2)+ere/2, (-rim+eim)/2)
    x4 = complex(-(term + (rre+ere)/2), -(rim + eim)/2)
    if abs(x1.imag) <0.00000000001:
        ans.append(x1.real)
        print(x1.real, end=' ')
    if abs(x2.imag) <0.00000000001:
        ans.append(x2.real)
        print(x2.real, end=' ')
    if abs(x3.imag) <0.00000000001:
        ans.append(x3.real)
        print(x3.real, end=' ')
    if abs(x4.imag) <0.00000000001:
        ans.append(x4.real)
        print(x4.real, end=' ')
    

if __name__ == '__main__':
    matrix = [
        1,2,-2,
        -2,5,-2,
        -6,6,-3
    ]

    matrix2 = [
        2,-12,
        1,-5
    ]

    matrix3 = [
        0,0,0,0,
        0,0,0,0,
        0,0,0,0,
        0,0,0,0
    ]
    
    getCubeRoot(matrix)
    print(ans)

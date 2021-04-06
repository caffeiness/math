a,b = input(),input()

#整数に変換
a,b = int(a),int(b)

#関数を定義
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b):
    return int(a*b/gcd(a,b))

print(gcd(a,b))
print(lcm(a,b))

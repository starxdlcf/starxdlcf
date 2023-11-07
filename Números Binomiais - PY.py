#"Triângulo de Pascal
#O triângulo de Pascal obedece a seguinte fórmula de números binomiais: {\displaystyle {\binom {n}{k}}={\frac {n!}{k!(n-k)!}}.}

n = eval(input("Insira o valor de N: "))
k = eval(input("Insira o valor de K: "))
x = n - k

def fat_n(N):
    cont_n = 1
    fatorial_n = 1
    while cont_n <= n:
        fatorial_n *= cont_n
        cont_n += 1
    return fatorial_n

def fat_k(K):
    cont_k = 1
    fatorial_k = 1
    while cont_k <= k:
        fatorial_k *= cont_k
        cont_k += 1
    return fatorial_k

def fat_x(X):
    cont_x = 1
    fatorial_x = 1
    while cont_x <= x:
        fatorial_x *= cont_x
        cont_x += 1
    return fatorial_x    

def numbi(f1, f2, f3):
    r = f1/(f2*f3)
    return r

rn = fat_n(n)
rk = fat_k(k)
rx = fat_x(x)

resultado_numbi = numbi(rn, rk, rx)
print(resultado_numbi)

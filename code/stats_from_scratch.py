# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

def mean(x):
    return sum(x)/len(x)


def median(x):
    x = sorted(x)
    n = len(x)
    if len(x)%2 == 1:
        return x[n//2]
    else:
        return mean([x[n//2], x[n//2-1]])


def mode(x):
    from collections import Counter
    
    d = Counter(sorted(nums))
    keys_sorted_by_value = [k for k, v in sorted(d.items(),
                                                 key=lambda item: item[1],
                                                 reverse=True)]
    return keys_sorted_by_value[0]


def weighted_mean(x, w):
    weighted_sum = 0
    for i in range(len(x)):
        weighted_sum += x[i]*w[i]
    return weighted_sum/sum(w)


def std(x):
    import math
    
    m = mean(x)
    n = len(x)
    sq_diff = [(i-m)**2 for i in x]
    return math.sqrt(sum(sq_diff)/n)


def quartiles(x):
    x = sorted(x)
    n = len(x)
    if n%2 == 1:
        part1, part2 = x[:n//2], x[n//2+1:]
    else:
        part1, part2 = x[:n//2], x[n//2:]
    return [median(part1), median(x), median(part2)]


def freq2data(x, freq):
    n = len(x)
    l = []
    for i in range(n):
        for j in range(freq[i]):
            l.append(x[i])
    return l


def iqr(x):
    q = quartiles(x)
    return q[2] - q[0]


def factorial(x):
    product = 1
    while x > 1:
        product *= x
        x -= 1
    return product


def permutation(n, r):
    return factorial(n)/factorial(n-r)


def combination(n, r):
    return permutation(n, r)/factorial(r)


def binomial_pdf(n, r, p):
        return combination(n, r) * p**r * (1-p)**(n-r)


def binomial_cdf(n, r, p):
    res = 0
    for i in range(r+1):
        res += combination(n, i) * p**i * (1-p)**(n-i)
    return res


def geometric_pdf(n, p):
    if n == 0:
        return 0
    else:
        return (1-p)**(n-1)*p


def poisson_pdf(k, lambda_):
    e = 2.71828
    return lambda_**k*e**(-lambda_)/factorial(k)


def z_score(x, mu, sigma):
    return (x-mu)/sigma


def normal_pdf(x):
    import math
    return(math.exp(-x**2/2)/math.sqrt(2*math.pi))


def normal_cdf(x):
    sum_ = 0
    for i in range(int(-1e6), int(x*1e5)):
        sum_ += normal_pdf(i/1e5)
    return sum_/1e5

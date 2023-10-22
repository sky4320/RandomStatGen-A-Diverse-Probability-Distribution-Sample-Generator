import random
import math
import sys

random.seed(10) # Set seed
u = random.random() # Init u

def main():
    if(len(sys.argv) <= 1):
        print("Invalid arguements, provide the type of distribution and required arguements for the distribution")
        return
    else:
        noofsamples = sys.argv[1]
        distribution = sys.argv[2].lower()

    if distribution == "bernoulli":
        if(len(sys.argv) == 4):
            print("Sample : ", bernoulli(int(noofsamples),float(sys.argv[3])))
        else:
            print("Invalid arguements for bernoulli distribution")
    elif distribution == "binomial":
        if(len(sys.argv) == 5):
            print("Sample :",binomial(int(noofsamples),int(sys.argv[3]),float(sys.argv[4])))
    elif distribution == "geometric":
        if(len(sys.argv) == 4):
            print("Sample : ", geometric(int(noofsamples),sys.argv[3:len(sys.argv)]))
        else:
            print("Invalid arguements for geometric distribution")
    elif distribution == "neg-binomial":
        if(len(sys.argv) == 5):
            print("Sample :",negBinomial(int(noofsamples),sys.argv[3:len(sys.argv)]))
        else:
            print("Invalid arguements for negative binomial distribution")
    elif distribution == "poisson":
        if(len(sys.argv) == 4):
            print("Sample : ", poisson(int(noofsamples),float(sys.argv[3])))
        else:
            print("Invalid arguements for poisson distribution")
    elif distribution == "arb-discrete":
         if(len(sys.argv) < 3):
             print("Invalid arguements for arb-discrete distribution")
         else:
             print("Sample:",arbitaryDiscrete(int(noofsamples), sys.argv[3:len(sys.argv)]))
    elif distribution == "uniform":
        if(len(sys.argv) == 5):
            print("Sample :",uniform(int(noofsamples),float(sys.argv[3]),float(sys.argv[4])))
        else:
            print("Invalid arguements for uniform distribution")
    elif distribution == "exponential":
        if(len(sys.argv) < 3):
            print("Invalid arguements for exponential distribution")
        else:
            print("Sample:",exponential(int(noofsamples),sys.argv[3:len(sys.argv)]))
    elif distribution == "gamma":
        if(len(sys.argv) < 3):
            print("Invalid arguements for gamma distribution")
        else:
            print("Sample:",gamma(int(noofsamples), sys.argv[3:len(sys.argv)]))
    elif distribution == "normal":
        if(len(sys.argv) < 3):
            print("Invalid arguements for normal distribution")
        else:
            print("Sample:",normal(int(noofsamples), sys.argv[3:len(sys.argv)]))
    else:
        print("Distribution type is not supported")

def bernoulli(noofsamples,p):
    result = []
    for i in range(0,noofsamples):
        u = random.random()
        if (u < p):
            result.append(1)
        else:
            result.append(0)
    return result

def binomial(noofsamples,n,p):
    result = []
    for i in range(noofsamples):
        cnt = 0
        for i in range(n):
            if random.random() <= p:
                cnt += 1
        result.append(cnt)
    return result

def geometric(noofsamples,Args):
    result = []
    p = float(Args[0])
    for i in range(noofsamples):
        cnt = 1
        while random.random() > p:
            cnt = cnt + 1
        result.append(cnt)
    return result

def negBinomial(noofsamples,Args):
    result =[]
    n = int(Args[0])
    p = Args[1:len(Args)]
    for i in range(noofsamples):
        result.append(sum(geometric(n,p)))
    return result


def poisson(noofsamples,p):
    result = []
    for i in range(noofsamples):
        cnt = 0
        u = random.random()
        while u >= math.exp((0.0-p)):
            cnt = cnt + 1
            u = u * random.random()
        result.append(cnt)
    return result

def cumulativeDistribution(p):
	temp = []
	for i in range(len(p)):
		temp.append(sum(p[0:i+1]))
	return temp

def arbitaryDiscrete(noofsamples,Args):
    result = []
    temp=[]
    for i in Args:
        temp.append(float(i))
    t = cumulativeDistribution(temp)
    if  t[-1] != 1:
        print("Sum of total of probabilities should be one")
        return
    for i in range(noofsamples):
        cnt = 0
        u = random.random()
        while  t[cnt] <= u:
            cnt = cnt + 1
        result.append(cnt)
    return result

def uniform(noofsamples,min,max):
    result = []
    if(min > max):
        temp = max
        max = min
        min = temp
    for i in range(noofsamples):
        result.append(min + ((max - min)* random.random()))
    return result

def exponential(noofsamples,Args):
    result = []
    lamda = float(Args[0])
    for i in range(noofsamples):
        result.append((0-(1/lamda))*math.log(1-random.random()))
    return result


def gamma(noofsamples,Args):
    result = []
    alpha  = int(Args[0])
    lamda = Args[1:len(Args)]
    for i in range(noofsamples):
        result.append(sum(exponential(alpha,lamda)))
    return result

def normal(noofsamples,Args):
    result = []
    μ = float(Args[0])
    σ = float(Args[1])
    for i in range(noofsamples):
        u1 = random.random()
        u2 = random.random()
        z1 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
        z2 = math.sqrt(-2 * math.log(u1)) * math.sin(2 * math.pi * u2)
        result.append(z1 * σ + μ)
        result.append(z2 * σ + μ)
    if noofsamples % 2 == 0:
        return result
    else:
        return result[0:len(result)-1]

main()

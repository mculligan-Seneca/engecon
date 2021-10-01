#This module is used to calculate the formulas used in eng economics


#Compound Amount Factor
#(F/P,i,n)=(1+i)^n
def cmpAmtFact(interest,ncmpounds):
    return(1+interest)**ncmpounds
#Present Worth Factor    
#(P/F,i,n)=1/(1+i)^n
def presWorthFact(interest,ncmpounds):
    return (1/cmpAmtFact(interest,ncmpounds))

#Uniform series compound amount factor
#(F/A,i,n)=(1+i)^n-1/i
def uniSeriesCmpAmtFact(interest,ncmpounds):
    return((cmpAmtFact(interest,ncmpounds)-1)/interest)

#Sinking fund factor
#(A/F,i,n)=i/[(1+i)^n-1]
def sinkFundFact(interest,ncmpounds):
    return(1/uniSeriesCmpAmtFact(interest,ncmpounds))

#Series present worth factor
#(P/A,i,n)=(1+i)^n-1/i(1+i)^n
def seriesPresWorthFact(interest,ncmpounds):
    return uniSeriesCmpAmtFact(interest,ncmpounds)*presWorthFact(interest,ncmpounds)

#Capital Recovery Factor
#(A/P,i,n)=i(1+i)^n/[(1+i)^n-1]
def capRecoveryFact(interest,ncmpounds):
    return sinkFundFact(interest,ncmpounds)*cmpAmtFact(interest,ncmpounds)




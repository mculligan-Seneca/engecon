from engecon import cmpAmtFact, presWorthFact,uniSeriesCmpAmtFact,sinkFundFact,seriesPresWorthFact,capRecoveryFact
from tabulate import tabulate


def main():

    compounds=int(input("Enter number of compounds "))
    interest=float(input("Enter interest % "))/100
    table=[]
    t=tabulate(['compounding periods','Compound Amount Factor','Present Worth Factor',
    'Sinking fund factor','Capital Recovery Factor','Uniform series compound amount factor',
    'Series present worth factor'])
    for i in range(1,compounds):
        table.append([i,cmpAmtFact(interest,i),presWorthFact(interest,i),sinkFundFact(interest,i),capRecoveryFact(interest,i),uniSeriesCmpAmtFact(interest,i),seriesPresWorthFact(interest,i)])
    
    print(tabulate(table,headers=['compounding periods','Compound Amount Factor','Present Worth Factor',
    'Sinking fund factor','Capital Recovery Factor','Uniform series compound amount factor',
    'Series present worth factor'],tablefmt="orgtbl"))




if __name__ =='__main__':
    main()
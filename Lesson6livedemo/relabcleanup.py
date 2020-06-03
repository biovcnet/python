import numpy as np
import csv

with open('suboxicGL3.csv', newline='\n') as csvfile:
    myReader = csv.reader(csvfile, delimiter=',')
    
    next(myReader)
 
    taxaList=[]
    sumList=[]
    
    for row in myReader:
        print(row)
        print('taxa: ',row[0])
        taxaList.append(row[0])
        print('reads, string: ',row[1:])
        floatReads=[float(x) for x in row[1:]]
        print('floatReads: ',floatReads)
        sumReads=sum(floatReads)
        
        print('total: ', sumReads)
        print('\n')
        sumList.append(sumReads)
        
        
descTotals, descTaxa = (list(t) for t in zip(*sorted(zip(sumList, taxaList))))

descTaxa.reverse()
descTotals.reverse()

top20Taxa=descTaxa[:20]
top20Totals=descTotals[:20]
 
top20relAb=[]
for t in top20Totals:
    print(t,'divided by ',sum(top20Totals))
    relAb=t/sum(top20Totals)
    print('relative abundance: ',relAb,'\n')
    top20relAb.append(relAb)

myOutHeaders=['OTU ID','Reads','Relative Abundance']

with open('top20RA_GL3_suboxic.csv', 'w', newline='') as f:
    writer = csv.writer(f,delimiter=',')
    writer.writerow(myOutHeaders)
    
    for i in range(len(top20Taxa)):
        outRow=[top20Taxa[i],str(top20Totals[i]),str(top20relAb[i])]
        print(outRow)
        writer.writerow(outRow)


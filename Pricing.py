__author__ = 'ronaldbjork'
import pdb

class Pricing:
    def __init__(self):
        r1 = (list(range(0,11)),"fixed",2000)
        r2 = (list(range(11,21)),"free",2000)
        r3 = (list(range(21,51)),"rate",100)
        r4 = (list(range(51,68)),"free",5000)
        r5 = (list(range(68,134)),"rate",75)
        r6 = (list(range(134,251)),"free",10000)
        r7 = (list(range(251,376)),"rate",40)
        r8 = (list(range(376,1000)),"free",15000)
        r9 = (list(range(1000,1701)),"rate",15)

        r10 = (list(range(0,10)), "rate",200)
        r12 = (list(range(10,13)), "FREE",2000)
        r13 = (list(range(13,33)), "rate",150)
        r14 = (list(range(33,80)), "FREE",10000)
        r15 = (list(range(80,160)), "rate",125)
        r16 = (list(range(160,200)),"FREE",20000)
        r17 = (list(range(200,500)),"rate",100)
        r18 = (list(range(500,666)),"FREE",50000)
        r19 = (list(range(666,1000)),"rate",75)

        self.ranges = [r1,r2,r3,r4,r5,r6,r7,r8,r9]
        self.ranges2 = [r10,r12,r13,r14,r15,r16,r17,r18,r19]

    def computeprice(self,counties):
        price = None
        totalnum = len(counties)
        numinstockcounties = len([c for c in counties if c['availability'] == "IN STOCK"])
        #pdb.set_trace()
        for r in self.ranges:
            if numinstockcounties in r[0]:
                if r[1] == "free" or r[1] == "fixed":
                    price = r[2]
                else:
                    price = r[2] * numinstockcounties
                break
        #pdb.set_trace()
        numnotstock = len([c for c in counties if not c['availability'] == "IN STOCK"])
        for r in self.ranges2:
            if numnotstock in r[0]:
                if r[1] == "FREE":
                    price2 = r[2]
                else:
                    price2 = r[2] * numnotstock
                break
        #pdb.set_trace()
        return numinstockcounties, price, numnotstock, price2, totalnum, price + price2



#if __name__ == "__main__":
    #p = Pricing()
    #print(p.computeprice(1000))

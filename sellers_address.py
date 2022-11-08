import os
import pandas as pd
import numpy as np
import re
filelist=[]
index1=[]
directory='F:\Text Books\Business Analytics\MG241 Marketing Management\Invoices\Yoshitha\\pdftotext'
for filename in os.listdir(directory):
    f=os.path.join(directory,filename)
    if os.path.isfile(f):
        filelist.append(f)
print(os.listdir(directory))
g=dict()
order=[]
brands=[]
quantity=[]
product=[]
invoicedate=[]
totalamount=[]
shippingaddress=[]
billingaddress=[]
paymentmethod=[]
shippingchargeslist=[]
fileorderno=0
za=0
newfilenolist=[]
namelist=[]
selleraddresslist=[]
for i in filelist:
    z=0
    an=0
    ay=0
    at=0
    ag=0
    ah=0
    found=0
    found1=0
    found2=0
    with open(i,'r') as fhand:
        for x in fhand:
            ax=0
            words=x.split()
            d=0
            '''for y in words:
                if y == 'of:':
                    try:
                        tst=int(words[d+1])+1
                        brands.append(words[d+2])
                        product.append(' '.join(re.findall('[0-9] of: [0-9]* \S+ (\S.*)',x)))
                        
                        #print((str(re.findall('[0-9] of: \S+' '',x))), i)
                    except:
                        brands.append(words[d+1])
                        product.append(' '.join(re.findall('[0-9] of: \S+ (\S.*)',x)))
                    z=z+1
                    if words[d+1] in ['realme']:
                        if z>1:
                            print(i, '@@@@@@@@@@@\n')
                    quantity.append(words[d-1]) #quantity coloumn
                d=d+1    
            if x[0:12]=='Order Placed':
                datestring=' '.join(re.findall('Order Placed: (\S+ \S+ \S+)',x))
                totalamountstring=' '.join(re.findall('Order Total: (\S+)',x))
            if re.search('Delivery Address:',x):
                at=1'''
                
            if re.search('Sold By :',x) or re.search('Sold By:',x):
                ah=1
            if ah==1 and re.search('\S+, [A-Za-z ]+, [0-9][0-9][0-9][0-9][0-9][0-9]', x):
                selleraddress=' '.join(re.findall('(\S+), [A-Za-z ]+, [0-9][0-9][0-9][0-9][0-9][0-9]', x))
                ah=0
                found2=1
                
            
            if at==1 and re.search('\S+, [A-Za-z ]+ [0-9][0-9][0-9][0-9][0-9][0-9]', x):
                shippinglst=' '.join(re.findall('(\S+), [A-Za-z ]+ [0-9][0-9][0-9][0-9][0-9][0-9]',x))
                at=0
            if re.search('Billing Address:',x):
                ag=1
                found1=1
            if ag==1 and re.search('\S+, [A-Za-z ]+ [0-9][0-9][0-9][0-9][0-9][0-9]', x):
                billinglst=' '.join(re.findall('(\S+), [A-Za-z ]+ [0-9][0-9][0-9][0-9][0-9][0-9]',x))
                ag=0
            if an==1:
                addon2=addon1+' '+x.rstrip()
                #print(addon2.rstrip())
                paymentmethodterm=' '.join(re.findall('(\S* \S*) Shipping:',addon2))
                if re.search('digits:',paymentmethodterm):
                    paymentmethodterm='Card'
                if paymentmethodterm=='':
                    print(i)
                    paymentmethodterm='BHIM UPI'
                an=an+1
            if re.search('Subtotal:',x):
                addon1=x
                addon1=addon1.rstrip()
                an=an+1
            if re.search('Shipping:',x):
                shippingchargeslistterm=' '.join(re.findall('Shipping: *([0-9]*.[0-9][0-9])',x))
                ax=1
            if ax==1 and shippingchargeslistterm=='':
                print(i)
            if ay==1:
               name=' '.join(re.findall('^(\S*)',x))
               ay=0
            if re.search('Delivery Address:',x):
                name=' '.join(re.findall('Delivery Address: *(\S+) \S',x))
                if name=='':
                    ay=1
                    found=1
        if found==0:
            name='N/A'
        if found1==0:
            billinglst='N/A'
        if found2==0:
            selleraddress='N/A'
    selleraddresslist.append(selleraddress)
                
            
                
    if z>1:#index adjustment
        order.append([fileorderno,z-1])
        za=za+1
    fileorderno=fileorderno+1
    '''for i in range(z):
        invoicedate.append(datestring)
        totalamount.append(totalamountstring)
        shippingaddress.append(shippinglst)
        paymentmethod.append(paymentmethodterm)
        shippingchargeslist.append(shippingchargeslistterm)
        namelist.append(name)
        billingaddress.append(billinglst)'''
#you should make a dictionary with key being the za where z is > 1 and value being a
#list containing z and fileno, so increse elements of index1 > fileno(i.e., list no) by z and insert
#fileno+1,+2....+z after the fileno in index1, then the indexing will be according to
#actual file numbers.
#the fallacy in above three lines is that we are changing the indexes of files
#which use to denote the file number, thus loosing the track of which element
#came from which file. Thus we keep same index number to elements from same file
#If this order of elements from same files gets jumbled see nxt comment
#print(os.listdir(directory))
for b in os.listdir(directory):
    numberpre=b[8:]
    number=numberpre[:-4]
    index1.append(int(number))
'''order=order[::-1]
for i in order:
    for b in range(i[1]):
        index1.insert(i[0]-len(index1)+1,index1[i[0]])
    if i[0]==18:
        print(index1) '''          
#if newfilenolist[b]*0.1*b is to be added in insert operation
#print(index1)
'''g['Brand']=brands
g['Quantity']=quantity
g['Product']=product
g['Invoice-Date']=invoicedate
g['Total Amount']=totalamount
g['Shipping Address']=shippingaddress
g['Payment Method']=paymentmethod
g['Shipping Charges']=shippingchargeslist
g['Name']=namelist
g['Billing Address']=billingaddress'''
g['Seller Address']=selleraddresslist
#print(g)
df=pd.DataFrame(g,index=index1)
df=df.sort_index(axis=0)
print(df)
#df.to_csv('F:\Text Books\Business Analytics\MG241 Marketing Management\Invoices\Yoshitha\pdftotext\\yoshitha.csv')

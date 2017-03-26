target = open('eredmeny.txt','w')

with open('bro-code.txt','r') as my_file:
    for line in my_file:
        target.write('"'+line[:-1]+'",\n');
        
target.close()
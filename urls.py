urls = '';
f=open('urls.txt','w')
for x in range(1, 133):
    urls = 'http://schlesinger.radcliffe.harvard.edu/onlinecollections/blackwell/item/47329707/%d\n' % (x)
    f.write(urls)
f.close
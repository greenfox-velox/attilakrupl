from itertools import count
def domain_name(url):
    domainName = url
    if "//" in domainName:
        domainName = domainName[domainName.index('/')+2:]
    if domainName[0] == 'w':
        domainName = domainName[domainName.index('w')+4:]
    elif '@' in domainName:
        domainName = domainName[domainName.index('@')+1:]
    if domainName.count('.') > 1:
        domainName = domainName[:domainName.rindex('.')]
        domainName = domainName[domainName.rindex('.')+1:]
    else:
        domainName = domainName[:domainName.index('.')]
    return domainName
print (domain_name("mailto:user@foo.example"))
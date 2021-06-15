import pprint

def disply_csv():
    f = open("./price.csv","r")
    content = f.readlines();
    f.close()
    pp = pprint.PrettyPrinter(4)
    pp.pprint(content)

def field(line):
    fld = line.strip().split(',')
    return fld[0]
 
  

def sort_csv(clm):
    f = open("./price.csv","r")
    content = f.readlines()
    head = content.pop(0)
    f.close()
    content.sort(key=field)
    pp = pprint.PrettyPrinter(4)
    print(head)
    pp.pprint(content)

  

#disply_csv()
sort_csv('Series reference')

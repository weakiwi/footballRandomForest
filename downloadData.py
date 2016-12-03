import grequests
from ssdb import SSDB
ssdb = SSDB(host='localhost', port=8888)
def init(howLong):
    a = []
    for i in range(howLong):
        a.append("http://zq.win007.com/jsData/teamInfo/teamDetail/tdl"+ str(i) +".js")
    return a
def downloadJs(url_list):
    url = url_list
    rs = (grequests.get(u) for u in url)
    a = grequests.map(rs)
    return a
def insertQueue(q_name, content):
    ssdb.qpush_front(q_name, content)
#ssdb.qclear('q')
#i = downloadJs(init(10000))
#for a in i:
#    a = a.content
#    if a[3:6] == "var":
#        insertQueue('q', a)
print ssdb.qpop('q')

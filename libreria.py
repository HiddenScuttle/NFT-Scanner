from types import NoneType
import requests
import json

API="N67SZ7EY8XFP4K3EW7WPKPVZAQNMGY34ZW" #API per eseguire le query
contractaddressv2="0xb932a70a57673d89f4acffbe830e8ed7f75fb9e0" #Contratto di superrare v2
startblockv2="8486734"
endblockv2="8487734"
result=[]

def get_apikey(): #funzione per restituire l' api key
    return API

def get_contractaddress(): #funzione per restituire il contratto
    return contractaddressv2

def get_startblock():
    return startblockv2

def get_number_block(): #funzione che restituisce l'ultimo numero del blocco delle transazioni di etherscan
    urlcount="https://api.etherscan.io/api?module=proxy&action=eth_blockNumber&apikey="+get_apikey()
    count=requests.get(urlcount)
    countjson=count.json()
    countstring=str(int(countjson["result"],16))
    return countstring


def write_json(): #funzione che scrive sul file json dopo aver memorizzato tutti i dati di etherscan
    global result
    with open('datacontractv2.json','w') as fp:
        json.dump(result,fp,indent=4,separators=(',',':'))
    with open("datacontractv2.json","r") as read_file:
        data=json.load(read_file)
    results= [json.dumps(record) for record in data]
    with open('datacontract.json','w') as obj:
        x=1
        obj.write('{\n')
        for i in results: 
            if x<results.__len__():
                obj.write('"transaction_'+str(x)+'":'+i+','+'\n')
            else:
                obj.write('"transaction_'+str(x)+'":'+i+'\n')
            x=x+1
        obj.write('}')


def query_request(countstring):
    while(int(endblockv2)<int(countstring)):
        print("Sono entrato in ciclo")
        request=request_url()
        append_in_result(request)
        update_start_end_block()
        print("Ciclo finito")
    print("Sono uscito dal while")
    last_update(countstring)
    append_in_result(request_url())

def request_url():
    global startblockv2
    global endblockv2
    urlv2="https://api.etherscan.io/api?module=account&action=tokennfttx&contractaddress="+contractaddressv2+\
        "&startblock="+startblockv2+"&endblock="+endblockv2+"&sort=desc&apikey="+API
    response_v2=requests.get(urlv2)
    ceck=response_v2.__str__()
    print(ceck)
    while ceck.__eq__("<Response [200]>")==False:
        print("Faccio di nuovo la richiesta")
        response_v2=requests.get(urlv2)
        ceck=response_v2.__str__()
        print(ceck)
    address_content_v2=response_v2.json()
    return address_content_v2

def append_in_result(address_content_v2):
    global result
    for i in address_content_v2["result"]:
        result.append(i)

def update_start_end_block():
    global startblockv2
    global endblockv2
    tmp=int(startblockv2)+1001
    startblockv2=str(tmp)
    tmp=tmp+1000
    endblockv2=str(tmp)
    print(startblockv2)
    print(endblockv2)

def last_update(countstring):
    global startblockv2
    global endblockv2
    tmp=int(startblockv2)+1001
    startblockv2=str(tmp)
    endblockv2=countstring
    print(startblockv2)
    print(endblockv2)

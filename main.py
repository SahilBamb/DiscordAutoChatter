import requests
import time
import sys

#authorization is your log-in information and url is the Discord channel's url
def sendMessage(message,auth,url,delay=0):
    payload = { 'content': message}
    header = {'authorization' : auth}
    print('sending message')
    print(message)
    requests.post(url,data=payload,headers=header)
    time.sleep(60 + (delay))


if __name__ == '__main__':
    count = 0
    with open('sampleexpressions.txt') as fin:
        for line in fin:
            count+=1
            sendMessage(line,sys.argv[1],sys.argv[2])
            if count==int(sys.argv[3]): exit()

        
     

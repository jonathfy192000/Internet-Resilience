import os
import json

#############also really easy to implement the abuf decoding here, so I can print the results, just need to use abuf_decoder from other file
#first need to add ] to the end of the file, for some reason they don't do that
#modify = open("test1.json", "a")
#modify.write("]")
#modify.close()

def get_ips_replace():
    #testA.json is a list of dictionaries
    if (os.path.exists("results.txt")):
        os.remove("results.txt")
    results = open("results.txt", "w")
    list_data = json.load(open("test1.json", "r"))
    for data in list_data:
        try: #if no src address, then that means no local resolvers were found (available), so the query was unable to execute
            results.write("src = {} ------------------------\n".format(data["resultset"][0]["src_addr"])) #src is always the same
        except:
            continue
        #if there is a src address, find all the dst addresses if pinged
        for query in data["resultset"]:
            try: #some of the entries don't have a dst_addr, that means they failed
                results.write(str(query["dst_addr"]) + "\n")
            except:
                continue

    results.close()

get_ips_replace()
#ex query result that actually worked
#{"fw":5020,"mver":"2.2.1","lts":104,"resultset":[{"time":1625875240,"lts":104,"subid":1,"submax":1,"dst_addr":"192.168.2.1","dst_port":"53","af":4,"src_addr":"192.168.2.100","proto":"UDP","qbuf":"iIwBAAABAAAAAAAABzEwMDAwMjMFYXRsYXMEcmlwZQNuZXQQYTBiNDY5MTg1NjA3N2NhYwAAAQAB","result":{"rt":74.077,"size":57,"abuf":"iIyBgwABAAAAAAAABzEwMDAwMjMFYXRsYXMEcmlwZQNuZXQQYTBiNDY5MTg1NjA3N2NhYwAAAQAB","ID":34956,"ANCOUNT":0,"QDCOUNT":1,"NSCOUNT":0,"ARCOUNT":0}}],"msm_id":30001,"prb_id":1000023,"timestamp":1625875240,"msm_name":"Tdig","from":"159.146.31.90","type":"dns","stored_timestamp":1625875380},
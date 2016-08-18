import httplib
from xml.dom.minidom import parse,parseString,Node

devKey='4f457588-2687-4686-bd9b-404c841bf615'
appKey='AnveshPa-EbayLapt-PRD-b577624e3-6e243508'
certKey='PRD-577624e36a74-f11c-403b-95ad-b0f5'
userToken='AgAAAA**AQAAAA**aAAAAA**DqirVw**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6ABkYSgC5GDoAmdj6x9nY+seQ**4WQDAA**AAMAAA**hvgKTbMapOVEvZ501NEfHKdIPL59r5DvT7C93gviXe5AoBC9IZ/4pBq1FGPx+LjIbImJqkhxndYHl6zBWCBimMfSWLBOQL2RNTIkSNneLslNIXJBR7LMvXVu08qYM/lPd/vXeh9+ZHEhnuV5eu0WdXDJTsWBJggJXg8SOdScSzAd0/9ByENulgOek772EVdtioP2Uxx2U9eZhv+mf2RojXqrCc8Hzsjo8NIvH8ScD9AKQdFiqk+3Ho6rnam+PVzewurupTufv9GLMXLXsHZO5jLEI9IzfgcAfLs4EWNmfDvQb6DcczenmYFhDmewIqMHlQvcEdssDzCfuy7+cKXV3TNaZbx7bynXdEKdbxRegwayjEmHAHAlhA8BXJ/3JOgwtBJVrJezwRNYlQJCMANURMTCZ+6Oa/CZ3fKCpHn8YanuAwhxISVHJKdk+275RzxNLxE1pGhgMmOmHXkGXZfFOC0nE0J41992SHTQBb4THebJa6C1loKduFSVeDvfsMahySm4CmkzkB/q3WcTnG1JjdMzrUOgezjH/Yh4E9E4mBDgk6A531WV7y79JNfWqcXarcZWAA8SIbt/JGJx2AZhCV+wZQhPOAn5YVoe4inMJ+WjhJV8hpc8LklbeOSc0hisGENknvAPvggKz0fkcWaCgelQ1irfYJ8tQMbGpZp/8MK8Q/nxX9bMWGJENwXMqIh0bCuqqub5K9iSTmg5o6nOQQmKa/WNVZkGZVc7zDwaKceYbx71qa+DVRfFrrK+n7cD'
serverUrl='api.ebay.com'

def getHeaders(apicall,siteId="0",compatibilityLevel="433") :
    headers=
    {
    "X-EBAY-API-COMPATIBILITY-LEVEL" : compatibilityLevel,
    "X-EBAY-API-DEV-NAME" : devKey,
    "X-EBAY-API-APP-NAME" : appKey,
    "X-EBAY-API-CERT-NAME" : certKey,
    "X-EBAY-API-CALL-NAME" : apicall,
    "X-EBAY-API-SITEID" : siteID,
    "Content-Type" : "text/xml"
    }

    return headers

def sendRequest(apicall,xmlparameters) :

    connection=httplib.HTTPSConnection(serverUrl)
    connection.request("POST",'/ws/api.dll',xmlparameters,getHeaders(apicall))
    response=connection.getresponse()
    if response.status!=200 :
        print 'Error sending request:'+response.json
    else :
        data=response.read()
        connection.close()
    return data

def getSingleValue(node,tag) :
    nl=node.getElementsByTagName(tag)
    if len(nl)>0 :
        tagNode=nl[0]
        if tagNode.hasChildNodes() :
            return tagNode.firstChild.nodeValue

    return '-1'                        

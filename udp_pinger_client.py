import socket
import time
from statistics import mean

HOST = "10.0.0.1"  # todo: specify the server's hostname or IP address inside the quotes
PORT =  12001 # todo: specify the port number used by the server

ping_response = []
   
for i in range(1,11):
    #Create the UDP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #Set the timeout to 1 second for connections
    s.settimeout(1)
    #Connect to the host on the defined port
    s.connect((HOST, PORT))
    
    #Construct the message to send to the server
    message = "Ping " + str(i) + ":"
    byte_msg = message.encode('utf-8')
    
    #Record the time prior to sending the message
    send = time.time()
    
    #Send the packet to the server 
    s.sendall(byte_msg)
    #Attempt to receive the response from the server withint the timeout
    try:
        data = s.recv(1024)
        receive = time.time()
        #Record the time the packet was received
        total_time = round((receive - send) * 10 ** 3, 3)
        ping_response.append(total_time)
        #Incorporate the RTT and server response into message to log to screen
        message = data.decode('utf-8') + " rtt = " + str(total_time) + " ms"
    #If response does not occur within the timeout value, print Request timed out
    except socket.timeout:
        message = message + " Request timed out"
    #Print the given response or time out message to screen
    print("{}".format(message))
print ("Summary values:")
print ("min_rtt: {} ms".format(min(ping_response)))
print ("max_rtt: {} ms".format(max(ping_response)))
print ("avg_rtt: {} ms".format(mean(ping_response)))


![task1](https://i.postimg.cc/qMdXd29W/1-distributed-web-infrastructure.png  "Distributed_web_infrastructure")

### some specifics about this infrastructure


> For every additional element, why you are adding it?

```
Load Balancer (HAproxy) : 
to increase the availability  of application by routing a portion of requests to each server

server2 :replica of server1 to distribute the work load

```

> What distribution algorithm your load balancer is configured with and how it works?

```
load balancer configured with Round-robin algorithm

Round-Robin algorithm :  Requests are distributed evenly across backend servers in a circular manner.
Least connections: Requests are sent to the server with the fewest active connections.
execution of algo : the first client to connect is sent to the first server, the second client goes to the second server,
the third client goes back to the first server, the fourth client back to the second server, and so on

```


> is  your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both?

```
my load balancer is enabling Active-Active setup 

Active-Active:
at leat two nodes both actively running the same kind of service simultaneously
active-passive:
at least two nodes but  not all nodes are going to be active
example:if the first node is already active, the second node must be passive or on standby

```


> How a database Primary-Replica (Master-Slave) cluster works?

```
The master-slave is a database architecture divided into a master database and slave databases. 
The slave database serves as the backup for the master database. 
The master database is used for the write operations, while read operations may be spread on multiple slave databases.
```

> What is the difference between the Primary node and the Replica node in regard to the application?

```
The Primary node is responsible for all the write operations the site needs
Replica node is capable of processing read operations
```

### issues are with this infrastructure

1. Single Points of Failure(SPOF)

echec of load balancer ==> the entire system stop working

2. Security Issues

No Firewall ==>  the servers are vulnerable to unauthorized access

No HTTPS  ==> no encryption , confidential data are exposed  to hackers

3. No Monitoring
 
no way to track  performance issues or potential security threats



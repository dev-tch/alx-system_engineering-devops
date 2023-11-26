![task2](https://i.postimg.cc/zGhMBzKx/Secured-and-monitored-infrastructure.png  "secured_and_monitorid_infrastructure")

### specifics about this infrastructure

> For every additional element, why you are adding it?

```
Firewalls :  to secure each server
SSL certificate : SSL certificates are what enable websites to use HTTPS
 which is more secure than HTTP
Monitoring (Sumologic) : ensures that all your systems are always up and running. 
```

> What are firewalls for ? 

```
Firewalls are  network security devices that monitor incoming and outgoing network traffic 
and permit or block data packets based on a set of security rules

```
> Why is the traffic served over HTTPS ?


```
HTTPS uses TLS (SSL) to encrypt normal HTTP requests and responses, making it safer and more secure

```

> What monitoring is used for ? 

```
- used to detect and identify issues before they impact users 
- identify and resolve issues after users are impacted.
- enable you to get notified about critical changes or issues affecting your production IT infrastructure

```

> How the monitoring tool is collecting data?


```
there two types of collecting 

Log monitoring :
search through log files looking for specific events that indicate problems with your systems

Network monitoring:

capture packets on their way through an internet protocol (IP) network so they can be analyzed later without interfering

```
> Explain what to do if you want to monitor your web server QPS?

```
Configure Sumo Logic to ingest metrics data from your web server
Define queries to extract QPS metrics
example: metric=* | timeslice 1h | avg(qps) as avg_qps by _timeslice
Create a Sumo Logic dashboard to visualize QPS metrics over time

```


### issues with this infrastructure:

1. Terminating SSL at the Load Balancer

data is decrypted before reaching web servers, posing a security risk

2. Single MySQL Server Accepting Writes

Single point of failure. If the MySQL server fails, the entire application may be affected

3.  Identical Components on Servers

If all servers have identical components, a single vulnerability could potentially affect the entire infrastructure

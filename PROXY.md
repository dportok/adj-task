# Provided Information
Imagine a server with the following specs:

- 4 times Intel(R) Xeon(R) CPU E7-4830 v4 @ 2.00GHz 56 cores

- 64GB of ram

- 2 tb HDD disk space

- 2 x 10Gbit/s nics

The server is used for SSL offloading and proxies around 25000 requests per second.

# Requested Information
Please let us know which metrics are interesting to monitor in that specific case and how would you do that?  What are the challenges of monitoring this?

## Analysis

**Note:** It is assumed that the server is configured in a way that it can handle the given traffic:

1. Number of open files at kernel level
2. Maximum number of connections at proxy level
3. TCP Port exhaustion at kernel level
4. All 56 cores of the server are being utilized from the Proxy (dedicate some of them to SSL offloading only etc)

The given server is powerful enough and it should be able to handle the given traffic without any significant issues. The only component that could be a potential bottleneck is the HDD, but this really depends on the size of the payload of the requests that the server receives. An SSD or a RAID 0 setup SSD would raise any concerns regarding storage speed. 

### Metrics
The metrics that would be interesting to monitor on this specific use case are the following:

1. HTTP requests sent to Proxy per second

2. Number of 4xx and 5xx errors returned by the Proxy

3. Number of bytes received and sent by the Proxy

4. Number of request errors

5. Percentage of active sessions

6. Number of reuqests on the queue, that are waiting to be served

7. Averate time spent in queue

8. Number of requests that have been rejected due to the fact the queue was full
 
9. The amount of time it takes to process a request

10. Round trip request processing time between Proxy and the Backend services

11. Number of Healthy hosts behind the Proxy

12. Numbert of Unhealthy hosts behind the Proxy

13. Number of Concurrent requests

14. All kind of metrics that could be taken into consideration when monitoring a server, such as CPU, RAM, Storage utilization, Resource saturation , Certifcate expriration, Waiting tine on shared resources etc

**Generally the metrics can be separated in 3 different categories:**

1. Metrics that are related to the Proxy server
2. Metrics that are user centric related (Frontend)
3. Metrics that are related to the backend servers and their dependencies (e.g databases)

### Metrics implementation
There are 2 different approaches on getting the metrics from the Proxy:

* Enable and scrape (through a script) the status page provided by the Proxy software under a specific time interval

The main disadvantage of this method is that there is no persistence of old statistics, so you would need to take care of this by using an appropriate data store

* Using an agent for your Monitoring tool of preference e.g Prometheus, that provides you information both for the server itself and the Proxy software as well (through the corresponding exporter

### Challenges

The main challenges for monitoring this real time / high traffic system are:

1. Getting as precise metris as you can
2. Correctly translating the values of your metrics
3. Setting appropriate thresholds, based on which alerts would come up
4. Correlate server metrics to service metrics in order to understand how the former ones impact the latter ones and thus your client's experience on your platform

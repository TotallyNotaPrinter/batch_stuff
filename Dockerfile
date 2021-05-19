FROM amazonlinux:2

RUN yum update -y
RUN amazon-linux-extras install epel -y 
RUN yum install stress-ng -y 

ENTRYPOINT ["/usr/bin/stress-ng", "--verbose"]
CMD []

FROM alpine:latest

RUN apk update && apk add stress-ng  

ENTRYPOINT ["/usr/bin/stress-ng", "--verbose"]
CMD []

# Problem
When I run `port_scanner.py` from within `docker-compose` environment, 
the program scans ports and finds them all as `open` on the first run. 
If I run it again, fewer ports are shown. If I run it again, the usual (like 22 and 80)
are open within the range.

Running `port_scanner.py` outside of docker container gives the usual open ports
on the first run.

Flipping `docker-compose` config from `network_mode: host` on/off 
and `network: host` on/off seems to have no effect

# Question
Why do I need to run the program multiple times within the container to get real values?

# With `docker-compose`
```
$ docker-compose up
$ docker-compose exec scanner python port_scanner.py
Port : 1 is open.
Port : 2 is open.
Port : ... is open.
Port : n is open.
# ^ ALL PORTS SHOWN AS OPEN

$ docker-compose exec scanner python port_scanner.py
Port : 22 is open.
Port : 80 is open.
# ^ REASONABLE OPEN PORTS SHOWN
```

# With `docker`
```
❯ docker build -t port-scanner:latest -f Dockerfile .
❯ docker run --network host port-scanner python port_scanner.py
Port : 1 is open.
Port : 2 is open.
Port : ... is open.
Port : n is open.
# ^ ALL PORTS SHOWN AS OPEN

❯ docker run  port-scanner python port_scanner.py
104.237.143.20
Port : 22 is open.
Port : 165 is open.
Port : 80 is open.
# ^ REASONABLE OPEN PORTS SHOWN
```

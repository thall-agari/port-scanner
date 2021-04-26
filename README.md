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

# Setup
```
$ docker-compose up
$ docker-compose exec scanner python port_scanner.py
Port : 1 is open.
Port : 2 is open.
Port : ... is open.
Port : n is open.
$ docker-compose exec scanner python port_scanner.py
Port : 22 is open.
Port : 80 is open.
```

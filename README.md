# Problem
When I run `port_scanner.py` from within `docker-compose` environment, 
the program scans ports and finds them all as `open` on the first run. 
If I run it again, fewer ports are shown. If I run it again, the usual (like 22 and 80)
are open within the range.

Running `port_scanner.py` outside of docker container gives the usual open ports
on the first run.

# Question
Why do I need to run the program multiple times within the container to get real values?

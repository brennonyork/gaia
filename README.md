Gaia is a simple provisioning system for physical nodes and clusters. At its core it acts much like make, but at a distributed level leveraging a few tricks within SSH to ease password management and a trivial configuration file to define sets of tasks. Moreover, it was built to be used as either a one-off script or as a library to programmatically setup for different clusters depending on your environment.

By default running bin/gaia will drop you into the Python REPL with a short help menu to explain what each option does. To use Gaia as a library just grab the src directory (gaia.py and ssh.py) and include gaia within your Python script.

```python
import gaia
gaia.intro()
```

Motivation
----------
I found, after multiple installations of Hadoop, Zookeeper, Storm, Accumulo, <distributed platform of choice here>, that I was continuously repeating myself over and over. I certainly had created a plethora of scripts to make it easier, but that didn't solve the root problem. Gaia was made to define all necessities once and easily deploy an unlimited number of times. Moreover, the environments are very shareable objects allowing for community involvement and support.

FAQs
----
Q: Why does GAIA natively drop the user into the Python REPL?
A: Because.

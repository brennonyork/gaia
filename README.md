Gaia is a simple provisioning system for physical nodes and clusters. It leverages a few tricks within SSH to streamline the process and uses a trivial configuration file for users to define a set of tasks related to a given environment.

Motivation
==========
I found, after multiple installations of Hadoop, Zookeeper, Storm, Accumulo, <distributed platform of choice here>, that I was continuously repeating myself over and over. I certainly had created a plethora of scripts to make it easier, but that didn't solve the root problem. Gaia was made to define all necessities once and easily deploy an unlimited number of times. Moreover, the environments are very shareable objects allowing for community involvement and support.

FAQs
====
Q: Why does GAIA natively drop the user into the Python REPL?
A: Because.

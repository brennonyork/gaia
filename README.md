Gaia is a simple provisioning system for physical nodes and clusters. At its core it acts much like make, but at a distributed level leveraging a few tricks within SSH to ease password management and a trivial configuration file to define sets of tasks. Moreover, it was built to be used as either a one-off script or as a library to programmatically setup for different clusters depending on your environment.

By default running bin/gaia will drop you into the Python REPL with a short help menu to explain what each option does. To use Gaia as a library just run the setup.py module as usual (python setup.py install). From there you should be able to import gaia like any other module.

```python
import gaia
gaia.intro()
```

Configuration Files
-------------------
Here is what we've got so far.

```bash
[hadoop:namenode]
run ls; hostname
```

Motivation
----------
I found, after multiple installations of Hadoop, Zookeeper, Storm, Accumulo, <distributed platform of choice here>, that I was continuously repeating myself over and over. I certainly had created a plethora of scripts to make it easier, but that didn't solve the root problem. Gaia was made to define all necessities once and easily deploy an unlimited number of times. Moreover, the environments are very shareable objects allowing for community involvement and support.

SSH Capabilities
----------------
The ssh class handles all socket implementation details related to remote command execution. The way ssh functions allows the user to only have to type the password once for execution of all commands in the task and without the necessity of passwordless ssh. Simply, it creates a socket file once the password is put in for all future traffic to pass through if specified. Once the socket file is removed (gracefully or otherwise) the session is terminated. Upon installation of Gaia through setup.py the ssh class is installed as well.

```python
import ssh
# Create an instance of the class by defining the host and optionally the user
# (else the current user is specified)
module = ssh.ssh('192.168.1.1', 'root')
module.open() # Creates the socket file
# Runs the command specified
module.run('ls && hostname')
# Copies the source directory into the target directory
# -- The copy happens just as if 'scp' were called on a directory with the
#    recursive flag. In this instance the result on the remote machine would
#    look like '/tmp/target_dir/src_dir'   
module.env('/tmp/src_dir', '/tmp/target_dir')
# Closes the ssh session gracefully
module.close()
```

FAQs
----
<ul><li><b>Why does Gaia natively drop the user into the Python REPL?</b></li>
<li>I wanted to ensure that users had a way of displaying the current configuration loaded into the system, especially if they were pulling from multiple files. Because loading files happens on a per-user basis the REPL seemed the best option so that a single show() function could be called. This alleviated longer shell calls with multiple flags (such as loading a configuration only to display its contents).</li></ul>

import sys, os
import subprocess as sp

class ssh:
    # The default path for storing the file socket needed by SSH
    path = "ControlPath=~/.ssh/%r@%h:%p.conn"

    def __init__(self, host, user=""):
        if(user):
            self.host = user+'@'+host
        else:
            self.host = host

    # Opens a connection to the remote machine and stores the socket
    # connection in a file residing in self.path
    def open(self):
        sp.Popen(["ssh", "-NfM", "-o", self.path, self.host]).wait()

    # Closes the above connection to the remote machine gracefully
    def close(self):
        sp.Popen(["ssh", "-o", self.path, "-O", "exit", self.host]).wait()

    # Acts as an SCP command moving, recursively, the indir to the outdir
    def env(self, indir, outdir):
        sp.Popen(["scp", "-qr", "-o", self.path, indir, self.host+':'+outdir]).wait()

    # Acts as an SSH command on the remote machine
    def run(self, cmd):
        sp.Popen(["ssh", "-o", self.path, self.host, cmd]).wait()

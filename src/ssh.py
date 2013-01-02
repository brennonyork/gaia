# will ask for password here
#ssh -NfM -o 'ControlPath=~/.ssh/%r@%h:%p.conn' "$HOST"

# uses existing connection, doesn't ask for password
#scp -o 'ControlPath=~/.ssh/%r@%h:%p.conn' $2 up@$HOST/tmp/
#ssh -o 'ControlPath=~/.ssh/%r@%h:%p.conn' up@$HOST '/tmp/makeup.sh && reboot'

# close the connection
#ssh -o 'ControlPath=~/.ssh/%r@%h:%p.conn' -O exit "$HOST"

import sys, os
import subprocess as sp

class ssh:
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

    def env(self, indir, outdir):
        sp.Popen(["scp", "-r", "-o", self.path, indir, self.host+':'+outdir]).wait()

    def run(self, cmd):
        sp.Popen(["ssh", "-o", self.path, self.host, cmd]).wait()

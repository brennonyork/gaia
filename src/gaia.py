import sys, os, pprint, ssh

_pp = pprint.PrettyPrinter(indent=2)
_task_list = {}

def load(f):
    task = ""
    with open(f, "r") as f:
        for line in f:
            # Remove any comments
            line = line.split('#')[0].strip()
            if(line):
                line = line.split(' ', 1)
                if(line[0][0] == '[' and line[0][-1] == ']'):
                    task = line[0][1:-1]
                    _task_list[task] = _task_list.get(task, [])
                elif(line[0] == "run"):
                    _task_list.get(task, []).append(line)
                elif(line[0] == "env"):
                    _task_list.get(task, []).append(line)
                else:
                    pass       

def show():
    _pp.pprint(_task_list)

def execute(env, host, user=""):
    if not (type(env) is list):
        env = [env]
    module = ssh.ssh(host, user)
    module.open()
    for task in env:
        if(task in _task_list):
            for i in _task_list[task]:
                if(i[0] == "env"):
                    try:
                        indir, outdir = i[1].split(' ')
                    except ValueError:
                        print "WARN: Too many agruments for", i[0], i[1], "; omitting."
                    module.env(indir, outdir)
                elif(i[0] == "run"):
                    module.run(i[1])
                else:
                    print "WARN: Cannot interpret", i[0], "as a command."
        else:
            print "ERROR: Cannot find", task, "in the list of loaded modules."
    module.close()

def generate(f=""):
    conf = ["# [ TASKNAME ]",
            "[sample] # <- The taskname",
            "# env INPUT_DIR OUTPUT_DIR",
            "env /tmp/dir /tmp # <- Saying to copy the 'dir' directory from '/tmp/dir' to",
            "                  #    '/tmp' of the remote machine",
            "# run COMMAND_SET",
            "run hostname; ls && echo \"Hello world!\" # <- Arbitrary commands to run",
            "                                        #    remotely"]
    if(f):
        with open(f, "w") as f:
            for i in conf:
                f.write(i+"\n")
    else:
        for i in conf:
            print i

def intro():
    print
    print "Gaia"
    print "This program is built to ease the deployment, provisioning, and setup of"
    print "physical nodes, clusters, etc. It leverages a simple configuration file to"
    print "determine groupings of tasks and then grants a minimal set of functions to"
    print "execute those tasks on machines. When Gaia boots up it loads the functions"
    print "described below into Python and drops the user into the REPL for execution."
    print
    print "load( filename ):"
    print "\tLoads a given configuration file into the system."
    print "execute( taskset, host, [user] ):"
    print "\tRuns the given task set as defined in the configuration on the"
    print "\tspecified host with the option of defining a user."
    print "show():"
    print "\tDisplays the current loaded task list and their respective individual"
    print "\ttasks."
    print "generate( [filename] ):"
    print "\tWrites a sample configuration file either to stdout or into the file if"
    print "\tone was specified."
    print "intro():"
    print "\tDisplays this introduction for reference"
    print "exit():"
    print "\tExits the current python REPL and returns to the calling shell."


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
                    indir, outdir = i[1].split(' ')
                    module.env(indir, outdir)
                elif(i[0] == "run"):
                    module.run(i[1])
                else:
                    print "WARN: Cannot interpret", i[0], "as a command."
        else:
            print "ERROR: Cannot find", task, "in the list of loaded modules."
    module.close()

def generate(f):
    with open(f, "w") as f:
        f.write("# [ TASKNAME ]\n");
        f.write("[sample] # <- The taskname\n")
        f.write("# env INPUT_DIR OUTPUT_DIR\n")
        f.write("env /tmp/dir /tmp # <- Saying to copy the 'dir' directory from '/tmp/dir' to\n")
        f.write("                  #    '/tmp' of the remote machine\n")
        f.write("# run COMMAND_SET\n");
        f.write("run hostname; ls && echo \"Hello world!\" # <- Arbitrary commands to run\n")
        f.write("                                        #    remotely\n")

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
    print "generate( filename ):"
    print "\tWrites a sample configuration file into the filename specified as"
    print "\twell as helpful comments to understand the concepts."
    print "intro():"
    print "\tDisplays this introduction for reference"
    print "exit():"
    print "\tExits the current python REPL and returns to the calling shell."

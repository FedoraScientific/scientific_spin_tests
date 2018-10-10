import subprocess
import sys

box_name = "Fedora-Scientific"

def vagrant_box_add(url):
    print(subprocess.check_output(["vagrant", "box", "add", url, "--force", "--name", box_name]).decode("utf-8"))

def vagrant_init():
    print(subprocess.check_output(["vagrant", "init", box_name, "--force"]).decode("utf-8"))

def vagrant_up():
    print(subprocess.check_output(["vagrant", "up"]).decode("utf-8"))
    

def run_tests():
    try:
        print(subprocess.check_output(["vagrant", "ssh", "--command", "bash /vagrant/run-tests.sh"], stderr=subprocess.STDOUT).decode("utf-8"))
    except subprocess.CalledProcessError as e:
        print(str(e.stdout))


def main():
    if len(sys.argv) != 2:
        sys.exit('Usage: run_tests_vagrant.py <vagrant_box_url>')
    print("Adding Vagrant box..")
    vagrant_box_add(sys.argv[1])
    print("Initializing Vagrant config")
    vagrant_init()
    print("Vagrant up")
    vagrant_up()    
    print("Running tests..")
    run_tests()

if __name__ == '__main__':
    main()



    
    
    

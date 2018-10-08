import subprocess
import sys

box_name = "Fedora-Scientifix.box"

def vagrant_box_add(url):
    print(subprocess.check_output(["vagrant", "box", "add", url, "--force", "--name", box_name]).decode("utf-8"))

def vagrant_init():
    print(subprocess.check_output(["vagrant", "init", box_name]).decode("utf-8"))

def vagrant_up(box):
    print(subprocess.check_output(["vagrant", "up"]).decode("utf-8"))
    

def run_tests():
    print(subprocess.check_output(["vagrant", "ssh", "--command", "curl", "--location", "--remote-name", "https://github.com/FedoraScientific/scientific_spin_tests/archive/master.zip"]).decode("utf-8"))
    print(subprocess.check_output(["vagrant", "ssh", "--command", "unzip master.zip"]).decode("utf-8"))
    print(subprocess.check_output(["vagrant", "ssh", "--command", "ls"]).decode("utf-8"))
    

def main():
    if len(sys.argv) != 2:
        sys.exit('Usage: run_tests_vagrant.py <vagrant_box_url>')
    vagrant_box_add(sys.argv[1])
    vagrant_init()
    vagrant_up()    
    run_tests()

if __name__ == '__main__':
    main()



    
    
    

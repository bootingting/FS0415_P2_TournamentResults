This is FS04515 P2: Tournament Results version 0.0
==================================================

What's in this release?
-----------------------
This release creates a Python module that uses PostgreSQL database to keep track of players and matches in a swiss pairing style game tournament

Resources
---------
https://www.udacity.com/
https://docs.python.org/2/library/
https://www.youtube.com/watch?v=djnqoEO2rLc
http://git-scm.com/downloads
https://www.virtualbox.org/wiki/Downloads
https://www.vagrantup.com/downloads

Build instructions
------------------
1. Before you can build, you will need to first install Python at https://www.python.org/ . This release was build on Python version 2.7.9

2. You will be using a virtual machine(VM) to run the database server and the VM is a Linux server system that runs on top of your own computer. 

3. To run the VM, you will need to have GIT, VirtualBox and Vagrant installed. GIT will install the configuration for the VM, while VirtualBox runs the VM. Vagrant is the software that configures the VM and let you share files between your host computer and VM.

4. For GIT, download at http://git-scm.com/downloads and install the version for your operating system. On Windows, Git will provide you with a Unix-style terminal and shell (Git Bash). (On Mac or Linux systems you can use the regular terminal program.)

5. For VirtualBox, download it from https://www.virtualbox.org/wiki/Downloads. Install the platform package for your operating system.  You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.

6. For Vagrant, download it from https://www.vagrantup.com/downloads.  Install the version for your operating system. For Windows operating system, the Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

7. Here's how to use GIT to fetch the VM configuration:
Windows: Use the Git Bash program (installed with Git) to get a Unix-style terminal. 
Other systems: Use your favorite terminal program.

From the terminal, run:
git clone http://github.com/udacity/fullstack-nanodegree-vm fullstack

This will give you a directory named fullstack.

8. Using the terminal, change directory to fullstack/vagrant (cd fullstack/vagrant), then type vagrant up to launch your virtual machine.

9. Once it is up and running, type vagrant ssh to log into it. This will log your terminal in to the virtual machine, and you'll get a Linux shell prompt. When you want to log out, type exit at the shell prompt.  To turn the virtual machine off (without deleting anything), type vagrant halt. If you do this, you'll need to run vagrant up again before you can log into it.

10. Go to the tournament folder by typing cd/vagrant/tournament

11. If you stype ls, the following files will be shown; tournament.py, tournament.sql and tournament_test.py. These are just empty shell files.

12. Replace all 3 files from your local vagrant directory with the files from GitHub. The vagrant directory is determined when you install vagrant, typically at C:\Users\XXX\fullstack\vagrant\tournament, in which XXX refers to your user acount name.

13. To setup the database, please type psql -f tournament.sql

14. Using the terminal, test the code by typing python tournament_test.py

15. You should see the following results:

vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py
1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
Success!  All tests pass!
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$


That's all, thanks!
------------------

--Ting Boo
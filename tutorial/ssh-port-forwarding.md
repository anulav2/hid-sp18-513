# SSH Port Forwarding
SSH Port forwarding (SSH tunneling) creates an encrypted secure connection
between a local computer and a remote computer through which services can be
relayed. Because the connection is encrypted, SSH tunneling is useful for  
transmitting information that uses an unencrypted protocol.

## Types of Port Forwarding
There are three types of SSH Port Forwarding :

	* Local Port Forwarding: Connections from the SSH client are forwarded via
							the SSH server, then to a destination server

	* Remote port forwarding: Connections from the SSH server are forwarded via
							the SSH client, then to a destination server

	* Dynamic port forwarding: connections from various programs are forwarded 
							via the SSH client, then via the SSH server, and 
							finally to several destination servers
              
## Prerequisites
  * Before you begin, you need to check if forwarding is allowed on the SSH server you will connect to.
  * You also need to have a SSH client on the computer you are working on. 

If you are using the OpenSSH server :  

	vi /etc/ssh/sshd_config 

and look for ## AllowTcpForwarding and change them to Yes. 

In addition, if you are going to use remote port forwarding (discussed later in this tutorial), 

you also have to set ## GatewayPorts to Yes. 

Then, you need to restart the server for the change to take effect.

## How to Restart the Server 
If you are on :

* Linux, depending upon the init system used by your distribution, run:

	  sudo systemctl restart sshd
	  sudo service sshd restart
	
 Note that depending on your distribution, you may have to change the service to ssh instead of sshd.

* Mac, you can restart the server using:

    sudo launchctl unload /System/Library/LaunchDaemons/ssh.plist
    sudo launchctl load -w /System/Library/LaunchDaemons/ssh.plist

* Windows and want to set up a SSH server, have a look at MSYS2 or Cygwin.





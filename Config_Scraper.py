from netmiko import ConnectHandler
import os
import time
import datetime

# Set the filename for the backup
backup_filename = str('Switch-Config-Backup-' + '{0:%Y-%m-%d-%H-%M-%S}'.format(datetime.datetime.now()) + '.cfg')

# Set the directory for the backup to be stored
backup_dir = str(UDF_1)

# Creates what the script will expect back from the CLI
hostname = str(UDF_2 + "#")

# Set the IP address, username, and password for the switch
switchDevice ={
            'device_type': 'cisco_ios',                                                 # Provide Switch OS
            'host': UDF_3,                                                   # Provide Switch IP
            'username': UDF_4,                                                    # Provide Switch username
            'password': UDF_5,                                            # Provide Switch password
}

# SSH to the switch and output the running config to a variable
ssh = ConnectHandler(**switchDevice)                                                    # Create a new SSH client
ssh.send_command("terminal datadump", expect_string=hostname)                          # Output show commands in one go
output_run_config = ssh.send_command("show running-config", expect_string=hostname)    # Output running config to variable
ssh.disconnect                                                                          # Close SSH session

# Open file and output switch config to the file
conf = open(backup_dir+'/'+backup_filename, 'w')                                        # Open new file
conf.write(output_run_config)                                                           # Output switch config to file
conf.close()                                                                            # Close  file

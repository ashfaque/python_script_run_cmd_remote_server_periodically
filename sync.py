import os
import sys
import time
import platform

script_dir = os.path.dirname(os.path.abspath(__file__))

current_platform = platform.system()
if current_platform == 'Linux':
    python = 'python3'
    python_bin_name = 'bin'
    cmd_to_clear_terminal = 'clear'
elif current_platform == 'Windows':
    python = 'python'
    python_bin_name = 'Scripts'
    cmd_to_clear_terminal = 'cls'
elif current_platform == 'Darwin':
    python = 'python3'
    python_bin_name = 'bin'
    cmd_to_clear_terminal = 'clear'
else:
    print('Unknown platform')
    sys.exit(1)    # 1 to exit with an error code. 0 to exit with success code.

try:
    import paramiko    # pip install paramiko
except ModuleNotFoundError as mnf:
    env_name = 'autoenv'

    # os.system(f'{python} -m venv {os.getcwd()}/{env_name}')
    # os.system(f'{os.getcwd()}/{env_name}/Scripts/python -m pip install --upgrade pip')
    # os.system(f'{os.getcwd()}/{env_name}/Scripts/python -m pip install --no-cache-dir --upgrade paramiko')
    os.system(f'{python} -m venv {script_dir}/{env_name}')
    os.system(f'{script_dir}/{env_name}/Scripts/python -m pip install --upgrade pip')
    os.system(f'{script_dir}/{env_name}/Scripts/python -m pip install --no-cache-dir --upgrade paramiko')
    os.system(f'{script_dir}/{env_name}/{python_bin_name}/{python} {os.path.abspath(__file__)}')    # Run this script again.



# Define server details
servers = [
    {
        'hostname': '192.168.0.111',
        'username': 'root',
        # 'password': 'your_password',
        'key_filename': r'E:\PATH\to\private_key\PRIVATE_KEY_FILE_NAME',
        'command': 'ls -l',
    },
    {
        'hostname': '192.168.0.111',
        'username': 'root',
        # 'password': 'your_password',
        'key_filename': r'E:\PATH\to\private_key\PRIVATE_KEY_FILE_NAME',
        'command': 'df -h',
    },
]

# Define the time interval in seconds
interval = 600    # 10 minutes
# interval = 10    # ! For Testing Purpose Only - 10 seconds

# Function to SSH into a server, run a command, and log the output
def ssh_and_run_command(server_info, log_file, loop_count):
    try:
        # Create an SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the server using the private key file
        ssh.connect(
            server_info['hostname'],
            username=server_info['username'],
            # password=server_info['password'],
            key_filename=server_info['key_filename']
        )
        
        # Run the command
        stdin, stdout, stderr = ssh.exec_command(server_info['command'])
        
        # Get the output
        output = stdout.read().decode()
        # output = stdout.read().decode('utf-8')

        # Log the output to a file
        with open(log_file, 'a') as f:
            f.write('\n' + '=' * 30 + f' {server_info["hostname"]} START - {loop_count} ' + '=' * 30 + '\n')
            f.write(f"Server: {server_info['hostname']} RAN ON:- {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(output)
            f.write('\n' + '=' * 30 + f' {server_info["hostname"]} END - {loop_count} ' + '=' * 30 + '\n')
        
        # Close the SSH connection
        ssh.close()

    except Exception as e:
        # print(f"Error connecting to {server_info['hostname']}: {e}")
        with open(log_file, 'a') as log:
                log.write('\n' + '#' * 40 + f' {server_info["hostname"]} ERROR-START - {loop_count} ' + '#' * 40 + '\n')
                log.write(f"Error connecting to {server_info['hostname']}:\n")
                log.write(str(e) + '\n')
                log.write('\n' + '#' * 40 + f' {server_info["hostname"]} ERROR-END - {loop_count} ' + '#' * 40 + '\n')

if __name__ == '__main__':
    loop_count = 1
    # Main loop
    while True:
        os.system(f'{cmd_to_clear_terminal}')
        print(f'{loop_count} - Running at {time.strftime("%Y-%m-%d %H:%M:%S")}...')
        # timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        # log_file = f"ssh_logs_{timestamp}.txt"

        # Get the current directory of the script

        # Create a log file in the script's directory
        log_file = os.path.join(script_dir, 'sync_history.log')


        for server_info in servers:
            ssh_and_run_command(server_info, log_file, loop_count)

        loop_count += 1

        # Wait for the specified interval
        time.sleep(interval)

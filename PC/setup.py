import wmi


def setup():
    """
    get pc settings
    """
    computer = wmi.WMI()
    os_info = computer.Win32_OperatingSystem()[0]    # operating system version
    proc_info = computer.Win32_Processor()[0]        # processor name
    gpu_info = computer.Win32_VideoController()[0]   # video card name

    os_name = os_info.Name.encode('utf-8').split(b'|')[0]
    os_version = ' '.join([os_info.Version, os_info.BuildNumber])
    system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB

    # conclusion preparation
    string = f"{'OS Name: {0}'.format(os_name)}\n {'OS Version: {0}'.format(os_version)}\n" \
             f" {'CPU: {0}'.format(proc_info.Name)}\n {'RAM: {0} GB'.format(system_ram)}\n " \
             f"{'Graphics Card: {0}'.format(gpu_info.Name)}"

    # save to file
    with open(r"C:\System32\x25x02x42\setup_pc.txt", "w", encoding="utf-8") as f:
        f.write(string)

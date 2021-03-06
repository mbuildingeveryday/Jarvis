import os
from plugin import plugin, require, LINUX, MACOS, WINDOWS


@require(platform=LINUX)
@plugin('shutdown')
def shutdown(jarvis, s):
    """
    Shutdown the system
    Uses:
    shutdown : asks for time
    shutdown -c : cancels shutdown
    """
    if s == '':
        s = jarvis.input('In how many minutes?: ')
    if s == '-c':
        os.system('sudo shutdown -c')
        jarvis.say('Shutdown operation cancelled')
        return
    string = 'sudo shutdown -t ' + str(s)
    os.system(string)


@require(platform=MACOS)
@plugin('shutdown')
def shutdown(jarvis, s):
    """
    Shutdown the system
    Uses:
    shutdown : asks for time
    shutdown -c : cancels shutdown
    """
    if s == '':
        s = jarvis.input('In how many minutes?: ')
    if s == '-c':
        os.system('sudo killall shutdown')
        jarvis.say('Shutdown operation cancelled')
        return
    string = 'sudo shutdown -h +' + str(s)
    os.system(string)


@require(platform=WINDOWS)
@plugin('shutdown')
def shutdown(jarvis, s):
    """
    Shutdown the system
    Uses:
    shutdown : asks for time
    shutdown -c : cancels shutdown
    """
    if s == '':
        s = jarvis.input('In how many seconds?: ')
    if s == '-c':
        os.system('shutdown /a')
        jarvis.say('Shutdown operation cancelled')
        return
    string = 'sudo shutdown /s /t ' + str(s)
    os.system(string)


@require(platform=LINUX)
@plugin('reboot')
def reboot(jarvis, s):
    """Reboot the system"""
    if s == '':
        s = jarvis.input('In how many minutes?: ')
    string = 'sudo shutdown -r -t ' + str(s)
    os.system(string)


@require(platform=MACOS)
@plugin('reboot')
def reboot(jarvis, s):
    """Reboot the system"""
    string = 'sudo shutdown -r now'
    os.system(string)


@require(platform=WINDOWS)
@plugin('reboot')
def reboot(jarvis, s):
    """Reboot the system"""
    if s == '':
        s = jarvis.input('In how many seconds?: ')
    string = 'shutdown /r /t ' + str(s)
    os.system(string)


@require(platform=WINDOWS)
@plugin('hibernate')
def reboot(jarvis, s):
    """Hibernates the system"""
    string = 'shutdown /h'
    os.system(string)


@require(platform=WINDOWS)
@plugin('log off')
def reboot(jarvis, s):
    """Log off the system"""
    string = 'shutdown /l'
    os.system(string)


@require(platform=WINDOWS)
@plugin('hybridsleep')
def reboot(jarvis, s):
    """Performs shutdown and prepares forfast startup"""
    string = 'shutdown /hybrid'
    os.system(string)


@require(native="systemctl", platform=LINUX)
@plugin('suspend')
def suspend(jarvis, s):
    """
    Suspend (to RAM) - also known as Stand By or Sleep mode.

    Operate PC on a minimum to save power but quickly wake up.
    """
    os.system('sudo systemctl suspend')


@require(native="systemctl", platform=LINUX)
@plugin('hibernate')
def hibernate(jarvis, s):
    """
    Hibernate - also known as "Suspend to Disk"

    Saves everything running to disk and performs shutdown.
    Next reboot computer will restore everything - including
    Programs and open files like the shutdown never happened.
    """
    os.system('sudo systemctl hibernate')


@require(native="systemctl", platform=LINUX)
@plugin('hybridsleep')
def hybridsleep(jarvis, s):
    """
    Hybrid sleep.
    Will quickly wake up but also survive power cut.
    Performs both suspend AND hibernate.
    Will quickly wake up but also survive power cut.
    """
    os.system("sudo systemctl hybrid-sleep")

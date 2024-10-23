# Widnows Forensics

## Windows Registry and Forensics

### Windows Registry

The Windows Registry is a hierarchical database that stores low-level settings for the Microsoft Windows operating system and for applications that opt to use the registry. The kernel, device drivers, services, Security Accounts Manager, and user interface can all use the registry. The registry also allows access to counters for profiling system performance.

The registry contains two basic elements: keys and values. Keys are containers that can contain values or further keys. Keys are referenced with a syntax similar to Windows' path names, using backslashes to indicate levels of hierarchy. For example, HKEY_LOCAL_MACHINE\Software\Microsoft\Windows refers to a subkey "Windows" of a subkey "Microsoft" of a subkey "Software" of the HKEY_LOCAL_MACHINE root key. Values are a set of data that is associated with a key. Each key in the registry has an associated ACL that determines which users can read or write it.

### Structure of the Registry

The registry on any Windows system contains the following five root keys:

1. HKEY_CURRENT_USER
2. HKEY_USERS
3. HKEY_LOCAL_MACHINE
4. HKEY_CLASSES_ROOT
5. HKEY_CURRENT_CONFIG

### Predefined Keys in the Windows Registry

| Folder/Predefined Key | Description | 
|-----------------------|-------------|
| **HKEY_CURRENT_USER** | Contains the root of the configuration information for the user who is currently logged on. The user's folders, screen colors, and Control Panel settings are stored here. This information is associated with the user's profile. This key is sometimes abbreviated as HKCU. |d|
| **HKEY_USERS** | Contains all the actively loaded user profiles on the computer. HKEY_CURRENT_USER is a subkey of HKEY_USERS. HKEY_USERS is sometimes abbreviated as HKU. |
| **HKEY_LOCAL_MACHINE** | Contains configuration information particular to the computer (for any user). This key is sometimes abbreviated as HKLM. |
| **HKEY_CLASSES_ROOT** | Is a subkey of `HKEY_LOCAL_MACHINE\Software`. The information that is stored here makes sure that the correct program opens when you open a file by using Windows Explorer. This key is sometimes abbreviated as HKCR. Starting with Windows 2000, this information is stored under both the HKEY_LOCAL_MACHINE and HKEY_CURRENT_USER keys. The `HKEY_LOCAL_MACHINE\Software\Classes` key contains default settings that can apply to all users on the local computer. The H`KEY_CURRENT_USER\Software\Classes` key has settings that override the default settings and apply only to the interactive user. The HKEY_CLASSES_ROOT key provides a view of the registry that merges the information from these two sources. HKEY_CLASSES_ROOT also provides this merged view for programs that are designed for earlier versions of Windows. To change the settings for the interactive user, changes must be made under `HKEY_CURRENT_USER\Software\Classes` instead of under HKEY_CLASSES_ROOT. To change the default settings, changes must be made under `HKEY_LOCAL_MACHINE\Software\Classes`. If you write keys to a key under HKEY_CLASSES_ROOT, the system stores the information under `HKEY_LOCAL_MACHINE\Software\Classes`. If you write values to a key under HKEY_CLASSES_ROOT, and the key already exists under `HKEY_CURRENT_USER\Software\Classes`, the system will store the information there instead of under `HKEY_LOCAL_MACHINE\Software\Classes`. |
| **HKEY_CURRENT_CONFIG** | Contains information about the hardware profile that is used by the local computer at system startup. |


### Why is it important in Forensics and Incident Response?

The Windows Registry is a treasure trove of information for forensic investigators. It contains information about the operating system, installed software, user activity, and much more. 
list of things that can be found in the registry:

1. User accounts
2. User activity
3. Network information
4. Installed software
5. USB devices
6. Last shutdown time
7. Last boot time
8. User logon/logoff times
9. Usernames and passwords
10. Wireless networks
11. Printers
12. File extensions
13. File associations
14. Recent documents


### Accessing registry hives offline

if you only have access to a disk image, you must know where the registry hives are located on the disk. The majority of these hives are located in the `C:\Windows\System32\Config` directory and are:

1. `Default` (mounted on `HKEY_USERS\DEFAULT`)
2. `SAM` (mounted on `HKEY_LOCAL_MACHINE\SAM`)
3. `SECURITY` (mounted on `HKEY_LOCAL_MACHINE\SECURITY`)
4. `SOFTWARE` (mounted on `HKEY_LOCAL_MACHINE\SOFTWARE`)
5. `SYSTEM` (mounted on `HKEY_LOCAL_MACHINE\SYSTEM`)

Additionally, 2 other hives are located in the user's profile `C:\Users\<username>\` directory:

1. `NTUSER.DAT` (mounted on HKEY_CURRENT_USER when a user logs in)
2. `USRCLASS.DAT` (mounted on HKEY_CURRENT_USER\Software\CLASSES)


The USRCLASS.DAT hive is located in the directory `C:\Users\<username>\AppData\Local\Microsoft\Windows`.

#### The Amcache Hive:

Apart from these files, there is another very important hive called the AmCache hive. This hive is located in `C:\Windows\AppCompat\Programs\Amcache.hve`. Windows creates this hive to save information on programs that were recently run on the system.

### Transaction Logs and Backups:

The registry hives are backed up in the `C:\Windows\System32\Config\RegBack` directory. These backups are created every time the system boots up. The files in this directory are:

1. `DEFAULT`
2. `SAM`
3. `SECURITY`
4. `SOFTWARE`
5. `SYSTEM`

### Tools for analyzing the registry:

1. **Regedit**: The built-in registry editor in Windows.
2. **Reg**: A command-line tool for managing the registry.
3. **Kape**: A tool for capturing and analyzing registry hives.
4. **FTK Imager**: A tool for capturing and analyzing registry hives.
5.  **FTK Registry Viewer**: A tool for analyzing registry hives.
6. **RegRipper**: A tool for extracting information from registry hives.


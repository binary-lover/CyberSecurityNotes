<h1  align = center>Nmap Notes<img style = "border-radius: 5%" align = center src = "https://cdn.shortpixel.ai/spai/q_lossless+ret_img+to_webp/www.stationx.net/wp-content/uploads/2022/12/Nmap-Cheat-Sheet-2.jpg">
</h1> 


1. **-sN** run host discovery to save time, it runs by defalut

2. **Host discovery** 
    - If you are a Root user (if any of below returns True it means the host is active)
        - Sends ICMP echo packet
        - TCP syn - 443
        - TCP Acknoledgement - 80
        - ICMP Time stamp requast    
    - if you are local user 
        - TCP syn - 443
        - TCP Acknoledgement - 80
###
3. **Targate**
    1. **IP Scan**
        ```
        sudo nmap 192.168.1.1               #Single IP 
        sudo nmap 192.168.1.0/24            #Subnet Range
        sudo nmap 192.168.1.0-255           #IP Range
        sudo nmap 192.168.1.1 192.168.1.2   #Specific IP
        sudo nmap -iL Host.txt              #Scan IP from txt file
        sudo nmap scanme.nmap.org           #Scan a Domain Name        
        ``` 
        **Note :** here we are not specifieng the targate port and thus nmap by default scan most common (1-1000) ports.


    2. **Port Scan / enumeration**
        
        ```
        sudo nmap 192.168.1.1 -p80           #Single port
        sudo nmap 192.168.1.1 -p80-450       #port range
        sudo nmap 192.168.1.1 -p22,80,145    #Distributed Ports
        sudo nmap 192.168.1.1 -p http        #Service Specific
        sudo nmap 192.168.1.1 -p T:22,U:53   #Protocol Specific
        sudo nmap 192.168.1.1 -p-            #All Ports
        sudo nmap 192.168.1.1 --top-ports 10 #It scan top 10 ports
        sudo nmap -p 21 --script=ftp* 192.168.1.13    #it will check the port is vurlnarable by using scripts reated to ftp

        ```
4. **Scan Techeniques :**
    1. TCP connect scan "-sT"
    2. TCP SYN scan "-sS"
    3. FIN scan "-sF"
    4. Xmas scan "-sX"
    5. Null scan "-sN"
    6. Ping scan "-sP"
    7. UDP scan "-sU"
    8. ACK scan "-sA"
    9. Virsion detection "-sV"
    1. OS detection "-O"
    1. verbosity     "-v"
    1. services + OS + Tracker = "-A"
    <p>for Example :</p>

    ```
    sudo nmap 192.168.1.1 -sS   #Syn scan
    sudo nmap 192.168.1.1 -sU   #UDP scan
    sudo nmap 192.168.1.1 -sA   #Ack scan
    sudo nmap 192.168.1.1 -sV   #it tells versions of services
    ```
5. **Scan Status**
    1. **Open :** - when host machine sent SYN packet and reciev SYN+ACK from test machine.
    2. **Closed :** - when host machine sent SYN package and reciev RST+ACK from test machine.
    3. **Filtered :** - when host machine sent SYN packet but do not get responce, may be due to firewall or package filter machanism.
    4. **Unfiltered :** - when host machine sent SYN packet but do not get onough response to identify weather it is open or closed. it may send dome incompete ICMP file with many errors.
    5. **Open|Filtered :** when host machine sent empty packet (-sN through null scan) and it reach to the test machine but host do not get any response
    6. **Closed|Filtered :**

6. **Scan Timing**

    |                                   | T0          | T1          | T2          | T3          | T4          | T5          |
    |-----------------------------------|-------------|-------------|-------------|-------------|-------------|-------------|
    | **Name**                          | Paranoid    | Sneaky      | Polite      | Normal      | Aggressive  | Insane      |
    | `min-rtt-timeout`                 | 100 ms      | 100 ms      | 100 ms      | 100 ms      | 100 ms      | 50 ms       |
    | `max-rtt-timeout`                 | 5 minutes   | 15 seconds  | 10 seconds  | 10 seconds  | 1250 ms     | 300 ms      |
    | `initial-rtt-timeout`             | 5 minutes   | 15 seconds  | 1 second    | 1 second    | 500 ms      | 250 ms      |
    | `max-retries`                     | 10          | 10          | 10          | 10          | 6           | 2           |
    | Initial (and minimum) scan delay (`--scan-delay`) | 5 minutes | 15 seconds | 400 ms      | 0           | 0           | 0           |
    | Maximum TCP scan delay            | 5 minutes   | 15,000      | 1 second    | 1 second    | 10 ms       | 5 ms        |
    | Maximum UDP scan delay            | 5 minutes   | 15 seconds  | 1 second    | 1 second    | 1 second    | 1 second    |
    | `host-timeout`                    | 0           | 0           | 0           | 0           | 0           | 15 minutes  |
    | `script-timeout`                  | 0           | 0           | 0           | 0           | 0           | 10 minutes  |
    | `min-parallelism`                 | Dynamic     | Dynamic     | Dynamic     | Dynamic     | Dynamic     | Dynamic     |
    | `max-parallelism`                 | 1           | 1           | 1           | Dynamic     | Dynamic     | Dynamic     |
    | `min-hostgroup`                   | Dynamic     | Dynamic     | Dynamic     | Dynamic     | Dynamic     | Dynamic     |
    | `max-hostgroup`                   | Dynamic     | Dynamic     | Dynamic     | Dynamic     | Dynamic     | Dynamic     |
    | `min-rate`                        | No minimum  | No minimum  | No minimum  | No minimum  | No minimum  | No minimum  |
    | `max-rate`                        | No maximum  | No maximum  | No maximum  | No maximum  | No maximum  | No maximum  |
    | `defeat-rst-ratelimit`            | Not enabled | Not enabled | Not enabled | Not enabled | Not enabled | Not enabled |

###
7. **Output Types :**

    ~~~
    sudo nmap scanme.nmap.org -oN       # Normal Text output
    sudo nmap scanme.nmap.org -oX       # XML Format
    sudo nmap scanme.nmap.org -oG       # Grapable Format
    sudo nmap scanme.nmap.org -oS       # Script Kiddie Format eg. Service -> 5eRv1c3     
    ~~~

###
8. **NSE :** - Nmap Scripting Engine (NSE), it helps in Firewall bypass, FTP enum, DNS enum, HTTP enum and many more.

    ~~~
    sudo nmap scanme.nmap.org --script http-headers     # brought response header of given ip/domain
    ls /usr/share/nmap/scripts | grep -e ftp    #it list all scripts related to ftp so you can perform on your need
    sudo nmap -p21 --script=ftp* 192.168.1.156       # it will perform all enum related to ftp
    #Output:
        ftp-anon.nse
        ftp-bounce.nse
        ftp-brute.nse
        ftp-libopie.nse
        ftp-proftpd-backdoor.nse
        ftp-syst.nse
        ftp-vsftpd-backdoor.nse
        ftp-vuln-cve2010-4221.nse
        tftp-enum.nse
        tftp-version.nse

    ~~~

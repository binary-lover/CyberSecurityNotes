
# Threat Intelligence

### Cryptographic Attacks

#### **Birthday Attack :**

- In a classroom of 23 students, there is a 50% chance that two students will have the same birthday.
  - For a class of 30 students, the probability increases to 70%.
- In digital world this is a hash collision.
  - Hash collision is when two different inputs produce the same output in a hash function.
  - Find through [bruet force]("/README.md/##Threat-Intelligence") attack.
- The Attacker will muliple inputs and hash them to find a collision.
  - Protect yourself with a larger hash size.
- MD5 hash

  - Message Digest Algorithm 5
  - First published in 1992
  - Collisions found in 1996

- **How to protect yourself from hash collision attacks?**
  To protect yourself from hash collision attacks, you should use a hash function that has a large output size. This makes it more difficult for an attacker to find a collision. You should also use a hash function that is resistant to collision attacks, such as SHA-256 or SHA-3.

#### **Rainbow Table Attack :**

- A rainbow table is a precomputed table for reversing cryptographic hash functions, usually for cracking password hashes.
- | Hash                             | Password |
  | -------------------------------- | -------- |
  | 5f4dcc3b5aa765d61d8327deb882cf99 | password |
  | 098f6bcd4621d373cade4e832627b4f6 | test     |
  | 25d55ad283aa400af464c76d713c07ad | 123456   |

  this is how a rainbow table looks like.

- **How to protect yourself from rainbow table attacks?**
  To protect yourself from rainbow table attacks, you should use a strong password hashing algorithm that includes a salt. A salt is a random value that is added to the password before it is hashed. This makes it more difficult for an attacker to use a rainbow table to crack the password.

#### **Online vs Offline Attacks :**

- **Online Attack :** Is against a live logon prompt.(live logon prompt: when you are trying to log in to a system)
- **Offline Attack :** The attacker working on their own independent computers to compromise a password hash.

- **How collision can make a hash function vulnerable?**
  if hash collision occurers, it means that two different inputs produce the same output in a hash function. This can be used by an attacker to create a malicious file that has the same hash as a legitimate file. This is known as a collision attack.

#### **Downgrade Attack :**

- A downgrade attack is a type of attack where an attacker forces a system to use an older, less secure version of a protocol or encryption algorithm. This can make it easier for the attacker to exploit vulnerabilities in the older version of the protocol or algorithm.

- **SSL Stripping :**

  - Combines an on-path attack with a downgrade attack.
  - Difficult to impliment but big returns for the attacker.
  - Attacker must sit between middle of the conversation.
  - Victim's browser page isn't encrypted.
  - Strip the `S` from `HTTPS` and the attacker can see the data.

- **How to protect yourself from downgrade attacks?**
  To protect yourself from downgrade attacks, you should always use the latest, most secure versions of protocols and encryption algorithms. You should also ensure that your systems are configured to reject connections that use older, less secure versions of protocols.

### impact of vulnerabilities

#### 1. Race condition:

- The behavior of software, electronic, oranother system's output is dependent on the timing, sequence of events, or a factor out of the user's control.

### Security checks

#### **Firewall**
- A network security system that monitors and controls incoming and outgoing network taraffic based on predetermined security rules.

  1. **ACL** (Access control lists): to contro incoming/outgoing traffic
     - Application-based: Protect the user from applications and serivices by monitoring and potentially blocking the input, output.
     - Network-based: filtering traffic based on firewall rules and allows only authorized traffic to pass in and out of the network.

- **Statefull vs Stateless**
  - Statefull: Stateful firewalls block traffic based on the state of th epacket within a session. It adds and maintains info about a user's connections in a state table,(connection table)
  - Stateless: use ACL to identify allowed add/or blok traffic through filtering

<br>

# Tech & Tools Install & Network Config components

### VPN connector:

A type of router device that allowes for the secure creation of VPN connections and for the safe delivery of messages between VPN nodes. Allows for the handling of a large quantity of VPN tunnels.

<!-- <a id="remote-acess"></a>

[click](#remote-acess) -->

- **Remote Acess :** A user-to-LAN connection used by romote users.

- **Site-to-Site :** Allows multiple sites to connect to remote sites over the internet.

#### **IPSec**:
A protocol suite for securing Internet Protocol(IP) communications. Encrypts and authenticates all of the packets in a session etween hosts or networks. Secures more applications then SSL and TLS.

#### **Tunnel mode :** The default mode for IPSec, the entire pack is protected.
  - Detail analysis of packets in Tunnel mode:
    - **Header:** The original IP header is encrypted and encapsulated in a new IP header. the new IP header contains the Destination IP address of the remote VPN gateway, when the packet reaches the remote VPN gateway, the new IP header is removed and the original IP header is restored. and sent to the real destination.
  
#### **Transport mode :** use to end-to-end communications in IPSec. Ex. encrypted Telnet or Remote Desktop session from a workstation to a server.
  - Detail analysis of packets in Transport mode:
    - **Header:** The original IP header is not encrypted, only the data portion of the packet is encrypted. The new IP header is not created, the original IP header is used to route the packet to the destination.

#### **Authenication Header (AH) :** 
- Provides connectionless integrity and data origin authentication for IP datagrams and provides protection against replay attacks.

- **what is replay attack?**
    - A replay attack is a form of network attack in which a valid data transmission is maliciously or fraudulently repeated or delayed. This is carried out either by the originator or by an adversary who intercepts the data and re-transmits it.
- **How AH protects against replay attacks?**
    - AH provides protection against replay attacks by including a sequence number in the AH header. This sequence number is used to ensure that each packet is unique and has not been replayed. If a packet with the same sequence number is received, it is discarded as a replayed packet.
- **But what if the adversary changes the sequence number?**
    - AH also includes a field called the Authentication Data field, which contains a hash of the packet data and the AH header. This hash is calculated using a secret key known only to the sender and receiver. If the sequence number is changed, the hash will not match, and the packet will be discarded.

#### **Encapsulating Security Payload (ESP) :**
- Provides confidentiality, data origin authentication, connectionless integrity, anit-replay, and limited traffic flow confidentiality.

- **Split tunnel vs Full tunnel :**
  - **Split tunnel:** Only the traffic destined for the corporate network is sent through the VPN tunnel. All other traffic is sent through the user's local internet connection.
  - **Full tunnel:** All traffic from the user's device is sent through the VPN tunnel, regardless of its destination.

- **Which tunnel is benifitial in which scenario?**
  - **Split tunnel:** 
    - is beneficial when the user needs to access both corporate resources and local internet resources simultaneously. It reduces the load on the corporate network and provides faster internet access for non-corporate traffic.
  - **Full tunnel:** is beneficial when the user needs to access only corporate resources and does not require access to local internet resources. It ensures that all traffic is encrypted and secure, even when accessing non-corporate resources.

#### **Transport Layer Security (TLS) :**
- A cryptographic protocol that provides secure communication over a computer network. It is widely used to secure web traffic and is the successor to SSL.
- Uses certificates issued by a Certificate Authority (CA) to authenticate the server and establish a secure connection.

### **NIPS/NIDS (Network Intrusion Prevention System)(Network Intrusion Detection System) :**
- **NIDS:** Monitors network traffic for suspicious activity and alerts the network administrator when potential threats are detected.
- **NIPS:** Monitors network traffic for suspicious activity and takes action to prevent potential threats from reaching their targets.

- **Signature-based :**
  - Signature-based detection uses predefined signatures to identify known threats. These signatures are based on patterns or characteristics of known attacks.
- **Heuristi/behavioral :**
  - Heuristic or behavioral detection uses algorithms to identify suspicious behavior that may indicate an attack. This approach is more proactive than signature-based detection and can detect previously unknown threats.
- **Anomaly-based :**
  - Anomaly-based detection uses baselines of normal network behavior to identify deviations that may indicate an attack. This approach is effective at detecting new and unknown threats but can also generate false positives.

- **Inline vs Passive :**
  - **Inline:** An inline NIPS/NIDS sits directly in the network traffic path and can actively block or modify traffic in real-time.
  - **Passive:** A passive NIPS/NIDS monitors network traffic without actively blocking or modifying traffic. It is typically used for monitoring and analysis purposes. Connected through a switch port mirroring or network tap.

  - **In-vand vs out-of-band :**
    - **In-band:** In-band NIPS/NIDS is deployed directly in the network traffic path and can monitor and analyze traffic in real-time.
    - **Out-of-band:** Out-of-band NIPS/NIDS is deployed outside the network traffic path and can monitor and analyze traffic offline. It is typically used for post-event analysis and forensics.

### SIEM (Security Information and Event Management) :

  - stands for Security Information and Event Management. It is a comprehensive approach to cybersecurity that involves the integration of security information management (SIM) and security event management (SEM) functions into a single security management system.

- **Some key features of SIEM include:**
  - **Log Management:** SIEM systems collect, aggregate, and store log data from a wide range of sources, including security devices, servers, and applications.
  - **Real-Time Monitoring:** SIEM systems provide real-time monitoring of security events, allowing security teams to detect and respond to threats as they occur.
  - **Threat Detection:** SIEM systems use advanced analytics and machine learning to detect and respond to security threats.
  - **Incident Response:** SIEM systems provide incident response capabilities, allowing security teams to investigate and respond to security incidents.
  - **Time Syncronization:** Ensures that all devices on the network are using the same time source, which is critical for accurate log correlation and analysis.


## software tools to assess the security posture of an organization

### **Protocol Analyzer :**
- A protocol analyzer is a tool that captures, analyzes, and decodes network traffic to help troubleshoot network issues, monitor network performance, and detect security threats.
- Ex: `Wireshark`, `tcpdump`, `Microsoft Network Monitor`.

#### **Tcpdump :**
  - A command-line packet analyzer that captures and displays network packets. It can be used to analyze network traffic, troubleshoot network issues, and detect security threats.

#### **Wireshark :**
  - A graphical packet analyzer that captures and displays network packets. It provides detailed information about network traffic, including packet contents, protocols used, and source/destination addresses.

### **Wireless scanner/crackers :**

#### **Wireless scanner :**
- A wireless scanner is a tool that scans for wireless networks in the vicinity and provides information about the networks, such as SSID, signal strength, encryption type, and security settings.
- ex: `NetStumbler`, `inSSIDer`, `Kismet`.

#### **Wireless cracker :**

- A wireless cracker is a tool that attempts to crack the encryption key of a wireless network to gain unauthorized access. It can use various techniques, such as brute force attacks, dictionary attacks, and rainbow table attacks.
- ex: `Aircrack-ng`, `Reaver`, `Fern Wifi Cracker`.
  - 1. **WEP** (Wired Equivalent Privacy) - WEP is an outdated wireless security protocol that is vulnerable to cryptographic attacks. It is no longer considered secure and should not be used to protect wireless networks.
  - 2. **WPA** (Wi-Fi Protected Access) - WPA is a wireless security protocol that provides stronger encryption and security features than WEP. It is recommended for securing wireless networks. only crackable with a dictionary attack, or a rainbow table attacks.
    - Encyption used here is TKIP (Temporal Key Integrity Protocol)


### **Stegnography tools :**

- Steganography tools are used to hide secret messages or data within other files, such as images, audio files, or text files. The hidden data is embedded in the cover file in a way that is not easily detectable.

- **Ex:** `Steghide`, `OpenStego`, `OutGuess`.

### **Banner Grabbing :**

- Banner grabbing is the process of collecting information about a target system, such as the operating system, services, and version numbers, by analyzing the banners or headers returned by the target system.

- **Ex:** `Netcat`, `Telnet`, `Nmap`.

### **command line tools :**

#### **Netstat (network stats) :**

```bash
netstat -a // Displays all active connections and the listening ports on the system. 
netstat -b // Displays the executable files associated with each connection.
netstat -n // Displays active connections without resolving hostnames.
```
#### **tracert (Windows)/traceroute (MacOS/Linux) :**
  - Uses the [ICMP](/README.md/#icmp) protocol to trace the route, time to live (TTL) of packets to a destination host.

```bash
tracert google.com // Traces the route
```
#### **nslookup :**
  - A command-line tool that queries DNS servers to obtain domain name or IP address information.

```bash
nslookup google.com // Resolves the IP address of the domain name.
```

#### **netcat :**
  - A versatile networking utility that can be used for port scanning, banner grabbing, file transfer, and other network-related tasks.

```bash
nc -v google.com 80 // Connects to the specified port on the target host.
```

#### **Nmap :**
  - A powerful network scanning tool that can be used to discover hosts, services, and vulnerabilities on a network.

```bash
nmap -sS google.com // Performs a SYN scan on the target host.
nmap -sV google.com // Determines the version of services running on the target host.
```

## troubleshooting common security issues

### **Unencrypted Credentials/clear text :**
  - All authentication must be encrypted. Unencrypted credentials can allow for attacker to: 
    - Steal credentials
    - Impersonate users
    - Gain unauthorized access to systems and data.
    - move to other networks.
    - maintain persistence.

### **Logs and event anomalies :**
  - block all outside access until the issue is resolved, backup the logs and ristrict access to more sensitive data till the issue is resolved.

### **Data exfiltration :**
  - Data exfiltration is the unauthorized transfer of data from a computer or network. It can be done through various methods, such as email, file transfer, or remote access tools.
  - To prevent data exfiltration, organizations should implement data loss prevention (DLP) solutions, monitor network traffic for suspicious activity, and restrict access to sensitive data.

### **Baseline deviation :**
  - Baseline deviation is when the normal behavior of a system or network changes significantly. This can be an indication of a security incident, such as a malware infection or unauthorized access.
  - for example, a sudden increase in network traffic or a spike in CPU usage may indicate a security incident.
  - To troubleshoot baseline deviation, organizations should monitor system and network performance, analyze logs and events for anomalies, and investigate any deviations from the baseline.


## Analyze and interpret output from security technologies

### **HIDS/HIPS :**
#### **HIDS:** Host-based Intrusion Detection System 
- Runs on a single computer and alerts of potential threats to help warn of attacks against the host.
#### **HIPS:** Host-based Intrusion Prevention System
- Runs on a single computer and intercepts potential threats to help prevent attacks against the host.

- **How to analyze and interpret output from HIDS/HIPS?**
  - Analyze logs and alerts generated by the HIDS/HIPS to identify potential security incidents.
  - Investigate any alerts or anomalies detected by the HIDS/HIPS to determine the cause and severity of the incident.
  - Take appropriate action to respond to security incidents, such as blocking malicious traffic, isolating compromised systems, and remediating vulnerabilities.

### **Antivirus :**
  - Antivirus software is designed to detect, prevent, and remove malware from a computer or network. It scans files and programs for known malware signatures and behavior patterns to protect against threats.

### **File integrity checkers :**
  - File integrity checkers are tools that monitor and verify the integrity of files on a system. They compare the current state of files against a known baseline to detect unauthorized changes or modifications.

  - **Can it be achive by git?**
    - Yes, git can be used as a file integrity checker by tracking changes to files and verifying their integrity using cryptographic hashes.
  
### **Host-based firewalls :**
  - Host-based firewalls are software firewalls that run on individual computers to monitor and control incoming and outgoing network traffic. They provide an additional layer of security by filtering traffic based on predefined rules.

### **Application whitelisting/blacklisting :**
  - Application whitelisting is a security measure that allows only approved applications to run on a system, while blacklisting blocks known malicious applications. This helps prevent unauthorized software from executing and reduces the risk of malware infections.

### **Removable media control :**
  - Removable media control is a security measure that restricts the use of external storage devices, such as USB drives and external hard drives, to prevent data exfiltration and malware infections.
  - It can achive by using Group Policy in Windows or third-party endpoint security solutions.
  - Also By bloking the USB ports in the BIOS.

### **Advanced malware tools :**
  - Advanced malware tools use advanced detection techniques, such as machine learning, behavioral analysis, and sandboxing, to detect and prevent sophisticated malware threats.
  - Ex: `CrowdStrike Falcon`, `FireEye`, `Cylance`.


### **Patch management tools :**
  - Patch management tools are used to manage and deploy software updates, patches, and security fixes to systems and applications. They help ensure that systems are up-to-date and protected against known vulnerabilities.
  - Ex: `WSUS`, `SCCM`, `Ivanti Patch`, `SolarWinds Patch Manager`.
  
### **UTM (Unified Threat Management) :**
  - UTM is a comprehensive security solution that combines multiple security features, such as firewall, antivirus, intrusion detection/prevention, VPN, and content filtering, into a single platform. It provides centralized security management and monitoring for networks.
  - Ex: `Fortinet FortiGate`, `Sophos UTM`, `WatchGuard Firebox`.

### **DLP (Data Loss Prevention) :**
  - DLP is a security solution that helps prevent the unauthorized transfer of sensitive data outside the organization. It monitors and controls data in motion, at rest, and in use to prevent data exfiltration and ensure compliance with data protection regulations.
  - Ex: `Symantec DLP`, `McAfee DLP`, `Digital Guardian`.

### **DEP (Data Execution Prevention) :**
  - Memory regions are marked as non-executable to protect against buffer overflow and other memory-based attacks.
  - DEP is a security feature that helps prevent malicious code from executing in memory. It marks certain memory regions as non-executable to protect against buffer overflow and other memory-based attacks.
  - DEP can be enabled in Windows through the Data Execution Prevention tab in System Properties.

### **Web application firewall :**
  - A firewall that looks monitors and filters packets carrying HTTP traffic using a set of communication rules.
  - Ex: `ModSecurity`, `Imperva SecureSphere`, `Barracuda WAF`.

## deploy mobile devices securely

### **Connection methods :**

#### **SATCOM (Satellite Communication) :**
- Satellite communication is a method of communication that uses satellites to transmit data between devices. It is commonly used for long-distance communication in remote areas where traditional communication methods are not available.
- **Poential security risks:**
  - Eavesdropping: Satellite signals can be intercepted by unauthorized parties, leading to data theft or espionage.
  - Jamming: Satellite signals can be disrupted or jammed by malicious actors, causing communication failures.
  - Spoofing: Satellite signals can be spoofed or manipulated to deceive users or gain unauthorized access to systems.
  - SATCOM devices are at risk of leaking geopositional data and remote code execution, are not easily updated remotely.

#### **ANT :**
- wireless sensor protocol that uses a 2.4 GHz ISM(Industrial, Scientific, and Medical) band to communicate. used in heart rate monitors, fitness trackers, and other wearable devices.
- **Poential security risks:**
  - `Eavesdropping`: ANT signals can be intercepted by unauthorized parties, leading to data theft or privacy violations.
  - `Spoofing`: ANT signals can be spoofed or manipulated to deceive users or gain unauthorized access to devices.
  - [`Replay attack`](/README.md/#replay-attack)s: Attackers can capture and replay ANT signals to impersonate legitimate devices or users.
  - [`Denial of Service (DoS)`](/README.md/#malware): Attackers can flood ANT devices with excessive traffic to disrupt communication or cause malfunctions.
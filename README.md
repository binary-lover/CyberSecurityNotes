
<h1 align = center> Keywords </h1>

<img align = "center" src = "https://assets-global.website-files.com/5b6df8bb681f89c158b48f6b/5ce426d9a4a48f75aee6f062_what-is-a-computer-network-p-800.jpeg">

###

1. **Hybric cloud** 

    - AWS constitute bridge between your on-premise invironment and AWS.
    - Part of your infrastructure is on the cloud
###
2. **AWS IAM (Identity and Access Management)** 
    - In Amazon Web Services (AWS), **IAM** (Identity and Access Management) is a web service that enables you to securely control access to AWS resources for your users. IAM allows you to manage users, groups, roles, and their corresponding level of permissions, ensuring that only authorized individuals or systems have access to specific AWS resources. This enhances the security of your cloud environment.
###

3. **Hybrid Clouds**
    - computing environment that combines elements of both private and public clouds, allowing data and applications to be shared between them.
    - In a hybrid cloud setup, some resources are managed in-house, within an organization's private cloud infrastructure, while others are hosted externally in a public cloud.
### 
4. **API**
    - Application Programming Interface. It is a set of rules and protocols that allows different software applications to communicate with each other.
###
5. **ARPANET**
    - The U.S. Advanced Research Projects Agency Network (ARPANET) was the first public packet-switched computer network. 
    - It was first used in 1969 and finally decommissioned in 1989. ARPANET's main use was for academic and research purposes.
###
6. **VPC** 
    - virtual private cloud which works like a private network to isolate the resources within it
###
7. **Subnet**
    - Subnet is defined set of netword IP address that are use to increase the seurity network and efficiency of network communication
    - ex: 10.0.0.0/24, 10.0.0.0/16
    - It has two parts 
        - **Public subnet :**
            - apps or services avalable for public
        - **Private subnet :**
            - things which is ment to be private
###
8. **NAT Gateway**
    - Network Address Translator(NAT) service  you can use this to an instance of private subnet can connect to service outside the VPC but external service cann't initiate connection with VPC
###
9. **NACL**
    - Networ Acess Control List (NACL) Virtual Firewall that protects the subnet.
###
10. **CISC & RISC**
    - CISC (Complex Instruction Set Computer) and RISC (Reduced Instruction Set Computer) are two types of CPU design. 
    - **Here are some differences:**
        - **CISC** uses a large set of complex machine language instructions, while **RISC** uses a reduced set of simpler instructions.
        - **Instructions:** RISC uses simple instructions that take one cycle, while CISC uses complex instructions that take multiple cycles.
        - **Focus:** RISC focuses on software, while CISC focuses on hardware.
        - **Instruction format:** RISC has a fixed instruction format, while CISC has a variable instruction format.
        - **Addressing modes:** RISC has fewer addressing modes, while CISC has a variety of different instructions that can be used for complex operations.
        - **Pipeline:** RISC uses simple pipelines, while CISC uses difficult pipelines.
###
11. **Kernel**
    - An operating system component which forms an interface between computer hardware and processes running on it.
        - Kernel Space: Memory space to run kernel      
        - User Space: Memory space to run user processes
        - Kernel programming languages: C, C++, RUST
###
12. **ISA(Instruction Set Architecture) :** Defines how CPU is controlled by a software

13. **Cloud :**  Shareable server over the interne
    - Private, Publi cloud
    - Eg: AWS, Microsoft Azure, GCP(Google cloud platform)
14. **Bare Metal :** Fresh server without an OS/applications.
15. **Hypervisor :** A software which creates virtual machines
    - Type 1: Directly installed on bare metal
        - Eg: KVM(Kernel-based virtual machine)
    - Type 2: Installed over a host OS
        - Eg: VMware(closed source), Virtual Box(open source)
###
16. **Virtual Machine :** A virtual machine (VM) is a digital version of a physical computer. It's a computer file, typically called an image, that behaves like an actual computer. VMs can be implemented using specialized hardware, software, or a combination of the two. 
    - Examples of VMs include:
        - VMware Workstation
        - Oracle VirtualBox
        - Oracle Secure Global Desktop
###
17. **oVirt :** oVert is a free, open souse virtualization management platform. It was founded by Red Hat as community project on which Red Hat Virtualization is based. For managing the virtual machine.
###
18. **Plugin :** 
    - A plugin is a software compnent that adds specific functionality to an existing computer program or web browser.
    - Plugins are designed to extend the capabilities of the host application without requiring any changes to its core code.
    - Eg. Adobe Flash Player, Java vm, QuickTheme etc.
###
19. **Server Layers Of OSI (Open Systems Interconeciton) :**
    - L7 - Application
    - L6 - Presentation
    - L5 - Cryptography
    - L4 - Port Number(16 bit)
    - L3 - IP Address (32 Bits) : Router
    - L2 - Hardware Address - NIC, MAC Address (48 Bits) : Ethernet (eth0)
    - L1 - Digital (1 and 0)
* **Ports :**
    - 0-1023:  Well known ports
    - 1024-49151: Resistered Ports
    - 49152-65535: Dyanmic Ports
###
20. **Switch** - connects devices in a network to each other, enabling them to talk by exchanging data packets.
###
21. **FPGA** - Field Programmable Gate Arrays  - Configurede after manufacturing
###
22. **Socket** - Software structure within a network node of a computer network that serves as an endpoint for sending and receiving data across the network
###
23. **TCP** - Transmission Control Protocol (TCP) is a standard that defines how to establish and maintain a network conversation by which applications can exchange data
    - **3 Way Handshake :**
        1. fitst PC send a random sequence no. and set SYN flag = 1 (syn = 1 for connection requst)
        2. secont PC reply for swquence with Acknowledgement no (sequence no + 1)and send ACK no =  1 (1 for confirmation ) in reply of SYN flag and also request for connection back with SYN flag = 1 to the first PC.
        3. When ACK & SYN and a sequence no recieve to first PC, it replies back in response to SYN with ACK no (sequence + 1 ) and ACK flag = 1.   
        <p>So this is how 3 Way Hand shake Happen In TCP </p>

    - **TCP header**
        
        ![TCP Header](https://media.geeksforgeeks.org/wp-content/uploads/TCPSegmentHeader-1.png)
        - **Sequence Number** – A 32-bit field that holds the sequence number, i.e, the byte number of the first byte that is sent in that particular segment. It is used to reassemble the message at the receiving end of the segments that are received out of order. 
 
        - **Acknowledgement Number** – A 32-bit field that holds the acknowledgement number, i.e, the byte number that the receiver expects to receive next. It is an acknowledgement for the previous bytes being received successfully. 

    - **Control flags –** These are 6 1-bit control bits that control connection establishment, connection termination, connection abortion, flow control, mode of transfer etc. Their function is:
        - URG: Urgent pointer is valid
        - ACK: Acknowledgement number is valid( used in case of cumulative acknowledgement)
        - PSH: Request for push
        - RST: Reset the connection
        - SYN: Synchronize sequence numbers
        - FIN: Terminate the connection


###
24. **MAC Address** - Media Access Control address is a unique identifier assigned for use as a network address in communications within a network segment.
###
25. **Protocol**- It is a standardized set of rules for formatting and processing data.
###
26. **Firmware** - It is a microcode or program that is embedded into the memory of hardware devices to help them operate
###
27. **TLS** - Transport Layer Security encrypts data sent over the Internet : Version 1.3
###
28. **Cache** - a cache is a high-speed data storage layer which stores a subset of data (temporary mermory)
###
29. Von Neuman Architecture **VS** Harvard Architecture 

![MergedImages](https://github.com/mohitpoonia/mohitpoonia/assets/142895350/0c89419c-74ba-4024-94e4-f751d391bb8d)
###
30. **Debian** - Linux Software/OS Family. also known as GNU/Linux
###
26. **VMware Workstation** - IT is a line of Desktop Hypervisor products which lets users run virtual machines, multiple OS
###
31. **VPN** - It establishes a digital connection between your computer and a remote server owned by a VPN provider, creating a point-to-point tunnel that encrypts your personal data, masks your IP address, and lets you sidestep website blocks and firewalls on the internet.
###
32. **Cryptography** - It is the practice and study of techniques for secure communication in the presence of adversarial behavior. It is about constructing and analyzing protocols that prevent third parties or the public from reading private messages. 
###
33. **Hypervisor** - It is a type of computer software, firmware or hardware that creates and runs virtual machines.

| Type I  | Type II |
| ------------- | ------------- |
| Native (bare metal)  | Hosted  |
| Directly on hardware and runs guest OS  | Runs on previously installed OS  |
| acts as light weight as it runs directly  | runs as software like other computer programs  |
###
34. **nginx** - NGINX is open source software for web serving, reverse proxying, caching, load balancing, media streaming, and more.
###
35. **Relational Databases :** The data is stored in tabular form just like table in privious to privious keyword.
    - looks like Excel spreadsheets, with links between them!
    - RDS stads for Relational Database SErvice
    - Its a managed DB service for DB use SQL as a Query Language
    - Eg. SQL, Posteres, MariaDB, Orele, Microsoft Server, Aurora (AWS).
###
36. **Aurora**
    - Aurora is a proprietary technology from AWS (not open sourced)
    - PostgreSQL and MySQL are both supported as Aurora DB
    - Aurora storage automatically  grows in increments of 10GB up to 128 TB.
###
37. **MX record :** - A DNS 'mail exchange' (MX) record directs email to a mail server. The MX record indicates how email messages should be routed in accordance with the Simple Mail Transfer Protocol (SMTP, the standard protocol for all email.
###
38. **AXFR :** - AXFR(global Asynchronous Transfer Full Range) is a protocol for “zone transfers” for replication of DNS data across multiple DNS servers. Unlike normal DNS queries that require the user to know some DNS information ahead of time, AXFR queries reveal resource records including subdomain names.
###
39. **Reverse lookup :** - In computer networks, a reverse DNS lookup or reverse DNS resolution (rDNS) is the querying technique of the Domain Name System (DNS) to determine the domain name associated with an IP address – the reverse of the usual "forward" DNS lookup of an IP address from a domain name.
###
40. **Brute force  :** - A brute-force attack is a trial-and-error method used by application programs to decode login information and encryption keys to use them to gain unauthorized access to systems.
###
41. **Subdomain :** - a subdomain is a separate part of your website that operates under the same primary domain name.
###
42. **Network Classes :**
    - Class A: 10.0.0.0 to 10.255.255.255
    - Class B: 172.16.0.0 to 172.31.255.255
    - Class C: 192.168.0.0 to 192.168.255.255
###
43. **Reverse engineering :** - The process of taking a piece of software or hardware and analyzing its functions and information flow so that its functionality and behavior can be understood.
###
44. **Bash :** - Bourne-again shell, is a command-line shell and scripting language used on Linux, macOS, and other Unix-like operating systems
###
45. **Vulnerablity :** - A vulnerability is a weakness that can be exploited by cybercriminals to gain unauthorized access to a computer system.
###
46. **Bind Shell :** - when we try to connect to vulnerable system through its random port
47. **Reverse Shell :** - When vunerable machine tries to connect 
### 

48. **Traffic smugling**
49. **Native Windows API**
50. **White listed domain abuse**
###
51. **CAP Theorem :** - Consistencey, Availablity, Partition tolerence
    - it is immposibble to distribute system to simultaneouslyprovide more than two of the three of the guarantees.
###
52. **ASIc :** - Applicaton Service Integrated Sercuit, use for bitcoin mining.
###
53. **ICMP :** - Internet Control Message Protocol (ICMP) is a network layer protocol that is used to diagnose communication errors. ICMP is used for diagnostics and network management. For example, the “ping” utility uses an ICMP request and ICMP reply message.
###
54. **Footprinting :** - The process of cybersecurity footprinting involve profiling organaisation  and collencting data about the network, host, employee and third-party partners. like which os used, which services used and its virsions, firewall protocols, IPs, DNS, 
###
55. **Enumeration :** - its nothing but geathering information about the ports. like its virsion, crediantial etc.
###
56. **Malware :** - It's an malecious software intended to harm or exploit any programmable devices, service or network.
###
57. **Payloads :** - Payload in the context of malware refers to malicious code that causes harm to the targeted victim. Malware payloads can be distributed by methods such as worms and phishing emails. 
    - Payloads can be delivered to your computer through: Email attachments, Malicious websites, USB drives. 
    - Today, malware authors typically encrypt the payload to hide the malicious code from antimalware detection and remediation tools
    

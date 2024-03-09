# Red Team Reconnaissance Techniques

## Table of Contents
- [Red Team Reconnaissance Techniques](#red-team-reconnaissance-techniques)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Reconnaissance Techniques](#reconnaissance-techniques)
    - [Active Reconnaissance](#active-reconnaissance)
      - [DNS Enumeration](#dns-enumeration)
      - [Subdomain Enumeration](#subdomain-enumeration)
      - [Whois Enumeration](#whois-enumeration)
      - [Port Scanning](#port-scanning)
      - [Service Enumeration](#service-enumeration)
      - [Vulnerability Scanning](#vulnerability-scanning)
      - [Social Engineering](#social-engineering)
    - [Passive Reconnaissance](#passive-reconnaissance)
      - [Google Dorking](#google-dorking)
      - [Shodan](#shodan)
      - [Censys](#censys)
      - [Recon-ng](#recon-ng)
      - [Maltego](#maltego)
      - [theHarvester](#theharvester)
      - [OSINT Framework](#osint-framework)
      - [SpiderFoot](#spiderfoot)
      - [Metagoofil](#metagoofil)
      - [Infoga](#infoga)
      - [Creepy](#creepy)
      - [Foca](#foca)
      - [Gathering Information from Social Media](#gathering-information-from-social-media)
  - [Conclusion](#conclusion)

## Introduction
Reconnaissance is the first phase of the cyber attack process. It is the process of gathering information about the target system. The information gathered is used to identify vulnerabilities and weaknesses in the target system. The reconnaissance phase is divided into two categories: Active and Passive reconnaissance. Active reconnaissance involves direct interaction with the target system, while passive reconnaissance involves gathering information without directly interacting with the target system. This document will discuss various reconnaissance techniques used by Red Teamers.

## Reconnaissance Techniques

### Active Reconnaissance 
Active reconnaissance involves direct interaction with the target system. The active reconnaissance techniques include DNS enumeration, subdomain enumeration, whois enumeration, port scanning, service enumeration, vulnerability scanning, and social engineering.

#### DNS Enumeration
DNS enumeration is the process of identifying the DNS records of the target system. The DNS records include the IP address, mail server, and other information about the target system. The DNS enumeration can be performed using tools like `nslookup`, `dig`, `wafw00f`, and `host`.
- Enumerating sites:
  - [dnsdumpster.com](https://dnsdumpster.com/)
  - [dnsdumpster.com](https://dnsdumpster.com/)
  - [robtex.com](https://www.robtex.com/)
  - [sitereport.netcraft.com](https://sitereport.netcraft.com/)

#### Subdomain Enumeration 
Subdomain enumeration is the process of identifying the subdomains of the target system. The subdomains can be identified using tools like `Sublist3r`, `Amass`, `Subfinder` and `dirb`.

#### Whois Enumeration
Whois enumeration is the process of identifying the domain registration information of the target system. The domain registration information includes the domain owner, domain registrar, and other information about the domain. The whois enumeration can be performed using the `whois` command.

#### Port Scanning
Port scanning is the process of identifying the open ports on the target system. The open ports can be identified using tools like `nmap`, `masscan`, and `unicornscan`.<br>
Learn more about Nmap: [Click here](/Nmap-Notes/README.md)

#### Service Enumeration
Service enumeration is the process of identifying the services running on the open ports of the target system. The services can be identified using tools like `nmap`, `netcat`, and `telnet`.

#### Vulnerability Scanning
Vulnerability scanning is the process of identifying the vulnerabilities in the target system. The vulnerabilities can be identified using tools like `Nessus`, `OpenVAS`, and `Nexpose`.

#### Social Engineering
Social engineering is the process of manipulating people to reveal confidential information. The social engineering techniques include phishing, pretexting, baiting, and tailgating.

### Passive Reconnaissance
Passive reconnaissance involves gathering information without directly interacting with the target system. The passive reconnaissance techniques include `Google dorking`, `Shodan`, `Censys`, `Recon-ng`, `Maltego`, `theHarvester`, `OSINT Framework`, `SpiderFoot`, `Metagoofil`, `Infoga`, `Creepy`, `Foca`, and gathering information from social media.

#### Google Dorking
Google dorking is the process of using advanced search operators to identify sensitive information on the internet. The advanced search operators include `site`, `filetype`, `intitle`, and `inurl`.

#### [Shodan](https://www.shodan.io/)
Shodan is a search engine that allows users to search for internet-connected devices. The search results include information about the device, such as the IP address, open ports, and services running on the device.
This was created by `John Matherly`, in 2009. <br>


#### Censys
This work similarly to Shodan, however, it is more focused on the security aspect of the devices.
This was created by the University of Michigan, in 2015.

#### Recon-ng
Recon-ng is a reconnaissance framework that allows users to gather information about the target system from various sources, such as search engines, social media, and public databases.
this framework was created by Tim `Tomes`, in `2013`. company: `Black Hills Information Security`.

#### Maltego
Maltego is a powerful open-source intelligence and forensics tool used in cybersecurity for visualizing and analyzing relationships between entities to gather information and identify potential security threats.
This was created by `Roelof Temmingh`, in 2008. company: `Paterva`.

#### [theHarvester](https://github.com/laramies/theHarvester)
TheHarvester is a cybersecurity tool for open-source intelligence gathering, designed to extract information from various public sources, such as search engines and DNS services.
This was created by `Christian Martorella`, in 2006.

#### [OSINT Framework](https://osintframework.com/)
OSINT Framework is a collection of various tools and resources for Open-Source Intelligence (OSINT) gathering in cybersecurity. It was created by `Justin Nordine` in 2015, a security professional, to assist analysts in efficiently accessing and utilizing OSINT tools.

#### [SpiderFoot](https://github.com/smicallef/spiderfoot)
SpiderFoot is an open-source intelligence (OSINT) tool used in cybersecurity for automated reconnaissance, information gathering, and footprinting of digital assets.
This was created by `Steve Micallef`, in 2009.

#### [Metagoofil](https://gitlab.com/kalilinux/packages/metagoofil)
Metagoofil is a tool in cybersecurity that enables information gathering through metadata extraction from public documents, such as PDFs, Word documents, and presentations, to reveal details about an organization's infrastructure and potential security vulnerabilities.
This was created by `Christian Martorella`, in 2006.

#### [Infoga](https://github.com/The404Hacking/Infoga)
Infoga is a cybersecurity tool for gathering email-related information, leveraging search engines and public sources to aid in targeted activities like phishing or security assessments.
This was created by `The404Hacking`, in 2013.

#### [Creepy](https://github.com/ilektrojohn/creepy)
Creepy in cybersecurity refers to malicious activities or tools designed to invade privacy, exploit vulnerabilities, or conduct unauthorized surveillance, posing a threat to individuals or organizations.
This was created by `ilektrojohn`, in 2012.

#### [Foca](https://github.com/ElevenPaths/FOCA)
FOCA (Fingerprinting Organizations with Collected Archives) is a cybersecurity tool used for metadata analysis to identify and assess information about organizations based on their publicly accessible documents and files.
This was created by `ElevenPaths`, in 2009.

#### Gathering Information from Social Media
Social media platforms like Facebook, Twitter, LinkedIn, and Instagram can be used to gather information about the target system. The information gathered includes the target's personal information, friends, and interests.

## Conclusion
Reconnaissance is the first phase of the cyber attack process. It is the process of gathering information about the target system. The information gathered is used to identify vulnerabilities and weaknesses in the target system. The reconnaissance phase is divided into two categories: Active and Passive reconnaissance. Active reconnaissance involves direct interaction with the target system, while passive reconnaissance involves gathering information without directly interacting with the target system. This document discussed various reconnaissance techniques used by Red Teamers.




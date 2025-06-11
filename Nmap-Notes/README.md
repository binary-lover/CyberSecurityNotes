<h1  align = center>Nmap Notes<img style = "border-radius: 5%" align = center src = "https://cdn.shortpixel.ai/spai/q_lossless+ret_img+to_webp/www.stationx.net/wp-content/uploads/2022/12/Nmap-Cheat-Sheet-2.jpg">
</h1>

---

## 1. **-sN**  
Run host discovery to save time; it runs by default.

---

## 2. **Host Discovery**

- **If you are a Root user:** (If any of the below returns True, the host is active)
    - Sends ICMP echo packet
    - TCP SYN (port 443)
    - TCP Acknowledgement (port 80)
    - ICMP Timestamp request
- **If you are a local user:**
    - TCP SYN (port 443)
    - TCP Acknowledgement (port 80)

---

## 3. **Target**

### 3.1 **IP Scan**

```bash
sudo nmap 192.168.1.1               # Single IP 
sudo nmap 192.168.1.0/24            # Subnet Range
sudo nmap 192.168.1.0-255           # IP Range
sudo nmap 192.168.1.1 192.168.1.2   # Specific IPs
sudo nmap -iL Host.txt              # Scan IPs from txt file
sudo nmap scanme.nmap.org           # Scan a Domain Name        
```
> **Note:** If no target port is specified, Nmap scans the most common (1-1000) ports by default.

### 3.2 **Port Scan / Enumeration**

```bash
sudo nmap 192.168.1.1 -p80           # Single port
sudo nmap 192.168.1.1 -p80-450       # Port range
sudo nmap 192.168.1.1 -p22,80,145    # Specific ports
sudo nmap 192.168.1.1 -p http        # Service-specific
sudo nmap 192.168.1.1 -p T:22,U:53   # Protocol-specific
sudo nmap 192.168.1.1 -p-            # All ports
sudo nmap 192.168.1.1 --top-ports 10 # Top 10 ports
sudo nmap -p 21 --script=ftp* 192.168.1.13 # Check FTP vulnerabilities with scripts
```

---

## 4. **Scan Techniques**

- TCP connect scan: `-sT`
- TCP SYN scan: `-sS`
- FIN scan: `-sF`
- Xmas scan: `-sX`
- Null scan: `-sN`
- Ping scan: `-sP`
- UDP scan: `-sU`
- ACK scan: `-sA`
- Version detection: `-sV`
- OS detection: `-O`
- Verbosity: `-v`
- Services + OS + Traceroute: `-A`

**Examples:**
```bash
sudo nmap 192.168.1.1 -sS   # SYN scan
sudo nmap 192.168.1.1 -sU   # UDP scan
sudo nmap 192.168.1.1 -sA   # ACK scan
sudo nmap 192.168.1.1 -sV   # Service version detection
```

---

## 5. **Scan Status**

- **Open:** Host sent SYN, received SYN+ACK from target.
- **Closed:** Host sent SYN, received RST+ACK from target.
- **Filtered:** Host sent SYN, no response (possible firewall/filter).
- **Unfiltered:** Not enough response to determine open/closed; may receive incomplete ICMP.
- **Open|Filtered:** Sent empty packet (null scan), no response.
- **Closed|Filtered:** No response, ambiguous status.

---

## 6. **Scan Timing**

|                | T0 (Paranoid) | T1 (Sneaky) | T2 (Polite) | T3 (Normal) | T4 (Aggressive) | T5 (Insane) |
|----------------|---------------|-------------|-------------|-------------|-----------------|-------------|
| min-rtt-timeout| 100 ms        | 100 ms      | 100 ms      | 100 ms      | 100 ms          | 50 ms       |
| max-rtt-timeout| 5 min         | 15 sec      | 10 sec      | 10 sec      | 1250 ms         | 300 ms      |
| initial-rtt-timeout| 5 min     | 15 sec      | 1 sec       | 1 sec       | 500 ms          | 250 ms      |
| max-retries    | 10            | 10          | 10          | 10          | 6               | 2           |
| scan-delay     | 5 min         | 15 sec      | 400 ms      | 0           | 0               | 0           |
| max TCP delay  | 5 min         | 15,000 ms   | 1 sec       | 1 sec       | 10 ms           | 5 ms        |
| max UDP delay  | 5 min         | 15 sec      | 1 sec       | 1 sec       | 1 sec           | 1 sec       |
| host-timeout   | 0             | 0           | 0           | 0           | 0               | 15 min      |
| script-timeout | 0             | 0           | 0           | 0           | 0               | 10 min      |
| min-parallelism| Dynamic       | Dynamic     | Dynamic     | Dynamic     | Dynamic         | Dynamic     |
| max-parallelism| 1             | 1           | 1           | Dynamic     | Dynamic         | Dynamic     |
| min-hostgroup  | Dynamic       | Dynamic     | Dynamic     | Dynamic     | Dynamic         | Dynamic     |
| max-hostgroup  | Dynamic       | Dynamic     | Dynamic     | Dynamic     | Dynamic         | Dynamic     |
| min-rate       | No minimum    | No minimum  | No minimum  | No minimum  | No minimum      | No minimum  |
| max-rate       | No maximum    | No maximum  | No maximum  | No maximum  | No maximum      | No maximum  |
| defeat-rst-ratelimit| Not enabled | Not enabled | Not enabled | Not enabled | Not enabled | Not enabled |

---

## 7. **Output Types**

```bash
sudo nmap scanme.nmap.org -oN       # Normal text output
sudo nmap scanme.nmap.org -oX       # XML format
sudo nmap scanme.nmap.org -oG       # Grepable format
sudo nmap scanme.nmap.org -oS       # Script Kiddie format (e.g., Service -> 5eRv1c3)
```

---

## 8. **NSE (Nmap Scripting Engine)**

NSE helps with firewall bypass, FTP/DNS/HTTP enumeration, and more.

```bash
sudo nmap scanme.nmap.org --script http-headers     # Show response headers
ls /usr/share/nmap/scripts | grep -e ftp            # List FTP-related scripts
sudo nmap -p21 --script=ftp* 192.168.1.156          # Run all FTP-related scripts
```
**Example Output:**
```
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
```

---

## 9. **Host Discovery Commands**

Used to find live hosts by sending ICMP, TCP SYN/ACK, or UDP packets.

```bash
sudo nmap -sn <target>          # Ping scan (no port scan)
sudo nmap -Pn <target>          # No ICMP echo request
sudo nmap -PS <target>          # TCP SYN ping
sudo nmap -PA <target>          # TCP ACK ping
sudo nmap -PU <target>          # UDP ping
sudo nmap -PE <target>          # ICMP echo ping
sudo nmap -PP <target>          # ICMP timestamp ping
sudo nmap -PR <target>          # ARP ping
sudo nmap -PM <target>          # Address mask
sudo nmap -R <target>           # Reverse DNS lookup
```

---

You have learned how ARP, ICMP, TCP, and UDP can detect live hosts. Any response from a host indicates it is online.

### **Quick Summary of Nmap Host Discovery Options**

| Scan Type              | Example Command                                      |
|------------------------|-----------------------------------------------------|
| ARP Scan               | `sudo nmap -PR -sn MACHINE_IP/24`                   |
| ICMP Echo Scan         | `sudo nmap -PE -sn MACHINE_IP/24`                   |
| ICMP Timestamp Scan    | `sudo nmap -PP -sn MACHINE_IP/24`                   |
| ICMP Address Mask Scan | `sudo nmap -PM -sn MACHINE_IP/24`                   |
| TCP SYN Ping Scan      | `sudo nmap -PS22,80,443 -sn MACHINE_IP/30`          |
| TCP ACK Ping Scan      | `sudo nmap -PA22,80,443 -sn MACHINE_IP/30`          |
| UDP Ping Scan          | `sudo nmap -PU53,161,162 -sn MACHINE_IP/30`         |

> **Tip:** Add `-sn` for host discovery only (no port scan). Omitting `-sn` will scan ports on live hosts.

### **Other Useful Options**

| Option | Purpose                        |
|--------|--------------------------------|
| -n     | No DNS lookup                  |
| -R     | Reverse-DNS lookup for all     |
| -sn    | Host discovery only            |

---

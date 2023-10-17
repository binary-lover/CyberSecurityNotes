# **************** Kyewords ****************
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

16. **Virtual Machine :** A virtual machine (VM) is a digital version of a physical computer. It's a computer file, typically called an image, that behaves like an actual computer. VMs can be implemented using specialized hardware, software, or a combination of the two. 
    - Examples of VMs include:
        - VMware Workstation
        - Oracle VirtualBox
        - Oracle Secure Global Desktop
###

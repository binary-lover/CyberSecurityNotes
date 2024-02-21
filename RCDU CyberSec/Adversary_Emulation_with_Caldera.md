## Adversary Emulation with Caldera

### What is Adversary Emulation?

- Advarsary Emulation is the process of emulating the tactics, techniques, behaviors of specific adversary.

- The object of adversary emulation is to assess(identify) improve how resilient an organization is againsed to a specific adversary/tactic/technique.

- Advarsary behavior is classified into 3 categories:(TTPs)
    - Tactics
    - Techniques
    - Procedures

- Advarsary TTps are used to outline how a specific adversary operates.

### what is Caldera?

- Caldera is a cyber security framework designed to easily automate adversary emulation, assist manual red teams and automate incident response.

- It is built on the MITRE ATT&CK framework and utilizes a client-server system, where the server is used to setup agents(client) and initiate operations.

- **The framework consistes of two components:**
    1. The core system. This is the framework code, consisting of what is available in this repository. include is an asynchronous command and control (C2) server with a REST API and a web interface.

    2. Plugins. These repositories expand the core framework capacities and providing additional functionality. Example including agents, reporting, collection of TTPs, and more.
# configure wazuh agent and manager for getting all logs

Today, we are going to configure the wazuh agent and manager for getting all logs from the agent machine. We will be using sysmon for this purpose. Sysmon is a Windows system service and device driver that logs system activity to the Windows event log. It is part of the Sysinternals Suite, which is a set of utilities from Microsoft.

## contents
* [configure ossec](#configure-ossec)
* [configure filebeat](#configure-filebeat)
* [create new index in wazuh dashboard](#create-new-index-in-wazuh-dashboard)
* [configure some rules on wazuh dashboard](#configure-some-rules-on-wazuh-dashboard)


### configure ossec

* file in 'C:/Program Files (x86)/ossec-agent/ossec.conf' 
* remove Application, Security, System from the <localfile> section in log analysis
* add the following lines to the <localfile> section in log analysis
    ```xml
    <localfile>
        <location>Microsoft-Windows-Sysmon/Operational</location>
        <log_format>eventchannel</log_format>
    </localfile>
    ```
* restart the agent 

* Download mimikatz on the agent machine
* If we run the command `mimikatz.exe` in the command line, the wazuh will not
  detect it.

### so let's configure wazuh manager

* open the file in nano 
  ```bash
  /var/ossec/etc/ossec.conf
  ```
* add the following lines to the <ossec_config> section
    ```xml
    <logall>yes</logall>
    <logall_json>yes</logall_json>
    ```
* restart the manager `systemctl restart wazuh-manager.service`

In order to wazuh start injusting the logs, we neet to change our configuration in filebeat

### configure filebeat

Note: Filebeat is a lightweight shipper for forwarding and centralizing log data. Installed as an agent on your servers, it monitors the log files or locations that you specify, collects log events, and forwards them either to Elasticsearch or to Logstash for indexing.

* open the file in nano 
  ```bash
  /etc/filebeat/filebeat.yml
  ```
* scroll down a little bit and find the line, make archive true
  ```yaml
  filebeat.modules:
  - module: wazuh
    alerts:
      enabled: true
    archives:
      enabled: true
  ```
  * restart filebeat `systemctl restart filebeat.service`


### Create New index in Wazuh dashboard

lets create a new index in wazuh for the logs we are going to send from filebeat

* go to the wazuh dashboard
* click on hamburger menu > management > stack management > index patterns
* click on create index pattern name: `wazuh-archives-**`, time field: `@timestamp` > create index pattern
* head over to the discover tab but you will not see any logs yet of mimikatz
* lets run the command `mimikatz.exe` in the command line and check if sysmon is detecting or not -> it's detecting
* now go back to the wazuh dashboard and check the discover tab, you will see the logs of mimikatz, yes it's working

### Configure some rules on wazuh dashboard

let's play with some rules on the wazuh dashboard
* go to the wazuh dashboard
* click on dropdown menu > management > rules > manage rules files
* search for `0800-sysmon_id_1.xml` and copy the following content for making custom rules
```xml
  <rule id="92000" level="4">
    <if_group>sysmon_event1</if_group>
    <field name="win.eventdata.parentImage" type="pcre2">(?i)\\(c|w)script\.exe</field>
    <options>no_full_log</options>
    <description>Scripting interpreter spawned a new process</description>
    <mitre>
      <id>T1059.005</id>
    </mitre>
  </rule>
```
* now click on create custom rule, edit the local.rules file and add the rule below the existing in it
```xml
  <rule id="100002" level="15">
    <if_group>sysmon_event1</if_group>
        <field name="win.eventdata.originalFileName" type="pcre2">(?i)mimikatz\.exe</field>
    <description>Mimikatz uses Detected</description>
    <mitre>
      <id>T1003</id>
    </mitre>
  </rule>
```

* now click on save and restart the wazuh manager and change the mimikatz.exe to iloveyou and start the mimikatz again

* We can see the logs in the dashboard
* now go to the alerts tab and you will see the alert for the mimikatz
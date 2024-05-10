# 0. My first postmortem

**Issue Summary:**

-   **Duration:**  Apr 15, 2024 5:00 AM to Apr 17, 2024 5:00 AM
-   **Impact:** The Nginx web server was running as the root user, posing a security risk. This could potentially allow an attacker to gain unrestricted access to the system.
-   **Root Cause:** Nginx was configured to run as the root user instead of the recommended nginx user, likely due to a misconfiguration or oversight.

**Timeline:**

-   **12:00 PM :** Issue detected during routine system check.
-   **12:05 PM :** Investigation initiated to determine the cause of Nginx running as root.
-   **12:10 PM :** Confirmed that Nginx was indeed running as root, posing a security risk.
-   **12:15 PM :** Immediate action taken to rectify the configuration.
-   **12:20 PM :** Nginx successfully reconfigured to run as the nginx user.

**Root Cause and Resolution:**

The root cause of the issue was the misconfiguration of Nginx, causing it to run as the root user instead of the nginx user. This misconfiguration was corrected by reconfiguring Nginx to run as the nginx user.

**Corrective and Preventative Measures:**

-   **Configuration Audit:** Conduct a thorough audit of all system configurations to ensure services are running with the appropriate user privileges.
-   **Automated Checks:** Implement automated checks to regularly scan for any instances where services are running as the root user.
-   **Security Training:** Provide additional training to system administrators on best practices for configuring and securing services.
-   **Documentation Update:** Update documentation to include clear instructions on configuring Nginx to run as the appropriate user.
-   **Regular Reviews:** Schedule regular reviews of system configurations to catch any potential misconfigurations early.


**Bash Script for Configuration:**

bash
```
#!/usr/bin/bash

# Stop Nginx service
service nginx stop

# Modify Nginx configuration to run as nginx user
sed -i 's/user\s*root;/user nginx;/' /etc/nginx/nginx.conf

# Start Nginx service
service nginx start
```
This script stops the Nginx service, modifies the configuration file to run Nginx as the nginx user, and then restarts the Nginx service to apply the changes.

By implementing these measures and ensuring Nginx runs with appropriate user privileges, the system's security posture is significantly enhanced, mitigating the risk of unauthorized access and potential system compromise.


# 1. Make people want to read your postmortem

**Issue Summary:**

-   **Duration:** Apr 15, 2024 5:00 AM to Apr 17, 2024 5:00 AM
-   **Impact:** The Nginx web server was caught red-handed running as the root user, giving it the keys to the kingdom. It’s like leaving the front door wide open while you're on vacation.
-   **Root Cause:** Nginx was suffering from an identity crisis, thinking it was Superman instead of just a humble nginx user.

**Timeline:**

-   **12:00 PM :** Like a vigilant neighborhood watch, our system check spotted Nginx strutting around as root.
-   **12:05 PM :** Panic stations! Investigation launched to uncover why Nginx was playing dress-up.
-   **12:10 PM :** Confirmed our worst fears – Nginx was indeed trying to be the root of all evil.
-   **12:15 PM :** Quick as lightning, we swooped in to correct the configuration.
-   **12:20 PM :** Victory dance! Nginx reconfigured to know its place as the nginx user.

**Root Cause and Resolution:**

Nginx’s confusion stemmed from a misconfiguration, where it believed it could fly as root when it should’ve been content with just being nginx. We straightened it out by reminding Nginx of its true identity and configuring it to run as the nginx user.

**Corrective and Preventative Measures:**

-   **Configuration Therapy:** Ensure all services are configured correctly, so they don’t suffer an identity crisis like poor Nginx.
-   **Automated Sanity Checks:** Set up automated checks to keep an eye on services' egos and promptly correct any delusions of grandeur.
-   **Humor Injection:** Maybe a good laugh can lighten the mood and make everyone more vigilant about system security.
-   **Beware of Imposters:** Train your team to spot imposters like Nginx pretending to be someone they're not.
-   **Stay Grounded:** Regularly review system configurations to prevent any more flights of fancy.

**Bash Script for Configuration:**

bash
```
#!/usr/bin/bash

# Stop Nginx service
service nginx stop

# Remind Nginx of its true identity
sed -i 's/user\s*root;/user nginx;/' /etc/nginx/nginx.conf

# Restart Nginx service
service nginx start 
```
This script serves as a reality check for Nginx, reminding it to stay grounded and run as the nginx user, not as some caped crusader trying to save the day.

With these measures in place, we’re confident that Nginx will no longer be tempted to don the cape and tights of the root user, ensuring a more secure and down-to-earth web server experience.

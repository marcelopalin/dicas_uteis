# CONFIGURANDO FAIL2BAN

https://www.digitalocean.com/community/tutorials/how-to-protect-an-nginx-server-with-fail2ban-on-ubuntu-14-04

https://blog.swmansion.com/limiting-failed-ssh-login-attempts-with-fail2ban-7da15a2313b

https://easyengine.io/tutorials/nginx/fail2ban/


# fail2ban logs


You can monitor fail2ban log file:


```bash
tail -f /var/log/fail2ban.log
```


# fail2ban-client

Você também pode usar o fail2ban-client para descobrir o status de uma determinada cadeia usando o seguinte comando:
fail2ban-client status nginx-req-limit

This will show:

Status for the jail: nginx-req-limit
|- filter
|  |- File list:    /var/log/nginx/test.com.error.log /var/log/nginx/example.com.error.log
|  |- Currently failed: 6
|  `- Total failed: 389
`- action
   |- Currently banned: 3
   |  `- IP list:   95.211.117.202 78.187.45.204 91.216.201.114 
   `- Total banned: 3



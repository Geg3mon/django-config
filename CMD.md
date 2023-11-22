
# Certbot generate   
```bash
docker-compose run --rm certbot certonly -v --webroot --webroot-path=/var/www --preferred-challenges http-01 --email email@gmail.com --agree-tos --no-eff-email --staging -d ${DOMAIN} -d www.${DOMAIN}
docker-compose run --rm certbot certonly -v --webroot --webroot-path=/var/www --preferred-challenges http-01 --email email@gmail.com --agree-tos --no-eff-email --force-renewal  -d ${DOMAIN} -d www.${DOMAIN}
```

# Dump db
```bash
python3 manage.py dumpdata --exclude auth.permission --exclude contenttypes --exclude admin.logentry --exclude sessions.session --exclude authtoken.token --exclude sites.site > server_data.json
```

# CRON Certbot/PostgreSQL/Nginx
```bash
0 0 */30 * * /usr/bin/docker-compose -f /root/{FOLDER}/docker-compose.yml run --rm certbot --quiet renew --webroot --webroot-path=/var/www >> /home/crontab/{FOLDER}/crontab_certbot_renew.txt 2>&1
0 */4 * * * /usr/bin/docker exec -w /app {FOLDER}_web_1 python3 manage.py dumpdata --exclude auth.permission --exclude contenttypes --exclude admin.logentry --exclude sessions.session --exclude authtoken.token --exclude sites.site > /home/crontab/{FOLDER}/server_data.json 2>> /home/{FOLDER}/crontab/crontab_db_log.txt
0 * */10 * * /usr/bin/docker-compose -f /root/{FOLDER}/docker-compose.yml restart nginx >> /home/crontab/{FOLDER}/crontab_nginx.txt 2>&1
```

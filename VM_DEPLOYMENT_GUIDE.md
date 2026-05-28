# Django Deployment to GCP Compute Engine (VM)
## Domain: drsaurav.blizon.tech

This guide covers deploying your Django app to a Google Cloud Compute Engine VM instance.

---

## Step 1: Create VM Instance

```bash
# Create a VM instance
gcloud compute instances create medantaclone-vm \
  --zone=us-central1-a \
  --machine-type=e2-medium \
  --image-family=ubuntu-2204-lts \
  --image-project=ubuntu-os-cloud \
  --boot-disk-size=30GB \
  --tags=http-server,https-server

# Create firewall rules
gcloud compute firewall-rules create allow-http \
  --allow tcp:80 \
  --target-tags http-server

gcloud compute firewall-rules create allow-https \
  --allow tcp:443 \
  --target-tags https-server
```

---

## Step 2: Get VM External IP

```bash
# Get the external IP address
gcloud compute instances describe medantaclone-vm \
  --zone=us-central1-a \
  --format='get(networkInterfaces[0].accessConfigs[0].natIP)'

# Note this IP - you'll need it for DNS configuration
```

---

## Step 3: Configure DNS

Go to your domain registrar (where `blizon.tech` is managed) and add:

**A Record:**
- Name: `drsaurav`
- Type: `A`
- Value: `YOUR_VM_EXTERNAL_IP`
- TTL: `3600`

Wait 5-10 minutes for DNS propagation.

---

## Step 4: SSH into VM and Setup

```bash
# SSH into the VM
gcloud compute ssh medantaclone-vm --zone=us-central1-a

# Once inside the VM, run the following commands:

# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and dependencies
sudo apt install -y python3.12 python3.12-venv python3-pip nginx git \
  mysql-client libmysqlclient-dev pkg-config supervisor

# Create app directory
sudo mkdir -p /var/www/medantaclone
sudo chown $USER:$USER /var/www/medantaclone
cd /var/www/medantaclone
```

---

## Step 5: Deploy Your Code

### Option A: Using Git (Recommended)

```bash
# Clone your repository
git clone YOUR_REPO_URL .

# Or if you don't have a git repo, use SCP from your local machine:
# (Run this from your LOCAL machine, not the VM)
# gcloud compute scp --recurse /Users/apple/Code/medantaclone/* \
#   medantaclone-vm:/var/www/medantaclone/ --zone=us-central1-a
```

### Option B: Upload via SCP (from your local machine)

```bash
# Run this on your LOCAL machine
cd /Users/apple/Code/medantaclone
gcloud compute scp --recurse . medantaclone-vm:/var/www/medantaclone/ --zone=us-central1-a
```

---

## Step 6: Setup Python Environment (on VM)

```bash
# Create virtual environment
cd /var/www/medantaclone
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
pip install gunicorn

# Create .env file for secrets
cat > .env << EOF
SECRET_KEY=$(python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
DEBUG=False
ALLOWED_HOSTS=drsaurav.blizon.tech,YOUR_VM_IP
DATABASE_URL=sqlite:///db.sqlite3
EOF

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput
```

---

## Step 7: Configure Gunicorn

```bash
# Create Gunicorn systemd service
sudo nano /etc/systemd/system/gunicorn.service
```

Paste this content:

```ini
[Unit]
Description=gunicorn daemon for medantaclone
After=network.target

[Service]
User=YOUR_USERNAME
Group=www-data
WorkingDirectory=/var/www/medantaclone
EnvironmentFile=/var/www/medantaclone/.env
ExecStart=/var/www/medantaclone/venv/bin/gunicorn \
    --workers 3 \
    --bind unix:/var/www/medantaclone/medantaclone.sock \
    medantaclone.wsgi:application

[Install]
WantedBy=multi-user.target
```

Replace `YOUR_USERNAME` with your actual username (run `whoami` to check).

```bash
# Start and enable Gunicorn
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo systemctl status gunicorn
```

---

## Step 8: Configure Nginx

```bash
# Create Nginx configuration
sudo nano /etc/nginx/sites-available/medantaclone
```

Paste this content:

```nginx
server {
    listen 80;
    server_name drsaurav.blizon.tech;

    client_max_body_size 100M;

    location = /favicon.ico { 
        access_log off; 
        log_not_found off; 
    }
    
    location /static/ {
        alias /var/www/medantaclone/staticfiles/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    location /media/ {
        alias /var/www/medantaclone/media/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/medantaclone/medantaclone.sock;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_redirect off;
    }
}
```

```bash
# Enable the site
sudo ln -s /etc/nginx/sites-available/medantaclone /etc/nginx/sites-enabled/

# Test Nginx configuration
sudo nginx -t

# Restart Nginx
sudo systemctl restart nginx
```

---

## Step 9: Setup SSL with Let's Encrypt

```bash
# Install Certbot
sudo apt install -y certbot python3-certbot-nginx

# Get SSL certificate
sudo certbot --nginx -d drsaurav.blizon.tech

# Follow the prompts:
# - Enter your email
# - Agree to terms
# - Choose to redirect HTTP to HTTPS (option 2)

# Test auto-renewal
sudo certbot renew --dry-run
```

---

## Step 10: Update Django Settings for Production

Edit `/var/www/medantaclone/medantaclone/settings.py`:

```python
import os
from pathlib import Path

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# Security settings
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
```

Install python-dotenv:
```bash
source /var/www/medantaclone/venv/bin/activate
pip install python-dotenv
```

---

## Step 11: Restart Services

```bash
# Restart Gunicorn
sudo systemctl restart gunicorn

# Restart Nginx
sudo systemctl restart nginx

# Check status
sudo systemctl status gunicorn
sudo systemctl status nginx
```

---

## Step 12: Test Your Deployment

Visit: `https://drsaurav.blizon.tech`

---

## Useful Commands

### View Logs
```bash
# Gunicorn logs
sudo journalctl -u gunicorn -f

# Nginx error logs
sudo tail -f /var/log/nginx/error.log

# Nginx access logs
sudo tail -f /var/log/nginx/access.log
```

### Restart Services
```bash
sudo systemctl restart gunicorn
sudo systemctl restart nginx
```

### Update Code
```bash
cd /var/www/medantaclone
git pull  # or upload new files via SCP
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
sudo systemctl restart gunicorn
```

### Database Backup
```bash
# Backup SQLite database
cp /var/www/medantaclone/db.sqlite3 /var/www/medantaclone/db.sqlite3.backup.$(date +%Y%m%d)

# Or create automated backups
sudo crontab -e
# Add: 0 2 * * * cp /var/www/medantaclone/db.sqlite3 /var/www/medantaclone/backups/db.$(date +\%Y\%m\%d).sqlite3
```

---

## Troubleshooting

### 502 Bad Gateway
```bash
# Check Gunicorn is running
sudo systemctl status gunicorn

# Check socket file exists
ls -la /var/www/medantaclone/medantaclone.sock

# Check permissions
sudo chown www-data:www-data /var/www/medantaclone/medantaclone.sock
```

### Static Files Not Loading
```bash
# Recollect static files
cd /var/www/medantaclone
source venv/bin/activate
python manage.py collectstatic --noinput

# Check permissions
sudo chown -R $USER:www-data /var/www/medantaclone/staticfiles
sudo chmod -R 755 /var/www/medantaclone/staticfiles
```

### Database Errors
```bash
# Run migrations
cd /var/www/medantaclone
source venv/bin/activate
python manage.py migrate
```

---

## Quick Deployment Script

Save this as `deploy_to_vm.sh` on your LOCAL machine:

```bash
#!/bin/bash
VM_NAME="medantaclone-vm"
ZONE="us-central1-a"
REMOTE_DIR="/var/www/medantaclone"

echo "📦 Uploading files to VM..."
gcloud compute scp --recurse . $VM_NAME:$REMOTE_DIR/ --zone=$ZONE

echo "🔄 Restarting services..."
gcloud compute ssh $VM_NAME --zone=$ZONE --command="
    cd $REMOTE_DIR
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py collectstatic --noinput
    sudo systemctl restart gunicorn
    sudo systemctl restart nginx
"

echo "✅ Deployment complete!"
```

Make it executable:
```bash
chmod +x deploy_to_vm.sh
./deploy_to_vm.sh
```

---

## Next Steps

1. ✅ VM created and configured
2. ✅ DNS pointing to VM IP
3. ✅ Code deployed
4. ✅ Gunicorn running
5. ✅ Nginx configured
6. ✅ SSL certificate installed
7. ✅ Site accessible at https://drsaurav.blizon.tech

**Optional Improvements:**
- Set up Cloud SQL for production database
- Configure Cloud Storage for media files
- Set up automated backups
- Configure monitoring and alerts
- Set up CI/CD pipeline

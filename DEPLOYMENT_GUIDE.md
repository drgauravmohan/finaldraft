# Django App Deployment to GCP Guide

## Domain: drsaurav.blizon.tech

This guide covers deploying your Django application to Google Cloud Platform using Cloud Run (recommended) or Compute Engine.

---

## Option 1: Cloud Run (Recommended - Easiest & Most Cost-Effective)

### Prerequisites
1. Google Cloud account with billing enabled
2. `gcloud` CLI installed on your machine
3. Docker installed locally

### Step 1: Install Google Cloud SDK

```bash
# macOS
brew install --cask google-cloud-sdk

# Initialize gcloud
gcloud init
gcloud auth login
```

### Step 2: Create Required Files

#### 2.1 Create `Dockerfile`

```dockerfile
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Run gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 medantaclone.wsgi:application
```

#### 2.2 Create `.dockerignore`

```
.env
.venv
env/
venv/
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
*.so
*.egg
*.egg-info/
dist/
build/
.git/
.gitignore
README.md
.DS_Store
db.sqlite3
```

#### 2.3 Update `requirements.txt`

Make sure you have all dependencies:

```bash
pip freeze > requirements.txt
```

#### 2.4 Create `cloudbuild.yaml` (Optional - for CI/CD)

```yaml
steps:
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/$PROJECT_ID/medantaclone', '.']
  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'gcr.io/$PROJECT_ID/medantaclone']
  - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
    entrypoint: gcloud
    args:
      - 'run'
      - 'deploy'
      - 'medantaclone'
      - '--image'
      - 'gcr.io/$PROJECT_ID/medantaclone'
      - '--region'
      - 'us-central1'
      - '--platform'
      - 'managed'
      - '--allow-unauthenticated'
images:
  - 'gcr.io/$PROJECT_ID/medantaclone'
```

### Step 3: Update Django Settings

Update `medantaclone/settings.py`:

```python
import os
from pathlib import Path

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = [
    'drsaurav.blizon.tech',
    '.run.app',  # For Cloud Run
    'localhost',
    '127.0.0.1',
]

# Database - Use Cloud SQL or keep SQLite for testing
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# For production with Cloud SQL (MySQL):
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'HOST': os.environ.get('DB_HOST'),
#         'PORT': '3306',
#         'NAME': os.environ.get('DB_NAME'),
#         'USER': os.environ.get('DB_USER'),
#         'PASSWORD': os.environ.get('DB_PASSWORD'),
#     }
# }

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files (if using Cloud Storage)
# DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
# GS_BUCKET_NAME = 'your-bucket-name'

# Security settings for production
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
```

### Step 4: Deploy to Cloud Run

```bash
# Set your GCP project
gcloud config set project YOUR_PROJECT_ID

# Build and deploy
gcloud run deploy medantaclone \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars "SECRET_KEY=your-secret-key-here" \
  --set-env-vars "DEBUG=False"

# Or build Docker image first
docker build -t gcr.io/YOUR_PROJECT_ID/medantaclone .
docker push gcr.io/YOUR_PROJECT_ID/medantaclone

gcloud run deploy medantaclone \
  --image gcr.io/YOUR_PROJECT_ID/medantaclone \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

### Step 5: Configure Custom Domain

```bash
# Map your custom domain
gcloud run domain-mappings create \
  --service medantaclone \
  --domain drsaurav.blizon.tech \
  --region us-central1

# Get the DNS records to configure
gcloud run domain-mappings describe \
  --domain drsaurav.blizon.tech \
  --region us-central1
```

**Configure DNS:**
1. Go to your domain registrar (where blizon.tech is registered)
2. Add the DNS records provided by the command above
3. Typically you'll need to add:
   - A record pointing to the Cloud Run IP
   - AAAA record for IPv6 (if provided)
   - Or CNAME record pointing to `ghs.googlehosted.com`

---

## Option 2: Compute Engine (VM-based)

### Step 1: Create a VM Instance

```bash
gcloud compute instances create medantaclone-vm \
  --zone=us-central1-a \
  --machine-type=e2-medium \
  --image-family=ubuntu-2204-lts \
  --image-project=ubuntu-os-cloud \
  --boot-disk-size=20GB \
  --tags=http-server,https-server
```

### Step 2: SSH into the VM

```bash
gcloud compute ssh medantaclone-vm --zone=us-central1-a
```

### Step 3: Install Dependencies on VM

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and dependencies
sudo apt install -y python3.12 python3.12-venv python3-pip nginx git mysql-client libmysqlclient-dev

# Install supervisor for process management
sudo apt install -y supervisor
```

### Step 4: Clone Your Repository

```bash
cd /home/$USER
git clone YOUR_REPO_URL medantaclone
cd medantaclone

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install gunicorn
```

### Step 5: Configure Gunicorn

Create `/etc/supervisor/conf.d/medantaclone.conf`:

```ini
[program:medantaclone]
directory=/home/YOUR_USERNAME/medantaclone
command=/home/YOUR_USERNAME/medantaclone/venv/bin/gunicorn --workers 3 --bind unix:/home/YOUR_USERNAME/medantaclone/medantaclone.sock medantaclone.wsgi:application
autostart=true
autorestart=true
stderr_logfile=/var/log/medantaclone.err.log
stdout_logfile=/var/log/medantaclone.out.log
user=YOUR_USERNAME
```

```bash
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start medantaclone
```

### Step 6: Configure Nginx

Create `/etc/nginx/sites-available/medantaclone`:

```nginx
server {
    listen 80;
    server_name drsaurav.blizon.tech;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        alias /home/YOUR_USERNAME/medantaclone/staticfiles/;
    }

    location /media/ {
        alias /home/YOUR_USERNAME/medantaclone/media/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/YOUR_USERNAME/medantaclone/medantaclone.sock;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/medantaclone /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### Step 7: Configure SSL with Let's Encrypt

```bash
sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d drsaurav.blizon.tech
```

### Step 8: Configure DNS

Point your domain to the VM's external IP:
1. Get VM IP: `gcloud compute instances describe medantaclone-vm --zone=us-central1-a --format='get(networkInterfaces[0].accessConfigs[0].natIP)'`
2. Add A record in your DNS: `drsaurav.blizon.tech` → `VM_EXTERNAL_IP`

---

## Database Options

### Option A: Cloud SQL (Recommended for Production)

```bash
# Create Cloud SQL instance
gcloud sql instances create medantaclone-db \
  --database-version=MYSQL_8_0 \
  --tier=db-f1-micro \
  --region=us-central1

# Create database
gcloud sql databases create medantaclone --instance=medantaclone-db

# Create user
gcloud sql users create dbuser \
  --instance=medantaclone-db \
  --password=YOUR_PASSWORD
```

### Option B: Keep SQLite (Simple, for low traffic)

Just ensure the SQLite database file is persisted in Cloud Run using a volume mount or Cloud Storage.

---

## Environment Variables

For Cloud Run, set environment variables:

```bash
gcloud run services update medantaclone \
  --update-env-vars SECRET_KEY=your-secret-key \
  --update-env-vars DEBUG=False \
  --update-env-vars DB_HOST=your-db-host \
  --update-env-vars DB_NAME=medantaclone \
  --update-env-vars DB_USER=dbuser \
  --update-env-vars DB_PASSWORD=your-password
```

---

## Post-Deployment Checklist

- [ ] Run migrations: `python manage.py migrate`
- [ ] Create superuser: `python manage.py createsuperuser`
- [ ] Collect static files: `python manage.py collectstatic`
- [ ] Test the site at https://drsaurav.blizon.tech
- [ ] Configure backups for database
- [ ] Set up monitoring and logging
- [ ] Configure CDN for static files (optional)

---

## Quick Start (Recommended Path)

**I recommend Cloud Run** because it's:
- ✅ Easier to deploy
- ✅ Auto-scaling
- ✅ Pay only for what you use
- ✅ Built-in HTTPS
- ✅ No server management

Run these commands:

```bash
# 1. Create Dockerfile (see above)
# 2. Deploy
gcloud run deploy medantaclone \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated

# 3. Map domain
gcloud run domain-mappings create \
  --service medantaclone \
  --domain drsaurav.blizon.tech \
  --region us-central1

# 4. Configure DNS as instructed
```

---

## Need Help?

Let me know if you need help with:
- Creating the Dockerfile
- Setting up Cloud SQL
- Configuring environment variables
- DNS configuration
- Any deployment issues

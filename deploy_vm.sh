#!/bin/bash

# Quick VM Deployment Script
# Run this from your LOCAL machine

set -e

VM_NAME="medantaclone-vm"
ZONE="us-central1-a"
REMOTE_DIR="/var/www/medantaclone"
LOCAL_DIR="/Users/apple/Code/medantaclone"

echo "🚀 Deploying to GCP Compute Engine VM"
echo "======================================"
echo ""

# Check if VM exists
echo "🔍 Checking VM status..."
if ! gcloud compute instances describe $VM_NAME --zone=$ZONE &> /dev/null; then
    echo "❌ VM '$VM_NAME' not found in zone '$ZONE'"
    echo "Please create the VM first or update the VM_NAME and ZONE variables"
    exit 1
fi

echo "✅ VM found"
echo ""

# Upload files
echo "📦 Uploading files to VM..."
cd $LOCAL_DIR
gcloud compute scp --recurse \
    --exclude=".git/*" \
    --exclude=".env/*" \
    --exclude="__pycache__/*" \
    --exclude="*.pyc" \
    --exclude=".DS_Store" \
    . $VM_NAME:$REMOTE_DIR/ --zone=$ZONE

echo ""
echo "🔧 Installing dependencies and restarting services..."

# Run commands on VM
gcloud compute ssh $VM_NAME --zone=$ZONE --command="
    set -e
    cd $REMOTE_DIR
    
    # Activate virtual environment
    source venv/bin/activate
    
    # Install/update dependencies
    pip install -r requirements.txt
    
    # Run migrations
    python manage.py migrate
    
    # Collect static files
    python manage.py collectstatic --noinput
    
    # Restart Gunicorn
    sudo systemctl restart gunicorn
    
    # Restart Nginx
    sudo systemctl restart nginx
    
    echo ''
    echo '✅ Services restarted successfully'
    echo ''
    echo '📊 Service Status:'
    sudo systemctl status gunicorn --no-pager | head -5
    sudo systemctl status nginx --no-pager | head -5
"

echo ""
echo "🎉 Deployment Complete!"
echo ""
echo "🌐 Your site should be live at: https://drsaurav.blizon.tech"
echo ""
echo "📝 To view logs, run:"
echo "   gcloud compute ssh $VM_NAME --zone=$ZONE"
echo "   sudo journalctl -u gunicorn -f"
echo ""

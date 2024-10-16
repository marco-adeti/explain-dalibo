# Pre-requisites
apt-get install libexpat1
source /srv/explain-deploy/explain-env/bin/activate
# Usage
ansible-playbook  /srv/explain-deploy/deploy.yaml
ansible-playbook  /srv/explain-deploy/deploy.yaml  --extra-vars "app_version=v2.8.0"
# Check repo version
git describe --exact-match --tags


# CC-BY-SA https://creativecommons.org/licenses/by-sa/4.0/deed.fr
# Librement inspiré de https://github.com/mdiflorio/ansible-python-ngnix-postgres

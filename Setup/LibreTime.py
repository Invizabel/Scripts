# or follow the docs: https://libretime.org/docs/admin-manual/install/install-using-docker/

import os

os.system('echo LIBRETIME_VERSION="4.5.0" > .env')
os.system("source .env")
os.system("wget 'https://raw.githubusercontent.com/libretime/libretime/$LIBRETIME_VERSION/docker-compose.yml'")
os.system("wget 'https://raw.githubusercontent.com/libretime/libretime/$LIBRETIME_VERSION/docker/config.template.yml'")

os.system("""echo '# Postgres
POSTGRES_PASSWORD=$(openssl rand -hex 16)

# RabbitMQ
RABBITMQ_DEFAULT_PASS=$(openssl rand -hex 16)

# Icecast
ICECAST_SOURCE_PASSWORD=$(openssl rand -hex 16)
ICECAST_ADMIN_PASSWORD=$(openssl rand -hex 16)
ICECAST_RELAY_PASSWORD=$(openssl rand -hex 16)' >> .env""")

os.system('bash -a -c "source .env; envsubst < config.template.yml > config.yml"')
os.system("sudo apt update && sudo apt install gettext-base")
os.system("docker compose run --rm api libretime-api migrate")
os.system("docker compose up -d")
os.system("docker compose ps")
os.system("docker compose logs -f")

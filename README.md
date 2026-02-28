# openECOE-All
* bajar tambien los submódulos (frontend y backend).
1. Comprobar si tienes la llave privada en el servidor
ls -l ~/.ssh/id_*



CREAR 
ssh-keygen -t ed25519 -C "scubero@sauron"
copiar la clave creada:
cat ~/.ssh/id_ed25519.pub

ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICQuUMzLgLljpq5FIdFQbYpMRzsaWX93LvT1n1nGCrH0 scubero@sauron

2. Verificar la conexión con GitHub
ssh -T git@github.com

ssh -T git@github.com
The authenticity of host 'github.com (140.82.121.4)' can't be established.
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'github.com' (ED25519) to the list of known hosts.
Hi sercutos! You've successfully authenticated, but GitHub does not provide shell access.


3. Clonar el repositorio (esto creará una nueva carpeta openECOE-All:
cd ~
git clone git@github.com:sercutos/openECOE-All.git

cambiar Cambia la URL del repositorio principal:
git remote set-url origin git@github.com:sercutos/openECOE-All.git
Configura los submódulos para que también usen SSH:
git submodule init
# Este comando "reescribe" las URLs de los submódulos a SSH si es necesario
git submodule update --init --recursive
Puedes arreglarlo rápidamente editando el archivo:

Bash
nano .gitmodules
Cambia cualquier url = https://github.com/nombre/repo por url = git@github.com:nombre/repo.

Luego aplica los cambios:

Bash
git submodule sync
git submodule update --init --recursive

4. clonar los submodulos, desde dentro de la carpeta openECOE-All (te pedirá el usuario/password) de github):

git submodule update --init --recursive

# kaggle-environment
Build and run a full Kaggle Jupyter/Python environment

**Dependencies:**
 - Packer (see https://www.packer.io/docs/install/index.html)
 ```
 curl -O https://releases.hashicorp.com/packer/1.1.0/packer_1.1.0_linux_amd64.zip
 unzip packer_1.1.0_linux_amd64.zip -d /usr/local/bin
 ```
 - Docker (see https://docs.docker.com/engine/installation/)
 - Ansible (see http://docs.ansible.com/ansible/latest/intro_installation.html)

**Build:**
  - `. ./kaggle-python.build`

**Run:**
  - `. ./kaggle-python.run`
  - Each of the following commands, when executed in the same shell as the
    command above, mounts the current working directory into a Docker container
    and runs the following process:
    - `kpython`: An Interactive Python Shell
    - `ikpython`: An Interactive iPython Shell
    - `kjupyter`: A Jupyter Notebook Server
    - `kbash`: A Bash Shell

**Tips:**
  - In order to have the commands in the section above persistently available:
      - `cat ./kaggle-python.run >> ~/.bash_aliases`
      - or `cp ./kaggle-python.run ~/.oh-my-zsh/custom/kaggle-python.zsh`
      (if you use oh-my-zsh)

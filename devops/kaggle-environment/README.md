# kaggle-environment
Build and run a full Kaggle Jupyter/Python environment

Dependencies:
 - Packer
 - Ansible
 - Docker

Build:
  `. ./kaggle-python.build`

Run:
  `. ./kaggle-python.run`
  Each of the following commands, when executed in the same shell as the command
  above, mounts the current working directory into a Docker container and runs
  the following process:
    `kpython`: An Interactive Python Shell
    `ikpython`: An Interactive iPython Shell
    `kjupyter`: A Jupyter Notebook Server
    `kbash`: A Bash Shell

Tips:
  In order to have the commands in the section above persistently available:
      `cat ./kaggle-python.run >> ~/.bash_aliases`
      or if you use oh-my-zsh:
        `cp ./kaggle-python.run ~/.oh-my-zsh/custom/kaggle-python.zsh`

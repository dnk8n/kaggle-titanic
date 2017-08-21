# kaggle-environment
Build and run a full Kaggle Jupyter/Python environment

Dependencies:
 - Packer
 - Ansible
 - Docker

Build:
- `. ./kaggle-python.build`

Run:
- `. ./kaggle-python.run`
- Each of the following commands mounts the current working directory into a
  Docker container and runs the following process:
  - kpython: An Interactive Python Shell
  - ikpython: An Interactive iPython Shell
  - kjupyter: A Jupyter Notebook Server
  - kbash: A Bash Shell

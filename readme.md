### Описание

Стенд для открытого урока "Виртуальная лаборатория на Vagrant"

### Как запустить

Должны быть установлены все зависимости.
VirtualBox - https://www.virtualbox.org/wiki/Downloads
Git - https://git-scm.com/downloads
Vagrant - https://www.vagrantup.com/downloads.html
Ansible - https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html

Далее:
```bash
git clone https://github.com/lalbrekht/vagrant.git

vagrant status # убедиться что vagrant установлен и Vagrantfile без ошибок

vagrant up # поднимаем стенд

vagrant ssh # зайти в виртуальную машину
```

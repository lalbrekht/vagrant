Role nginx
==========

Настройка web сервера nginx

Role Variables
--------------

[defaults/main.yml](defaults/main.yml)


Example Playbook
----------------

    - hosts: servers
      roles:
         - role: sedovandrew.nginx
           nginx_http_default_server_port: 8080
           nginx_http_default_server_root: "/usr/share/nginx/html"

Test Role
---------

    molecule test

License
-------

BSD

Author Information
------------------

Sedov Andrey

e-mail: sedoy80@gmail.com

# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "archlinux/archlinux"

  # Forward port 5000 (Flask default) to port 8080 on the host machine
  config.vm.network "forwarded_port", guest: 5000, host: 8080

  config.vm.provision "shell", inline: <<-SHELL
    sudo pacman -Syu --noconfirm
    sudo pacman -S git nano vim python python-virtualenv python-pip --noconfirm

    python -m venv flask_venv
    source flask_venv/bin/activate
    pip install Flask
  SHELL

  # Copy the Flask app to the VM
  config.vm.provision "file", source: "hello.py", destination: "/home/vagrant/hello.py"

  config.vm.provision "shell", inline: <<-SHELL
    source flask_venv/bin/activate
    nohup flask --app /home/vagrant/hello run --host=0.0.0.0 &
  SHELL
end

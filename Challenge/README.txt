-> PARA USO DA FERRAMENTA É NECESSÁRIO A INSTALACAO DO PYTHON
	-> EM WINDOWS
		> pip install python

	-> EM LINUX
		-> UBUNTU/DEBIAN
			$ sudo apt install python3
		-> FEDORA
			$ sudo dnf install python3
		-> CENTOS/RHEL
			$ sudo yum install python3

-> PARA USO DA SECAO DE VARRUDURA EM IMAGENS
	instalar o tesserocr para o python

	-> EM WINDOWS
		Baixar o arquivo correspondente ao Windows da máquina via					https://github.com/simonflueckiger/tesserocr-windows_build/releases
		Então realizar a instalacao com o comando 
		> pip install <package_name>.whl

	-> EM LINUX 
		-> UBUNTU/DEBIAN
			$ apt-get install tesseract-ocr libtesseract-dev libleptonica-dev pkg-config
			$ pip install tesserocr
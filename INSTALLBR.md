#Tutorial de Instalação

Primeiramente, caso já não tenha, irá precisar instalar uma versão da linguagem Python,

## Instalação do Python :

###Linux

É bem provavel que sua distribuição de Linux já tenha Python instalado. Para checar se tem (e qual a versão ele é), abra o terminal e digite o seguinte comando:

command-line
```$ python3 --version
```Resultado : Python 3.5.1

Se você tem uma 'micro versão' diferente instalada ex: 3.5.0 no lugar da 3.5.1, você não precisa atualizar.
Mas se você não tem python ou tem uma versão diferente, como 2.7, siga os passos para seu sistema:

####Debian or Ubuntu
command-line
```$ sudo apt-get install python3.5```

####Fedora (até versão 21)
command-line
```$ sudo yum install python3```

####Fedora (22+)
command-line
```$ sudo dnf install python3```

openSUSE
command-line
```$ sudo zypper install python3```


### macOS ( OS X )
O macOS já vem com python 2.7 instalado, e para atualizar, siga os passos a seguir:

Antes de você instalar Python no seu macOS, você precisa hablitar a instalação de pacotes que não são da App Store. Vá para  System Preferences, clique em "Security & Privacy," e na aba "General". Mude a opção "Allow apps downloaded from:" de "Mac App Store," para "Mac App Store and identified developers."

Baixe o instalador Python do site oficial da linguagem:  https://www.python.org/downloads/release/python-351/

Verifique se a instalação foi bem scedida abrindo o Terminal e digitando:
command-line
```$ python3 --version
``` Resultado: Python 3.5.1`

###Windows

Você pode baixar Python para Windoes do website oficial:
https://www.python.org/downloads/release/python-351/. Durante a instalação, lembre-se do diretório onde ela está sendo feita, pois irá precisar mais tarde.

Preste atenção em uma coisa: Na segunda tela da instalação "Customize", role para baixo e na opção "Add python.exe to the Path" selecione  "Will be installed on local hard drive".

Não esqueça de adicionar Python para o caminho.


## Virtualenv - ambiente virtual (Opcional, mas recomendado)

Antes de instalarmos qualquer pacote, podemos usar uma ferramenta muito útil para manter seu ambiente de desenvolvimento organizado e separado de outros no seu computador, tornando as configurações independetes das do resto do computador. Isso irá prevenir problemas no fututo. Isso fucniona como as Workspaces de Java.

Você precisa escolher o diretório onde irá desenvolver seu projeto. É recomendável que seja dentro de sua pasta de projetos, e que seu repositório GIT esteja dentro dela (vamos chegar nisso depois).

###Unix :

``` 
pip3 install virtualenv
mkdir noma_pasta && cd nome_pasta
python3 -m venv virtualenv_nome(nome de sua escolha)
```


NOTA 1: Se você tem apenas uma vesão de Python, você não percisará do "3" no comando. então pode usar "pip instal..." no lugar.

NOTA 2: Caso você esteja usando uma versão antiga de Python que não tenha PIP instalado, você pode baixa-lo aqui: https://pip.pypa.io/en/latest/installing/

Iniciando o Virtualenv:


``` $ source virtualenv_nome/bin/activate
```

NOTA: As vezes "source" pode não estar dispoível, nesse caso, tente o seguinte:

``` $ . virtualenv_nome/bin/activate
```



###Windows:
Primeiro, instale o virtualenv 
```
C:\%userprofile%\Python35-32\Scripts\pip.exe install virtualenv
```

Assumindo que você irá criar uma pasta em : C:\Users\me\projetos\VirtualEnv\recogVirtual, 

Creiando o VEnv
```
C:\%userprofile%\Python35-32\Scripts\virtualenv.exe C:\Users\me\%userprofile%\projetos\VirtualEnv\recogVirtual
```

Ativação: 
```
C:\%userprofile%\projetos\VirtualEnv\recogVirtual\Scripts\activate
```


####É aqui que você deve fazer a clonagem deste repositório git.
####```git clone https://github.com/peixebabel/simple-recognition.git```


## Instalando o Scikit-learn, o Framework de Python para Machine Learning

Esta biblioteca depende de NumPy e SciPy. para instala-las, digite:

``` pip3 install NumPy SciPy
pip3 install -U scikit-learn ```


##Caffe Framework

Esta parte é bem diferente pra cada sistema, então você pode seguir um guia passo a passo aqui (Usuario de macOS: Chequem a baixo primeiro): [caffe.berkeleyvision.org/installation](http://caffe.berkeleyvision.org/installation.html#prerequisites)

### macOS -> Homebrew
Para a instalação no macOS, você precisará do Homebrew Package Manager.
Para isso, você precisa instalar a Command line tools. Caso tenha o Xcode instalado, digite no terminal : ```xcode-select --install```

Ou você pode baixar de: [developer.apple](http://developer.apple.com/)


Agora para instalar o proprio Homebrew, digite no terminal:
``` ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" ```

A partir de agora siga o passo a passo do site da Caffe Framework (acima)

# Testes variados com o Pytest.

## Sobre este repositório no Github: pytest-varied-tests 

Este projeto foi iniciado com o objetivo de montar e testar modelos da aplicação do _`Pytest Framework`_ para apoiar a utilização no dia a dia de profissionais da área de desenvolvimento e testes de softwares.

:point_right: As definições de termos técnicos ou recursos deste material estarão listados no final deste _README_ o item _Definições_.

## Preparação do Ambiente

Para este tutorial você precisa ter o _`Python`_ e o _`git`_ instalado. O _`Python`_ pode pode ser baixado [aqui](https://www.python.org/downloads/), e o _"command line"_ para o _`git`_ pode ser baixado [aqui](https://git-scm.com/downloads), para mas detalhes procure na _internet_ como instalar o _`Python`_ e o _`git`_ em seu sistema operacional.
<br>

### Copiando o repositório: [  _`git clone`_ ]

Para fazer a cópia deste repositório, selecione uma pasta local em seu computador utilizando _prompt de comandos_ e use o comando abaixo:

```shell
git clone https://github.com/smedina1304/pytest-varied-tests.git
```

em seguida acesse a pasta do projeto:

```shell
cd pytest-varied-tests.git
```


## Ambiente Python

Para poder rodar o projeto pelo _`Pytest`_ é necessário a instalação de alguns módulos, para isso é indicado a preparação de um ambiente virtual para o _`Python`_ e utilização do arquivo _`requirements.txt`_ para seguir as versões recomendadas dos pacotes.

### Preparação de um ambiente virtual em Python.

Um ambiente virtual em Python é um diretório isolado que contém seu próprio interpretador Python, bibliotecas e scripts. Ele permite que você gerencie as dependências do seu projeto de forma isolada, evitando conflitos com outros projetos ou com o sistema operacional.

Imagine que você tem dois projetos Python:

- Projeto 1: Requer a biblioteca de um Pacote na versão 1.0.
- Projeto 2: Requer a biblioteca de um Pacote na versão 2.0.

Se você instalar ambas as versões do Pacote diretamente no Python do sistema, poderá ter problemas de compatibilidade entre os projetos, gerando erros nos momentos de executalos.

Um ambiente virtual resolve esse problema. Você pode criar um ambiente virtual para cada projeto e instalar as bibliotecas necessárias com as versões específicas que cada projeto precisa. Dessa forma, os projetos não interferem entre si e evita conflitos.

Para criar o ambiente virtual, esteja na pasta _´pytest-varied-tests.git´_ com o _prompt de comandos_ aberto e entre com a seguinte instrução:

```shell
python -m venv venv
```

<br>

Para ativar este ambiente virtual entre com o seguinte comando conforme o sistema operacional:

- Ativando o ambiente virtual **`"venv"`** no Windows via Powershell.

```shell
.\venv\Scripts\Activate.ps1
```

:point_right: Obs: No windows para funcionamento do **`"venv"`** pode ser necessário executar o seguinte comando via Powershell:

```shell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

<br>

- Ativando o ambiente virtual **`"venv"`** no Windows via CMD.

```shell
.\venv\Scripts\activate.bat
```

<br>

- Ativando o ambiente virtual **`"venv"`** no `Linux` ou `MAC`.

```shell
source ./venv/Scripts/activate
```
<br>

Para verificar que está funcionando e o ambiente foi ativado, deve aparecer o nome do ambiente destacado com prefixo _`venv`_ do seu prompt de comandos.
<br>

Para desativar o ambiente virtual **`"venv"`**:
<br>

```shell
deactivate
```
<br>

:exclamation: **ATENÇÃO:** Este comando deve ser usado apenas quando não for mais necessário a execução no ambiente virtual.

<br>

### Instalação dos pacotes necessários para este projeto.

Todos os Pacotes _`Python`_ com a devida versão utilizada para este projeto estão listados no arquivo _`requirements.txt`_, e podem ser instalados utilizando o comando abaixo:

```shell
pip install -r requirements.txt
```

<br>

## Definições:

### O que é o _`Python`_  e o _`Pytest Framework`_ ?

`Python` é uma linguagem de programação de alto nível, amplamente utilizada por sua simplicidade, versatilidade e grande comunidade de desenvolvedores. Ela é conhecida por sua sintaxe clara e legível, tornando-a ideal para iniciantes quanto para experientes.

`Pytest` é um framework de testes de software para Python que facilita a escrita, execução e organização de testes unitários e de integração. Ele é conhecido por sua simplicidade, flexibilidade e robustez.











# report
pytest --html=./reports/report.html

# report customized
https://plainenglish.io/blog/create-your-customized-html-report-in-pytest-9c6b521b7e99


# links
https://dev.to/m4rri4nne/automating-your-api-tests-using-python-and-pytest-23cc
https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest
https://testdriven.io/blog/flask-pytest/ 
https://pytest-selenium.readthedocs.io/en/latest/user_guide.html#quick-start
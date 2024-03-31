# Kit de Transcrição com Whisper

## Descrição

Este projeto usa o modelo Whisper da OpenAI para transcrever arquivos de áudio e vídeo em texto. Foi projetado para ser fácil de usar, permitindo que os usuários convertam seus arquivos multimídia em conteúdo escrito usando tecnologias avançadas de aprendizado de máquina.

## Requisitos

- Python 3.8 ou superior.
- Chocolatey
- CUDA (para usuários com GPU NVIDIA)

## Descrição dos Arquivos

- **`requirements.txt`**: Contém uma lista dos pacotes Python necessários para executar os scripts de transcrição, incluindo o modelo Whisper para lidar com arquivos multimídia.
- **`setup_environment.bat`**: Este script em formato batch foi projetado para preparar o ambiente Python necessário para o projeto. Sua principal função é automatizar vários processos, incluindo a criação de um ambiente virtual e a instalação das dependências especificadas em **`requirements.txt`**. Além disso, ele cuida da instalação do FFmpeg através do Chocolatey e do PyTorch versão 12.1.
- **`run_script.bat`**: Este arquivo batch é usado para iniciar o processo de transcrição. Fornece um método simples para iniciar a transcrição com um clique duplo.
- **`transcribe.py`**: O script principal de Python que usa o modelo Whisper para transcrever arquivos de áudio e vídeo. Inclui a lógica para o processamento de arquivos multimídia e a geração da transcrição.

## Estrutura de Pastas

- **`input/`**: Pasta onde os usuários devem colocar os arquivos de áudio ou vídeo que desejam transcrever.
- **`output/`**: Pasta onde as transcrições geradas pelo script serão salvas. Cada transcrição é nomeada de acordo com seu arquivo de origem. As transcrições são salvas nos formatos (srt, tsv, txt, vtt).

## Instalação

1. **Clonar o Projeto**: Comece clonando o repositório ou baixando os arquivos do projeto em sua máquina local.
2. **Configurar o Ambiente**:
    - Navegue até o diretório do projeto.
    - Execute **`setup_environment.bat`** como administrador. Este script criará um ambiente virtual Python e instalará as dependências necessárias.

Consulte nosso guia detalhado para [instalar o Whisper no Windows](https://mistercontenidos.com/pt/como-instalar-o-whisper-no-windows-um-guia-simples-e-passo-a-passo/).

## Uso

1. **Preparar seus Arquivos Multimídia**: Coloque os arquivos de áudio ou vídeo que você deseja transcrever na pasta **`input/`**.
2. **Executar a Transcrição**:
    - Clique duas vezes em **`run_script.bat`** para iniciar o processo de transcrição.
    - O script processa automaticamente todos os arquivos presentes na pasta **`input/`** e gera as transcrições na pasta **`output/`**.
3. **Acessar as Transcrições**: Após a conclusão do processo de transcrição, você poderá encontrar os textos resultantes na pasta **`output/`**. Cada arquivo de transcrição terá o nome do arquivo original para fácil identificação.

## Idiomas

- [Ingles](README.md)
- [Español](docs/es/README_ES.md)
# Cofre Eletrônico com Arduino, Raspberry Pi e Sockets

Este projeto acadêmico implementa um sistema de cofre eletrônico que integra hardware (Arduino) e software (Raspberry Pi) por meio de comunicação via sockets TCP.
O sistema permite o controle remoto da abertura e fechamento do cofre, utilizando autenticação por senha.

## 🔧 Funcionalidades

- **Controle de Acesso:** O cofre é controlado por um servidor que verifica a senha fornecida pelo cliente.
- **Simulação de Abertura/Fechamento:** Um servo motor simula a abertura e o fechamento do cofre.
- **Indicação de Status:** LEDs indicam se o acesso foi concedido ou negado.
- **Comunicação Segura:** Utiliza sockets TCP para a comunicação entre cliente (Raspberry Pi) e servidor (Arduino).

## 🧰 Componentes Utilizados

- **Arduino Uno** – Responsável pelo controle do hardware (servo motor e LEDs).
- **Raspberry Pi** – Atua como cliente, enviando a senha para o servidor.
- **Servo Motor** – Simula a abertura e o fechamento do cofre.
- **LEDs** – Indicam o status do acesso (verde para acesso concedido, vermelho para acesso negado).
- **Conexão via Sockets TCP** – Comunicação entre o cliente e o servidor.

## 📁 Estrutura do Projeto

```
COFRE-utilizando-Arduino-Raspberry-Sockets/
├── client.py           # Código do cliente (Raspberry Pi)
├── server.py           # Código do servidor (Arduino)
├── sketch_may20a.ino   # Código Arduino para controle do servo motor e LEDs
└── README.md           # Documentação do projeto
```

## 🚀 Como Executar o Projeto

### 1. Configurar o Arduino

- Carregue o arquivo `sketch_may20a.ino` no Arduino utilizando a IDE do Arduino.
- Conecte o servo motor e os LEDs aos pinos especificados no código.

### 2. Configurar o Raspberry Pi

- Certifique-se de que o Raspberry Pi está conectado à mesma rede que o Arduino.
- Instale as dependências necessárias para executar o `client.py`.
- Execute o cliente com o comando:

  ```bash
  python3 client.py
  ```

### 3. Operação

- O cliente solicitará a entrada de uma senha.
- A senha é enviada ao servidor via socket TCP.
- O servidor verifica a senha e, se correta, aciona o servo motor para abrir o cofre e acende o LED verde. Caso contrário, o LED vermelho é aceso.

## 👥 Integrantes

- Gustavo (1135697)
- Isadora (1136123)
- Leonardo (1135568)

## 📄 Licença

Este projeto é de uso acadêmico e não possui uma licença específica.

---

Para mais detalhes, consulte o repositório original: [COFRE-utilizando-Arduino-Raspberry-Sockets](https://github.com/isaguirredc/COFRE-utilizando-Arduino-Raspberry-Sockets/tree/main).

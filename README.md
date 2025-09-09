# Diffie-Hellman Key Exchange in Python

This repository demonstrates a simple implementation of the Diffie-Hellman key exchange algorithm using Python sockets. It includes a server and a client script that exchange information to derive a shared secret key over a network connection.

## Overview

Diffie-Hellman key exchange is a cryptographic protocol that allows two parties to securely share a secret key over an insecure channel. This secret can then be used for encrypted communication. This project provides educational code for understanding the basic principles of the exchange.

## Files

- `server.py` — Runs the server that initiates the key exchange.
- `client.py` — Runs the client that connects to the server and completes the exchange.

## How It Works

1. The server and client each choose a private key.
2. They exchange public keys generated from their private keys and some agreed-upon parameters (prime `p` and base `g`).
3. Both sides compute the shared secret independently, which will be identical.

## Usage

### 1. Start the Server

```bash
python server.py
```

The server will listen for incoming connections on `127.0.0.1:12345`.

### 2. Run the Client

Open a new terminal window and run:

```bash
python client.py
```

This will connect to the server, perform the key exchange, and print the shared secret.

## Example Output

**Server:**
```
Server listening on 127.0.0.1:12345...
Connection from ('127.0.0.1', 54321) established.
<shared secret>
```

**Client:**
```
Server says: 23, 6, 8
<shared secret>
```

## Notes

- This code is for educational purposes and is not suitable for production use.
- The prime and base values are small for simplicity. For real cryptographic applications, much larger values must be used.
- No encryption or authentication is performed beyond the key exchange.

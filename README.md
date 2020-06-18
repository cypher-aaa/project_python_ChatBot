# Making a Twitch Chat Bot

## Installation

In order to use the bot you first have to decrypt the *Settings.py.secret* file. For that purpose, install **git secret**. On Windows, you can do that with:
```bash
git clone https://github.com/sobolevn/git-secret.git git-secret
cd git-secret && make build
PREFIX="/usr/local" make install
```
For other installation methods, check *https://git-secret.io/installation*. After that, decrypt the file with the password (contact the authors/contributors).
```bash
git secret reveal Settings.py
```

## Usage
To run the bot, write

```bash
run run.py
```
or
```bash
python run.py
```
in console. Then choose one or more commands out of the list below and type them in Twitch chat (link is commented in the *Settings.py* file). It is recommended to open the chat beforehand so that you can see the bot connect.

### Commands
Here is a list of all the available commands at this point:
- **!commands** - get list of all available commands;
- **!hello** - have the bot greet you;
- **!clear** - clear chat;
- **!date** - current date (local);
- **!time** - current time (local);
- . . . to be continued.

## Authors and acknowledgment
The two contributors to the project are **@cypher-aaa** and **@SashaCot**.

## Support
For any type of further assistance, contact **alekseev4321@gmail.com**.

## Contributing
Feel free to contact the aforementioned e-mail to express your ideas for the project!

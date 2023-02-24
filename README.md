# chatgpt
Playing around with openai API

## Usage

Option 1 - Using Local Python for testing (with venv):
```
cd /tmp
python3 -m venv chatgpt
cd chatgpt
source bin/activate
git clone https://github.com/bruno-sf/chatgpt
pip install -r chatgpt/requirements.txt
export OPENAI_API_KEY="YOUR KEY"
python3 chatgpt/python_chatgpt.py
python3 chatgpt/python_chatgpt.py "Write me PEP-8 python boiler plate code"
```
![img](https://i.imgur.com/BuJ8pyy.png)

Option 2 - Using Docker for testing:
```
export OPENAI_API_KEY="YOUR KEY"
docker run -e OPENAI_API_KEY=${OPENAI_API_KEY} brunoferreira/chatgpt

or

echo OPENAI_API_KEY="sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" > .env
docker run --env-file ./env brunoferreira/chatgpt "Write me PEP-8 python boiler plate code"
```

Option 3 - Buildind a local Docker image with your key installed (preferred method):
```
export OPENAI_API_KEY="YOUR KEY"
docker build --build-arg API_VALUE=$OPENAI_API_KEY -t chatgpt-${USER} .
docker run chatgpt-${USER}
```

![img](https://i.imgur.com/uplvcx8.png)

* Just an extra stuff if you like alias:
```
alias @dkr_chatgpt='[ "$OPENAI_API_KEY" ] || { read -sp "Please provide API KEY (not echoed): " _OPENAI ; export OPENAI_API_KEY=${_OPENAI}; }; docker run --rm --env OPENAI_API_KEY=${OPENAI_API_KEY} brunoferreira/chatgpt'
```
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

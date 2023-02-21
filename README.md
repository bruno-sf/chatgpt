# chatgpt
Playing around with openai API

## Usage

Using Local Python for testing (with venv):
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

Using Docker (preferred method):
```
docker run -e OPENAI_API_KEY="sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" brunoferreira/chatgpt
or
echo OPENAI_API_KEY="sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" > .env
docker run --env-file ./env brunoferreira/chatgpt "Write me PEP-8 python boiler plate code"
```
![img](https://i.imgur.com/uplvcx8.png)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

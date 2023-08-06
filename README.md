# rugpt3-docker
ruGPT-3.5-13B docker gradio client server
### Installation
```
git clone https://github.com/format37/rugpt3-docker.git
cd rugpt3-docker
sh build.sh
```
### Gradio server
```
sh run.sh
```
Go to [http://localhost:7860](http://localhost:7860)
### Gradio client
```
cd client
pip install -r requirements.txt
python3 client.py
```
### Source
[https://huggingface.co/ai-forever/ruGPT-3.5-13B](https://huggingface.co/ai-forever/ruGPT-3.5-13B)
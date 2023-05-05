# Step 1: Install Dependencies
Run following commands to install project dependencies:
```shell
pip install llama-index
pip install gradio
pip install PyCryptodome
pip install PyPDF2
pip install openai 
```

# Step 2: Build The Index
Run following command to build the index:
```shell
OPENAI_API_KEY="<YOUR_OPENAI_API_KEY>" python index-builder.py
```
Index is stored in `./data` directory

# Step 3: Start The Web UI
Start the web interface:
```shell
OPENAI_API_KEY="<YOUR_OPENAI_API_KEY>" python webchat-server.py
```

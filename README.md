# DSAEventServer
This is a simple application that generates a list of results from a swimming session as JSON.

## Usage
### Building the container
``` podman build -t charmrapi . ```

### Running the container
``` podman run -p 8080:80 localhost/charmrapi ```

#### Expected output
```
INFO     Using path src/accountsapi.py                                                                                                                                                                           
INFO     Resolved absolute path /code/src/accountsapi.py                                                                                                                                                         
INFO     Searching for package file structure from directories with __init__.py                                                                                                                                  
         files                                                                                                                                                                                                   
INFO     Importing from /code/src                                                                                                                                                                                
                                                                                                                                                                                                                 
 ╭─ Python module file ─╮                                                                                                                                                                                        
 │                      │                                                                                                                                                                                        
 │  🐍 accountsapi.py   │                                                                                                                                                                                        
 │                      │                                                                                                                                                                                        
 ╰──────────────────────╯                                                                                                                                                                                        
                                                                                                                                                                                                                 
INFO     Importing module accountsapi                                                                                                                                                                            
INFO     Found importable FastAPI app                                                                                                                                                                            
                                                                                                                                                                                                                 
 ╭─── Importable FastAPI app ────╮                                                                                                                                                                               
 │                               │                                                                                                                                                                               
 │  from accountsapi import app  │                                               
 │                               │                                               
 ╰───────────────────────────────╯                                               
                                                                                 
INFO     Using import string accountsapi:app                                     
                                                                                 
 ╭─────────── FastAPI CLI - Production mode ───────────╮                        
 │                                                     │                        
 │  Serving at: http://0.0.0.0:80                      │                        
 │                                                     │                        
 │  API docs: http://0.0.0.0:80/docs                   │                        
 │                                                     │                        
 │  Running in production mode, for development use:   │                        
 │                                                     │                        
 │  fastapi dev                                        │                        
 │                                                     │                        
 ╰─────────────────────────────────────────────────────╯                        
                                                                                 
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)

```

### Connecting to the server
Open a web browser to [http://127.0.0.1:8080/account](http://127.0.0.1:8080/account)

### Output
You should receive a randomly generated set of results in JSON format.

e.g. 
```
[{"first_name":"Emily","family_name":"Williams","age":25,"swimming_stroke":"Freestyle","time":101,"classifier":2},{"first_name":"Emily","family_name":"Smith","age":44,"swimming_stroke":"Freestyle","time":118,"classifier":9},{"first_name":"Olivia","family_name":"Smith","age":25,"swimming_stroke":"Butterfly","time":64,"classifier":10},{"first_name":"John","family_name":"Williams","age":18,"swimming_stroke":"Freestyle","time":72,"classifier":3},{"first_name":"Jane","family_name":"Jones","age":37,"swimming_stroke":"Freestyle","time":92,"classifier":14},{"first_name":"Michael","family_name":"Brown","age":35,"swimming_stroke":"Breaststroke","time":66,"classifier":10},{"first_name":"Emily","family_name":"Williams","age":8,"swimming_stroke":"Backstroke","time":119,"classifier":12},{"first_name":"David","family_name":"Williams","age":32,"swimming_stroke":"Backstroke","time":48,"classifier":11},
```




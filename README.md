# FastAPI Proxy Server

This project is a FastAPI-based proxy server that forwards requests to target URLs. It includes CORS middleware to handle cross-origin requests.

## Features

- Proxy requests to any target URL
- Supports multiple HTTP methods (GET, POST, PUT, DELETE, OPTIONS, HEAD, PATCH)
- Handles CORS with configurable origins, methods, headers, and credentials

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- httpx

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/prd-vu-cuong/fastapi-proxy.git
   cd fastapi-proxy
   
2. Install dependencies using Poetry:

   ```sh
   poetry install
   

## Usage

1. Run the server using Uvicorn:

```sh
poetry run uvicorn app.main:app --reload
```

2. Send requests to the proxy server:

```sh       
curl -X GET http://localhost:8000/https://jsonplaceholder.typicode.com/posts
```


## Configuration

The CORS middleware is configured in main.py:
```sh
app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

You can modify the allow_origins, allow_credentials, allow_methods, and allow_headers parameters as needed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
import httpx
import uvicorn

app = FastAPI()

app.add_middleware(
    middleware_class=CORSMiddleware,  # noqa
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.api_route("/{target_url:path}", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH"])
async def proxy(request: Request, target_url: str):
    if not (target_url.startswith("http://") or target_url.startswith("https://")):
        return Response(
            status_code=400,
            content={"error": "URL start with http:// or https://"}
        )
    headers = dict(request.headers)
    headers.pop("host", None)

    body = await request.body()

    async with httpx.AsyncClient(follow_redirects=True) as client:
        try:
            resp = await client.request(
                method=request.method,
                url=target_url,
                headers=headers,
                content=body,
                cookies=request.cookies,
                params={k: v for k, v in request.query_params.items() if k != "url"}
            )

            return Response(
                content=resp.content,
                status_code=resp.status_code,
                headers=dict(resp.headers),
            )
        except Exception as e:
            return Response(content=f"Error: {str(e)}", status_code=500)


if __name__ == "__main__":
    uvicorn.run("proxy_server:app", host="0.0.0.0", port=8003)

from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}


@app.get("/")
async def root():
    """Redirect to docs"""
    return RedirectResponse(url="/docs/")


@app.post("/files/")
async def create_file(file: bytes | None = File(default=None)):
    # 可以通过使用标准类型注解并将
    # None
    # 作为默认值的方式将一个文件参数设为可选:
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(
        file: UploadFile = File(description="A file read as UploadFile")
):
    # 可以将 File() 与 UploadFile 一起使用，例如，设置额外的元数据

    return {"filename": file.filename}


@app.post("/uploadfile2/")
async def create_upload_file2(
        files: list[UploadFile] = File(description="A list of files read as UploadFile")
):
    # 可用同一个「表单字段」发送含多个文件的「表单数据」。
    # 上传多个文件时，要声明含bytes或UploadFile的列表（List）

    return {"filenames": [file.filename for file in files]}


@app.post("/files2/")
async def create_file2(
    file: bytes = File(), fileb: UploadFile = File(), token: str = Form()
):
    # 可以同时使用 File 和 Form，但是 File 必须在 Form 之前声明，否则 FastAPI 会认为它是一个文件名。
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }


# UploadFile 与 bytes 相比有更多优势：
# 使用 spooled 文件：
# 存储在内存的文件超出最大上限时，FastAPI 会把文件存入磁盘；
# 这种方式更适于处理图像、视频、二进制文件等大型文件，好处是不会占用所有内存；
# 可获取上传文件的元数据；
# 自带 file-like async 接口；
# 暴露的 Python SpooledTemporaryFile 对象，可直接传递给其他预期「file-like」对象的库。
# UploadFile
# UploadFile 的属性如下：
# filename：上传文件名字符串（str），例如， myimage.jpg；
# content_type：内容类型（MIME 类型 / 媒体类型）字符串（str），例如，image/jpeg；
# file： SpooledTemporaryFile（ file-like 对象）。其实就是 Python文件，可直接传递给其他预期 file-like 对象的函数或支持库。
# UploadFile 支持以下 async 方法，（使用内部 SpooledTemporaryFile）可调用相应的文件方法。
# write(data)：把 data （str 或 bytes）写入文件；
# read(size)：按指定数量的字节或字符（size (int)）读取文件内容；
# seek(offset)：移动至文件 offset （int）字节处的位置；
# 例如，await myfile.seek(0) 移动到文件开头；
# 执行 await myfile.read() 后，需再次读取已读取内容时，这种方法特别好用；
# close()：关闭文件。

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="reqFileAndForm:app", host="127.0.0.1", port=8080, reload=True)

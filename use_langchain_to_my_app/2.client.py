from langserve import RemoteRunnable

#现在让我们设置一个客户端，以便以编程方式与我们的服务进行交互。我们可以使用 langserve.RemoteRunnable 轻松做到这一点。 使用这个，我们可以像在客户端运行一样与服务的链进行交互。

remote_chain = RemoteRunnable("http://localhost:8000/chain/")
output=remote_chain.invoke({"language": "chinese", "text": "this shit goes hard,from the south to the east"})
print(output)

from livereload import Server


def on_reload():
    print("Web-site rebuilded")


on_reload()
server = Server()
server.watch("index.html", on_reload)
server.serve(root=".")
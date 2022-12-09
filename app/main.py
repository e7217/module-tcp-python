from model.Server import Server, ServerBuilder

if __name__ ==  "__main__":

    server = Server()
    builder = ServerBuilder(server)
    builder.create_server()
    builder.start()



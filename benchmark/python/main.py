
def main(args):
    if "name" in args:
        return {"hello": "Hello, %s!" % args["name"]}
    return {"hello": "world"}

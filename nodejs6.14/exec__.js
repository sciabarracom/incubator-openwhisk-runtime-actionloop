function main(args) {
    if(args.name) {
        return {
            "hello": "Hello "+args.name
        }
    } 
    return {"hello": "world"}
}
module.exports = main

package main

import (
	"bufio"
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"os/exec"
)

var out io.ReadCloser
var in io.WriteCloser
var bufin *bufio.Writer
var bufout *bufio.Reader
var pipeIn, pipeOut *os.File

func handler(w http.ResponseWriter, r *http.Request) {
	data, _ := ioutil.ReadAll(r.Body)
	data = append(data, '\n')
	bufin.Write(data)
	bufin.Flush()
	fmt.Printf("request: %s", data)
	res, _ := bufout.ReadBytes('\n')
	fmt.Printf("response: %s", res)
	w.Write(res)
	if f, ok := w.(http.Flusher); ok {
		f.Flush()
	}
}

func main() {
	file := os.Args[1]
	fmt.Printf("%s\n", file)
	cmd := exec.Command(file)
	in, _ = cmd.StdinPipe()
	pipeOut, pipeIn, _ = os.Pipe()
	cmd.ExtraFiles = []*os.File{pipeIn}
	cmd.Env = []string{"OW_DEBUG=/tmp/debug.log"}
	bufin = bufio.NewWriter(in)
	//out, _ = cmd.StdoutPipe()
	bufout = bufio.NewReader(pipeOut)

	cmd.Start()
	fmt.Println("started...")
	fmt.Printf("pid: %d\n", cmd.Process.Pid)
	http.HandleFunc("/run", handler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}

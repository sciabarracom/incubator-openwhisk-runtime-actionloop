package main

import (
	"bytes"
	"encoding/base64"
	"encoding/json"
	"flag"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"strings"
)

// Init data
var Init = flag.String("init", "", "init data")

// Run data
var Run = flag.String("run", "", "run data")

// MainFunc function
var MainFunc = flag.String("main", "main", "main function")

// Repeat flag
var Repeat = flag.Int("repeat", 1, "repeat count")

// Debug flag
var Debug = flag.Bool("debug", false, "debugging")

func doPost(url string, data []byte) {
	if *Debug {
		log.Printf(">>> %s\n", url)
	}

	req, err := http.NewRequest("POST", url, bytes.NewBuffer(data))
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		log.Printf("!!! Connection Error: %s -> %s\n", url, err)
		return
	}
	defer resp.Body.Close()
	if resp.StatusCode != 200 {
		log.Printf("!!! Http Error: %s -> %s\n", url, resp.Status)
	}
	body, _ := ioutil.ReadAll(resp.Body)
	if *Debug {
		log.Printf("<<< %s", string(body))
	}
}

func encodeInit(filename string) ([]byte, error) {
	buf, _ := ioutil.ReadFile(*Init)
	toEncode := make(map[string]interface{})
	toEncode["main"] = *MainFunc
	if strings.HasSuffix(filename, ".zip") || strings.HasSuffix(filename, ".exe") {
		toEncode["binary"] = true
		toEncode["code"] = base64.StdEncoding.EncodeToString(buf)
	} else {
		toEncode["code"] = string(buf)
	}
	res, err := json.Marshal(map[string]interface{}{"value": toEncode})
	if *Debug {
		fmt.Printf("encodeInit: %s\n", res)
	}
	return res, err
}

func main() {
	flag.Parse()
	log.SetFlags(0)
	var initData []byte
	var runData []byte

	if *Init != "" {
		initData, _ = encodeInit(*Init)
	}

	if *Run != "" {
		runData, _ = ioutil.ReadFile(*Run)
	}

	for _, port := range flag.Args() {
		//fmt.Println(port)
		if len(initData) > 0 {
			u := fmt.Sprintf("http://localhost:%s/init", port)
			doPost(u, initData)
		}
		if len(runData) > 0 {
			for i := 0; i < *Repeat; i++ {
				u := fmt.Sprintf("http://localhost:%s/run", port)
				doPost(u, runData)
			}
		}
	}
}

package main

import (
	"etcdDemo/client"
	"fmt"
	"log"
	"time"
)

func main() {
	cli := client.NewEtcdClient([]string{
		"http://101.34.252.82:2379",
		"http://101.34.252.82:22379",
		"http://101.34.252.82:32379",
	})

	err := cli.Put("hello", "world", 3*time.Second)
	if err != nil {
		log.Fatalln(err)
	}

	resp, err := cli.Get("hello", 3*time.Second)
	if err != nil {
		log.Fatalln(err)
	}

	fmt.Println(resp)
}

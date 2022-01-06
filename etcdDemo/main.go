package main

import (
	"etcdDemo/client"
	"fmt"
	"log"
	"time"
)

const key string = "hello-ttl"

func main() {
	cli := client.NewEtcdClient([]string{
		"http://localhost:2379",
		"http://localhost:22379",
		"http://localhost:32379",
	})

	err := cli.PutWithKeepAlive(key, "world", 3*time.Second)
	if err != nil {
		log.Fatalln(err)
	}

	go func() {
		for i := 0; i < 20; i++ {
			time.Sleep(time.Second)
			cli.Put(key, fmt.Sprintf("word-%d", i), 3*time.Second)

		}
	}()

	cli.Watch(key)

	// for i := 0; i < 20; i ++ {
	// 	time.Sleep(time.Second)
	// 	resp, err := cli.Get(key, 3*time.Second)
	// 	if err != nil {
	// 		log.Fatalln(err)
	// 	}
	//
	// 	fmt.Printf("Index: %d, Resp: %s\n", i, resp)
	// }
}

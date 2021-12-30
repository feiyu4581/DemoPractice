package client

import (
	"context"
	"fmt"
	clientv3 "go.etcd.io/etcd/client/v3"
	"log"
	"time"
)

type EtcdClient struct {
	Endpoints   []string
	DialTimeout time.Duration
	client      *clientv3.Client
}

func NewEtcdClient(endpoints []string) *EtcdClient {
	client := EtcdClient{Endpoints: endpoints, DialTimeout: 5 * time.Second}

	cli, err := clientv3.New(clientv3.Config{
		Endpoints:   client.Endpoints,
		DialTimeout: client.DialTimeout,
	})

	if err != nil {
		log.Fatalln(err)
	}

	client.client = cli
	return &client
}

func (client *EtcdClient) Get(key string, timeout time.Duration) (string, error) {
	ctx, cancel := context.WithTimeout(context.Background(), timeout)
	defer cancel()
	resp, err := client.client.Get(ctx, key)
	if err != nil {
		return "", err
	}

	fmt.Println(resp)
	return "ok", nil
}

func (client *EtcdClient) Put(key string, value string, timeout time.Duration) error {
	ctx, cancel := context.WithTimeout(context.Background(), timeout)
	defer cancel()
	resp, err := client.client.Put(ctx, key, value)
	if err != nil {
		return err
	}

	fmt.Println(resp)
	return nil
}

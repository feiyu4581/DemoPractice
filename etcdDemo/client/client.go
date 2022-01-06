package client

import (
	"context"
	"fmt"
	clientV3 "go.etcd.io/etcd/client/v3"
	"log"
	"time"
)

type EtcdClient struct {
	Endpoints   []string
	DialTimeout time.Duration
	client      *clientV3.Client
}

func NewEtcdClient(endpoints []string) *EtcdClient {
	client := EtcdClient{Endpoints: endpoints, DialTimeout: 5 * time.Second}

	cli, err := clientV3.New(clientV3.Config{
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
	_, err := client.client.Get(ctx, key)
	if err != nil {
		return "", err
	}

	return "ok", nil
}

func (client *EtcdClient) Put(key string, value string, timeout time.Duration) error {
	ctx, cancel := context.WithTimeout(context.Background(), timeout)
	defer cancel()
	_, err := client.client.Put(ctx, key, value)
	if err != nil {
		return err
	}

	return nil
}

func (client *EtcdClient) PutWithKeepAlive(key string, value string, timeout time.Duration) error {
	ctx, cancel := context.WithTimeout(context.Background(), timeout)
	defer cancel()

	lease, err := client.client.Grant(ctx, 5)
	if err != nil {
		log.Fatalln(err)
	}

	_, err = client.client.Put(ctx, key, value, clientV3.WithLease(lease.ID))
	if err != nil {
		log.Fatalln(err)
	}

	ch, err := client.client.KeepAlive(context.Background(), lease.ID)
	if err != nil {
		log.Fatalln(err)
	}

	go func() {
		for resp := range ch {
			fmt.Printf("续约 %d\n", resp.ID)
		}
	}()

	return nil
}

func (client *EtcdClient) Watch(key string) {
	rch := client.client.Watch(context.Background(), key)
	for rsp := range rch {
		for _, ev := range rsp.Events {
			fmt.Printf("%s %q : %q\n", ev.Type, ev.Kv.Key, ev.Kv.Value)
		}
	}
}
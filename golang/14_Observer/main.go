package main

import (
	"14_Observer/observer"
	"14_Observer/subject"
	"context"
	"fmt"
	"os"
)

func main() {
	ctx := context.Background()
	si := new(subject.ServerInterrupt)
	si.Listen()

	servers := []observer.IServer{
		new(observer.GinServer),
		new(observer.GinServer2),
	}

	for _, server := range servers {
		si.Register(server)
		go func(server observer.IServer) {
			if err := server.Run(ctx); err != nil {
				fmt.Printf("run error: %v \n", err)
				os.Exit(1)
			}
		}(server)
	}

	select {}
}

package observer

import (
	"context"
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
	"time"
)

type IServer interface {
	Run(ctx context.Context) error
	Shutdown(ctx context.Context) error
}

type GinServer struct {
	srv *http.Server
}

func (g *GinServer) Run(ctx context.Context) error {
	e := gin.New()

	//測試關機是否會等待
	e.GET("test", func(context *gin.Context) {
		<-time.After(25 * time.Second)
		context.Data(http.StatusOK, "application/json; charset=utf-8", []byte("ok"))
	})

	g.srv = &http.Server{
		Addr:    ":8080",
		Handler: e,
	}

	if err := g.srv.ListenAndServe(); err != nil && err != http.ErrServerClosed {
		fmt.Printf("listen: %s\n", err)
		return err
	}

	return nil
}

func (g *GinServer) Shutdown(ctx context.Context) error {
	if err := g.srv.Shutdown(ctx); err != nil {
		return fmt.Errorf("Server Shutdown: %v\n", err)
	}

	return nil
}

type GinServer2 struct {
	srv *http.Server
}

func (g *GinServer2) Run(ctx context.Context) error {
	e := gin.New()
	e.GET("test", func(context *gin.Context) {
		<-time.After(5 * time.Second)
		context.Data(http.StatusOK, "application/json; charset=utf-8", []byte("ok"))
	})

	g.srv = &http.Server{
		Addr:    ":8081",
		Handler: e,
	}

	if err := g.srv.ListenAndServe(); err != nil && err != http.ErrServerClosed {
		fmt.Printf("listen: %s\n", err)
		return err
	}

	return nil
}

func (g *GinServer2) Shutdown(ctx context.Context) error {
	if err := g.srv.Shutdown(ctx); err != nil {
		return fmt.Errorf("Server2 Shutdown: %v\n", err)
	}

	return nil
}

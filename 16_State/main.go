package main

import (
	"fmt"
)

// State interface 定義了所有狀態的行為
type State interface {
	handle() error
}

// ConcreteStateA 實現 State interface
type ConcreteStateA struct{}

func (c *ConcreteStateA) handle() error {
	fmt.Println("進入 ConcreteStateA 狀態")
	return nil
}

// ConcreteStateB 實現 State interface
type ConcreteStateB struct{}

func (c *ConcreteStateB) handle() error {
	fmt.Println("進入 ConcreteStateB 狀態")
	return nil
}

// Context 為擁有狀態的物件，也是Client接口
type Context struct {
	state State
}

func (c *Context) setState(s State) {
	c.state = s
}

func (c *Context) request() error {
	return c.state.handle()
}

func state1() {
	// 初始化一個Context物件，初始狀態為 ConcreteStateA
	context := &Context{
		state: &ConcreteStateA{},
	}

	// 改變狀態為 ConcreteStateB
	context.setState(&ConcreteStateB{})
	// 發送請求，執行 ConcreteStateB 的行為
	context.request()

	// 改變狀態為 ConcreteStateA
	context.setState(&ConcreteStateA{})
	// 發送請求，執行 ConcreteStateA 的行為
	context.request()
}

// Context2 為擁有狀態的物件，也是Client接口
type Context2 struct {
	state State2
}

func (c *Context2) setState(s State2) {
	c.state = s
}

func (c *Context2) request() error {
	return c.state.handle(c)
}

// State2 interface 定義了所有狀態的行為
type State2 interface {
	handle(*Context2) error
}

// ConcreteStateC 實現 State interface
type ConcreteStateC struct{}

func (c *ConcreteStateC) handle(context *Context2) error {
	fmt.Println("進入 ConcreteStateC 狀態")
	fmt.Println("轉成 ConcreteStateD 狀態")
	context.state = &ConcreteStateD{}
	return nil
}

// ConcreteStateD 實現 State interface
type ConcreteStateD struct{}

func (c *ConcreteStateD) handle(context *Context2) error {
	fmt.Println("進入 ConcreteStateD 狀態")
	fmt.Println("轉成 ConcreteStateE 狀態")
	context.state = &ConcreteStateE{}
	return nil
}

type ConcreteStateE struct{}

func (c *ConcreteStateE) handle(context *Context2) error {
	fmt.Println("進入 ConcreteStateE 狀態")
	fmt.Println("轉成 ConcreteStateC 狀態")
	context.state = &ConcreteStateC{}
	return nil
}

func state2() {
	// 初始化一個Context物件，初始狀態為 ConcreteStateA
	context := &Context2{
		state: &ConcreteStateC{},
	}
	for i := 0; i < 5; i++ {
		context.request()
	}
}

func main() {
	fmt.Println("test state1")
	state1()
	fmt.Println("test state2")
	state2()
}

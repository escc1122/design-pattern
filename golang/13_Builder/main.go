package main

import "fmt"

type IBuild interface {
	SetHead()
	SetBody()
	SetFooter()
	get() *Document
}

type BuildA struct {
	head   string
	body   string
	footer string
}

type BuildB struct {
	head   string
	body   string
	footer string
}

type Document struct {
	head   string
	body   string
	footer string
}

type Director struct {
	build IBuild
}

func newDirector(build IBuild) *Director {
	return &Director{
		build: build,
	}
}

func (d *Director) setBuilder(b IBuild) {
	d.build = b
}

func (d *Director) make() *Document {
	d.build.SetHead()
	d.build.SetBody()
	d.build.SetFooter()
	return d.build.get()
}

func (b *BuildA) SetHead() {
	b.head = "build a head"
}

func (b *BuildA) SetBody() {
	b.body = "build a body"
}

func (b *BuildA) SetFooter() {
	b.footer = "build a footer"
}

func (b *BuildA) get() *Document {
	return &Document{
		head:   b.head,
		body:   b.body,
		footer: b.footer,
	}
}

func (b *BuildB) SetHead() {
	b.head = "build b head"
}

func (b *BuildB) SetBody() {
	b.body = "build b body"
}

func (b *BuildB) SetFooter() {
	b.footer = "nil"
}

func (b *BuildB) get() *Document {
	return &Document{
		head:   b.head,
		body:   b.body,
		footer: b.footer,
	}
}

func main() {
	director := newDirector(&BuildA{})
	// &{build a head build a body build a footer}
	fmt.Println(director.make())

	director.setBuilder(&BuildB{})
	//&{build b head build b body nil}
	fmt.Println(director.make())
}

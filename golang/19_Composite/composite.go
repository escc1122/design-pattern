package main

import "fmt"

type IComposite interface {
	add(iTree IComposite)
	remove(iTree IComposite)
	show(depth int)
}

type Folder struct {
	name   string
	iTrees []IComposite
}

type File struct {
	name   string
	iTrees []IComposite
}

func (f *File) add(iTree IComposite) {
	fmt.Println("file no add")
}

func (f *File) remove(iTree IComposite) {}

func (f *File) show(depth int) {
	tab := ""
	for i := 0; i < depth; i++ {
		tab = tab + "\t"
	}

	fmt.Printf("%s--%s\n", tab, f.name)

	for _, tree := range f.iTrees {
		tree.show(depth + 2)
	}
}

func (f *Folder) add(iTree IComposite) {
	f.iTrees = append(f.iTrees, iTree)
}

func (f *Folder) remove(iTree IComposite) {
	for i, tree := range f.iTrees {
		if tree == iTree {
			f.iTrees = append(f.iTrees[:i], f.iTrees[i+1:]...)
			break
		}
	}
}

func (f *Folder) show(depth int) {
	tab := ""
	for i := 0; i < depth; i++ {
		tab = tab + "\t"
	}

	fmt.Printf("%s--%s\n", tab, f.name)

	for _, tree := range f.iTrees {
		tree.show(depth + 2)
	}
}

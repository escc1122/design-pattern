package main

// 開始亂寫了

import "fmt"

type IData interface {
	showData(depth int)
}
type Folder2 struct {
	name string
}

func (f *Folder2) showData(depth int) {
	tab := ""
	for i := 0; i < depth; i++ {
		tab = tab + "\t"
	}

	fmt.Printf("%s--%s\n", tab, f.name)
}

type File2 struct {
	name string
}

func (f *File2) showData(depth int) {
	tab := ""
	for i := 0; i < depth; i++ {
		tab = tab + "\t"
	}

	fmt.Printf("%s--%s\n", tab, f.name)
}

type ICompositeGenerics[T comparable] interface {
	add(iTree ICompositeGenerics[T])
	remove(iTree ICompositeGenerics[T])
	//show(depth int)

	show2(depth int, aaa func(d int, t T))
}

type Node[T comparable] struct {
	data   T
	iTrees []ICompositeGenerics[T]
}

func (n *Node[T]) add(iTree ICompositeGenerics[T]) {
	n.iTrees = append(n.iTrees, iTree)
}

func (n *Node[T]) remove(iTree ICompositeGenerics[T]) {
	for i, tree := range n.iTrees {
		if tree == iTree {
			n.iTrees = append(n.iTrees[:i], n.iTrees[i+1:]...)
			break
		}
	}
}

func (n *Node[T]) show2(depth int, callBack func(depth int, t T)) {
	callBack(depth, n.data)
	for _, tree := range n.iTrees {
		tree.show2(depth+2, callBack)
	}
}

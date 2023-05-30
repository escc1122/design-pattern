package main

// 試著用泛型改寫練習
// 不過這個例子顯得很多餘,看看就好

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

type ICompositeGenerics[T IData] interface {
	add(iTree ICompositeGenerics[T])
	remove(iTree ICompositeGenerics[T])
	show(depth int)
}

// nodes 這種不行,在處理 function add 資料型態無法正確
//type nodes interface {
//	*File2 | *Folder2
//}
//	type Node[T nodes] struct {
//		data   T
//		iTrees []ICompositeGenerics[T]
//	}

type Node[T IData] struct {
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

func (n *Node[T]) show(depth int) {
	n.data.showData(depth)

	for _, tree := range n.iTrees {
		tree.show(depth + 2)
	}
}

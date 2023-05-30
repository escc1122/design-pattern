package main

import "testing"

func TestNode_show(t *testing.T) {
	root := &Node[IData]{data: &Folder2{name: "root"}}
	folder_a := &Node[IData]{data: &Folder2{name: "folder_a"}}
	folder_b := &Node[IData]{data: &Folder2{name: "folder_b"}}
	folder_d := &Node[IData]{data: &Folder2{name: "folder_d"}}
	folder_e := &Node[IData]{data: &Folder2{name: "folder_e"}}
	folder_f := &Node[IData]{data: &Folder2{name: "folder_f"}}

	file_a := &Node[IData]{data: &File2{name: "file_a"}}
	file_d := &Node[IData]{data: &File2{name: "file_d"}}
	file_b := &Node[IData]{data: &File2{name: "file_b"}}
	file_c := &Node[IData]{data: &File2{name: "file_c"}}
	file_e := &Node[IData]{data: &File2{name: "file_e"}}
	file_f := &Node[IData]{data: &File2{name: "file_f"}}

	root.add(folder_a)
	root.add(folder_d)
	root.add(file_a)
	root.add(file_d)
	root.add(file_b)
	folder_d.add(folder_b)
	folder_b.add(folder_e)
	folder_b.add(file_b)
	folder_b.add(file_c)
	folder_d.add(file_e)
	folder_e.add(folder_f)
	folder_f.add(file_f)

	//root.show(1)

	root.show2(1, func(d int, data IData) {
		data.showData(d)
	})

}

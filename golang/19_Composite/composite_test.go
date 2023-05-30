package main

import "testing"

func TestFolder_show(t *testing.T) {
	root := &Folder{name: "root"}
	folder_a := &Folder{name: "folder_a"}
	folder_b := &Folder{name: "folder_b"}
	//folder_c := &Folder{name: "folder_c"}
	folder_d := &Folder{name: "folder_d"}
	folder_e := &Folder{name: "folder_e"}
	folder_f := &Folder{name: "folder_f"}
	file_a := &File{name: "file_a"}
	file_d := &File{name: "file_d"}
	file_b := &File{name: "file_b"}
	file_c := &File{name: "file_c"}
	file_e := &File{name: "file_e"}
	file_f := &File{name: "file_f"}

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

	root.show(1)
}

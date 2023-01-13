package main

import (
	"fmt"
	"reflect"
	"sync"
)

type singleton struct {
}

var _singleInstance *singleton

var lock = &sync.Mutex{}

func GetInstance() *singleton {
	if _singleInstance == nil {
		lock.Lock()
		defer lock.Unlock()
		if _singleInstance == nil {
			_singleInstance = &singleton{}
		}
	}
	return _singleInstance
}

var (
	_singleInstance2 *singleton
	once             = &sync.Once{}
)

func GetInstance2() *singleton {
	once.Do(func() {
		_singleInstance2 = &singleton{}
	})
	return _singleInstance2
}

func main() {
	a := GetInstance()
	b := GetInstance()

	//824633975376
	//824633975376
	fmt.Println(reflect.ValueOf(a).Pointer())
	fmt.Println(reflect.ValueOf(b).Pointer())

	c := GetInstance2()
	d := GetInstance2()
	//824633975392
	//824633975392
	fmt.Println(reflect.ValueOf(c).Pointer())
	fmt.Println(reflect.ValueOf(d).Pointer())
}

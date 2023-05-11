package testtype

import (
	"context"
	"errors"
)

const (
	TESTA = iota
)

type TestType interface {
	Handle(ctx context.Context) error
}

type TestTypeStruct struct {
	Id    int64
	Type  int
	State int
}

// 註冊 TransferType
var instanceFunc = make(map[int]func(TestTypeStruct) TestType)

// 註冊 TransferType
func register(name int, getFunc func(TestTypeStruct) TestType) {
	if _, ok := instanceFunc[name]; ok {
		panic(errors.New("instanceFunc is repeated"))
	}
	instanceFunc[name] = getFunc
}

func GetInstance(testTypeStruct TestTypeStruct) TestType {
	if f, ok := instanceFunc[testTypeStruct.Type]; ok {
		return f(testTypeStruct)
	}
	return nil
}

// nextFlow 跑到下一個flow
func nextState(ctx context.Context, testTypeStruct *TestTypeStruct) error {
	testTypeStruct.State++
	return nil
}

var temp = make(map[int64]*TestTypeStruct)

func PushRedis(testTypeStruct *TestTypeStruct) {
	temp[testTypeStruct.Id] = testTypeStruct
}

func GetRedis(id int64) (*TestTypeStruct, bool) {
	testTypeStruct, ok := temp[id]
	delete(temp, id)
	return testTypeStruct, ok
}

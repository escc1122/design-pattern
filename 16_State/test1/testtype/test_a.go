package testtype

import (
	"context"
	"fmt"
)

const (
	TESTSTATE1 = iota
	TESTSTATE2
	TESTSTATESUCCESS
)

func init() {
	register(TESTA, func(testTypeStruct TestTypeStruct) TestType {
		return &testA{&testTypeStruct}
	})
}

type testA struct {
	testTypeStruct *TestTypeStruct
}

func (t *testA) state1(ctx context.Context) error {
	nextState(ctx, t.testTypeStruct)
	fmt.Println("state1 success")
	PushRedis(t.testTypeStruct)
	return nil
}

func (t *testA) state2(ctx context.Context) error {
	nextState(ctx, t.testTypeStruct)
	fmt.Println("state2 success")
	PushRedis(t.testTypeStruct)
	return nil
}

func (t *testA) success(ctx context.Context) error {
	fmt.Println("success")
	return nil
}

func (t *testA) Handle(ctx context.Context) error {
	switch t.testTypeStruct.State {
	case TESTSTATE1:
		t.state1(ctx)
	case TESTSTATE2:
		t.state2(ctx)
	case TESTSTATESUCCESS:
		t.success(ctx)
	}
	return nil
}

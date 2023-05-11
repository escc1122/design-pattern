package main

import (
	"context"
	"test1/testtype"
	"time"
)

func main() {
	id := int64(124142)
	testTypeStruct := &testtype.TestTypeStruct{
		Id:    id,
		Type:  testtype.TESTA,
		State: 0,
	}
	testtype.PushRedis(testTypeStruct)
	for {
		testTypeStruct, ok := testtype.GetRedis(id)
		if !ok {
			return
		}
		testType := testtype.GetInstance(*testTypeStruct)
		ctx, _ := context.WithTimeout(context.Background(), 3*time.Second)
		testType.Handle(ctx)
	}

}

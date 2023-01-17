package main

import "fmt"

type ISimpleFactory interface {
	toDo() float64
	setNumberA(float64)
	setNumberB(float64)
}

type Add struct {
	numberA float64
	numberB float64
}

func (a *Add) toDo() float64 {
	return a.numberA + a.numberB
}
func (a *Add) setNumberA(numberA float64) {
	a.numberA = numberA
}
func (a *Add) setNumberB(numberB float64) {
	a.numberB = numberB
}

type Sub struct {
	numberA float64
	numberB float64
}

func (s *Sub) toDo() float64 {
	return s.numberA - s.numberB
}

func (s *Sub) setNumberA(numberA float64) {
	s.numberA = numberA
}
func (s *Sub) setNumberB(numberB float64) {
	s.numberB = numberB
}

func Create(factoryType string) (ISimpleFactory, error) {
	if factoryType == "add" {
		return &Add{}, nil
	}

	if factoryType == "sub" {
		return &Sub{}, nil
	}

	return nil, fmt.Errorf("err")
}

func main() {
	add, _ := Create("add")
	add.setNumberA(10)
	add.setNumberB(5)

	fmt.Println(add.toDo())

	sub, _ := Create("sub")
	sub.setNumberA(10)
	sub.setNumberB(5)
	fmt.Println(sub.toDo())
}

package main

import "fmt"

type CaffeineBeverage interface {
	Brew()
	AddCondiments()
	BoilWater()
	PourInCup()
	//PrepareRecipe()
}

type Coffee struct{}

func (c *Coffee) Brew() {
	fmt.Println("Dripping coffee through filter")
}

func (c *Coffee) AddCondiments() {
	fmt.Println("Adding sugar and milk")
}

func (c *Coffee) BoilWater() {
	fmt.Println("Boiling water")
}

func (c *Coffee) PourInCup() {
	fmt.Println("Pouring coffee into cup")
}

//func (c *Coffee) PrepareRecipe() {
//	c.BoilWater()
//	c.Brew()
//	c.PourInCup()
//	c.AddCondiments()
//}

type Tea struct{}

func (t *Tea) Brew() {
	fmt.Println("Steeping the tea")
}

func (t *Tea) AddCondiments() {
	fmt.Println("Adding lemon")
}

func (t *Tea) BoilWater() {
	fmt.Println("Boiling water")
}

func (t *Tea) PourInCup() {
	fmt.Println("Pouring tea into cup")
}

//func (t *Tea) PrepareRecipe() {
//	t.BoilWater()
//	t.Brew()
//	t.PourInCup()
//	t.AddCondiments()
//}

type CaffeineBeverageWithTemplateMethod struct{}

func (cb *CaffeineBeverageWithTemplateMethod) PrepareRecipe(caffeineBeverage CaffeineBeverage) {
	caffeineBeverage.BoilWater()
	caffeineBeverage.Brew()
	caffeineBeverage.PourInCup()
	caffeineBeverage.AddCondiments()
}

func main() {
	coffee := &Coffee{}
	tea := &Tea{}

	beverageMaker := &CaffeineBeverageWithTemplateMethod{}

	beverageMaker.PrepareRecipe(coffee)
	beverageMaker.PrepareRecipe(tea)
}

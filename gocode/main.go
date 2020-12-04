package main

import "fmt"

func main() {
	ch1 := make(chan int)
	pump(ch1)          // pump hangs
	fmt.Println(<-ch1) // prints only 1
}

func pump(ch chan int) {
	for i := 1; ; i++ {
		ch <- i
	}
}

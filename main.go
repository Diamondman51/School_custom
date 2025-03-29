// package main

// import (
// 	"os"
// 	"strconv"
// 	"math"
// 	// "time"
// )

// func main() {
// 	var channel1 chan string = make(chan string)
// 	var channel2 chan string = make(chan string)

// 	go func() {
// 		for i := 0; true; i++ {
// 			str := strconv.Itoa(i)
// 			channel1 <- str
// 			// time.Sleep(2 * time.Second)
// 		}
// 	}()

// 	go func() {
// 		for i := 0; true; i++ {
// 			str := strconv.Itoa(i)
// 			channel2 <- str
// 			println(i)
// 			if i == 150000 {
// 				break
// 			// time.Sleep(500 * time.Millisecond)
// 		}}
// 	}()

// 	os.Create("test.txt")
// 	math.Pow(2, 3)
// 	file, error := os.OpenFile("test.txt", os.O_APPEND, os.ModeAppend)
// 	for {
// 		select {
// 		case msg1 := <-channel1:
// 			if error != nil {
// 				println("Error opening file")}
// 			file.WriteString(msg1)
// 		case msg2 := <-channel2:
// 			if error != nil {
// 				println("Error opening file")
// 			}
// 			file.WriteString(msg2)
			
// 		}
// 	}

// }

package main

import "fmt"

func main() {
	var ch chan string = make(chan string, 2)
	ch <- "lola"
	ch <- "ada"
	ch <- "opgpg"
	close(ch)
	c := 0
	for h := range ch {
		if c == 3 {
			break
		}
		fmt.Println(h)
		c++
	}

}



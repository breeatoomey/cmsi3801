package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"sync"
)

func download(url string, wg *sync.WaitGroup, results chan string) {
	defer wg.Done()

	resp, err := http.Get(url)
	defer resp.Body.Close()

	if err != nil {
		results <- fmt.Sprintf("Error downloading %s: %v", url, err)
		return
	}

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		results <- fmt.Sprintf("Error reading body of %s: %v", url, err)
		return
	}

	results <- string(body)
}

func main() {
	url := os.Args[1]

	// Define WaitGroup and Channel
	var wg sync.WaitGroup
	results := make(chan string)

	// Spawn multiple goroutines
	for i := 0; i < 5; i++ { // Adjust thread count as needed
		wg.Add(1)
		go download(fmt.Sprintf("%s-%d", url, i+1), &wg, results)
	}

	// Wait for all goroutines to finish
	wg.Wait()

	// Collect and print results
	for i := 0; i < 5; i++ {
		result := <-results
		fmt.Println(result)
	}
}

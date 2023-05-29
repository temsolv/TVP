//go:author Artem Solbonov

package main

import (
	"flag"
	"fmt"
	"image"
	"image/jpeg"
	"os"
	"sync"
)

// Регистрируем формат JPEG для чтения изображений в пакете image.
func init() {
	image.RegisterFormat("jpeg", "jpeg", jpeg.Decode, jpeg.DecodeConfig)
}

func main() {
	// Открываем файл с изображением "image.jpg" и закрываем его по завершению.
	imgfile, _ := os.Open("image.jpg")
	defer imgfile.Close()

	// Декодируем JPEG-изображение и проверяем наличие ошибок.
	img, err := jpeg.Decode(imgfile)
	if err != nil {
		fmt.Print("File opening error!")
	}

	// Получаем границы изображения и определяем его ширину и высоту.
	bounds := img.Bounds()
	width, height := bounds.Max.X, bounds.Max.Y

	// Определяем флаг "t" для задания количества потоков.
	// По умолчанию устанавливаем значение 1.
	threads := flag.Int("t", 1, "Number of threads")

	// Парсим командную строку и обновляем значение флага "t".
	flag.Parse()

	// Вывод в консоль количества потоков
	fmt.Println("Количество потоков:", *threads)

	// Определяем размер чанка для каждой горутины.
	// Чанк - количество пикселей, которая должна обработать 1 горутина.
	chunkSize := (width*height + *threads - 1) / *threads

	// Создаем буферизированные каналы для каждого цвета.
	// Буферизированные каналы имееют строго определенный размер.
	redCh := make(chan int, chunkSize)
	greenCh := make(chan int, chunkSize)
	blueCh := make(chan int, chunkSize)

	// Создаём WaitGroup для синхронизации горутин.
	// WaitGroup - счетчик, отслеживающий, сколько горутин выполняется в данный момент.
	// wg хранит количество заданных горутин.
	var wg sync.WaitGroup

	// Добавляем количество горутин в wg, * - указатель на значение переменной.
	wg.Add(*threads)

	// Запускаем горутины для чтения цветов пикселей.
	for i := 0; i < *threads; i++ {
		start := i * chunkSize
		end := (i + 1) * chunkSize
		if end > width*height {
			end = width * height
		}
		// Запуск горутины
		go GetColors(img, height, width, start, end, redCh, greenCh, blueCh, &wg)
	}

	// Закрываем каналы после того, как все горутины заверишили работу
	// Анонимная горутина (запускается без присвоения имени)
	go func() {
		// wg.Wait() - метод, используемый для блокировки выполнения программы
		// до тех пор, пока все горутины, добавленные в WaitGroup не закончат свою работу
		wg.Wait()
		close(redCh)
		close(greenCh)
		close(blueCh)
	}()

	// Создаем массивы для хранения полученных цветов изображения
	var redArr []int
	var blueArr []int
	var greenArr []int

	// Цикл по длине пикселей изображения, считывающий
	// значения из каналов в массивы.
	// Получение значения реализуется через оператор <-
	for i := 0; i < width*height; i++ {
		redArr = append(redArr, <-redCh)
		greenArr = append(greenArr, <-greenCh)
		blueArr = append(blueArr, <-blueCh)
	}

	// Обрабатываем результаты по своему усмотрению
	fmt.Print(redArr)
}

// getColors читает цвета пикселей изображения в заданном диапазоне
// и отправляет их в соответствующие каналы. Он также уведомляет WaitGroup
// о завершении работы горутины.
//
// Аргументы:
// img - изображение, цвета пикселей которого необходимо получить.
// height, width - размеры изображения.
// start, end - диапазон пикселей, которые необходимо обработать.
// redCh, greenCh, blueCH - буферизированные каналы для отправки
// цветов пикселей соответствующего цвета.
// wg - указатель на WaitGroup, используемый для синхронизации горутин.
func GetColors(img image.Image, height int, width int, start int, end int,
	redCh chan<- int, greenCh chan<- int, blueCh chan<- int, wg *sync.WaitGroup) {

	// В цикле обрабатываем пиксели в заданном диапазоне.
	for i := start; i < end; i++ {
		y := i / width
		x := i % width

		// Получаем значения цветов пикселя в формате RGBA.
		r, g, b, _ := img.At(x, y).RGBA()

		// Отправляем значения цветов в соответствующие каналы.
		redCh <- int(r) / 257
		greenCh <- int(g) / 257
		blueCh <- int(b) / 257
	}

	// Уведомляем WaitGroup о завершении работы горутины.
	// Метод Done() уменьшает счетчик горутин на 1.
	defer wg.Done()
}

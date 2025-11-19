// Знаходимо елементи зі сторінки
const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d"); // інструмент для малювання
const startBtn = document.getElementById("startBtn");
const scoreEl = document.getElementById("score");
const mobileButtons = document.querySelectorAll(".mobile-controls button");
 
// Розмір сітки гри
const tileSize = 16;          // розмір клітинки в пікселях
const tileCount = 20;         // 20x20 клітинок
const canvasSize = tileSize * tileCount; // 320x320
 
// Налаштовуємо канвас точно під сітку
canvas.width = canvasSize;
canvas.height = canvasSize;
 
// Змінні гри
let snake = [];        // масив сегментів змійки
let direction = { x: 1, y: 0 }; // поточний напрям (спочатку вправо)
let food = { x: 10, y: 10 };    // позиція їжі
let gameInterval = null;        // id setInterval
let score = 0;
let isGameOver = false;
 
// Функція запуску/перезапуску гри
function startGame() {
    // Початкова змійка з 3 сегментів
    snake = [
        { x: 8, y: 10 },
        { x: 7, y: 10 },
        { x: 6, y: 10 }
    ];
 
    direction = { x: 1, y: 0 }; // рух вправо
    score = 0;
    isGameOver = false;
    scoreEl.textContent = score;
 
    // Генеруємо нову їжу
    placeFood();
 
    // Якщо попередній інтервал існував – зупиняємо
    if (gameInterval) {
        clearInterval(gameInterval);
    }
 
    // Оновлюємо гру кожні 100 мс
    gameInterval = setInterval(gameLoop, 100);
}
 
// Основний цикл гри
function gameLoop() {
    if (isGameOver) return;
 
    update(); // оновити стан (логіка)
    draw();   // перемалювати картинку
}
 
// Оновлення стану гри (логіка)
function update() {
    const head = snake[0];
 
    // Нова голова змійки
    const newHead = {
        x: head.x + direction.x,
        y: head.y + direction.y
    };
 
    // Перевірка зіткнення зі стінкою
    if (
        newHead.x < 0 ||
        newHead.x >= tileCount ||
        newHead.y < 0 ||
        newHead.y >= tileCount
    ) {
        endGame();
        return;
    }
 
    // Перевірка зіткнення з собою
    for (let i = 0; i < snake.length; i++) {
        if (snake[i].x === newHead.x && snake[i].y === newHead.y) {
            endGame();
            return;
        }
    }
 
    // Додаємо нову голову на початок масиву
    snake.unshift(newHead);
 
    // Перевірка: чи з’їли їжу?
    if (newHead.x === food.x && newHead.y === food.y) {
        score++;
        scoreEl.textContent = score;
        placeFood();
        // Хвіст не видаляємо – змійка росте
    } else {
        // Видаляємо останній елемент (хвіст)
        snake.pop();
    }
}
 
// Малювання всього кадру
function draw() {
    // Очищаємо поле
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
 
    // Малюємо їжу
    ctx.fillStyle = "red";
    ctx.fillRect(
        food.x * tileSize,
        food.y * tileSize,
        tileSize,
        tileSize
    );
 
    // Малюємо змійку
    for (let i = 0; i < snake.length; i++) {
        // Голова – яскравіша
        if (i === 0) {
            ctx.fillStyle = "#00e676";
        } else {
            ctx.fillStyle = "#00c853";
        }
 
        const segment = snake[i];
        ctx.fillRect(
            segment.x * tileSize,
            segment.y * tileSize,
            tileSize - 1,
            tileSize - 1
        );
    }
}
 
// Випадкова позиція їжі
function placeFood() {
    food.x = Math.floor(Math.random() * tileCount);
    food.y = Math.floor(Math.random() * tileCount);
 
    // Щоб їжа не з’явилась всередині змійки
    for (let i = 0; i < snake.length; i++) {
        if (snake[i].x === food.x && snake[i].y === food.y) {
            // Якщо співпало – генеруємо ще раз
            placeFood();
            break;
        }
    }
}
 
// Закінчення гри
function endGame() {
    isGameOver = true;
    clearInterval(gameInterval);
    alert("Гру закінчено! Ваш рахунок: " + score);
}
 
// Обробка клавіатури (стрілки)
document.addEventListener("keydown", (event) => {
    // Забороняємо розворот на 180° (щоб змійка не входила сама в себе)
    if (event.key === "ArrowUp" && direction.y !== 1) {
        direction = { x: 0, y: -1 };
    } else if (event.key === "ArrowDown" && direction.y !== -1) {
        direction = { x: 0, y: 1 };
    } else if (event.key === "ArrowLeft" && direction.x !== 1) {
        direction = { x: -1, y: 0 };
    } else if (event.key === "ArrowRight" && direction.x !== -1) {
        direction = { x: 1, y: 0 };
    }
});
 
// Обробка кнопок на телефоні
mobileButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
        const dir = btn.getAttribute("data-dir");
 
        if (dir === "up" && direction.y !== 1) {
            direction = { x: 0, y: -1 };
        } else if (dir === "down" && direction.y !== -1) {
            direction = { x: 0, y: 1 };
        } else if (dir === "left" && direction.x !== 1) {
            direction = { x: -1, y: 0 };
        } else if (dir === "right" && direction.x !== -1) {
            direction = { x: 1, y: 0 };
        }
    });
});
 
// Натискаємо на кнопку "Почати гру"
startBtn.addEventListener("click", () => {
    startGame();
});
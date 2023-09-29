<!DOCTYPE html>
<html>
<head>
    <title>Aprendiz SENA</title>
    <link rel="stylesheet" type="text/css" href="Matriz.css">
</head>
<body>
    <h1>Aprendiz Rubén Darío Triviño Díaz - Programa ADSO</h1>
    <h1>Matriz</h1>
    <table>
        <tbody id="matrix">
            <?php for ($i = 0; $i < 10; $i++) : ?>
                <tr>
                    <?php for ($j = 0; $j < 5; $j++) : ?>
                    <td id="cell-<?php echo $i; ?>-<?php echo $j; ?>" class="white-cell"></td>
                    <?php endfor; ?>
                </tr>
            <?php endfor; ?>
        </tbody>
    </table>
    <div class="button-container">
        <button id="randomButton">Seleccionar Aleatoriamente</button>
        <button id="clearButton">Limpiar Matriz</button>
    </div>
    <div class="gracias">¡¡Gracias!!</div>
    <script>
        const matrix = document.getElementById("matrix").getElementsByTagName("td");
        const selectedPositions = [];

        function disableRowColumn(row, column) {
            if (selectedPositions.length < 5) {
                for (let i = 0; i < 10; i++) {
                    const cellRow = matrix[i * 5 + column];
                    const cellColumn = matrix[row * 5 + i];
                    cellRow.classList.add("disabled");
                    cellRow.textContent = "X";
                    cellColumn.classList.add("disabled");
                    cellColumn.textContent = "X";
                }
                selectedPositions.push({ row, column });
                if (selectedPositions.length === 5) {
                    disableMatrix();
                }
            }
        }

        function enableMatrix() {
            selectedPositions.forEach(pos => {
                for (let i = 0; i < 10; i++) {
                    const cellRow = matrix[i * 5 + pos.column];
                    const cellColumn = matrix[pos.row * 5 + i];
                    cellRow.classList.remove("disabled");
                    cellRow.textContent = "";
                    cellColumn.classList.remove("disabled");
                    cellColumn.textContent = "";
                }
            });
            selectedPositions.length = 0;
        }

        function disableMatrix() {
            for (const cell of matrix) {
                cell.onclick = null;
            }
        }

        function clearMatrix() {
            enableMatrix();
        }

        function selectRandomCell() {
            if (selectedPositions.length < 5) {
                let availableCells = [];
                for (let i = 0; i < matrix.length; i++) {
                    if (!matrix[i].classList.contains("disabled")) {
                        availableCells.push(i);
                    }
                }
                
                if (availableCells.length > 0) {
                    const randomIndex = Math.floor(Math.random() * availableCells.length);
                    const randomCell = matrix[availableCells[randomIndex]];
                    const row = Math.floor(availableCells[randomIndex] / 5);
                    const column = availableCells[randomIndex] % 5;
                    
                    disableRowColumn(row, column);
                }
            }
        }

        for (let i = 0; i < 10; i++) {
            for (let j = 0; j < 5; j++) {
                const cell = document.getElementById(`cell-${i}-${j}`);
                cell.addEventListener("click", () => disableRowColumn(i, j));
            }
        }

        const clearButton = document.getElementById("clearButton");
        clearButton.addEventListener("click", clearMatrix);

        const randomButton = document.getElementById("randomButton");
        randomButton.addEventListener("click", selectRandomCell);
    </script>
</body>
</html>

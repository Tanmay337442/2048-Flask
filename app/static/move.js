window.addEventListener("keydown", function (event) {

    var key;

    if (event.code == "ArrowUp" || event.code == "KeyW") {
        key = "w";

    } else if (event.code == "ArrowLeft" || event.code == "KeyA") {

        key = "a";

    } else if (event.code == "ArrowDown" || event.code == "KeyS") {

        key = "s";

    } else if (event.code == "ArrowRight" || event.code == "KeyD") {

        key = "d";

    }

    if (key != null) {

        fetch('/update-game', {
            method: 'POST',
            body: JSON.stringify({
                key: key
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(response => response.json())
            .then(response => {
                console.log(response);
                if (response.error) {
                    console.log(response);
                } else {
                    var cells = document.querySelectorAll('.cell');
                    for (var row = 0; row < response.mat.length; row++) {
                        for (var col = 0; col < response.mat[row].length; col++) {
                            var cellIndex = row * 4 + col;
                            if (response.mat[row][col] != 0) {
                                cells[cellIndex].textContent = response.mat[row][col];
                                cells[cellIndex].className = "cell cell-" + response.mat[row][col];
                            } else {
                                cells[cellIndex].textContent = "";
                                cells[cellIndex].className = "cell";
                            }

                        }
                    }
                    document.querySelector('.score').textContent = "Score: " + response.score;
                    if (response.state == "win") {
                        document.querySelector('.message').textContent = "You won!";
                        document.querySelector('dialog').showModal();
                    } else if (response.state == "loss") {
                        document.querySelector('.message').textContent = "You lost!";
                        document.querySelector('dialog').showModal();
                    }
                }

            });

    }

});
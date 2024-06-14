# PyJSFaceAPI (Windows Only)

## Overview

This project provides a Python-based solution for face detection and recognition that can be integrated with a Node.js application. The Python code is bundled into an executable using PyInstaller, allowing Node.js to interact with it through the `spawn` function. **This project is designed to work only on Windows.**

## Features

- Face detection
- Face recognition
- Bundled as an executable for easy integration with Node.js

## Requirements

- Python 3.11+
- Windows OS

## Setup

### Python Environment

1. **Clone the repository:**

    ```sh
    git clone https://github.com/daniel-onyenwee/py-js-face-api.git
    cd py-js-face-api
    ```

2. **Initialize the virtual environment:**

    ```sh
    .\Scripts\activate  # On Windows
    ```

3. **Install the required Python packages:**

    ```sh
    pip install dlib-19.24.1-cp311-cp311-win_amd64.whl
    pip install -r requirements.txt
    ```

### Create Executable

```sh
.\build.bat
```

This will generate an executable in the `dist` directory.

## Usage

### Node.js Integration

1. **Node.js script to interact with the Python executable:**

    ```javascript
    const { spawn } = require('child_process');
    const path = require('path');

    const pythonExecutable = path.join(__dirname, 'dist', 'py-js-face-api.exe');

    function recognizeFace(imagePath) {
        return new Promise((resolve, reject) => {
            const pythonProcess = spawn(pythonExecutable, [imagePath]);

            pythonProcess.stdout.on('data', (data) => {
                console.log(`stdout: ${data}`);
                resolve(data.toString());
            });

            pythonProcess.stderr.on('data', (data) => {
                console.error(`stderr: ${data}`);
                reject(data.toString());
            });

            pythonProcess.on('close', (code) => {
                console.log(`py-js-face-api.exe exited with code ${code}`);
            });
        });
    }

    // Example usage
    recognizeFace('path_to_image.jpg')
        .then(result => console.log(result))
        .catch(error => console.error(error));
    ```

2. **Running the Node.js script:**

    ```sh
    node index.js
    ```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [MIT](LICENSE.md) file for more details.

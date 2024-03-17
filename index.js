const { spawn } = require('child_process');
const express = require('express');
const multer = require('multer');
const path = require('path');

const app = express();
const port = 3000;

// Set up multer for file upload
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, 'uploads/')
  },
  filename: function (req, file, cb) {
    cb(null, file.originalname)
  }
});

const upload = multer({ storage: storage });

// Serve the index.html file
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// app.post('/upload', upload.single('salesData'), (req, res) => {
//   const pythonProcess = spawn('python3', ['prediction_script.py', req.file.path]);

//   let predictions = '';

//   pythonProcess.stdout.on('data', (data) => {
//     predictions += data.toString();
//   });

//   pythonProcess.stderr.on('data', (data) => {
//     console.error(`Error: ${data}`);
//     res.status(500).send('An error occurred during prediction.');
//   });

//   pythonProcess.on('close', () => {
//     res.send(predictions);
//   });
// });
app.post('/upload', upload.single('salesData'), (req, res) => {
  const pythonProcess = spawn('python3', ['prediction_script.py', req.file.path]);

  let predictions = '';

  pythonProcess.stdout.on('data', (data) => {
    predictions += data.toString();
  });

  pythonProcess.stderr.on('data', (data) => {
    console.error(`Error: ${data}`);
    res.status(500).send('An error occurred during prediction.');
  });

  pythonProcess.on('close', (code) => {
    console.log(`Python process exited with code ${code}`);
    console.log(`Predictions: ${predictions}`);
    res.send(predictions);
  });
});

// Handle PUT request to update HTML content
app.put('/update-html', (req, res) => {
  const predictions = req.body; // Assuming the predictions data is sent in the request body
  // Update HTML content in browser
  // Example: res.send('<h2>Predictions: ' + predictions + '</h2>');
});


app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});

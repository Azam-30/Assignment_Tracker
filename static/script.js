document.getElementById('loadData').addEventListener('click', function () {
  var rollNumber = document.getElementById('rollNumber').value.trim();

  if (!rollNumber) {
      document.getElementById('span-value').innerText = 'Please enter a roll number.';
      return;
  }

  fetch('/load_data/', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          'X-CSRFToken': getCookie('csrftoken')  // Include CSRF token
      },
      body: 'roll_no=' + encodeURIComponent(rollNumber)
  })
  .then(response => response.json())
  .then(data => {
      let pythonTable = document.getElementById('python-table');
      let dataStructuresTable = document.getElementById('data-structures-table');
      let messageDiv = document.getElementById('message');
      let spanValue = document.getElementById('span-value');

      pythonTable.innerHTML = '';  // Clear existing table data
      dataStructuresTable.innerHTML = '';  // Clear existing table data
      messageDiv.innerHTML = '';  // Clear existing message

      // Python Assignments Table
      let pythonData = data.python_data;
      if (pythonData.length > 0) {
          let headerRow = '<tr><th>Roll No</th><th>Assignment 1</th><th>Assignment 2</th><th>Assignment 3</th><th>Assignment 4</th><th>Assignment 5</th><th>Assignment 6</th></tr>';
          let rows = pythonData.map(row => `<tr><td>${row.roll_no}</td><td>${row.assignment1}</td><td>${row.assignment2}</td><td>${row.assignment3}</td><td>${row.assignment4}</td><td>${row.assignment5}</td><td>${row.assignment6}</td></tr>`).join('');
          pythonTable.innerHTML = headerRow + rows;
      } else {
          pythonTable.innerHTML = '<tr><td colspan="7">No data found</td></tr>';
      }

      // Data Structures Table
      let dataStructuresData = data.data_structures_data;
      if (dataStructuresData.length > 0) {
          let headerRow = '<tr><th>Roll No</th><th>Assignment 1</th><th>Assignment 2</th><th>Assignment 3</th><th>Assignment 4</th><th>Assignment 5</th><th>Assignment 6</th></tr>';
          let rows = dataStructuresData.map(row => `<tr><td>${row.roll_no}</td><td>${row.assignment1}</td><td>${row.assignment2}</td><td>${row.assignment3}</td><td>${row.assignment4}</td><td>${row.assignment5}</td><td>${row.assignment6}</td></tr>`).join('');
          dataStructuresTable.innerHTML = headerRow + rows;
      } else {
          dataStructuresTable.innerHTML = '<tr><td colspan="7">No data found</td></tr>';
      }

      if (pythonData.length > 0 || dataStructuresData.length > 0) {
          messageDiv.textContent = 'Data loaded successfully!';
          messageDiv.style.color = 'green';
      } else {
          messageDiv.textContent = 'No data found for the provided roll number.';
          messageDiv.style.color = 'red';
      }
  })
  .catch(error => {
      document.getElementById('span-value').innerText = 'Error loading data.';
      console.error('Error:', error);
  });
});

// Helper function to get CSRF token
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}



// Particle.js Initialization
particlesJS("particles-js", {
  particles: {
      number: { value: 160, density: { enable: true, value_area: 800 } },
      color: { value: "#ffffff" },
      shape: {
          type: "circle",
          stroke: { width: 0, color: "#000000" },
          polygon: { nb_sides: 5 },
          image: { src: "img/github.svg", width: 100, height: 100 },
      },
      opacity: {
          value: 1,
          random: true,
          anim: { enable: true, speed: 1, opacity_min: 0, sync: false },
      },
      size: {
          value: 3,
          random: true,
          anim: { enable: false, speed: 4, size_min: 0.3, sync: false },
      },
      line_linked: {
          enable: false,
          distance: 150,
          color: "#ffffff",
          opacity: 0.4,
          width: 1,
      },
      move: {
          enable: true,
          speed: 1,
          direction: "none",
          random: true,
          straight: false,
          out_mode: "out",
          bounce: false,
          attract: { enable: false, rotateX: 600, rotateY: 600 },
      },
  },
  interactivity: {
      detect_on: "canvas",
      events: {
          onhover: { enable: true, mode: "bubble" },
          onclick: { enable: true, mode: "repulse" },
          resize: true,
      },
      modes: {
          grab: { distance: 400, line_linked: { opacity: 1 } },
          bubble: { distance: 250, size: 0, duration: 2, opacity: 0, speed: 3 },
          repulse: { distance: 400, duration: 0.4 },
          push: { particles_nb: 4 },
          remove: { particles_nb: 2 },
      },
  },
  retina_detect: true,
});

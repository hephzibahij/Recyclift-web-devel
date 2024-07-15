document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting in the traditional way

    // Get form values
    const name = document.getElementById('name').value;
    const address = document.getElementById('address').value;
    const weight = document.getElementById('weight').value;

    // Display output
    const output = document.getElementById('output');
    output.innerHTML = `<p>Thank you for registering, <strong>${name}</strong>!</p>
                        <p>Address: ${address}</p>
                        <p>Estimated Weight: ${weight} kg</p>`;
});
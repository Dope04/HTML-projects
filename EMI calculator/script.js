function calculateEMI() {
    const principal = parseFloat(document.getElementById("principal").value);
    const interest = parseFloat(document.getElementById("interest").value) / 100; // Convert to decimal
    const tenure = parseFloat(document.getElementById("tenure").value) * 12; // Convert years to months
  
    // Formula for EMI calculation
    const emi = (principal * interest * Math.pow(1 + interest, tenure)) / (Math.pow(1 + interest, tenure) - 1);
  
    // Display the calculated EMI with two decimal places
    document.getElementById("emi-output").innerHTML = `EMI: ₹ ${emi.toFixed(2)}`;
  }
  
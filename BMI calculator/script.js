function calculateBMI() {
    const height = parseFloat(document.getElementById("height").value);
    const weight = parseFloat(document.getElementById("weight").value);
  
    if (isNaN(height) || isNaN(weight)) {
      alert("Please enter valid values for height and weight.");
      return;
    }
  
    const bmi = weight / Math.pow(height / 100, 2);
  
    let resultText;
    if (bmi < 18.5) {
      resultText = "Underweight";
    } else if (bmi >= 18.5 && bmi <= 24.9) {
      resultText = "Normal weight";
    } else if (bmi >= 25 && bmi <= 29.9) {
      resultText = "Overweight";
    } else {
      resultText = "Obese";
    }
  
    document.getElementById("result").innerHTML = `Your BMI is: ${bmi.toFixed(2)} - ${resultText}`;
  }
  
# Ex.05 Design a Website for Server Side Processing
# Date:03.10.2025
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
```
server.html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Power Calculator</title>
  <style>
    html, body {
      height: 100%;
      margin: 0;
      display: flex;
      justify-content: center; /* horizontal center */
      align-items: center;     /* vertical center */
      font-family: Arial, sans-serif;
      background-color: #6a1b9a;
    }
    .container {
      text-align: center;
      padding: 20px;
      border-radius: 12px;
      background-color: #ffd700;
      box-shadow: 0 4px 12px #212121;
      border-radius:40px 10px 40px 10px;
    }
    input {
      padding: 6px;
      margin: 6px 0;
      width: 120px;
    }
    button {
      padding: 8px 16px;
      margin-top: 10px;
      cursor: pointer;
    }
  </style>
</head>
<body>

  <div class="container">
    <h1>Power Calculator (P = I² × R)</h1>

    <div>
      <label>Current (I in A): </label>
      <input type="number" id="current" step="any"><br>

      <label>Resistance (R in Ω): </label>
      <input type="number" id="resistance" step="any"><br>

      <button onclick="calculatePower()">Calculate</button>
    </div>

    <h2 id="result">Power will appear here</h2>
  </div>

  <script>
    function calculatePower() {
      let I = parseFloat(document.getElementById("current").value);
      let R = parseFloat(document.getElementById("resistance").value);

      if (!isNaN(I) && !isNaN(R)) {
        let P = I * I * R;
        document.getElementById("result").innerText = "Power = " + P + " Watts";
      } else {
        document.getElementById("result").innerText = "Please enter both values!";
      }
    }
  </script>

</body>
</html>

views.py

from django.shortcuts import render 
def calculate_power(request):

    if request.method == "POST":
        Intensity = float(request.POST.get("Intensity"))
        Resistance = float(request.POST.get("Resistance"))
        Power = ((Intensity)**2 ) * Resistance 
        print(f"Intensity: {Intensity} I, Resistance: {Resistance} R, Power: {Power}")
    return render(request,'serverapp/server.html')

    urls.py

    from django.contrib import admin
from django.urls import path
from serverapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.calculate_power, name='calculate_power'),
]

```

# SERVER SIDE PROCESSING:
# HOMEPAGE:
![alt text](<Screenshot (50).png>)

![alt text](<Screenshot (51).png>)


# RESULT:
The program for performing server side processing is completed successfully.


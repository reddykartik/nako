const form = document.getElementById("checker-form");
const sourceCode = document.getElementById("source-code")
const result = document.getElementById("result");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const code = sourceCode.value.trim();
  if (!code) {
    result.hidden = false;
    result.textContent = "Oi, enter some python code!!";
    return;
  }

  result.hidden = false;
  result.textContent = "Analyzing your code...";
  try {
    const response = await fetch("/api/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        source_code: code,
      }),
    });
    const data = await response.json();
    if (!response.ok) {
      result.textContent = data.message || data.error || "Something went wrong.";
      return;
    }
    const label = data.prediction === 1 ? "Vulnerable" : "Safe";
    result.textContent = `Model prediction: ${label}`;
    // result.textContent = `Model prediction: Class ${data.prediction}`;
  } catch (error) {
    result.textContent = "Could not connect to the prediction API.";
    console.error(error);
  }
});

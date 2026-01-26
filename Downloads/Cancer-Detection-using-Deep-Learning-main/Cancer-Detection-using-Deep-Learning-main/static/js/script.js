document.addEventListener("DOMContentLoaded", () => {
    const loadingElement = document.getElementById('loading');
    const predEliment = document.getElementById('preds');
    const resultElement = document.getElementById('result');
    const resultMessageElement = document.getElementById('result-message');

    // Simulate loading and cancer detection result after 5 seconds
    setTimeout(() => {
        loadingElement.classList.add('hidden');
        resultElement.classList.remove('hidden');
        resultMessageElement.textContent = predEliment.innerText; // You can update this message based on actual result
    }, 5000); // 5000 milliseconds = 5 seconds
});
